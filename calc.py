from add import *
from sub import *
from mul import *
from div import *


if __name__ == '__main__':
    print("Choose between the following option: \n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication ")
    x = int(input("Enter our option number:"))

    n = input("Enter the number: ")
    m = input("Enter the number: ")
	
    if x == 1:
        print("Addition result: ", add(n,m))
    elif x == 2:
        print("Subtraction result: ", sub(n, m))
    elif x == 3:
        print("Division result: ", div(n, m))
    elif x == 4:
        print("Multiplication result: ", mul(n, m))
    else:
	print ("invalid")
