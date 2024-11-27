# Opening a file in python with reading only
file = open("file.txt", "r")
data = file.read()
print(data)

# Opeining a file with write
file1 = open("file.txt", "w")
data1 = file1.write("Hello too!!")
print(data1)