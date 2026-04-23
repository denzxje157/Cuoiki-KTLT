import random
import data_loader
import quiz_engine
import logger

en, vi = data_loader.lay_du_lieu()

print("--- CHUONG TRINH TRAC NGHIEM ---")
chon = input("Chon che do (1: Viet-Anh, 2: Anh-Viet): ")

diem = 0
cau_sai = []

for i in range(10):
    dung = random.randint(0, len(en) - 1)
    ds_lua_chon = quiz_engine.tao_bo_dap_an(dung, len(en))
    
logger.ghi_ket_qua(diem, cau_sai)
print("Da xong!")