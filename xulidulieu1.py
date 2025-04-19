import pandas as pd
# Đọc dữ liệu từ tệp CSV
csv_path = # "historical_air_quality_2021_vi.csv"  # Đường dẫn đến tệp CSV
df = pd.read_csv(csv_path)

# Thay thế các ô có dấu "-" bằng 0
df = df.replace("-", 0)  # Thay thế tất cả "-" bằng 0

# Chuyển đổi cột thời gian sang định dạng datetime
df["Thời gian cập nhật"] = pd.to_datetime(df["Thời gian cập nhật"], format='mixed', errors='coerce')

# Xóa các cột không cần thiết
df = df.drop(columns=["Trạng thái cảnh báo", "Mức độ cảnh báo"])

# Lọc các trạm Huế, HCM và Hà Nội
hue_df = df[df["Tên trạm"].str.contains("Huế", case=False, na=False)]
hcm_df = df[df["Tên trạm"].str.contains("Hồ Chí Minh", case=False, na=False)]
hanoi_df = df[df["Tên trạm"].str.contains("Hà Nội", case=False, na=False)]

# Lưu dữ liệu đã lọc vào các tệp CSV riêng biệt, bao gồm tất cả dữ liệu
hue_df.to_csv( , index=False)  # Dữ liệu trạm tại Huế: "hue_data.csv"
hcm_df.to_csv( , index=False)  # Dữ liệu trạm tại Hồ Chí Minh: hcm_data.csv
hanoi_df.to_csv( , index=False)  # Dữ liệu trạm tại Hà Nội: hanoi_data.csv

print("Dữ liệu đã được xử lý và lưu vào các tệp CSV riêng biệt.")
