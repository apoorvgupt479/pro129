# Import pandas
import pandas as pd
 
# reading csv file
data1 =  pd.read_csv("data2.csv")

#cleaner for NaN
data1 = data1.dropna()

data1["Radius"] = pd.to_numeric(data1.Radius,errors='coerce')
data1["Radius"] = data1["Radius"]*0.102763

data1["Mass"] = pd.to_numeric(data1.Mass,errors='coerce')
data1["Mass"] = data1["Mass"]*0.000954588

#merging the csv files
data1 = pd.concat(
   map(pd.read_csv, ["data1.csv", "data2.csv"]), ignore_index=True)

#convert dataset to csv
data1.to_csv("final_data.csv")
