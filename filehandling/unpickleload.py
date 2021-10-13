import pickle

f = open("studentdata.data", "rb")

# using the load method of pickle module,
# the obj is being unpickled/deserialised from a file
obj = pickle.load(f)
obj.display()
f.close()