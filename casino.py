def main():
    import random
    secret_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    random_num = random.randint(0, 29)
    secret = secret_num[random_num]
    your_guesses = []

    for x in range(5):
        guess = int(raw_input("Guess the secret number (between 1 and 30): "))
        your_guesses.append(guess)

        if guess == secret:
            print "You guessed it - congratulations! It's number: %s" % secret
            print "Number of attempts: %s" % len(your_guesses)
            break
        elif guess < secret:
            print "go up!"
        elif guess > secret:
            print "go down!"

if __name__ == "__main__":
    main()
