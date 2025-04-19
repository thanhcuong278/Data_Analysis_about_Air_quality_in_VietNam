import pandas as pd

# Đọc dữ liệu từ tệp CSV gốc
# csv_path = # "tong_hop_3_tinh.csv"
df = pd.read_csv(csv_path)

# Tạo cột "Tháng" nếu chưa có
if "Tháng" not in df.columns:
    df["Tháng"] = pd.to_datetime(df["Thời gian cập nhật"], format='ISO8601', errors='coerce', utc=True).dt.strftime("%m/%Y")

# Xác định các cột mong muốn
expected_columns = ["CO", "Sương", "Độ ẩm", "NO2", "O3", "Áp suất", "Bụi PM10", "Bụi PM2.5", "SO2", "Nhiệt độ", "Tốc độ gió", "Chỉ số AQI"]

# Thêm các cột bị thiếu với giá trị NaN hoặc giá trị mặc định
for column in expected_columns:
    if column not in df.columns:
        df[column] = float("nan")  # Giá trị mặc định là NaN

# Lọc dữ liệu cho các tháng cụ thể (01/2021 đến 11/2021)
months_to_include = ["01/2021", "02/2021", "03/2021", "04/2021", "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021"]
df_filtered = df[df["Tháng"].isin(months_to_include)]

# Tính giá trị trung bình theo tháng
monthly_average_df = df_filtered.groupby("Tháng").agg({column: "mean" for column in expected_columns}).reset_index()

# Làm tròn các giá trị số tới một chữ số thập phân
monthly_average_df = monthly_average_df.round(1)

# Xuất bảng thống kê trung bình theo tháng
output_path_avg = # "tong_hop_trung_binh_theo_thang.csv"
monthly_average_df.to_csv(output_path_avg, index=False)

print("Bảng thống kê trung bình theo tháng đã được tạo và lưu tại:", output_path_avg)
