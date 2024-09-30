# Khởi tạo danh sách công việc
to_do_list = []

# Hiển thị menu tùy chọn
def hien_thi_menu():
    print("\nChương trình quản lý danh sách công việc")
    print("1. Thêm công việc")
    print("2. Xóa công việc")
    print("3. Xem danh sách công việc")
    print("4. Thoát")

# Thêm công việc vào danh sách
def them_cong_viec():
    cong_viec = input("Nhập tên công việc cần thêm: ")
    to_do_list.append(cong_viec)
    print(f"Đã thêm công việc: {cong_viec}")

# Xóa công việc khỏi danh sách
def xoa_cong_viec():
    xem_danh_sach()  # Hiển thị danh sách trước khi xóa
    try:
        index = int(input("Nhập số thứ tự công việc muốn xóa: "))
        if 0 <= index < len(to_do_list):
            cong_viec_da_xoa = to_do_list.pop(index)
            print(f"Đã xóa công việc: {cong_viec_da_xoa}")
        else:
            print("Số thứ tự không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số thứ tự hợp lệ!")

# Hiển thị danh sách công việc
def xem_danh_sach():
    if len(to_do_list) == 0:
        print("Danh sách công việc trống.")
    else:
        print("\nDanh sách công việc:")
        for i, cong_viec in enumerate(to_do_list):
            print(f"{i}. {cong_viec}")

# Chương trình chính
def chuong_trinh_quan_ly():
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng (1-4): ")
        
        if lua_chon == '1':
            them_cong_viec()
        elif lua_chon == '2':
            xoa_cong_viec()
        elif lua_chon == '3':
            xem_danh_sach()
        elif lua_chon == '4':
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

# Gọi chương trình chính
chuong_trinh_quan_ly()
