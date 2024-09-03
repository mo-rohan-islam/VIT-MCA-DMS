def gcd(a, b):
    while b!=0:
        r = a%b
        a=b
        b=r
    return a

def main():
    print("Enter 2 numbers to find the GCD\n")
    num1 = int(input('Enter the 1st number: '))
    num2 = int(input('Enter the 2nd number: '))
    print(f'\nThe GCD of {num1} and {num2} is {gcd(num1, num2)}')

if __name__ == '__main__':
    main()