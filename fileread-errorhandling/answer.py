try:
    file = open("sample.txt", "w")
    data = file.write("Hello World!!")
except:
    print("File not found.")
finally:
    file.close()