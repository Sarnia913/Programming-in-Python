i=int(input('enter the number of first fibonachi series items:'))
s=0
p=1
if i==1:
    print(s)
elif i==2:    
    print(s)
    print(p)
else:
  print(s)
  print(p)  
  for i in range(i-2):
      t=s+p
      print(t)
      s=p
      p=t
      
      
