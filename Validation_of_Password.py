import re
name=input('enter name:')
ID=input('enter ID number:')
mobil=input('mobile number:')
password=input('enter password:')

if re.search(name , password):
    print('The password is invalid. It should not include name.')
elif re.search(ID , password):
    print('The password is invalid. It should not include  ID.')
elif re.search(mobil, password):
    print('The password is invalid. It should not include  mobile number.')    
else:
    print(password,'is a valid password')
