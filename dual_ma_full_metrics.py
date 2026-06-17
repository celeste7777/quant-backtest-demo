import pandas as pd
import numpy as np
print("====Strategy====")
df= pd.DataFrame({
    "prices":[100,104,101,102,106,106,107,105,104]
})

df["return"] = (df["prices"] - df["prices"].shift(1))/df["prices"].shift(1)
# return 回答的问题是今天涨了多少 描述的是市场发生了什么
df["MA3"] = df["prices"].rolling(3).mean()
df["MA5"] =df["prices"].rolling(5).mean()

df["signals"] = np.where(
    df["MA3"] > df["MA5"],
    1,
    np.where(
        df["MA3"] < df["MA5"],
        -1,
        0)
)
# signal 回答的是我要不要买 比如MA3 > MA5 得到signal=1 意思是我决定做多 所以他描述的是我的决策
df["strategy_return"] = df["signals"].shift(1) * df["return"]
# 而最后的strategy return描述的是我的策略赚了多少钱 你看比如今天return = 5% signal=1 买入 那我赚了
Total_Return = df["strategy_return"].sum()
Average_Return = df["strategy_return"].mean()
Risk_Return = df["strategy_return"].std()
Sharpe_Ratio = Average_Return / Risk_Return

Wins = df["strategy_return"] > 0
# 大于0的就是True 小于0的是False Wins是一整个序列 有True 有False python是每个元素都比较一次 大于0就true
Win_Rate = Wins.sum() / len(Wins)
# Win.sum()是True的合计 为什么呢 因为python中True等于1 而False等于0 所以啊 求和 其实是True的个数
# 而len(Wins)是这一列总共有多少个元素 所以呢我们做胜率分析 就直接除就好了啊


profit = (df["strategy_return"] * (df["strategy_return"]>0)).sum()
loss = abs((df["strategy_return"] * (df["strategy_return"]<0)).sum())
profit_Factor = profit / loss
# 这个是做盈亏比分析 也就是亏一单位 能赚多少 那个abs是取绝对值 亏损是负的 但是我们不想看正负 只看比例

print(df["prices"].cummax())
df["peak"] = df["prices"].cummax()
# cummax() 意思是到目前为止出现的最高值 算历史最高点 peak的意思是顶峰 峰值
df["drawdown"] = (df["prices"] - df["peak"])/df["peak"]
# 算回撤
Max_Drawdown = f"{((abs(df['drawdown'])).max())* 100}%"
# 找回撤最大的那一次，是绝对值啊 如果没加绝对值那就是找最小的那个值了 但是在后面输出的时候要输出正数哦（找到最惨的一次）

print("====Strategy report====")
print(df)
print('Total Return:',Total_Return)
print('Average Return:',Average_Return)
print('Risk Return:',Risk_Return)
print('Sharpe Ratio:',Sharpe_Ratio)
print('Win_Rate:',Win_Rate)
print("profit_Factor:",profit_Factor)
print("Max_Drawdown:",Max_Drawdown)