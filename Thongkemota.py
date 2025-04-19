import pandas as pd
import streamlit as st
# Đường dẫn đến các tệp CSV
hue_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/hue_data.csv"  # Đường dẫn đến tệp CSV cho Huế
hcm_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/hcm_data.csv"  # Đường dẫn đến tệp CSV cho Hồ Chí Minh
hanoi_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/hanoi_data.csv"  # Đường dẫn đến tệp CSV cho Hà Nội

# Đọc dữ liệu từ các tệp CSV
hue_df = pd.read_csv(hue_path)
hcm_df = pd.read_csv(hcm_path)
hanoi_df = pd.read_csv(hanoi_path)

# Chỉ lấy các cột liên quan đến thống kê mô tả: NO2, O3, SO2, PM2.5, PM10
columns_of_interest = ["NO2", "O3", "SO2", "Bụi PM2.5", "Bụi PM10"]

hue_stats = hue_df[columns_of_interest].describe()  # Thống kê cho Huế
hcm_stats = hcm_df[columns_of_interest].describe()  # Thống kê cho Hồ Chí Minh
hanoi_stats = hanoi_df[columns_of_interest].describe()  # Thống kê cho Hà Nội

# Hiển thị tiêu đề ứng dụng
st.title("Thống kê mô tả cho các trạm chất lượng không khí")

# Thống kê mô tả cho dữ liệu Huế
st.subheader("Thống kê mô tả cho Huế")
st.write(hue_stats)

# Thống kê mô tả cho dữ liệu Hồ Chí Minh
st.subheader("Thống kê mô tả cho Hồ Chí Minh")
st.write(hcm_stats)

# Thống kê mô tả cho dữ liệu Hà Nội
st.subheader("Thống kê mô tả cho Hà Nội")
st.write(hanoi_stats)
