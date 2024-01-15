import pandas as pd

def top_names(year, filename):
    # Load data from file
    df = pd.read_csv(filename)

    # Filter by year
    df = df[df['Year'] == year]
    


    # Group by name and sum the counts
    name_counts = df.groupby('Name')['Rank'].sum()

    # Sort by count in descending order and get top 10     
    top_names = df.sort_values(["Name"], ascending=[True])
   # top_names = name_counts.sort_values(ascending=True)[:10]

    # Print the top 10 names
    print(top_names.to_string())



# Example usage: print top 10 names in year 1960
top_names(2019, "California 1960-2021 M.csv")
