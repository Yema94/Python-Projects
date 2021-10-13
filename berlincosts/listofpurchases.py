"""orderList = ["Ginger Garlic Paste", "Gram Flour", "Green Chillies", "Bhindi", "Tindore", "MTR Roasted Vermicelli",
             "Paneer", "MTR Idly Mix", "Chillies Whole Ex Hot", "Maggi 20 Packets set", "Annam Mamra", "Laila Basmati "
                                                                                                       "Rice Green 5kg",
             "Priya Tomato Pickle 300gm", "Chana Dal 500g", "Toor Dal 500g", "Moong Dal 500g", "Malabar Paratha 10 piece"
                                                                                               " Packet"]
#print(orderList)
priceDict = {}
for i in orderList: priceDict[i]=input(" Cost ")
print(priceDict)
"""

orderList = input("Enter the list of items purchased separated by commas : \n").split(',')
print(orderList)
print(len(orderList))