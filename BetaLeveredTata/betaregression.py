import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from totalReturns import df_market, df_tata

X = df_market[['Returns']]
y = df_tata['Returns']

model = LinearRegression()
model.fit(X, y)
y_predict = model.predict(X)

r2 = r2_score(y, y_predict)
alpha = model.intercept_
beta = model.coef_[0]

plt.scatter(X, y, color = 'red', label = 'Actual Returns')
plt.plot(X, y_predict, color='blue', label = 'Regression line')

plt.xlabel('Market Returns')
plt.ylabel('Tata Returns')
plt.title('Linear Regression of Tata returns (vs) Market Returns')
plt.text(0.05, 0.95, f'Intercept (alpha): {alpha:.4f}\n Slope (Beta): {beta:.4f}'
         ,transform = plt.gca().transAxes, fontsize = 10, verticalalignment = 'top',
          bbox = dict(boxstyle='round', facecolor='white', alpha = 0.5) )
plt.legend()

plt.savefig('regression_plot.png', dpi=400)
plt.show()

with open("tata_results.txt", "a") as file:
    file.write("The results between Market and Tata Motors\n")
    file.write(f"Beta levered of Tata Motors : {beta}\n")
    file.write(f"Alpha for the regression : {alpha}")


