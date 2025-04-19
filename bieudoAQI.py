import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os  # Để làm việc với hệ thống tệp

# Tiêu đề ứng dụng Streamlit
st.title("Biểu đồ Chỉ số AQI của TP. Hồ Chí Minh, Huế, và Hà Nội (2021)")

# Dữ liệu chỉ số AQI từ tháng 1 đến tháng 11/2021 cho ba tỉnh
data = {
    'Tháng': ['01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021', '07/2021', '08/2021', '09/2021', '10/2021', '11/2021'],
    'Hồ Chí Minh': [101.00, 91.20, 71.56, 76.09, 60.46, 49.70, 50.00, 63.18, 37.56, 51.50, 78.38],
    'Huế': [18.89, 51.87, 23.33,0,0,0,0,0,0,0,0],  # Có ít hơn 11 mục
    'Hà Nội': [157.78, 128.93, 131.00, 109.80, 93.29, 62.10, 68.00, 78.00, 90.22, 90.83, 85.00]
}

# Đảm bảo mọi cột có cùng số lượng mục
expected_length = len(data['Tháng'])  # Độ dài mong muốn là 11

for key, value in data.items():
    if len(value) != expected_length:
        print(f"Cột '{key}' có số lượng mục không phù hợp ({len(value)}), phải là {expected_length}")

# Chỉnh lại cột 'Huế' để có đủ 11 mục
data['Huế'] += [0.0] * (expected_length - len(data['Huế']))  # Thêm giá trị 0.0 để cân bằng chiều dài

# Sau khi sửa lỗi, tạo DataFrame
df = pd.DataFrame(data)


# Vẽ biểu đồ
fig, ax = plt.subplots()
ax.plot(df['Tháng'], df['Hồ Chí Minh'], label='Hồ Chí Minh', linestyle='-', marker='o')
ax.plot(df['Tháng'], df['Huế'], label='Huế', linestyle='-', marker='o')
ax.plot(df['Tháng'], df['Hà Nội'], label='Hà Nội', linestyle='-', marker='o')

# Thêm nhãn giá trị cho mỗi điểm
for i in range(len(df['Tháng'])):
    ax.text(df['Tháng'][i], df['Hồ Chí Minh'][i], f"{df['Hồ Chí Minh'][i]:.2f}", ha='left', va='bottom', fontsize=8)
    ax.text(df['Tháng'][i], df['Huế'][i], f"{df['Huế'][i]:.2f}", ha='right', va='top', fontsize=8)
    ax.text(df['Tháng'][i], df['Hà Nội'][i], f"{df['Hà Nội'][i]:.2f}", ha='center', va='bottom', fontsize=8)

ax.set_xlabel('Tháng')
ax.set_ylabel('Chỉ số AQI')
ax.set_title('Biểu đồ Chỉ số AQI của TP. Hồ Chí Minh, Huế, và Hà Nội (2021)')
ax.legend()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)

# Lưu vào thư mục hiện tại
file_path = "C:/Users/Duy Khanh/OneDrive/Desktop/train_pyhton./bieudoAQI.png"  # Đường dẫn và tên tệp
fig.savefig(file_path)  # Lưu biểu đồ vào file