import pickle
import student

f = open("studentdata.data", "wb")
s = student.Student("kota", 23, 99)

# using the dump method of pickle module,
# serialising an object into a file
pickle.dump(s, f)
f.close()

