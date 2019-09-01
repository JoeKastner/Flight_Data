
#%% Import Libraries
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine

#%% Create connection to PostgreSQL database
engine = create_engine('postgresql+psycopg2://joek318:wolphin85@mydbinstance.c39czh0r7sit.us-east-2.rds.amazonaws.com/joek318')

#%% Download airport data and create dataframe
airport = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat',header=-1)
airport.columns = ['AIRPORT_ID','NAME','CITY','COUNTRY','IATA','ICAO','LATITUDE','LONGITUDE','ALTITUDE','TIMEZONE','DST','TZ_DB','TYPE','SOURCE']
airport.set_index('AIRPORT_ID')

#%% Create connection to PostgreSQL database, load airport data and read results to validate data loaded correctly
airport.to_sql('AIRPORT_DATA',con=engine,if_exists='replace'
pd.read_sql_table('AIRPORT_DATA',con=engine)

#%% Download airline data and create dataframes
airline = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat',header=0)
airline.columns = ['AIRLINE_ID','AIRLINE_NAME','AIRLINE_ALIAS','IATA','ICAO','CALLSIGN','COUNTRY','ACTIVE']
airline.set_index('AIRLINE_ID')

#%% Load airline data and read results to validate data loaded correctly
airline.to_sql('AIRLINE_DATA',con=engine,if_exists='replace')
pd.read_sql_table('AIRLINE_DATA',con=engine)

#%% Download airplane route data and create dataframes
routes = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat',header=0)
routes.columns = ['AIRLINE','AIRLINE_ID','SOURCE_AIRPORT','SOURCE_AIRPORT_ID','DESTINATION_AIRPORT','DESTINATION_AIRPORT_ID','CODESHARE','STOPS','EQUIPMENT']

#%% Load airplane route data and read results to validate data loaded correctly
routes.to_sql('ROUTES',con=engine,if_exists='replace')
pd.read_sql_table('ROUTES',con=engine)


#%%
