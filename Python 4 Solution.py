import random
    
for i in range (3):
    r = random.randint(1, 50)
    print("Package weight: ", r)
    if r <= 2 :
        print("Shipping rate: $ 1.10")
        print("Shipping charge: $", r * 1.10)
    elif 2 < r <= 6 :
        print("Shipping rate: $ 2.20")
        print("Shipping charge: $", r * 2.20)
    elif 6 < r <= 10 :
        print("Shipping rate: $ 3.70")
        print("Shipping charge: $", r * 3.70)
    elif 10 < r <=20 :
        print("Shipping rate: $4.50")
        print("Shipping charge: $", r * 4.50)
    elif r > 20 :
        print("The package is over 20 pounds and cannot be shipped")

    print()   



