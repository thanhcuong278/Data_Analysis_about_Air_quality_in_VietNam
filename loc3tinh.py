import pandas as pd
from datetime import datetime
from unidecode import unidecode  # Thư viện để loại bỏ dấu

# Đọc dữ liệu từ tệp CSV gốc
csv_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/historical_air_quality_2021_vi.csv"
df = pd.read_csv(csv_path)

# Chuyển đổi "Thời gian cập nhật" sang định dạng datetime
df["Thời gian cập nhật"] = pd.to_datetime(df["Thời gian cập nhật"], errors='coerce', utc=True)

# Tạo cột "Tháng"
df["Tháng"] = df["Thời gian cập nhật"].dt.strftime("%m/%Y")

# Chuyển đổi các cột sang kiểu số và xử lý giá trị không hợp lệ
cols_to_convert = ["Chỉ số AQI", "CO", "Độ ẩm", "Áp suất", "Bụi PM10", "Bụi PM2.5", "Nhiệt độ", "Tốc độ gió", "NO2", "O3", "SO2"]

for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "").replace("-", "0"), errors='coerce')

# Loại bỏ các hàng có giá trị NaN trong các cột cần thiết
df = df.dropna(subset=cols_to_convert)

# Chuyển đổi tên trạm sang không dấu
df["Tên trạm"] = df["Tên trạm"].apply(lambda x: unidecode(str(x)))

# Chỉ lấy dữ liệu cho 3 tỉnh Huế, Hà Nội, Ho Chi Minh (không dấu)
provinces = ["Hue", "Ha Noi", "Ho Chi Minh"]
df_provinces = df[df["Tên trạm"].str.contains("|".join(provinces), case=False)]

# Xác định tên tỉnh/thành phố dựa trên tên trạm (không dấu)
def get_province_name(station_name):
    station_name_lower = station_name.lower()  # Chuyển về chữ thường để kiểm tra
    if "hue" in station_name_lower:
        return "Huế"
    elif "ha noi" in station_name_lower:
        return "Hà Nội"
    elif "ho chi minh" in station_name_lower or "tphcm" in station_name_lower:
        return "TPHCM"
    else:
        return "Khác"

df_provinces["Tỉnh/Thành phố"] = df_provinces["Tên trạm"].apply(get_province_name)

# Đảm bảo cột "Tỉnh/Thành phố" không có giá trị NaN
df_provinces = df_provinces.dropna(subset=["Tỉnh/Thành phố"])

# Nhóm dữ liệu theo "Mã trạm", "Tháng", và "Tỉnh/Thành phố" và tính trung bình
summary_df = df_provinces.groupby(["Mã trạm", "Tháng", "Tỉnh/Thành phố"]).agg({
    "Chỉ số AQI": "mean",
    "CO": "mean",
    "Độ ẩm": "mean",
    "Áp suất": "mean",
    "Bụi PM10": "mean",
    "Bụi PM2.5": "mean",
    "Nhiệt độ": "mean",
    "Tốc độ gió": "mean",
    "NO2": "mean",
    "O3": "mean",
    "SO2": "mean",
}).reset_index()

# Làm tròn các giá trị tới một chữ số thập phân
summary_df = summary_df.round(1)

# Xuất dữ liệu sang tệp CSV mới
output_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/tong_hop_3_tinh.csv"
summary_df.to_csv(output_path, index=False)

print("Dữ liệu đã được xuất thành công tại:", output_path)
