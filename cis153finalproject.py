'''
Victor Van
00319912
CIS153: Final Project
11/28/2023, Due: 12/17/2023
'''

import pandas as pd
import matplotlib.pyplot as plt

def covid_dataframe():
    columns_needed = ["Province_State", "Country_Region", "Date", "Confirmed", "Deaths"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    return covid_data_file

def covid_data_dates(covid_data_file):
    unordered_dates = set(covid_data_file["Date"].unique())  # eliminating duplicate dates
    dates = sorted([pd.to_datetime(date) for date in unordered_dates])
    return dates

def covid_data_infected(covid_data_file):
    covid_data_file["Date"] = pd.to_datetime(covid_data_file["Date"])
    infected_cases = covid_data_file.groupby("Date")["Confirmed"].sum()
    return infected_cases

def covid_data_deaths(covid_data_file):
    death_count = covid_data_file.groupby("Date")["Deaths"].sum()
    return death_count

def covid_data_recovered(covid_data_file):
    covid_data_file["Recoveries"] = covid_data_file["Confirmed"] - covid_data_file["Deaths"]
    recoveries = covid_data_file.groupby("Date")["Recoveries"].sum()
    return recoveries

def main():
    x = covid_dataframe()
    plt.title("COVID-19: Infected Cases, Death Counts, and Recoveries Over Time in USA")
    plt.xlabel("Time (Y-M)")
    plt.ylabel("Number of Cases (in Thousands)")
    plt.grid()
    done = False
    while not done:
        dates = covid_data_dates(x)
        cases = covid_data_infected(x)
        deaths = covid_data_deaths(x)
        recovered = covid_data_recovered(x)
        user_input = int(input("Choose an option: \n 1) Plot All Data \n 2) Plot Infected Cases \n 3) Plot Death Count \n 4) Plot Recoveries \n 5) Exit Program\n"))
        if user_input == 1:
            plt.plot(dates, cases / 1000, color = "orange", label = "Infected Cases")
            plt.plot(dates, deaths / 1000, color = "red", label = "Deaths")
            plt.plot(dates, recovered / 1000, color = "green", label = "Recoveries")
            done = True
        elif user_input == 2:
            plt.plot(dates, cases / 1000, color = "orange", label = "Infected Cases")
        elif user_input == 3:
            plt.plot(dates, deaths / 1000, color = "red", label = "Deaths")
        elif user_input == 4:
            plt.plot(dates, recovered / 1000, color = "green", label = "Recoveries")
        elif user_input == 5:
            done = True
        else:
            print("Error: Choose a number 1-5.")
    plt.legend()
    plt.show()
    return

main()