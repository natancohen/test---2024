def result(num = int(input("Enter a number: "))):
    if num > 0 and num < 100:
        if num >= 90:
            print("excellent")
        elif num >= 60 and num < 90:
            print("nice")
        else:
            print("failed")
    else:
        print("The number is out of range")


result()

