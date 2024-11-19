from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:password@localhost/students'
db = SQLAlchemy(app)


# Определение входных параметров и их типов данных
input_params = {
    'usability': float,
    'safety': float,
    'flexibility': float
}

# Определение выходной переменной
output_variable = 'quality'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Получение входных значений из форм в html
    usability = float(request.form['usability'])
    safety = float(request.form['safety'])
    flexibility = float(request.form['flexibility'])

    # Создание pandas DataFrame для хранения данных
    data = pd.DataFrame({
        'usability': [usability, usability + 1, usability + 222],
        'safety': [safety, safety + 333331, safety + 2],
        'flexibility': [flexibility, flexibility + 1, flexibility + 3332]
    })

    # Расчет матрицы корреляции
    corr_matrix = data.corr()

    # Произведение регрессионного анализа
    X = data[['usability', 'safety']]
    y = data['flexibility']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    #  Создание "тепловой карты" матрицы корреляции
    plt.figure(figsize=(5, 3))  # Размер картинки 5 на 3
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.savefig('static/correlation_matrix.png', bbox_inches='tight')  # Save the picture with a tight bounding box

    # Расчет переменной (качество)
    quality = model.predict(X)[0]

    # Создание регрессионного графика
    y_pred = model.predict(X)
    plt.figure(figsize=(4, 2))  # Размер картинки 4 на 2
    plt.scatter(X['usability'], y)
    plt.plot(X['usability'], y_pred, color='red')
    plt.title('Regression Plot')
    plt.xlabel('Usability')
    plt.ylabel('Flexibility')
    plt.savefig('static/regression_plot.png', bbox_inches='tight')

    # Рендеринг результатов
    return render_template('results.html', corr_matrix=corr_matrix, quality=quality)

if __name__ == '__main__':
    app.run(debug=True)
