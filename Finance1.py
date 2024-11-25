import numpy as np 
## PORTFOLIO RETURN CALCULATION
stock_prices=np.array([10,20,30])
log_returns=np.log(stock_prices[1:]/stock_prices[:-1])
print("log returns:",log_returns) 

stock_prices=np.array([40,50,60])
log_returns=np.log(stock_prices[1:]/stock_prices[:-1])
print("log returns:",log_returns)

stock_prices=np.array([70,80,90])
log_returns=np.log(stock_prices[1:]/stock_prices[:-1]) 
print("log returns:",log_returns) 
returns=np.array([[0.69314718, 0.40546511],[0.22314355, 0.18232156],[0.13353139, 0.11778304]])
weights=np.array([0.5,0.2])
portfolio_returns=np.dot(returns,weights)
print("portfolio returns:",portfolio_returns)

##STATISTICAL ANALYSIS FOR FINANCE
 # Mean and Standard Deviation (Volatility)
mean_return=np.mean(returns, axis=0)
volatility=np.std(returns, axis=0)
print("means returns:",mean_return)
print("volatility (standard deviation):",volatility)
    # Covariance and Correlation
cov_matrix = np.cov(returns.T) 
print("Covariance Matrix:\n", cov_matrix)
    # Correlation Matrix
corr_matrix = np.corrcoef(returns.T) 
print("Correlation Matrix:\n", corr_matrix)
    
    ####-TILL CORRELATION DONE
    ## note[JAB V CODE COPY KARO ENSURE KI 1ST LETTER SE LAST HOA , AIESE NHI KI 1ST letter se pehle ka kuch blanl copy kar diya hoa, ya last letter  KE badh KUCH BLANK copy kr diya hoa, if aiese huwa toa error aayega keh ke unexppected error]





