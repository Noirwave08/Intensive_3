import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Функция для загрузки данных
def load_data():
    return pd.read_excel("test_predicted.xlsx")

# Функция для отображения графика
def plot_forecast(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['final_predicted_price'], marker='o', linestyle='-', label='Прогнозируемая цена')
    plt.xlabel("Дата")
    plt.ylabel("Цена на арматуру")
    plt.title("Прогноз цен на арматуру")
    plt.legend()
    st.pyplot(plt)

# Интерфейс приложения
st.title("Прогноз цен на арматуру")

# Загрузка данных
data = load_data()

# Выбор даты
selected_date = st.selectbox("Выберите дату:", data['date'].astype(str))

# Отображение прогноза
predicted_price = data.loc[data['date'].astype(str) == selected_date, 'final_predicted_price'].values
if predicted_price.size > 0:
    st.write(f"### Прогнозируемая цена на {selected_date}: **{predicted_price[0]:.2f}** руб./тонна")
else:
    st.write("Данные для выбранной даты отсутствуют.")

# Построение графика
plot_forecast(data)
