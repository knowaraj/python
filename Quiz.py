print("\nWelcome to Quiz contest with Real Moneyy!\n")
list=[
    ["Who killed Bahubalii?","Bahubali","Katappa","Mahismati","Bhasme Don",2],
    ["Who is real Spiderman?","Peter","peter","peTer","None",4],
    ["Whats most sold phone brand?","Samsung","Oppo","iphone","Vivo",1],
    ["Which language is this code?","C","Java","Python","Sudhha Nepali",3],
    ["What year is this?","2023","2080","2024","2070",2],
    ["Whats is V in roman?","1","2","5","7",3]
      
      ]
money=[100,200,300,400,500,1000]
i=0
paisa=0
for i in range (len(list)):
    question=list[i]
    print(f"The question for {money[i]} is {question[0]}\n")
    print(f"1.{question[1]}        2.{question[2]}")
    print(f"3.{question[3]}        4.{question[4]}\n")
    choice=int(input("\n Enter your choice or Enter 0 to Exit : "))
    if(choice==0):
        paisa=money[i-1]

    if(choice==question[5]):
        print("Congratulation your answer is correct !!\n")
        paisa=money[i]
    else:
        print(f"\nSorry wrong answer ! \n")
        break

print(f"Your takeaway money is {paisa}")


