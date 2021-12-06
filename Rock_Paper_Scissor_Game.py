import random
n=5
n1=0
x1=0
y1=0
while n1<n:
    print('round number:',n1+1)
    x=int(input('Enter 1,2,3 for scissors, paper, stone respectively.[1-3]:'))
    y=random.randint(1,3)
    if x==y:
        print('Both of the competitors have chosen the same materials.try again.')
        continue
    elif (x==1 and y==2 ) or (x==2 and y==3) or (x==3 and y==1):
        x1+=1
        n1+=1
        print('round number:',n1,'you chose:',x,'computer chose:',y,'you are winner.')
        if x1>int(n/2):
            break
    else:
        y1+=1
        n1+=1
        print('round number:',n1,'you chose:',x,'computer chose:',y,'computer is winner.')
        if y1>int(n/2):
            break
if x1>y1 :
    print('YOU WON!CONGRATULATIONS!')
else:
    print('YOU LOST!TRY AGAIN.')
        
