input=open('standalone.txt', 'r')
for c in input:
    s=list(map(str, c.split()))
    for e in range len(s):
        if s[e]=="a" or s[e]=="the" or s[e]=="an":
            s[e]="..."
            print(" ".join(s))
            print("A: a")
            print("B: an")
            print("C: the")
            print("D: ")
