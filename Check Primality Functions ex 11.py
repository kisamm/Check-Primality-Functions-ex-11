

number = int(input("Enter yout number "))
listRange = [x for x in range(2,number) if number % x == 0]

def divisors():
    if number >1:
        if len(listRange) == 0:
            print("Prime")
        else:
            print("Not prime")

divisors()



