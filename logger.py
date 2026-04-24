def ghi_ket_qua(diem, ds_cau_sai):
    f = open("ketqua.txt", "a", encoding="utf-8")
    f.write(f"Ket qua: {diem}/10. Sai {len(ds_cau_sai)} cau.\n")
    if len(ds_cau_sai) > 0:
        f.write("Chi tiet cau sai:\n")
        for cau in ds_cau_sai:
            f.write("- " + cau + "\n")
    f.write("-" * 20 + "\n")
    f.close()
