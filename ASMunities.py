def find_by_ma(ds, ma):
    for i, nv in enumerate(ds):
        if nv.ma == ma:
            return i, nv
    return -1, None

def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Không được bỏ trống.")

def input_float(prompt, allow_zero=True):
    while True:
        val = input(prompt).strip()
        try:
            v = float(val)
            if not allow_zero and v == 0:
                print("Không được để 0.")
                continue
            return v
        except:
            print("Nhập số hợp lệ.")
