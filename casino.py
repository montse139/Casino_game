secret = 3
guess = int(raw_input("guess the number"))
if guess == secret:
    print "Congratulations!"
elif guess < secret:
    print "go up!"
elif guess > secret:
    print "go down!"

# Casino_game
