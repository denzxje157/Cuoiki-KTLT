# Chương Trình Trắc Nghiệm Từ Vựng Tiếng Anh-Việt (KTLT)

## 📝 Tổng Quan
Đây là một chương trình trắc nghiệm tương tác để kiểm tra và rèn luyện từ vựng tiếng Anh-Việt. Người dùng có thể chọn hai chế độ:
- **Chế độ 1**: Tiếng Việt → Tiếng Anh (cho tiếng Việt, chọn tiếng Anh)
- **Chế độ 2**: Tiếng Anh → Tiếng Việt (cho tiếng Anh, chọn tiếng Việt)

Chương trình sẽ đưa ra 10 câu hỏi ngẫu nhiên, mỗi câu có 3 lựa chọn trắc nghiệm. Kết quả sẽ được lưu vào file `ketqua.txt`.

---

## 🏗️ Cấu Trúc Hệ Thống

```
Cuoiki-KTLT/
├── main.py              # Chương trình chính
├── Data_loader.py       # Module tải dữ liệu từ vựng
├── quiz_engine.py       # Module tạo câu hỏi trắc nghiệm
├── logger.py            # Module ghi kết quả
├── tuvung.txt           # Dữ liệu từ vựng (CSV format)
├── ketqua.txt           # File lưu kết quả (tự động tạo)
└── README.md            # File hướng dẫn này
```

---

## 📋 Chi Tiết Các Module

### 1. **main.py** - Chương Trình Chính
**Vai trò**: Điều phối toàn bộ luồng chương trình

**Quy trình hoạt động**:
1. Import các module cần thiết (`Data_loader`, `quiz_engine`, `logger`, `random`)
2. Tải dữ liệu từ vựng bằng `Data_loader.lay_du_lieu()`
3. Hiển thị menu chế độ:
   - Mode 1: Dịch từ Tiếng Việt sang Tiếng Anh
   - Mode 2: Dịch từ Tiếng Anh sang Tiếng Việt
4. Chạy vòng lặp 10 câu hỏi:
   - Chọn ngẫu nhiên 1 từ vựng (không trùng lặp)
   - Tạo 3 đáp án (1 đúng, 2 sai) bằng `quiz_engine.tao_bo_dap_an()`
   - Hiển thị câu hỏi theo mode đã chọn
   - Nhận trả lời từ người dùng
   - So sánh với đáp án đúng
   - Cộng điểm nếu đúng, ghi lại nếu sai
5. Lưu kết quả bằng `logger.ghi_ket_qua()`
6. Hiển thị tổng điểm và thông báo xem chi tiết trong `ketqua.txt`

**Biến chính**:
- `list_tienganh`: Danh sách từ vựng tiếng Anh
- `list_tiengviet`: Danh sách từ vựng tiếng Việt
- `chon`: Lựa chọn mode của người dùng
- `diem`: Tổng điểm đạt được
- `danh_sach_cau_sai`: Danh sách các câu trả lời sai
- `cau_da_hoi`: Danh sách vị trí các câu đã hỏi (tránh lặp lại)

---

### 2. **Data_loader.py** - Module Tải Dữ Liệu
**Vai trò**: Đọc và xử lý file dữ liệu từ vựng

**Hàm chính**: `lay_du_lieu()`

**Chi tiết hoạt động**:
1. Mở file `tuvung.txt` với encoding UTF-8
2. Đọc từng dòng trong file
3. Loại bỏ khoảng trắng thừa (`strip()`)
4. Bỏ qua dòng trống
5. Tách dữ liệu theo dấu phẩy (`,`)
   - Phần tử đầu tiên: Tiếng Anh (`tach[0]`)
   - Phần tử thứ hai: Tiếng Việt (`tach[1]`)
6. Thêm vào danh sách tương ứng
7. Trả về 2 danh sách: `(list_en, list_vi)`
8. Nếu file không tồn tại, hiển thị thông báo lỗi

**Format file tuvung.txt**:
```
word_english,word_vietnamese
apple,quả táo
table,bàn
```

---

### 3. **quiz_engine.py** - Module Tạo Câu Hỏi
**Vai trò**: Tạo bộ 3 đáp án cho mỗi câu hỏi

**Hàm chính**: `tao_bo_dap_an(vi_tri_dung, tong_so_tu)`

**Tham số**:
- `vi_tri_dung`: Vị trí (index) của từ đúng trong danh sách
- `tong_so_tu`: Tổng số từ vựng có sẵn

**Chi tiết hoạt động**:
1. Chọn ngẫu nhiên vị trí sai thứ nhất (`vi_tri_sai1`)
   - Đảm bảo không trùng với vị trí đúng
2. Chọn ngẫu nhiên vị trí sai thứ hai (`vi_tri_sai2`)
   - Đảm bảo không trùng với vị trí đúng và vị trí sai thứ nhất
3. Tạo danh sách gồm 3 vị trí: `[vi_tri_dung, vi_tri_sai1, vi_tri_sai2]`
4. Xáo trộn danh sách ngẫu nhiên (`random.shuffle()`)
5. Trả về danh sách 3 vị trí đã xáo trộn

**Ý nghĩa**: Đảm bảo 3 đáp án không lặp lại và vị trí đáp án đúng luôn thay đổi

---

### 4. **logger.py** - Module Ghi Kết Quả
**Vai trò**: Lưu kết quả quiz vào file

**Hàm chính**: `ghi_ket_qua(diem, ds_cau_sai)`

**Tham số**:
- `diem`: Số điểm đạt được (0-10)
- `ds_cau_sai`: Danh sách các từ vựng trả lời sai

**Chi tiết hoạt động**:
1. Mở file `ketqua.txt` ở chế độ append (thêm vào cuối)
2. Ghi dòng kết quả: `"Ket qua: {diem}/10. Sai {len(ds_cau_sai)} cau.\n"`
3. Nếu có câu sai:
   - Ghi tiêu đề: `"Chi tiet cau sai:\n"`
   - Ghi từng câu sai với định dạng: `"- word_en - word_vi\n"`
4. Ghi dòng phân cách: 20 dấu gạch ngang
5. Đóng file

**Output format trong ketqua.txt**:
```
Ket qua: 8/10. Sai 2 cau.
Chi tiet cau sai:
- apple - quả táo
- table - bàn
--------------------
```

---

## 🔄 Luồng Hoạt Động Chi Tiết

```
START
  ↓
[1] Load dữ liệu từ tuvung.txt (Data_loader.py)
  ↓
[2] Hiển thị menu chọn chế độ
  ↓
[3] Khởi tạo: diem = 0, danh_sach_cau_sai = [], cau_da_hoi = []
  ↓
[4] FOR i = 1 TO 10:
      ├─→ Chọn ngẫu nhiên vị trí từ (không trùng cau_da_hoi)
      ├─→ Thêm vào cau_da_hoi
      ├─→ Tạo 3 đáp án bằng tao_bo_dap_an()
      ├─→ Hiển thị câu hỏi theo mode
      ├─→ Nhận trả lời người dùng
      ├─→ IF trả lời == đáp án đúng
      │   ├─→ In "Chính xác!"
      │   └─→ diem += 1
      │  ELSE
      │   ├─→ In "Sai rồi!"
      │   └─→ Thêm vào danh_sach_cau_sai
      └─→ Tiếp theo câu hỏi
  ↓
[5] Ghi kết quả bằng logger.ghi_ket_qua()
  ↓
[6] Hiển thị tổng điểm
  ↓
END
```

---

## 💾 Định Dạng File Dữ Liệu

### tuvung.txt (Input)
- **Format**: CSV (Comma-Separated Values)
- **Encoding**: UTF-8
- **Cấu trúc**: Mỗi dòng gồm 2 cột cách nhau bằng dấu phẩy
  ```
  tieng_anh,tieng_viet
  hello,xin chào
  goodbye,tạm biệt
  ```

### ketqua.txt (Output)
- **Mode**: Append (thêm vào cuối file)
- **Encoding**: UTF-8
- **Nội dung**: Kết quả mỗi lần chạy chương trình
  ```
  Ket qua: 10/10. Sai 0 cau.
  --------------------
  Ket qua: 7/10. Sai 3 cau.
  Chi tiet cau sai:
  - word1 - tư1
  - word2 - tư2
  - word3 - tư3
  --------------------
  ```

---

## 🚀 Cách Sử Dụng

### Yêu cầu
- Python 3.x
- File `tuvung.txt` chứa danh sách từ vựng

### Chạy chương trình
```bash
python main.py
```

### Bước thực hiện
1. Chạy lệnh trên
2. Chọn chế độ (1 hoặc 2)
3. Trả lời 10 câu hỏi (chọn 1, 2, hoặc 3)
4. Xem kết quả cuối cùng
5. Kiểm tra chi tiết trong `ketqua.txt`

---

## 📊 Quy Trình Tư Duy Của Chương Trình

1. **Khởi tạo**: Load dữ liệu → Chọn mode
2. **Vòng lặp Quiz**: 
   - Chọn từ ngẫu nhiên
   - Tạo đáp án
   - So sánh kết quả
3. **Lưu trữ**: Ghi kết quả vào file
4. **Kết thúc**: Hiển thị tổng điểm

---

## ⚠️ Lưu Ý
- File `tuvung.txt` phải tồn tại trong cùng thư mục với `main.py`
- Format dữ liệu phải đúng: `english,vietnamese` (cách nhau bằng phẩy)
- Kết quả sẽ được lưu lặp lại trong `ketqua.txt` (không ghi đè)
- Danh sách 10 câu hỏi không lặp lại trong một lần chạy nhưng có thể trùng giữa các lần chạy khác nhau

---

## 🔧 Có Thể Cải Tiến
- Thêm tính năng chọn số lượng câu hỏi
- Thêm tính năng xem lại các câu sai
- Thêm thống kê theo thời gian
- Thêm tính năng random từ từ một chủ đề cụ thể
- Cải thiện UI/UX