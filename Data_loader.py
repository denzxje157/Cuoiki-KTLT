def lay_du_lieu():
    list_en = []
    list_vi = []
    try:
        f = open("tuvung.txt", "r", encoding="utf-8")
        for dong in f:
            dong = dong.strip()
            if dong != "":
                tach = dong.split(",")
                list_en.append(tach[0])
                list_vi.append(tach[1])
        f.close()
    except:
        print("Khong tim thay file tuvung.txt!")
    return list_en, list_vi