import pandas as pd
import folium
import branca.colormap as cm
from folium import plugins

# Dữ liệu mẫu với các thành phố, tọa độ, và chỉ số AQI
data = pd.DataFrame({
    'Thành phố': ['Hà Nội', 'TP. Hồ Chí Minh', 'Huế'],
    'Vĩ độ': [21.0285, 10.8231, 16.4637],
    'Kinh độ': [105.8542, 106.6297, 107.5905],
    'AQI': [70, 66.4, 31.4]  # Chỉ số AQI
})

# Tạo bản đồ Folium với kiểu màu nền xám trắng
map = folium.Map(location=[14.0583, 108.2772], zoom_start=6, tiles='cartodbpositron')

# Thêm MarkerCluster để nhóm các điểm gần nhau
marker_cluster = plugins.MarkerCluster().add_to(map)

# Tạo thang màu với branca.colormap
# Thang màu từ vàng đến đỏ (biểu thị mức độ ô nhiễm tăng dần)
color_map = cm.linear.YlOrRd_09.scale(data['AQI'].min(), data['AQI'].max())

# Thêm các Marker cho mỗi thành phố với màu sắc dựa trên chỉ số AQI
for index, row in data.iterrows():
    popup_content = f"Thành phố: {row['Thành phố']}<br>AQI: {row['AQI']}<br>"

    # Xác định màu của Marker dựa trên giá trị AQI
    marker_color = color_map(row['AQI'])  # Lấy màu từ thang màu dựa trên giá trị AQI

    folium.CircleMarker(  # Sử dụng CircleMarker để dễ nhận biết màu
        location=[row['Vĩ độ'], row['Kinh độ']],
        radius=10,  # Kích thước của Marker
        color='black',  # Đường viền
        fill=True,  # Điền màu bên trong
        fill_color=marker_color,  # Màu của Marker dựa trên chỉ số AQI
        fill_opacity=0.7,  # Độ trong suốt của màu
        popup=popup_content,  # Nội dung khi click vào Marker
    ).add_to(marker_cluster)

# Thêm chú thích màu (color bar) vào bản đồ
color_map.caption = "Chỉ số AQI"  # Tiêu đề cho chú thích màu
color_map.add_to(map)  # Thêm chú thích vào bản đồ

# Lưu bản đồ vào tệp HTML
map.save('Map1.html')
