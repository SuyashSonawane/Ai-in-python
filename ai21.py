import time
import random
import math
i=1
print('Intailizing  ..................................');time.sleep(0.5)                                                     # time pass
while i<5:
    print('.\n');time.sleep(0.5)
    i=i+1
print("Starting GUI Framework...................................");time.sleep(1.5)
print('Waiting for frame to get populated.....................');time.sleep(1.5)
print('Getting root thread access /////\\\\\\\\\\\\////');time.sleep(1.5)
print('Successfully started "SMART" ');time.sleep(.5)
while i<15:
    print('.\n');time.sleep(.5)
    i=i+1
print('Successfully  started!!');print('=====================================================')
print("Give me a Name so that you can call me with that ::::::::]"  )                                  #ask for name
idname=input()
talk0=('Ok '+idname+' is a good name', 'I thought you would give better name than '+idname+' !!,ok no problemo I will compromise','Thanks for such a cool name!! '+idname+' ! is a good name')#rect to name
time.sleep(1.00)

print(random.choice(talk0));print("")                                                                                                                                   #random rect to name
time.sleep(1.50)
print("So lets get started..........\nIm ",idname," an AI developed by  <<Suyash.geek>>  version_1.0 still developing......." );print("")                         #ai intro
print("As you set my name ,I want ur name too!!")
uname=input('Plzz type here:::::::::>')                                                                                                                                         #user name input
time.sleep(1.00)
print("Hmm,Great name");print("But , I want ur nickname too!!")
nickname=input('Nickname here::::::>')                                                                                                                                          #user nickname
time.sleep(1.00)
print("Waah, ",uname," also know as",nickname," !!")                                                                                                #user flr
print('And please give you gender ,so that i can manipulate my language ^_^   (M \ G )')
gen=str(input('==>'))
time.sleep(1.00)

print("Now Im familiar with you , now you can use my functions  ^_^ ")
time.sleep(1.20)




while True :
    print("============================================================")
    print("No. Functions")
    print(" 1.Division ")
    print(" 2. Multiply ")
    print(" 3. Addition ")
    print(" 4.  Advance iit function (still developing...)")
    print(" 5. Chat")
    print(" 6. Exit")
    cmd=int(input('==>'))
    if cmd==1:
        a=input('number to divide::')
        a=int(a)
        b=input('number to divide with ::')
        b=int(b)
        if b==0:
            print(nickname,"!! I think you dont know maths............but as Im here I will tell you its _Infinite_")
        else :
            print("your ans is: :",a/b)
    elif cmd==2:
        a=input(' number to multi::')
        a=int(a)
        b=input(' number to multi with::')
        b=int(b)
        print("Your answer is ", a*b )
    elif cmd==3:
        a=input(' number to add::')
        a=int(a)
        b=input(' number to add with::')
        b=int(b)
        print("Your answer is ", a+b )
    elif cmd ==6:                                                                                                                                            #byeeee
        print("Bye See you later!!"+nickname);time.sleep(3.00)
        break
    elif cmd ==5:
        print("You are a chatter box!! ^_^"+nickname)
        print("So what are your hobbies,",uname,"?")
        a=str(input('==>'))
        time.sleep(1.00);print("OOh!,I like",a,"too")
        time.sleep(1.00);print("What is your recent score in it??");score=input("==>")
        talk2=('Hmm,you play quite good','If I had a body I may score more than you','You have same score as Siri has in last game with me')#talk jokes
        time.sleep(1.00);print(random.choice(talk2));time.sleep(0.50);print("Just joking")
        print('' )
        time.sleep(1.25)
    elif cmd ==4:
        print("============================================================")
        print("OOh!! your a study kid "); time.sleep(1.00);print("hmm, np I will help you")
        print("Here is what you can do....")
        while True:
            time.sleep(1.25)
            print("============================================================")
            print("1. Greatest Integer Function")
            print("2. Simultaneous equation solving")
            print("3. Quadratic solving")
            print("4. Back to main menu");cmd2=int(input("==>"))
            if  cmd2==1:
                a= input('Enter a number such as .eg. 2.55 with a decimal to find out the greatest integer  :::::::::>')
                a=float(a)
                b=math.floor(a)
                print('Your answer is ::', b)
            elif cmd2==2:
                print("even if a, b,c  anyone is zero plz input the zero below")
                print("input the value below")
                a1=input('a1==>')
                a1=int(a1)
                b1=input('b1==>')
                b1=int(b1)
                c1=input('c1==>')
                c1=int(c1)
                a2=input('a2==>')
                a2=int(a2)
                b2=input('b2==>')
                b2=int(b2)
                c2=input('c2==>')
                c2=int(c2)
                d= (a1*b2) - (a2*b1);d=int(d)
                if d== 0:
                    print("Im solving by Cramers rule and D is 0 ,therefore X, Y  are not defined ")
                else:
                    dx= (c1*b2)-(c2*b1 );    dy=(a1*c2)-(a2*c1);  x=dx/d;y=dy/d
                    x1=str(x)
                    y1=str(y)
                    print( "this is the answer" , "X==>",x1 ," and Y==>", y1 )

            elif cmd2==3:
                print("============================================================")
                print("")
                print("Enter a Quadratic Equation ")
                a=input('Coeffecient of X square====> ')
                b=input('Coeffecient of X ====> ')
                c=input('Constant term ====> ')
                a=int(a)
                b=int(b)
                c=int(c)
                D=int(b**2-4*a*c)
                if D<0:
                    print("The determinant is less than 0 ,, the equation has non real roots ,, Sorry! I m still learning about Complex numbers  ")
                else:
                    D=math.sqrt(D)
                    e1=-1*b+D
                    X1=str(e1/2)
                    e2=-1*b-D
                    X2=str(e2/2)
                    print(  X1  ,  X2)
            elif cmd2==4:
                break
    

    else:
        print("Invaild option")
