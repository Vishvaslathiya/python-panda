import pandas as pd
import numpy as np

# Create sample portfolio data
# Let's assume we have a portfolio of selected stocks from both markets
# This is sample data for illustration purposes
portfolio_returns = pd.DataFrame({
    'Date': pd.date_range(start='2006-01-31', end='2023-12-31', freq='ME'),
    'Portfolio_Return': np.random.normal(0.008, 0.025, 216)  # Monthly returns with mean 0.8% and std 2.5%
})

# Calculate market returns from the provided data
aus_market = pd.DataFrame({
    'Date': pd.to_datetime([date for date in range(2006, 2024)]),
    'Price': [4929.6, 5669.9, 6339.8, 3722.3, 4870.6, 4745.2, 4056.6, 4648.9, 5352.2, 5411.0, 
              5295.9, 5665.8, 6065.1, 5646.4, 6684.1, 6587.1, 7444.6, 7038.7]
})

aus_market['Market_Return'] = aus_market['Price'].pct_change()

# Risk-free rate (from provided data)
rf_rate_annual = 0.03  # 3% for Australia
rf_rate_monthly = (1 + rf_rate_annual)**(1/12) - 1

def calculate_performance_metrics(portfolio_returns, market_returns, rf_rate):
    """Calculate key performance metrics"""
    # Annualize returns
    portfolio_return_annual = (1 + portfolio_returns.mean())**12 - 1
    market_return_annual = (1 + market_returns.mean())**12 - 1
    
    # Calculate volatilities (annualized)
    portfolio_vol = portfolio_returns.std() * np.sqrt(12)
    market_vol = market_returns.std() * np.sqrt(12)
    
    # Calculate beta
    covariance = np.cov(portfolio_returns, market_returns)[0][1]
    market_variance = np.var(market_returns)
    beta = covariance / market_variance
    
    # Sharpe Ratio
    sharpe_ratio = (portfolio_return_annual - rf_rate_annual) / portfolio_vol
    
    # Treynor Ratio
    treynor_ratio = (portfolio_return_annual - rf_rate_annual) / beta
    
    # Jensen's Alpha
    expected_return = rf_rate_annual + beta * (market_return_annual - rf_rate_annual)
    jensen_alpha = portfolio_return_annual - expected_return
    
    # Information Ratio
    active_returns = portfolio_returns - market_returns
    information_ratio = active_returns.mean() / active_returns.std() * np.sqrt(12)
    
    return {
        'Annual Return': portfolio_return_annual,
        'Annual Volatility': portfolio_vol,
        'Beta': beta,
        'Sharpe Ratio': sharpe_ratio,
        'Treynor Ratio': treynor_ratio,
        "Jensen's Alpha": jensen_alpha,
        'Information Ratio': information_ratio
    }

# Calculate monthly returns
portfolio_monthly_returns = portfolio_returns['Portfolio_Return']
market_monthly_returns = aus_market['Market_Return'].dropna()

# Calculate performance metrics
metrics = calculate_performance_metrics(portfolio_monthly_returns[:len(market_monthly_returns)], 
                                     market_monthly_returns,
                                     rf_rate_monthly)

# Format results
results = pd.DataFrame({
    'Metric': list(metrics.keys()),
    'Value': list(metrics.values())
})
results['Value'] = results['Value'].round(4)

print("\nPortfolio Performance Metrics:")
print(results.to_string(index=False))

# Calculate cumulative returns for visualization
portfolio_cum_returns = (1 + portfolio_monthly_returns).cumprod()
market_cum_returns = (1 + market_monthly_returns).cumprod()