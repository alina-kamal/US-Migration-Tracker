import csv
import pandas as pd
import matplotlib.pyplot as plt
from searchRegion import searchRegion
import numpy as np

def searchRegion (Region):
  i = 1900
  list = [[]]
  countIndex = 0
  firstRow = []
  fileName = ""
  while i < 2023:
    try:
      fileName = "YearSeperatedFiles/" + Region + " " + str(i) + " M.csv"
      with open (fileName) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
          firstRow = []
          firstRow.extend(row)
          break
        list.clear()  # clear the list before appending data
        for row in csvReader:
          list.append(row)
          countIndex+=1
    except:
      i = i
    i+= 1
  if list == [[]]:
    print("\nUnable to find any region")
    output = []
  else:
    output = pd.DataFrame(list,columns = firstRow)
  return output
