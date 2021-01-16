import random
number = random.randint(1,10)
def guessing_number(n):
            if n < number :
                print("<<TOO LOW>>")
            elif n > number :
                print("<<TOO FAR>>")
            elif n == number:
                print("<<BINGOO!! YOU WON!>>")
                return True


def main():
    print("NOTE: You have only 3 attempt to guess the right answer!!")
    for i in range(3):
        n = int(input("Guess a number between 1 and 10 : "))
        if guessing_number(n) == True:
            break

main()
