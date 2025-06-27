import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def unlever_beta_calculator(beta_levered, tax_rate, debt_to_equity):
    beta_unlevered = beta_levered / (1 + (1-tax_rate) * debt_to_equity)
    return beta_unlevered

def run_regression(x, y, x_label, y_label):

    model = LinearRegression()
    model.fit(x,y)

    alpha = model.intercept_
    beta = model.coef_[0]
    y_predicted = model.predict(x)

    plt.figure(figsize= (8,5))
    plt.scatter(x, y, color = 'red', label = 'Actual Data')
    plt.plot(x, y_predicted, color='blue', label = 'Regression line' )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Linear Regression')

    #plt.text(x.min().iloc[0], max(y), f' y = {alpha:.2f} + {beta:.2f}x', fontsize = 10,
            # bbox = dict(facecolor = 'white', alpha = 0.6))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show()

    return alpha, beta