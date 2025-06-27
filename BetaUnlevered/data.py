import pandas as pd
import numpy as np
from maths import run_regression 
from maths import unlever_beta_calculator

if __name__ == "__main__":
        df_mahindra = pd.read_excel('mahindra.xlsx')
        df_maruti = pd.read_excel('marutisuzuki.xlsx')
        df_olectra = pd.read_excel('olectra.xlsx')
        df_market = pd.read_excel('market_returns.xlsx')

        df_mahindra['Returns'] = np.log(df_mahindra['Price']/df_mahindra['Price'].shift(1)) * 100
        df_mahindra.loc[0, 'Returns'] = 0

        df_maruti['Returns'] = np.log(df_maruti['Price']/df_maruti['Price'].shift(1)) * 100
        df_maruti.loc[0, 'Returns'] = 0

        df_olectra['Returns'] = np.log(df_olectra['Price']/df_olectra['Price'].shift(1)) * 100
        df_olectra.loc[0, 'Returns'] = 0 

        df_market['Returns'] = np.log(df_market['Price']/df_market['Price'].shift(1)) * 100
        df_market.loc[0, 'Returns'] = 0

        X_universal = df_market[['Returns']]

        y_mahindra = df_mahindra['Returns']
        alpha_mahindra, beta_levered_mahindra = run_regression(X_universal, y_mahindra, 'Market Returns', 'Mahindra Returns')
        
        y_maruti = df_maruti['Returns']
        alpha_maruti, beta_levered_maruti = run_regression(X_universal, y_maruti, 'Market Returns', 'Maruti Returns')
        

        y_olectra = df_olectra['Returns']
        alpha_olectra, beta_levered_olectra = run_regression(X_universal, y_olectra, 'Market Returns', 'Olectra Returns')

        tax_rate = 0.25
        DE_mahindra = 1.4481
        DE_maruti = 0.009
        DE_olectra = 0.2421
        
        beta_unlevered_mahindra = unlever_beta_calculator(beta_levered_mahindra, tax_rate, DE_mahindra)
        #print(beta_unlevered_mahindra)

        beta_unlevered_maruti = unlever_beta_calculator(beta_levered_maruti, tax_rate, DE_maruti)
        #print(beta_unlevered_maruti)
        
        beta_unlevered_olectra = unlever_beta_calculator(beta_levered_olectra, tax_rate, DE_olectra)
        #print(beta_unlevered_olectra)

        sum = beta_unlevered_olectra + beta_unlevered_mahindra + beta_unlevered_maruti
        beta_unlevered = sum / 3
        #print(beta_unlevered)

        with open("beta_results.txt", "a") as file:
                file.write("Final Beta Results\n")
                file.write(f"Mahindra - Levered Beta : {beta_levered_mahindra} || Unlevered Beta : {beta_unlevered_mahindra}\n")
                file.write(f"Maruti Suzuki - Levered Beta : {beta_levered_maruti} || Unlevered Beta : {beta_unlevered_maruti}\n")
                file.write(f"Olectra Company - Levered Beta : {beta_levered_olectra} || Unlevered beta : {beta_unlevered_olectra}\n")

                file.write(f"Average Unlevered beta : {beta_unlevered}\n")


        


