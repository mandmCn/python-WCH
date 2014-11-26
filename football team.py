print " We are looking for members of the football team! Let's see if you can join."

gender = str(raw_input("Are you a boy or a girl? type in m or f."))
age = int(raw_input("How old are you?"))

if gender == "m":
    print " Sorry, we only want girls."
if gender == "f":
    if age < 10:
        print "Too young, girl! Wait till years later!"
    if age > 12:
        print "You are too old to join."
    if age >=10 <=12:
        print "welcome to the team!"
        
