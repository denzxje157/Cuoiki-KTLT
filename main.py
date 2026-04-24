import random
import Data_loader
import quiz_engine
import logger

list_tienganh, list_tiengviet = Data_loader.lay_du_lieu()

print("--- CHUONG TRINH TRAC NGHIEM ---")
print("1: Viet-Anh")
print("2: Anh-Viet")
chon = input("Chọn chế độ (1 hoặc 2): ")

diem = 0
danh_sach_cau_sai = []

cau_da_hoi = [] 

for i in range(10):
    vi_tri_dung = random.randint(0, len(list_tienganh) - 1)
    while vi_tri_dung in cau_da_hoi:
        vi_tri_dung = random.randint(0, len(list_tienganh) - 1)
    
    cau_da_hoi.append(vi_tri_dung)

    ba_dap_an = quiz_engine.tao_bo_dap_an(vi_tri_dung, len(list_tienganh))

    print("\n--- Câu số", i + 1, "---")

    if chon == '1':
        print("Từ '" + list_tiengviet[vi_tri_dung] + "' có nghĩa Tiếng Anh là gì?")

        for n in range(len(ba_dap_an)):
            chi_so_dap_an = ba_dap_an[n]
            print(str(n + 1) + ". " + list_tienganh[chi_so_dap_an])
    else:
        print("Tưd '" + list_tienganh[vi_tri_dung] + "' có nghĩa Tiếng Việt là gì?")
        for n in range(len(ba_dap_an)):
            chi_so_dap_an = ba_dap_an[n]
            print(str(n + 1) + ". " + list_tiengviet[chi_so_dap_an])

    cau_tra_loi = input("Nhập lựa chọn của bạn (1, 2, 3): ")

    dap_an_dung_nam_o_so = 0
    for n in range(len(ba_dap_an)):
        if ba_dap_an[n] == vi_tri_dung:
            dap_an_dung_nam_o_so = n + 1

    if cau_tra_loi == str(dap_an_dung_nam_o_so):
        print("=> Chính xác!")
        diem = diem + 1 
    else:
        print("=> Sai rồi!")
        tu_sai = list_tienganh[vi_tri_dung] + " - " + list_tiengviet[vi_tri_dung]
        danh_sach_cau_sai.append(tu_sai)

logger.ghi_ket_qua(diem, danh_sach_cau_sai)

print("Đã xong, bạn đúng được", diem, "/ 10 câu.")
print("Kiểm tra file ketqua.txt để xem chi tiết nha.")