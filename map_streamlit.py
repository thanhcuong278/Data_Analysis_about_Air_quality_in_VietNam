import streamlit as st
import plotly.express as px
import pandas as pd

# Tiêu đề ứng dụng
st.title("Bản đồ Chất lượng Không khí tại Việt Nam")

# Dữ liệu với các thành phố, tọa độ, và chỉ số AQI
data = pd.DataFrame({
    'Thành phố': ['Hà Nội', 'TP. Hồ Chí Minh', 'Huế'],
    'Vĩ độ': [21.0285, 10.8231, 16.4637],  # Thêm tọa độ
    'Kinh độ': [105.8542, 106.6297, 107.5905],  # Thêm kinh độ
    'AQI': [70, 66.4, 31.4]  # Chỉ số AQI
})

# Tạo thang màu từ xanh (chỉ số thấp) đến đỏ (chỉ số cao)
custom_color_scale = [
    [0, 'lightgreen'],  # Xanh lá nhạt cho chỉ số thấp
    [0.5, 'orange'],  # Chuyển sang cam
    [1, 'red']  # Đỏ đậm cho chỉ số cao
]

# Tạo scatter mapbox hiển thị mức độ AQI
fig = px.scatter_mapbox(
    data,
    lat='Vĩ độ',
    lon='Kinh độ',
    color='AQI',  # Màu sắc theo chỉ số AQI
    color_continuous_scale=custom_color_scale,  # Thang màu tùy chỉnh
    hover_name='Thành phố',
    hover_data=['AQI'],  # Thông tin bổ sung khi di chuột
    zoom=5,
    height=500,
    width=700,
    size=[10] * len(data),  # Kích thước cố định của các điểm
    size_max=10  # Kích thước tối đa
)

# Tùy chỉnh kiểu bản đồ với màu sắc trung tính cho phần nền
fig.update_layout(
    mapbox_style="carto-positron",  # Kiểu bản đồ với màu trắng/xám nhẹ
    coloraxis_colorbar=dict(
        title="Chỉ số AQI",  # Tiêu đề cho thang màu
        ticks="outside"  # Định dạng đánh dấu
    ),
    mapbox=dict(
        bearing=0,  # Giữ góc nhìn phẳng
        pitch=0,  # Giữ góc nhìn phẳng
        center=dict(lat=16.0, lon=107.0),  # Tập trung vào Việt Nam
        zoom=5  # Mức độ phóng to
    )
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)  # Hiển thị biểu đồ
