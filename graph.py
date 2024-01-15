import pandas as pd
import matplotlib.pyplot as plt

# Try specifying the delimiter and encoding parameters
californiaDf = pd.read_csv('California 1960-2021 M.csv', delimiter=',', encoding='latin1')
australiaDf = pd.read_csv('Australia 1952-2021 M.csv', delimiter=',', encoding='latin1')

# Display all rows and columns
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

#print("The data for California is:")
#print(californiaDf)

#print("The data for Australia is:")
#print(australiaDf)

#names for the files
df2 = australiaDf[['Name']].copy()
#print(df2.to_string(index=False))

#if user searches for 'top 10 australia names' print out the top 10 names of df2

df3 = californiaDf[['Name']].copy()
#print(df3.to_string(index=False))

def searchCaliforniaGraph():
    # Get user input for the search term
    search_term = input("Enter search term: ")

    # Filter the California dataframe based on the search term
    filtered_df = californiaDf.loc[californiaDf['Name'].str.contains(search_term, case=False)]

    # Print the filtered dataframe
    print(filtered_df.to_string(index=False))

    # Plot the frequency of the name over the years
    filtered_df.groupby('Year')['Count'].sum().plot(kind='line')
    plt.title(f"Frequency of {search_term} in California")
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.show()

def search_australia_graph():
    # Get user input for the search term
    search_term = input("Enter search term: ")

    # Filter the Australia dataframe based on the search term
    filtered_df = australiaDf.loc[australiaDf['Name'].str.contains(search_term, case=False)]

    # Print the filtered dataframe
    print(filtered_df.to_string(index=False))

    # Plot the frequency of the name over the years
    filtered_df.groupby('Year')['Count'].sum().plot(kind='line')
    plt.title(f"Frequency of {search_term} in Australia")
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.show()

searchCaliforniaGraph()
search_australia_graph()