import pandas as pd
import numpy as np
def backtest(prices,strategy):
    # 先创建一个表格
    df = pd.DataFrame({
        "prices":prices
    })
    # 这个语法就是做收益率的，今天比昨天涨了多少
    df["return"] = df["prices"].pct_change()
    # 做买卖信号 今天价格大于昨天价格就买......
    if strategy == "momentum":
        df["signal"] = np.where(
            df["prices"] > df["prices"].shift(1),
            1,
            np.where(
                df["prices"] < df["prices"].shift(1),
                -1,
                0
            )
        )
    elif strategy == "Moving Average":
        df["MA5"] = df["prices"].rolling(5).mean()
        df["MA3"] = df["prices"].rolling(3).mean()
        df["signal"] = np.where(
            df["MA3"] > df["MA5"],
            1,
            np.where(
                df["MA3"] < df["MA5"],
                -1,
                0
            )
        )
    elif strategy == "Mean Reversion":
        # 均线策略 与均线比 高了就卖低了就买 因为我认为价格始终会回到均线附近
        df["MA5"] = df["prices"].rolling(5).mean()
        df["signal"] = np.where(
            # 价格比均线低5%，买
            df["prices"] < df["MA5"],
            1,
            np.where(
                # 价格比均线高5%，卖
                df["prices"] > df["MA5"],
                -1,
                0
            )
        )
    df = df.dropna()
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
    results = {
        "df": df,
        "total": total,
        "average": average,
        "risk": risk,
        "sharpe_ratio": sharpe_ratio,
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "max_drawdown": max_drawdown
    }
    return results
strategies = ["momentum", "Moving Average", "Mean Reversion"]
final_results = []
prices = [100,104,101,102,104,103,104,102,102,106,107,102,102,105,105,104,104,107,102,109]
for s in strategies:
    results = backtest(prices,s)
    final_results.append(
        {"strategy":s,
        "total":results["total"],
        "average":results["average"],
        "risk":results["risk"],
        "sharpe_ratio":results["sharpe_ratio"],
        "win_rate":results["win_rate"],
        "profit_factor":results["profit_factor"],
        "max_drawdown":results["max_drawdown"]
         }
    )

result_df = pd.DataFrame(final_results)
print(result_df)
