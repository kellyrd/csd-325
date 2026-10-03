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