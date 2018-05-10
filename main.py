import random
score=0
z=1
while z==(1):
    a=random.randint(1, 100)
    b=random.randint(1,2)
    c=random.randint(1, 100)
    mass=str(a) + ("kilograms=mass")
    if b==(1):
        speed=str(c) + ("m/s=speed")
        print (mass)
        print (speed)
        q1=input("What's the kinetic energy? Just the number.")
        speed2=((c)**2)*(a)/2
        if int(q1)==speed2:
            score+=1
            print ("Yay! you scored a point! Your current score is %s." % score)
        else:
            print ("Game over! Your score was %s!" % score)
            score=0
    elif b==(2):
        height=str(c) + ("meters")
        print (height)
        print (mass)
        q1=input("What's the gravitational potential energy?")
        answer=(a)*(c)
        if int(q1)==answer:
            score+=1
            print ("Yay! you scored a point! Your current score is %s." % score)
        else:
            print ("Game over! Your score was %s!" % score)
            score=0
