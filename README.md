# Quantitative Trading Backtesting Demo
Self-written Python backtesting scripts for learning classic trading strategies.
All price data is manually created synthetic data without real market data.

## File Introduction
1. momentum_single_ma.py
Realize momentum strategy and single moving average strategy, calculate total return and Sharpe ratio.
2. dual_ma_full_metrics.py
Double moving average crossover strategy. Contains full performance metrics: total return, Sharpe ratio, win rate, profit factor, maximum drawdown.
Core logic: shift signal forward one period to avoid look-ahead bias.
3. backtest_function.py
Encapsulate complete backtest logic into reusable function, automatically output all evaluation indicators after inputting price sequence.

## Strategies Covered
Momentum Strategy, Single MA Strategy, Double MA Crossover Strategy

## Performance Indicators
Total return, average return, volatility(risk), Sharpe ratio, win rate, profit factor, maximum drawdown
