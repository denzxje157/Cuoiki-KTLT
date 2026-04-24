import random

def tao_bo_dap_an(vi_tri_dung, tong_so_tu):
    # Chọn 2 vị trí sai ngẫu nhiên, đảm bảo không trùng với vị trí đúng
    vi_tri_sai1 = random.randint(0, tong_so_tu - 1)
    while vi_tri_sai1 == vi_tri_dung:
        vi_tri_sai1 = random.randint(0, tong_so_tu - 1)
        
    vi_tri_sai2 = random.randint(0, tong_so_tu - 1)
    while vi_tri_sai2 == vi_tri_dung or vi_tri_sai2 == vi_tri_sai1:
        vi_tri_sai2 = random.randint(0, tong_so_tu - 1)

    # Trộn vị trí của đáp án đúng và sai
    lua_chon = [vi_tri_dung, vi_tri_sai1, vi_tri_sai2]
    random.shuffle(lua_chon)
    return lua_chon