



question_list=[
    ["which is the capital of India ?"],
    ["who is prime minister of India ?"],
    ["which course teach in Navgurukul ?"],
    ["who is the father of India"]
]
option=[
    ["Goa","Karnatak","kerla","New Delhi"],
    ["Ramnath Kovind","Jawaharlal Nehru","Narendra Modi","Atalbihari Vajpei"],
    ["Software Engineering","Agriculture","Science and Technologi","Medical Course"],
    ["Mahatma Gandhi","Ramnath Kovind","Atalbihari Vajpei","APJ Abdul Kalam"]
]
op50_50=[
    ["1)Goa","4)New Delhi"],
    ["2)Jawaharlal Nehru","3)Narendra Modi"],
    ["1)Software Engineering","3)Science and Technologi"],
    ["1)Mahatma Gandhi","2)APJ Abdul Kalam"]
]
ans_list=[4,3,1,1]
print("kon banega karodpati,KBC")
print("lets start the game")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(option[i]):
        k=option[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("do you want to use life line:-")
        if life_line=="yes":
            c+=1
            print(op50_50[i])
            s+=10000
    Ans=int(input("enter your option:-"))
    if ans_list[i]==Ans:
        print("your answer is correct",s)
        s+=10000
    else:
        print("your answer is wrong")
        break
    i+=1

