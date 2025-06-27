import pandas as pd
import numpy as np

df_market = pd.read_excel('market_returns.xlsx')
df_market['Returns'] = np.log(df_market['Price']/df_market['Price'].shift(1)) * 100

total_sum = df_market['Returns'].sum()
market_average = total_sum / len(df_market['Returns'])

df_market['Average'] = market_average
df_market.loc[0, 'Returns'] = 0



df_tata = pd.read_excel('tatamotors.xlsx')

df_tata['Returns'] = np.log(df_tata['Price']/df_tata['Price'].shift(1)) * 100

total_s = df_tata['Returns'].sum()
t_average_returns = total_s/len(df_tata['Returns'])

df_tata['Average'] = t_average_returns
df_tata.loc[0,'Returns'] = 0

with open("tata_results.txt", "a") as file:
    file.write("Market Averages and Tata Returns Averages\n")
    file.write(f"Market Average (Rm) : {market_average}\n")
    file.write(f"Tata Motors market average : {t_average_returns}\n")

