from math import sqrt

def is_prime(n):
    if n<=1:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n+1):
        if n%i==0:
            return False
    return True

def main():
    user_input = int(input("Enter a number: "))
    result = is_prime(user_input)
    if result:
        print(f'{user_input} is a Prime Number.')
    else:
        print(f'{user_input} is Not a Prime Number.')

if __name__ == '__main__':
    main()
