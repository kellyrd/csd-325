"""
Kelly Dimick
Date: 10/02/2026
Assignment: 4.3 – Sitka Weather Menu Program

## Program Description
This program reads weather data from the Sitka, Alaska CSV file and provides a simple text-based menu that allows the user to view high or low temperature plots.

## Using the Weather Menu

When the program starts, it displays a simple text-based menu:

1. View high temperatures  
2. View low temperatures  
3. Exit  

### Selecting an Option
- Type the number of the option you want.
- Press Enter.
- The program will perform the selected action and return to the menu.

### Menu Options Explained
**Option 1:** Generates a Matplotlib line chart showing Sitka’s high temperatures.  
**Option 2:** Generates a Matplotlib line chart showing Sitka’s low temperatures.  
**Option 3:** Ends the program.

You may run options 1 and 2 as many times as you like. Choose option 3 to exit.
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

def load_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high, and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
        return(dates, highs, lows)

   
# Plot the high temperatures.
#plt.style.use('seaborn')
def plot_highs(dates,highs): 
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def plot_lows(dates,lows): 
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    dates, highs, lows = load_weather_data(filename)
    while True:
        print("\nSitka Weather Menu")
        print("1. View high temperatures")
        print("2. View low temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, 3): ")

        if choice == "1":
            print("Displaying high temperatures")
            plot_highs(dates, highs)

        elif choice == "2":
            print("Displaying low temperatures")
            plot_lows(dates, lows)

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()