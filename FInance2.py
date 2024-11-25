### TIME SERIES ANALYSIS

import numpy as np
## Sample stock prices for 4 consecutive days
stock_prices=np.array([10,20,30,40])
# Calculate the 3-day moving average
moving_average_3_day=np.convolve(stock_prices, np.ones(3)/3, mode='valid')
# Print the results
print("stock_prices:", stock_prices)
print("moving average 3 day:", moving_average_3_day)

## Cumulative returns(VVI- toa yaha par, why we are using stock_prices? q ki hum cumulative returns stock_prices ka hie nikal rhae hai toa hum jish ka nikalnege ush ka yaha par aayega, it it is like, log retiurn upar me likha hoata than , hum yaha v ;log_returns likh tey okay)
cumulative_returns = np.cumprod(1 + stock_prices) - 1
print("Cumulative Returns for each day:", cumulative_returns)

### Portfolio Optimization
## Calculate portfolio variance using asset covariance.


cov_matrix=np.array( [[0.0903506,0.04527552],[0.04527552,0.02278654]])
# Given portfolio weight
weights =np.array([0.5,0.3])
# Portfolio variance
portfolio_variance=np.dot(weights.T, np.dot(cov_matrix, weights))
print("Portfolio Variance:", portfolio_variance)

###Monte Carlo Simulation for Finance

s0=100
mu=0.05
sigma=0.2
T=3
Dt=3/252
n_steps=int(T/Dt)
random_shocks=np.random.normal(0,1,n_steps)
price_path=np.exp(np.cumsum((mu-0.05*sigma**2)*Dt+sigma*np.sqrt(Dt)*random_shocks))
print("simulated price return:", price_path)

###Value at Risk (VaR)
## Calculate 5% VaR
var_95=np.percentile(returns,5)
print("Value At Risk(95% of confidence):", var_95)

### Principal Component Analysis (PCA)

#( eish ke liye hamare pass pehle se assets return and covarinace matrix hona cha hieye, jaies emne upar nikala hae, YA PHIR AAP NAYA NIKALOA #SURU se, aur jab hum eigen vectors ka N laga ke ya bina N lagayeh normally print kremge the value remian same)
 
## Eigenvalue Decomposition

asset_returns=np.array([[0.01, 0.02], [0.03, 0.01], [-0.01, -0.02]])
cov_matrix=np.cov(asset_returns.T)

eigenvalues, eigenvectors= np.linalg.eig(cov_matrix)
print("eigenvalues:", eigenvalues)
print("eigenvectors:\n", eigenvectors)
print("eigenvectors:", eigenvectors)


