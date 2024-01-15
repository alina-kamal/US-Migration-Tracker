import pandas as pd

# Try specifying the delimiter and encoding parameters
californiaDf = pd.read_csv('California1960-2021M.csv', delimiter=',', encoding='latin1')
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

#if user searchs fpr 'top 10 australia names' print out the top 10 names of df2

df3 = californiaDf[['Name']].copy()
#print(df3.to_string(index=False))

def searchCalifornia():
    # Get user input for the search term
    search_term = input("Enter search term: ")

    # Filter the California dataframe based on the search term
    filtered_df = californiaDf.loc[californiaDf['Name'].str.contains(search_term, case=False)]

    # Print the filtered dataframe
    print(filtered_df.to_string(index=False))

def search_australia():
    # Get user input for the search term
    search_term = input("Enter search term: ")

    # Filter the California dataframe based on the search term
    filtered_df = australiaDf.loc[australiaDf['Name'].str.contains(search_term, case=False)]

    # Print the filtered dataframe
    print(filtered_df.to_string(index=False))

searchCalifornia()
search_australia()