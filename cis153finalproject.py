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
#print(covid_data_file.head(2500))
#print(covid_data_file)
#print(covid_data_file.to_string()) # IO takes about 5-10 minutes. Don't print this unless you absolutely needed.
#print(covid_data_file.columns)
#columns_needed = ["Province_State", "Country_Region", "Date", "Confirmed", "Deaths"]


def covid_data_dates():
    columns_needed = ["Date"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    unordered_dates = set(covid_data_file["Date"].unique()) # eliminating duplicate dates
    dates = sorted([pd.to_datetime(date) for date in unordered_dates])
    #print(dates)
    return dates

def covid_data_infected():
    columns_needed = ["Date", "Confirmed"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    covid_data_file["Date"] = pd.to_datetime(covid_data_file["Date"])
    infected_cases = covid_data_file.groupby("Date")["Confirmed"].sum()
    #print(infected_cases)
    return infected_cases

def covid_data_deaths():
    columns_needed = ["Date", "Deaths"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    death_count = covid_data_file.groupby("Date")["Deaths"].sum()
    #print(death_count)
    return death_count


def covid_data_recovered():
    columns_needed_names = ["Date", "Confirmed", "Deaths"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed_names)
    covid_data_file["Recoveries"] = covid_data_file["Confirmed"] - covid_data_file["Deaths"]
    recoveries = covid_data_file.groupby("Date")["Recoveries"].sum()
    #print(recoveries)
    return recoveries

def plot_covid_data(dates, infected_cases, death_count, recoveries):
    plt.plot(dates, infected_cases)
    plt.plot(dates, death_count)
    plt.plot(dates, recoveries)
    plt.show()
    #print(dates, infected_cases, death_count, recoveries)
    return

plot_covid_data(covid_data_dates(), covid_data_infected(), covid_data_deaths(), covid_data_recovered())