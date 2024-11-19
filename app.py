from flask import Flask, request, render_template
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

# Define input parameters and their data types
input_params = {
    'usability': float,
    'safety': float,
    'flexibility': float
}

# Define output variable
output_variable = 'quality'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get input values from form
    usability = float(request.form['usability'])
    safety = float(request.form['safety'])
    flexibility = float(request.form['flexibility'])

    # Create a pandas DataFrame to store the data
    data = pd.DataFrame({
        'usability': [usability],
        'safety': [safety],
        'flexibility': [flexibility]
    })

    # Calculate correlation matrix
    corr_matrix = data.corr()

    # Replace NaN values with 0
    corr_matrix = corr_matrix.fillna(0)

    # Perform regression analysis
    X = data[['usability', 'safety', 'flexibility']]
    y = pd.Series([1]) # dummy output variable (we'll calculate it later)
    X = sm.add_constant(X)
    model= sm.OLS(y, X).fit()

    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(6, 4))  # Make the picture smaller
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.savefig('static/correlation_matrix.png', bbox_inches='tight')  # Save the picture with a tight bounding box

    # Calculate output variable (quality)
    quality = model.predict(X)[0]

    # Create a regression plot
    X = data[['usability', 'safety']]
    y = data['flexibility']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)
    plt.figure(figsize=(6, 4))  # Make the picture smaller
    plt.scatter(X['usability'], y)
    plt.plot(X['usability'], y_pred, color='red')
    plt.title('Regression Plot')
    plt.xlabel('Usability')
    plt.ylabel('Flexibility')
    plt.savefig('static/regression_plot.png', bbox_inches='tight')  # Save the picture with a tight bounding box

    # Render results template
    return render_template('results.html', corr_matrix=corr_matrix, quality=quality)

if __name__ == '__main__':
    app.run(debug=True)
