try:
    file=open("students.txt","r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File does not exist")

except Exception as e:
    print("Error", e)