import pandas as pd
import matplotlib.pyplot as plt

def covid_dataframe():
    columns_needed = ["Province_State", "Country_Region", "Date", "Confirmed", "Deaths"]
    covid_data_file = pd.read_csv("usa_county_wise.csv", usecols = columns_needed)
    return covid_data_file

def covid_data_dates(covid_data_file):
    unordered_dates = set(covid_data_file["Date"].unique()) # eliminating duplicate dates
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

def plot_covid_data(dates, infected_cases, death_count, recoveries):
    plt.title("COVID-19: Infected Cases, Death Counts, and Recoveries Over Time in USA")
    plt.xlabel("Time (Y-M)")
    plt.ylabel("Number of Cases (in Thousands)")
    plt.grid()
    plt.plot(dates, infected_cases / 1000, color = "orange", label = "Infected Cases")
    plt.plot(dates, death_count / 1000, color = "red", label = "Deaths")
    plt.plot(dates, recoveries / 1000, color = "green", label = "Recoveries")
    plt.legend()
    plt.show()
    return

x = covid_dataframe()

plot_covid_data(covid_data_dates(x), covid_data_infected(x), covid_data_deaths(x), covid_data_recovered(x))