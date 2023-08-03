import random
name = input("What is your name? ")
print("Good Luck ! ", name)

words=['dhiraj','sowmya','suman','aditya','piyush','princy','rishav','gaurav']

ans_word=random.choice(words);

ans=''



chances=5

while chances>0: 

    failed=0


    guess=input('guess a character :')
    ans+=guess
    

    for char in ans_word:
        if char in ans:
            print(char)
        else:
            print("_")
            failed+=1

    if(failed==0):
        print()
        print("hurrayy u won ra reyyy mowa!!")
        print('The word is',ans_word)
        break

    if guess not in ans_word:
        chances-=1
        print('wrong')
        print('you have ',chances,' more left')
        if chances==0:
            print('Game over....you lost bitch!!!')
  
        