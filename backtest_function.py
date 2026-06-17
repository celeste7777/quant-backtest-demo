import pandas as pd
import numpy as np
def backtest(prices):
    # 先创建一个表格
    df = pd.DataFrame({
        "prices":prices
    })
    # 这个语法就是做收益率的，今天比昨天涨了多少
    df["return"] = df["prices"].pct_change()
    # 做买卖信号 今天价格大于昨天价格就买......
    df["signal"] = np.where(
        df["prices"] > df["prices"].shift(1),
        1,
        np.where(
            df["prices"] < df["prices"].shift(1),
            -1,
            0
        )
    )
    df["strategy_return"] = df["return"] * df["signal"].shift(1)
    # 指标
    total = df["strategy_return"].sum()
    average = df["strategy_return"].mean()
    risk = df["strategy_return"].std()
    sharpe_ratio = average/risk
    wins = df["strategy_return"] > 0
    win_rate = wins.sum()/len(wins)
    profit = (df["strategy_return"] * (df["strategy_return"] > 0)).sum()
    loss = (df['strategy_return'] * (df['strategy_return'] < 0)).sum()
    profit_factor = profit/abs(loss)
    df["peak"]= df["prices"].cummax()
    df["draw_down"] = (df["prices"] - df["peak"])/ df["peak"]
    max_drawdown = df["draw_down"].min()

    return df,total, average, risk, sharpe_ratio, win_rate, profit_factor, max_drawdown

df,total_return,average_return,Risk,Sharpe_Ratio,Win_rate,Profit_factor,Max_drawdown = backtest([120,124,104,108,104,107,112,104,107,115])
print(df)
print("total_return:",total_return)
print("average_return:",average_return)
print("Risk:",Risk)
print("Sharpe_Ratio:",Sharpe_Ratio)
print("Win_rate:",Win_rate)
print("Profit_factor:",Profit_factor)
print("Max_drawdown:",abs(Max_drawdown))