try:
    with open("sample.tx", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("This is a Sample.txt file")
    print("It contains multiple Lines")
