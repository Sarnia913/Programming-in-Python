import random
#creating the dictionary for the rooms 
reserve_book={}

for i in ['A','B','C']:
    for j in range(1,4):
        for k in range(1,5):
              reserve_book[str(i)+str(j)+str(k)]=[]

     
for i in ['A','B','C']:
       for j in [1,3]:
          del reserve_book[str(i)+str(j)+'4']
for i in ['A','B','C']:
       del reserve_book[str(i)+str(3)+'3']          

# fill them primarily with random dates:[1-31], remove duplicates and sort them          

for k in reserve_book.keys():
    for i in range(10):
         reserve_book[k].append(random.randint(1,31))
    reserve_book[k]=list(dict.fromkeys(reserve_book[k]))
    reserve_book[k].sort()
# now print the dictionary keys(room numbers) and their values( reservation history )   
for k in reserve_book:
    print(k,':',reserve_book[k])

#asking the guest for information and reservation    
n=0
f=0

while n<561:
  date=input('Enter the dates of reservation[1-31]:')
  date=date.split()
  date=[int(s) for s in date if s.isdigit()]
  date.sort()
  if date[-1]>31 or date[0]<1:
    print('wrong DATE.Please try again.')
    continue
  room=input('Enter the class of room[A-C]:')
  if room not in ['A','B','C']:
    print('wrong CLASS.Please try again.')
    continue 
  bednumber=int(input('Enter the number of the bed[1-3]:'))
  if bednumber not in range(1,4):
     print('wrong BEDNUMBER.Please try again.')
     continue
  
  p=room+str(bednumber)
  for k in reserve_book.keys():
      if p in k:
          check =  all(item not in reserve_book[k] for item in date)
          if check is True:
               print('The date is avaialable in room:',k)
               reserve_book[k]=reserve_book[k]+date
               reserve_book[k].sort()
               print(k,':',reserve_book[k])
               n=n+1
               f=1
              
               name=input('enter your name:fname lname:')
               print('The room',k,'is booked now for',name)
               break
  if f==0:
      print('The date is not available.please try again')
      continue

