
#%% Import Libraries
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine

#%% Download airport data and create dataframe
data = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat',header=-1)
data.columns = ['AIRPORT_ID','NAME','CITY','COUNTRY','IATA','ICAO','LATITUDE','LONGITUDE','ALTITUDE','TIMEZONE','DST','TZ_DB','TYPE','SOURCE']
data.set_index('AIRPORT_ID')
#%% Create connection to PostgreSQL database
engine = create_engine('postgresql+psycopg2://joek318:wolphin85@mydbinstance.c39czh0r7sit.us-east-2.rds.amazonaws.com/joek318')

#%%
data.to_sql('AIRPORT_DATA',con=engine)

#%%
pd.read_sql_table('AIRPORT_DATA',con=engine)

#%%
