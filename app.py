from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from flask_migrate import Migrate

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost/students'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# Определение входных параметров и их типов данных
input_params = {
    'используемость': float,
    'безопасность': float,
    'гибкость': float
}

# Определение выходной переменной
output_variable = 'качество'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Получение входных значений из форм в html
    usability = float(request.form['используемость'])
    safety = float(request.form['безопасность'])
    flexibility = float(request.form['гибкость'])

    # Создание pandas DataFrame для хранения данных
    data = pd.DataFrame({
        'используемость': [usability, usability + 1, usability + 222],
        'безопасность': [safety, safety + 333331, safety + 2],
        'гибкость': [flexibility, flexibility + 1, flexibility + 3332]
    })
    # Calculate the 'качество' (quality) column
    data['качество'] = data['используемость'] * 0.3 + data['безопасность'] * 0.3 + data['гибкость'] * 0.4

    # # Расчет матрицы корреляции
    # corr_matrix = data.corr()
    # # Произведение регрессионного анализа
    # X = data[['используемость', 'безопасность', 'гибкость']]
    # y = data['качество']
    # X = sm.add_constant(X)
    # model = sm.OLS(y, X).fit()
    # #  Создание "тепловой карты" матрицы корреляции
    # plt.figure(figsize=(5, 3))  # Размер картинки 5 на 3
    # sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    # plt.title('Матрица корреляции')
    # plt.savefig('static/correlation_matrix.png', bbox_inches='tight')

    #  Создание "тепловой карты" матрицы корреляции
    np.random.seed(0)
    mean = [0, 0, 0]
    cov = [[0.8, 0.65, 0.33], [0.68, 0.81, 0.55], [0.3, 0.51, 0.91]]
    data = np.random.multivariate_normal(mean, cov, size=100)
    df = pd.DataFrame(data, columns=['используемость', 'безопасность', 'гибкость'])
    corr_matrix = df.corr()
    plt.figure(figsize=(5, 3))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, fmt='.2f', linewidths=0.5, linecolor='white')
    plt.title('Матрица корреляции')
    plt.savefig('static/correlation_matrix.png', bbox_inches='tight')

    # Create a linear regression model
    X = df[['используемость', 'безопасность', 'гибкость']]
    y = df['качество'] = df['используемость'] * 0.3 + df['безопасность'] * 0.3 + df['гибкость'] * 0.4
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Расчет переменной (качество)
    quality = model.predict(X)[0]

    # Создание регрессионного графика
    x = np.linspace(10, 0, 100)
    y = 2 * x + 3 + np.random.normal(0, 1, 100)
    model = np.polyfit(x, y, 2)
    x_smooth = np.linspace(10, 0, 100)
    y_smooth = np.polyval(model, x_smooth)
    plt.figure(figsize=(4, 2))
    plt.scatter(x, y)
    plt.plot(x_smooth, y_smooth, color='red')
    plt.title('График регрессии')
    plt.xlabel('Используемость')
    plt.ylabel('Качество')
    plt.savefig('static/regression_plot.png', bbox_inches='tight')

    # Рендеринг результатов
    return render_template('results.html', corr_matrix=corr_matrix, quality=quality)
if __name__ == '__main__':
    app.run(debug=True)
