import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dữ liệu
@st.cache
def load_data():
    return pd.read_csv("Credit_risk_processed.csv")  # Đảm bảo tệp đúng định dạng CSV

data = load_data()

# Tiêu đề chính
st.title("Dashboard Phân tích Dữ liệu - Tập Dữ liệu Đã Tiền Xử Lý")

# Hiển thị dữ liệu
st.header("1. Hiển thị Dữ liệu")
st.write("Xem qua tập dữ liệu:")
st.dataframe(data)

# Thống kê tổng quan
st.header("2. Thống kê Tổng quan")
st.write(data.describe())

# Biểu đồ phân phối
st.header("3. Phân phối Các Biến Số")
column = st.selectbox("Chọn cột để hiển thị phân phối:", data.select_dtypes(include=["float64", "int64"]).columns)

fig, ax = plt.subplots()
ax.hist(data[column], bins=30, edgecolor="black", alpha=0.7)
ax.set_title(f"Phân phối của cột {column}")
ax.set_xlabel(column)
ax.set_ylabel("Tần suất")
st.pyplot(fig)

# Mối quan hệ giữa các biến
st.header("4. Mối Quan Hệ Giữa Các Biến")
x_axis = st.selectbox("Chọn biến X:", data.columns)
y_axis = st.selectbox("Chọn biến Y:", data.columns)

fig, ax = plt.subplots()
ax.scatter(data[x_axis], data[y_axis], alpha=0.6)
ax.set_title(f"Mối quan hệ giữa {x_axis} và {y_axis}")
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
st.pyplot(fig)

# Bộ lọc
st.header("5. Lọc Dữ Liệu")
filter_column = st.selectbox("Chọn cột để lọc:", data.columns)
unique_values = data[filter_column].unique()
selected_value = st.selectbox("Chọn giá trị:", unique_values)

filtered_data = data[data[filter_column] == selected_value]
st.write("Dữ liệu sau khi lọc:")
st.dataframe(filtered_data)
