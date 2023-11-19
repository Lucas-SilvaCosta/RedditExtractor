import os
import time
import matplotlib.pyplot as plt
import pandas as pd

## Plot Blockchain posts and growth per year graph
def PostsGrowthPerYear(dataFrameOpt):
    # Reading from scraper generated file
    if dataFrameOpt:
        data = pd.read_json("./hyperledger.json")
        title = "Hyperledger Fabric"
    else:
        data = pd.read_json("./blockchain.json")
        title = "Blockchain"

    # Convert Date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Create a new column for the year of each entry
    data['Year'] = data['Date'].dt.year

    # Create data frame counting the number of entries for each year
    entries = data['Year'].value_counts().sort_index().reset_index()
    entries.columns = ['Year', 'Number of Posts'] 

    # Plotting graphs
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar graph for the number of entries
    ax1.bar(entries['Year'], entries['Number of Posts'], color='skyblue', label='Number of Posts')
    ax1.set_xlabel('Year')
    ax1.set_xticks(entries['Year'])
    ax1.set_ylabel('Number of Posts', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    ax1.grid(axis='y')

    # Line graph for the growth trend
    ax2 = ax1.twinx()
    ax2.plot(entries['Year'], entries['Number of Posts'].cumsum(), color='orange', label='Cumulative Posts')
    ax2.set_ylabel('Cumulative Posts', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    fig.tight_layout()
    plt.title('Number of Posts and Growth Trend on Reddit about '+title+' per Year')
    plt.show()

## Plot Interaction on Blockchain posts and growth per year graph
def InteractionsGrowthPerYear(dataFrameOpt):
    # Reading from scraper generated file
    if dataFrameOpt:
        data = pd.read_json("./hyperledger.json")
        title = "Hyperledger Fabric"
    else:
        data = pd.read_json("./blockchain.json")
        title = "Blockchain"

    # Convert Date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Create a new column for the year of each entry
    data['Year'] = data['Date'].dt.year

    # Create a new column for the interaction of each entry
    data['Interactions'] = data['Upvotes'] + data['Comments']

    # Create data frame containing the sum of interactions on posts by year
    entries = data.groupby('Year')['Interactions'].sum().reset_index()
    entries.columns = ['Year', 'Number of Interactions'] 

    # Plotting graphs
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar graph for the number of entries
    ax1.bar(entries['Year'], entries['Number of Interactions'], color='skyblue', label='Number of Interactions')
    ax1.set_xlabel('Year')
    ax1.set_xticks(entries['Year'])
    ax1.set_ylabel('Number of Interactions', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    ax1.grid(axis='y')

    # Line graph for the growth trend
    ax2 = ax1.twinx()
    ax2.plot(entries['Year'], entries['Number of Interactions'].cumsum(), color='orange', label='Cumulative Interactions')
    ax2.set_ylabel('Cumulative Interactions', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    fig.tight_layout()
    plt.title('Number of Interactions and Growth Trend on Reddit Posts about '+title+' per Year')
    plt.show()

if __name__ == '__main__':
    while True:
        print("Choose graph to plot:")
        print("    1- Number of Posts and Growth Trend on Reddit about Blockchain per Year")
        print("    2- Number of Interactions and Growth Trend on Reddit Posts about Blockchain per Year")
        print("    3- Number of Posts and Growth Trend on Reddit about Hyperledger Fabric per Year")
        print("    4- Number of Interactions and Growth Trend on Reddit Posts about Hyperledger Fabric per Year")
        print("\n    0- Leave")
        dataFrameOpt = int(input())
        if dataFrameOpt == 0:
            break
        elif dataFrameOpt == 1:
            PostsGrowthPerYear(0)
        elif dataFrameOpt == 2:
            InteractionsGrowthPerYear(0)
        elif dataFrameOpt == 3:
            PostsGrowthPerYear(1)
        elif dataFrameOpt == 4:
            InteractionsGrowthPerYear(1)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid Value..\n")
            time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

