#Sequence type : LIST

countriesList = ["India", "Germany", "Sweden"]
countriesList.append("Norway")
#del countriesList[2]
countriesList.pop(2)
#countriesList.remove("Sweden")
countriesList.insert(2, "Switzerland")
print(countriesList)


#Sequence type : SET
"""Is there a way to remove an item from the SET using the index instead of 
element ? """

countriesSet = set(countriesList)
countriesSet.add("Sweden")
countriesSet.remove("Switzerland")
#countriesSet.discard("Switzerland")
#countriesSet.pop()
print(countriesSet)