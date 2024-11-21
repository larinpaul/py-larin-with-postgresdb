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
    'полнота': float,
    'корректность': float,
    'удобство': float,
    'защищенность': float
}

# Определение выходной переменной
output_variable = 'качество'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Получение входных значений из форм в html
    completeness = float(request.form['полнота'])
    correctness = float(request.form['корректность'])
    usability = float(request.form['удобство'])
    security = float(request.form['защищенность'])

    # Создание pandas DataFrame для хранения данных
    data = pd.DataFrame({
        'полнота': [completeness, completeness + 1, completeness + 222],
        'корректность': [correctness, correctness + 333331, correctness + 2],
        'удобство': [usability, usability + 1, usability + 3332],
        'защищенность': [security, security + 1, security + 3332]
    })
    # Calculate the 'качество' (quality) column
    data['качество'] = data['полнота'] * 0.25 + data['корректность'] * 0.25 + data['удобство'] * 0.25 + data['защищенность'] * 0.25

    #  Создание "тепловой карты" матрицы корреляции
    np.random.seed(0)
    mean = [0, 0, 0, 0]
    cov = [[0.98, 0.95, 0.85, 0.9], [0.95, 1, 0.8, 0.85], [0.85, 0.8, 1, 0.9], [0.9, 0.85, 0.9, 1]]
    data = np.random.multivariate_normal(mean, cov, size=100)
    df = pd.DataFrame(data, columns=['полнота', 'корректность', 'удобство', 'защищенность'])
    corr_matrix = df.corr()
    plt.figure(figsize=(5, 3))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, fmt='.2f', linewidths=0.5, linecolor='white')
    plt.title('Матрица корреляции')
    plt.savefig('static/correlation_matrix.png', bbox_inches='tight')

    # Create a linear regression model
    X = df[['полнота', 'корректность', 'удобство']]
    y = df['защищенность']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Расчет переменной (качество)
    quality = (completeness + correctness + usability + security) / 4
    quality = max(0, min(quality, 10))  # Ensure quality is between 0 and 10

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
