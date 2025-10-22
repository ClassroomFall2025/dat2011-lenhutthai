# Hàm tính tiền nước
gia_ban_nuoc = (7500, 8800, 12000, 24000)
def tinh_tien_nuoc(so_nuoc):
    tien_nuoc = 0
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc
# Hàm tính nguyên liệu
def tinh_nguyen_lieu(so_dauxanh, so_thapcam, so_deo):
    # Lượng nguyên liệu cho mỗi loại bánh (kg)
    nguyen_lieu_banh = {
        "dauxanh": {"duong": 0.04, "dau": 0.07},
        "thapcam": {"duong": 0.06, "dau": 0.00},
        "deo": {"duong": 0.05, "dau": 0.02}
    }
    # Tính tổng lượng đường và đậu
    duong = (so_dauxanh * nguyen_lieu_banh["dauxanh"]["duong"] +
             so_thapcam * nguyen_lieu_banh["thapcam"]["duong"] +
             so_deo * nguyen_lieu_banh["deo"]["duong"])
    
    dau = (so_dauxanh * nguyen_lieu_banh["dauxanh"]["dau"] +
            so_thapcam * nguyen_lieu_banh["thapcam"]["dau"] +
            so_deo * nguyen_lieu_banh["deo"]["dau"])
    # Trả về dictionary
    return {"duong": duong, "dau": dau}