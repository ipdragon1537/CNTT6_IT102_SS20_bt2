# 1.
# Lỗi IndexError: tuple index out of range xảy ra tại dòng r = p[2]
# vì tuple của "SofM" chỉ có 2 phần tử: ("SofM", 150)
# nên chỉ truy cập được p[0] và p[1], còn p[2] không tồn tại.
# "Levi" chạy được vì có đủ 3 phần tử: ("Levi", 120, 2500).
# 2.
# Nếu sửa "SofM" thành ("SofM", 150, 2800),
# chương trình sẽ sập ở dòng:
# b = (m * 10) + (int(r) * 0.5)
# khi xử lý "Optimus" vì r = "N/A".
# Hàm int("N/A") không chuyển đổi được sang số nguyên.
# Exception: ValueError: invalid literal for int() with base 10: 'N/A'
# 3.
# print("Đang xử lý:", p) giúp xác định chính xác bản ghi
# đang được xử lý trước khi lỗi xảy ra.
# Nhờ đó dễ phát hiện dữ liệu nào bị thiếu trường hoặc sai định dạng.
# 4.
# Theo Clean Code nên đổi tên:
# ds -> players
# p  -> player
# t  -> player_name
# m  -> matches_played
# r  -> mmr
# b  -> bonus_rp
# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu trường MMR
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR là chữ
]

def calculate_bonus(matches, mmr):
    """
    Hàm chuyên dụng để tính toán tiền thưởng (RP).
    Nhận vào số trận và điểm MMR, trả về tiền thưởng.
    """
    return (matches * 10) + (int(mmr) * 0.5)

def process_bonus(player_records):
    """
    Hàm duyệt danh sách, bẫy lỗi dữ liệu và hiển thị kết quả.
    """
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in player_records:
        # Lấy tên trước tiên để có thể dùng trong các câu thông báo lỗi
        name = record[0] 
        
        try:
            matches = record[1]
            mmr = record[2]  # Rủi ro sinh lỗi IndexError nằm ở đây
            
            # Rủi ro sinh lỗi ValueError (do ép kiểu int) nằm trong hàm này
            bonus = calculate_bonus(matches, mmr) 
            
            # In kết quả nếu mọi thứ đều hợp lệ
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            # Bẫy lỗi thiếu độ dài Tuple
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
            
        except ValueError:
            # Bẫy lỗi không thể ép kiểu chuỗi sang số
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
process_bonus(data)