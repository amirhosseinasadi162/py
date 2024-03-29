#pandas_different_ways_of_creating_dataframe %% 
import pandas as pd

# %%
df1 = pd.read_csv("weather_data.csv")
df1

# %% [markdown]
# # USING DICTIONARY

# %%
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017'],
    'temperature': [32,35,28,25],
    'windspeed': [6,7,2,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow']
}
df = pd.DataFrame(weather_data)
df

# %% [markdown]
# # Using list

# %%
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow'),
    ('1/4/2017',25,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df

# %% [markdown]
# # Using list of Dictionary

# %%
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    {'day': '1/4/2017', 'temperature': 25, 'windspeed': 2, 'event': 'Snow'}
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


