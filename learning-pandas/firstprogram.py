import pandas as pd
print(pd.__version__)

"""Datasets in Pandas are usually multi-dimensional tables, called Dataframes"""

'''Cleaning Data'''
#df = pd.read_csv('data.csv')
df = pd.read_csv('dirtydata.csv')

'''- Removing rows with empty/null values'''
'''new_df = df.dropna() #removes rows with empty cells and returns new Dataframe, original df stays
print(df.info()) #original stays as it is
df.dropna(inplace = True) #removes all rows with empty cells from the original dataframe
print(df.info()) #modified 
print(new_df.info())'''

'''Replaces all Empty cells in the whole DataFrame'''
'''new_df = df.fillna(4343) #replaces all empty cells with "4343" and returns new dataframe
print(new_df.to_string())

df.fillna(4343, inplace = True) #replaces all empty cells with "4343" and modifies original dataframe
print(df.to_string())'''

'''Replaces all empty cells of a specified column '''
'''df['Calories'].fillna(4343, inplace = True)
print(df.to_string())'''

'''Replace specified column using its own Mean, Median, or Mode value'''
df['Calories'].fillna(df['Calories'].mean(), inplace = True)
'''print(df.loc[17])'''

'''Handling Wrong Format'''
# Correcting the format
df['Date'] = pd.to_datetime(df['Date'])
# Deleting the row
df.dropna(subset = ['Date'], inplace = True)


'''Handling Wrong Data'''
for i in df.index:
   if df.loc[i, 'Duration'] > 120:
       # Replacing the wrong data
       #df.loc[i, 'Duration'] = 120
       # Removing the row with wrong data
       df.drop(i, inplace = True)

'''Handling Duplicates'''
#print(df.duplicated()) #returns true if a row is duplicate
df.drop_duplicates(inplace = True) #removes the duplicate row


print(df.to_string())



"""
'''Load .csv Files into DataFrame'''
df = pd.read_csv('data.csv')
#print(df.to_string()) #returns entire dataframe
#print(df) #returns reduced dataframe (only 1st five rows and last five rows)
#print(df.head()) #default: first 5 rows of the dataframe
#print(df.head(10)) #first 10 rows of the dataframe
#print(df.tail()) #default: last five rows
#print(df.tail(10)) #last 10 rows
print(df.info())

'''Loading .json files into a dataframe'''
#df = pd.read_json('data.json')
#print(df.to_string()) #entire dataframe
#print(df) #reduced dataframe

'''Load a python Dict into a DataFrame'''
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df.to_string())
print(df)
"""
























""" 
'''Series is like colomn'''
#Creating a Pandas series from a list
a = [1, 7, 2]
myvar = pd.Series(a) # labeled with index numbers
print(myvar)
print(myvar[2]) #access an item by refering to the index nmber

myvar = pd.Series(a, index=["x", "y", "z"]) # own labels with index arguments
print(myvar)
print(myvar["z"]) #access an item by referring to the label


# Key/Value Objects as series
#The keys of the dict becomes the labels
calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories)
print(myvar)

#Include only day1, day2 items to the series
myvar = pd.Series(calories, index=['day1', 'day2'])
print(myvar)
print(myvar['day1'])


'''A DataFrame is the whole table'''
#Creating a dataframe with two series
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"], #series/column 1
    'passings': [3, 7, 2] # series/column 2
}
myvar = pd.DataFrame(mydataset) #loading data into the dataframe object
print(myvar)
print(myvar.loc[0]) #returns first row of the data
print(myvar.loc[[0,1]]) #returns a pandas series

myvar = pd.DataFrame(mydataset, index = ['brand1', 'brand2', 'brand3']) #labeling/naming my rows/indexes
print(myvar)
print(myvar.loc['brand1']) #locate or refer the named index
"""