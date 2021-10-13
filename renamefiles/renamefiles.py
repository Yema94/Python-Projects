import os

path = "C:/Users/yeshwanth/PycharmProjects/pythonProject"
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, file.lower()))