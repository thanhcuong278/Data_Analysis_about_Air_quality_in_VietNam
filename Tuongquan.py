import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Đọc dữ liệu từ tệp CSV
csv_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/tong_hop_trung_binh_theo_thang.csv"
df = pd.read_csv(csv_path)

# Xử lý dữ liệu nếu cần thiết
df["Tháng"] = pd.to_datetime(df["Tháng"], format="%b-%y", errors='coerce')

# Khởi tạo đồ thị
fig, ax = plt.subplots(figsize=(12, 8))

# Chọn màu sắc cho các chất ô nhiễm
colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Màu xanh lam, xanh lá, đỏ, cyan, tím, vàng

# Danh sách các chất ô nhiễm và tên tương ứng trên trục x
pollutants = ['Bụi PM10', 'Bụi PM2.5', 'CO', 'NO2', 'O3', 'SO2']

# Tạo biểu đồ cho từng chất ô nhiễm
for i, pollutant in enumerate(pollutants):
    sns.scatterplot(data=df, x=pollutant, y='Chỉ số AQI', color=colors[i], ax=ax, label=pollutant)

# Thêm đường hồi quy cho chỉ số AQI (có thể thêm một đường hồi quy tổng hợp hoặc riêng biệt cho từng chất ô nhiễm)
sns.regplot(data=df, x='Bụi PM10', y='Chỉ số AQI', scatter=False, ax=ax, color='k', line_kws={'label': 'Đường hồi quy PM10'})

# Thêm tiêu đề và chú thích
ax.set_title('Mối tương quan giữa Chỉ số AQI và các chất ô nhiễm')
ax.set_xlabel('Chất ô nhiễm')
ax.set_ylabel('Chỉ số AQI')
ax.legend()  # Hiển thị chú thích

# Hiển thị trên Streamlit và xuất sang tệp
st.pyplot(fig)  # Hiển thị trên Streamlit
fig.savefig("C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton/combined_scatterplot_output.png")  # Xuất sang tệp
