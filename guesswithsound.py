import random, pygame, sys
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([200,100])

ahoy = pygame.mixer.Sound("Ahoy.wav")
tooLow = pygame.mixer.Sound("TooLow.wav")
tooHigh = pygame.mixer.Sound("TooHigh.wav")
what = pygame.mixer.Sound("WhatsYerGuess.wav")
gotit = pygame.mixer.Sound("AvastGotIt.wav")
dead = pygame.mixer.Sound("NoMore.wav")


secret = random.randint(1, 99)
guess = 0
tries = 0

print "AHOY!  I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99.  I'll give you 6 tries. "
ahoy.play()
pygame.time.delay(8000) 

while guess != secret and tries < 6:
    what.play()
    guess = input("What's yer guess? ")       
    if guess < secret:
        print "Too low, ye scurvy dog!"
        tooLow.play()
        pygame.time.delay(3000)
    elif guess > secret:
        print "Too high, landlubber!"
        tooHigh.play()
        pygame.time.delay(3000)
    tries = tries + 1                         

if guess == secret:
    print "Avast! Ye got it!  Found my secret, ye did!"
    gotit.play()
else:
    print "No more guesses!  Better luck next time, matey!"
    print "The secret number was", secret
    dead.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()