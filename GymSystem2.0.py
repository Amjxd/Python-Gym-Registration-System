##CardScanner.py
from random import randint
import os
from tkinter import *
import ast
from PIL import Image, ImageTk

class System():

    def register(self):
        user_info = []
        while True:
            try:
                fn = str(input('First Name: '))
            except:
                print('Invalid Name')
            else:
                break
        while True:
            try:
                ln = str(input('Last Name: '))
            except:
                print('Invalid Name')
            else:
                break
        while True:
            try:
                phone = int(input('Phone Number: ' ))
            except:
                print('Invalid Phone Number')
            else:
                break
        while True:
            try:
                term = int(input('Term (# of Months): '))
            except:
                print('Invalid Number')
            else:
                break
        while True:
            try:
                goal = str(input('Athletic Goal: ' ))
            except:
                print('Invalid Goal')
            else:
                break
        date = input('Date (YYYY/MM/DD): ')
        y_or_n = input('Take Picture? (Y or N): ')
        if y_or_n == 'Y':
            pic = input('Picture File: ')
        else:
            pic = 'no_pic.png'
        user_info.extend((fn,ln,phone,term,goal,date,pic))

        def unique_ID(user_info):
            user_id = []
            i = 0
            alpha = randint(65,91)
            letter = chr(alpha)
            user_id.append(letter)
            while 9 > i:
                user_id.append(randint(0,10))
                i += 1
            user_ID = []
            for i in user_id:
                i = str(i)
                user_ID.append(i)
            user_ID = ''.join(user_ID)
            user = {user_ID:user_info}
            return user

        user = unique_ID(user_info)
        with open("GymMembers.txt.","w") as f:
            f.write(f'{user} \n')
        

        
    def pull(self,code):
        with open("GymMembers.txt.",'r') as m:
            for line in m:
                t = code in line
                if t == True:
                    return line
        
    def display(self,userinfo,code):
        #Turns String Representation Dictionary into Dictionary
        dic = ast.literal_eval(userinfo)

        #User Info
        root = Toplevel()
        root.title(f'{dic[code][0]} {dic[code][1]}')
        root.configure(background = 'powder blue')
        root.resizable(width=False,height = False)

        #Picture Display
        pic = str(dic[code][6])
        load = Image.open(pic)
        render = ImageTk.PhotoImage(load)
        img = Label(root, image = render)
        img.image = render
        img.grid(column=20,row=10)

        #NAME
        namelay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "NAME:")
        namelay.grid(column = 0, row = 0,sticky = W,pady=0)
        name = Label(root,text=f'{dic[code][0]} {dic[code][1]}',bg='powder blue', font = ('arial',14))
        name.grid(column= 1, row = 0,sticky = W,pady=0)
        
        #PHONE
        phonelay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "PHONE NUMBER:")
        phonelay.grid(column = 0, row = 1,sticky = W)
        phone = Label(root,text=f'{dic[code][2]}',bg='powder blue', font = ('arial',14))
        phone.grid(column= 1, row = 1,sticky = W)

        #DATE
        datelay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "REGISTRY DATE:")
        datelay.grid(column = 0, row = 2,sticky = W,pady=0)
        date = Label(root,text=f'{dic[code][5]}',bg='powder blue', font = ('arial',14))
        date.grid(column= 1, row = 2,sticky = W,pady=0)
        
        #TERM
        termlay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "# OF MONTHS:")
        termlay.grid(column = 0, row = 3,sticky = W)
        term = Label(root,text=f'{dic[code][3]}',bg='powder blue', font = ('arial',14))
        term.grid(column= 1, row = 3,sticky = W)

        #GOAL
        goallay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "ATHLETIC GOAL:")
        goallay.grid(column = 0, row = 4,sticky = W)
        goal = Label(root,text=f'{dic[code][4]}',bg='powder blue', font = ('arial',14))
        goal.grid(column= 1, row = 4,sticky = W)

        #line break
        breaklay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "")
        breaklay.grid(column = 0, row = 6,sticky = W)

        #User ID
        idlay = Label(root, font = ('arial',14,'bold'), bg = 'powder blue',text= "USER ID:")
        idlay.grid(column = 0, row = 7,sticky = W)
        id1 = Label(root,text=f'{code}',bg='powder blue', font = ('arial',14))
        id1.grid(column= 1, row = 7,sticky = W)

    def submit_ID(self):
        global code
        code = search.get()
        contents = entry.pull(code)
        display = entry.display(contents,code)
 

entry = System()
code = 0
reg = Tk()
reg.title('Command Centre')
reg.configure(background = 'powder blue')
reg.resizable(width=False,height = False)
reg.geometry("260x100+0+0")
searchlabel = Label(text = 'ID',font=('arial',15,'bold'),bg='powder blue')
searchlabel.grid(column=0,row=0)
search = Entry(reg, borderwidth = 5)
search.grid(column = 1,row=0) 
register = Button(reg, text = 'Register',width=7,height=4,font=('arial',15,'bold'),bd=4,highlightbackground="powder blue",command = entry.register)
register.grid(column=1,row=2)
submit = Button(reg, text = 'Submit',width=6,height=4,font=('arial',15,'bold'),bd=4,highlightbackground="powder blue",command = entry.submit_ID)
submit.grid(column=0,row=2)
reg.mainloop()











            


    

    
        
