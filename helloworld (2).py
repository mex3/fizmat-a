point=0
print ("helloworld")
print("Hello what is your name?")
a=input()
n=1
while n:
    print("Dear "+a+", Have you worked somewhere before turned to us?")
    b=input()
    if b.find("No")>-1 or b.find("no")>-1:
        print(" Have you got specialized education?")
        c=input()
        if c.find("No")>-1 or c.find("no")>-1:
            print("You do not come to us")
            break
    print("Do you enter into organized terrorist community?")
    d=input()
    if d.find("Yes")>-1 or d.find("yes")>-1:
        print("You do not come to us")
        break
    print("Have you identified mental disorder?")
    e=input()
    if d.find("Yes")>-1 or d.find("yes")>-1:
        print("You do not come to us")
        break
    print( "Have you sitted in prison?")
    g=input()
    if g.find("Yes")>-1 or g.find("yes")>-1:
        point+=1
    else:
        point-=1
    print("What would you like to get paid?(write number)")
    h=int(input())
    if h>=50000:
        point-=1
    else:
        point+=1
    print("Have you children?")
    j=input()
    if j.find("Yes")>-1 or j.find("yes")>-1:
        point+=1
    else:
        point-=1
    print("Have you house?")
    k=input()
    if k.find("Yes")>-1 or k.find("yes")>-1:
        point+=1
    else:
        point-=1
    n=0
    if point>=0:
              print("You're hired. Come back tomorrow.Your salary is 40000.")
    else:
            print("You do not come to us")
           
           

    
          
           
