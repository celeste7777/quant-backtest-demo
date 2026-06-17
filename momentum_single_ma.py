import pandas as pd
import numpy as np
print("=====Strategy 1 动量策略=====")
df1 = pd.DataFrame({
    "prices":[100,104,101,102,106,106,107,105,104]
})
df1["return"] = (df1["prices"] - df1["prices"].shift(1))/df1["prices"].shift(1)
# calculate the rate of return

df1["signals1"] = np.where(
    df1["prices"] > df1["prices"].shift(1),
    1,
    np.where(
        df1["prices"] < df1["prices"].shift(1),
        -1,
        0
    )
)
# make signals of buying or selling

df1["strategy_return1"] = df1["signals1"] * df1["return"]
# calculate the strategy returns

Total1 = df1["strategy_return1"].sum()
Average1 = df1["strategy_return1"].mean()
Risk1 = df1["strategy_return1"].std()
Sharpe_Ratio1 = Average1 / Risk1
print("====Strategy1's report====")
print(df1)
print("Total return1:",Total1)
print("Average return1:",Average1)
print("Risk return1:",Risk1)
print("Sharpe ratio1:",Sharpe_Ratio1)
# The final return across various metrics


print("====Strategy2 均线策略====")
df2= pd.DataFrame({
    "prices":[100,104,101,102,106,106,107,105,104]}
)

df2["return"] = (df2["prices"] - df2["prices"].shift(1))/df2["prices"].shift(1)
# calculate the rate of return

df2["Moving average3"] = df2["prices"].rolling(3).mean()
df2["signals2"] = np.where(
    df2["prices"] > df2["Moving average3"],
    1,
    np.where(
        df2["prices"] < df2["Moving average3"],
        -1,
        0
    )

)
# Make signals of buying or selling

df2["strategy_return2"] = df2["signals2"] * df2["return"]
# calculate the strategy returns

Total2 = df2["strategy_return2"].sum()
Average2 = df2["strategy_return2"].mean()
Risk2 = df2["strategy_return2"].std()
Sharpe_Ratio2 = Average2 / Risk2
print("====Strategy2's report====")
print(df2)
print("Total return2:",Total2)
print("Average return2:",Average2)
print("Risk return2:",Risk2)
print("Sharpe ratio2:",Sharpe_Ratio2)
# The final return across various metrics

if Sharpe_Ratio2 > Sharpe_Ratio1:
    print('I suggest that we should use the strategy2 ')
elif Sharpe_Ratio2 == Sharpe_Ratio1:
    print('I think both of them are great')
else:
    print('I suggest that we should use the strategy1 ')