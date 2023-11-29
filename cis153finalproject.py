'''
Victor Van
00319912
CIS153: Final Project
11/28/2023, Due: 12/17/2023
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#covid_data_file = pd.read_csv("usa_county_wise.csv")

#print(covid_data_file.head())
#print(covid_data_file.to_string()) # IO takes about 5-10 minutes. Don't print this unless you absolutely needed.

def covid_data_dates():
    columns_needed = ["Province_State", "Country_Region", "Date", "Confirmed", "Deaths"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    unordered_dates = set(covid_data_file["Date"].unique()) # eliminating duplicate dates
    dates = sorted([pd.to_datetime(date) for date in unordered_dates])
    #print(dates)
    return dates

def covid_data_infected():
    return

def covid_data_deaths(dates):
    return

def covid_data_recovered():
    return

def plot_covid_data():
    return