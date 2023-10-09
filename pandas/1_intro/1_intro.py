#1_intro
import pandas as pd


# %%
df =pd.read_csv("nyc_weather.csv")
df

# %%
df["Temperature"].max()

# %%
df['EST'][df['Events']=='Rain']

# %%
df["Temperature"][df["Events"]=="Rain"]

# %%
df.fillna(0, inplace=True)
df['WindSpeedMPH'].mean()

# %%



