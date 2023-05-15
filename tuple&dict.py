school_class={}
while True:
    name=input("enter student's name: ")
    if name=="":
        break
    score=int(input("enter student's score: "))
    if score not in range(0,11):
        break
    if name in school_class:
        school_class[name]+=(score,)
    else:
        school_class[name]=(score,)

for name in sorted(school_class.keys()):
    add=0
    counter=0
    for score in school_class[name]:
        add+=score
        counter+=1
    print(name,":",add/counter)