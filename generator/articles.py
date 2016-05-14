input_file=open('standalone.txt', 'r')
ans=["a","an","the","-"]
sen=0
score=0
a=1
for c in input_file:
    s=list(map(str, c.split()))
    for e in range (len(s)):
        if s[e]=="a" or s[e]=="the" or s[e]=="an":
            correct=s[e]
            s[e]="..."
            print(" ".join(s))
            print("A: a")
            print("B: an")
            print("C: the")
            print("D: -")
            answ=input()
            if ord(answ)-65==ans.index(correct):
                print("You are right!")
                score+=1
            else:
                print("Your're wrong :-(. Correct answer is "+correct)
            print("Do you want to continue? Answer 'Yes or 'No''")
            a=input()
            sen+=1
            break
    if a=="No":
        print("See you, darling!Your game was absolutly brilliant! Your score: "+score+"/"+sen)
