#!/usr/bin/env python
# coding: utf-8

# In[19]:


data = {'1001':{'name':'Mohit','email':'mohit@gmail.com','password':'trial678','city':'Jaipur','balance':69000},
       '1002':{'name':'Anurag','email':'anurag@gmail.com','password':'test123','city':'Jaipur','balance':69000},
       '1003':{'name':'Manish','email':'manish@gmail.com','password':'checking345','city':'Jaipur','balance':69000},
       '1004':{'name':'Astha','email':'astha@gmail.com','password':'testing123','city':'Jaipur','balance':69000}}


# ## LOGIN SIGNUP 

# In[11]:


def main():
    import sys
    import time
    print('*'*127)
    print()
    print('Welcome to bank portal'.center(120))
    print()
    print('*'*127)
    print()
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('1. Login\n2. Sign Up\n3. Exit')
    print()
    ip = input('Enter your choice')
    if ip == '1':
        login()
    elif ip == '2':
        signup()
    elif ip =='3':
        exit()
        print("successfully exited")
    else : 
        print('Enter wrong choice')


# ## LOGIN

# In[12]:


def login():
    import getpass
    import time
    print('*'*127)
    print()
    print('Welcome to login section'.center(120))
    print()
    print('*'*127)
    print()
   
    usr= input('Enter your username')
    if usr in data.keys():
        print('Loading...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        pas = getpass.getpass('Enter your password')
        print('Processing...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        if pas == data[usr]['password']:
            print()
            print('Loading...')
            time.sleep(2)
            print()
            print('*'*127)
            print()
            print('Login Successful'.center(120))
            print()
            print('*'*127)
            print()
            print('1. Credit\n2.Debit\n3.Balance\n4.Log Out')
            choice = input('Enter Choice')
            if choice == '1':
                credit(usr)
            elif choice == '2':
                debit(usr)
            elif choice == '3':
                chkbalance(usr)
            elif choice == '4':
                exit()
                print("successfully exited")
            else:
                print('Wrong Choice')
            
        else:
            print('Your password does not match')
            login()
    else:
        print('Your account does not found')
        print('Create your account')
        print('Redirecting')
        time.sleep(2)
        signup()
        


# ##  SIGNUP

# In[13]:


def signup():
    import getpass
    import random
    import string
    import smtplib
    import time
    
    name = input('Enter name')
    email = input('Enter email id')
    passw = getpass.getpass('Enter password') 
    d = string.digits + string.ascii_letters
    o = ""
    
    for i in range(6):
        o = o + random.choice(d)
       
    conn = smtplib.SMTP("smtp.gmail.com" , 587)
    conn.starttls()
    gmail = input("enter your gmail id")
    pas = getpass.getpass()
    conn.login(gmail,pas)
    conn.sendmail(gmail , email, f"SUBJECT:OTP \n\n\n\nYOUR OTP IS: {o}")
    print('OTP send')
    time.sleep(3)
    accno = int(list(data.keys())[-1]) + 1
    accno = str(accno)
    print(accno)
    ot = input('Enter varification code')
    if ot == o:
        data[accno]= {'name':name,'email':email,'password':passw}
        print('Processing...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print(f'{name} account is successfuly created')
        time.sleep(2)
        login()
    else:
        print('Wrong OTP ...Try again')
        signup()


# In[14]:


def credit(usr):
    bal = int(input('Enter amount to credit'))
    data[usr]['balance'] += bal
    print(f'Your amount {bal} has been successfuly credited')
    print(f"Your current balance {data[usr]['balance']}")


# In[15]:


def debit(usr):
    bal = int(input('Enter amount to debit'))
    if data[usr]['balance'] >= bal:
        data[usr]['balance'] -= bal
        print(f'Your amount {bal} has been successfuly debited')
    else:
        print('Not have sufficient amount in your account')
    
    print(f"Your current balance {data[usr]['balance']}")


# In[16]:


def chkbalance(usr):
      print(f"Your current balance is : {data[usr]['balance']}")


# In[20]:


main()


# In[ ]:




