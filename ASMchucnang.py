import csv
import os
from ASMnhanvien import NhanVien, TiepThi, TruongPhong
from ASMunities import find_by_ma, input_nonempty, input_float

DATA_FILE = "data.csv"
CSV_HEADER = ["type","ma","ho_ten","luong","doanh_so","ty_le","luong_trach_nhiem"]

# Y2: load (đọc file)
def load_from_file(filename=DATA_FILE):
    ds = []
    if not os.path.exists(filename):
        return ds
    with open(filename, mode="r", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=CSV_HEADER)
        # skip header if present
        first = next(reader, None)
        # detect header row
        if first and first.get("type","").lower() == "type":
            # already header, continue reading real rows
            pass
        else:
            # first is actual row (not header) -> process it
            if first:
                row = first
                _append_row_to_ds(row, ds)
        for row in reader:
            _append_row_to_ds(row, ds)
    return ds

def _append_row_to_ds(row, ds):
    t = (row.get("type") or "NV").strip().upper()
    if t == "TT":
        ds.append(TiepThi.from_dict(row))
    elif t == "TP":
        ds.append(TruongPhong.from_dict(row))
    else:
        ds.append(NhanVien.from_dict(row))

# Y1: save (lưu file)
def save_to_file(ds, filename=DATA_FILE):
    with open(filename, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
        writer.writeheader()
        for nv in ds:
            writer.writerow(nv.to_dict())
    print(f"Đã lưu {len(ds)} nhân viên vào '{filename}'.")

# Y1 (nhập & lưu)
def nhap_nhan_vien(ds):
    print("Chọn loại nhân viên: 1-Hành chính, 2-Tiếp thị, 3-Trưởng phòng")
    loai = input_nonempty("Loại (1/2/3): ")
    ma = input_nonempty("Mã nhân viên: ")
    # kiểm tra mã trùng
    idx, _ = find_by_ma(ds, ma)
    if idx != -1:
        print("Mã đã tồn tại. Hủy nhập.")
        return
    ho_ten = input_nonempty("Họ tên: ")
    luong = input_float("Lương cơ bản (VND): ", allow_zero=False)
    if loai == "2":
        doanh_so = input_float("Doanh số (VND): ")
        ty_le = input_float("Tỉ lệ hoa hồng (%) : ")
        nv = TiepThi(ma, ho_ten, luong, doanh_so, ty_le)
    elif loai == "3":
        luong_tn = input_float("Lương trách nhiệm (VND): ")
        nv = TruongPhong(ma, ho_ten, luong, luong_tn)
    else:
        nv = NhanVien(ma, ho_ten, luong)
    ds.append(nv)
    print("Đã thêm nhân viên:")
    print(nv)

# Y3: tìm theo mã (giao diện)
def tim_theo_ma(ds):
    ma = input_nonempty("Nhập mã cần tìm: ")
    idx, nv = find_by_ma(ds, ma)
    if idx == -1:
        print("Không tìm thấy.")
    else:
        print("Tìm được:\n", nv)

# Y4: xóa theo mã
def xoa_theo_ma(ds):
    ma = input_nonempty("Nhập mã cần xóa: ")
    idx, nv = find_by_ma(ds, ma)
    if idx == -1:
        print("Không tìm thấy.")
        return
    confirm = input(f"Xác nhận xóa {nv.ho_ten} (y/n)? ").strip().lower()
    if confirm == "y":
        ds.pop(idx)
        save_to_file(ds)
        print("Đã xóa và cập nhật file.")
    else:
        print("Hủy xóa.")

# Y5: cập nhật theo mã
def cap_nhat_theo_ma(ds):
    ma = input_nonempty("Nhập mã cần cập nhật: ")
    idx, nv = find_by_ma(ds, ma)
    if idx == -1:
        print("Không tìm thấy.")
        return
    print("Nhân viên hiện tại:\n", nv)
    print("Bỏ trống nếu không muốn thay đổi.")
    new_name = input("Họ tên mới: ").strip()
    if new_name:
        nv.ho_ten = new_name
    new_luong = input("Lương mới (VND): ").strip()
    if new_luong:
        try:
            nv.luong = float(new_luong)
        except:
            print("Giá trị lương không hợp lệ. Giữ nguyên.")

# Y6: tìm theo khoảng thu nhập
def tim_theo_khoang_luong(ds):
    print("Nhập khoảng thu nhập (VND). Ví dụ: 5000000 15000000")
    while True:
        parts = input("Min Max: ").split()
        if len(parts) != 2:
            print("Nhập chính xác 2 số (min và max).")
            continue
        try:
            a = float(parts[0]); b = float(parts[1])
            if a > b:
                a, b = b, a
            break
        except:
            print("Nhập số hợp lệ.")
    found = [nv for nv in ds if a <= nv.get_thunhap() <= b]
    if not found:
        print("Không có nhân viên trong khoảng.")
    else:
        print(f"Tìm được {len(found)} nhân viên:")
        for nv in found:
            print(nv)

# Y7: sắp xếp theo họ tên
def sap_xep_theo_ho_ten(ds):
    def key_name(nv):
        parts = nv.ho_ten.strip().split()
        last = parts[-1].lower() if parts else ""
        return (last, nv.ho_ten.lower())
    ds.sort(key=key_name)
    print("Đã sắp xếp theo họ/tên.")

# Y8: sắp xếp theo thu nhập
def sap_xep_theo_thu_nhap(ds, descending=True):
    ds.sort(key=lambda nv: nv.get_thunhap(), reverse=descending)
    print("Đã sắp xếp theo thu nhập.")

# Y9: top 5 thu nhập cao nhất
def top_5_thu_nhap(ds):
    if not ds:
        print("Danh sách rỗng.")
        return
    ds_sorted = sorted(ds, key=lambda nv: nv.get_thunhap(), reverse=True)
    top5 = ds_sorted[:5]
    print("Top 5 nhân viên theo thu nhập:")
    for nv in top5:
        print(nv)

# hiển thị toàn bộ danh sách
def xuat_danh_sach(ds):
    if not ds:
        print("Danh sách rỗng.")
    else:
        for nv in ds:
            print(nv)
