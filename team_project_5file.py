import pandas as pd
from subprocess import call
from ethnicolr import census_ln

def process_file(file_path):
    while True:
        print('Enter the year (either 2000 or 2010):')
        yearInput = input()
        if yearInput not in ['2000', '2010']:
            print('Invalid year entered. Please enter either 2000 or 2010.')
        else:
            year = int(yearInput)
            break
    
    # read the csv file into a pandas DataFrame
    df = pd.read_csv(file_path, header=None, names=["Year", "Sex", "Rank", "Name", "Count"])
    census_ln(df, 'Name')

    call(["census_ln", "-y", str(year), "-o", "output-census" + str(year) + ".csv", "-l", "3", file_path])

    # read the output file and print its contents
    df_output = pd.read_csv('output-census' + str(year) + '.csv', skiprows=[1])
    
    df_output = df_output.dropna()
    
    return df_output.to_string(index=False, float_format='%.2f')

print('Enter the name of the file:', end = "")
processFileInput = input()

output = process_file(processFileInput)
print(output)
