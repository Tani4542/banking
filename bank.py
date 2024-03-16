from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
title=Label(win,text="Bank Automation",font=('arial',60,'bold','underline'),bg='powder blue')
title.pack()

def home_screen():
    frm=Frame(win)
    frm.configure(bg="white")
    frm.place(relx=.1,rely=.2,relwidth=.8,relheight=.7)
    
    def open_click():
        frm.destroy()
        openaccount_screen()
    def recover_click():
        frm.destroy()
        recoverpass_screen()
        
    def login_click():
        acc=acn_entry.get()
        pwd=pass_entry.get()
        if len(acc)==0 or len(pwd)==0:
            messagebox.showwarning("login","empty field found")
        else:
            frm.destroy()
            welcome_screen()
    
        
    img=PhotoImage(file='login.png')
    label_img = Label(frm, image=img, bg="white")
    label_img.image = img
    label_img.place(relx=.1,rely=.1)
    
    heading=Label(frm,text='Sing in', fg='#052c65',bg='white',font=('arial',23,'bold','underline'))
    heading.place(relx=.57,rely=.1)
    
    def on_enter(e):
        acn_entry.delete(0,'end')
    def on_leave(e):
        name=acn_entry.get()
        if name=='':
            acn_entry.insert(0,'Account Number')
    acn_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='black',border=0)

    acn_entry.insert(0,"Account")
    acn_entry.bind('<FocusIn>',on_enter)
    acn_entry.bind('<FocusOut>',on_leave)
    acn_entry.place(relx=.45,rely=.22)
    acn_entry.focus()
    
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.26)
    def on_enter(e):
        pass_entry.delete(0,'end')
    def on_leave(e):
        name=pass_entry.get()
        if name=='':
            pass_entry.insert(0,'Password')    
    pass_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='black',border=0)
    pass_entry.insert(0,"Password")
    pass_entry.bind('<FocusIn>',on_enter)
    pass_entry.bind('<FocusOut>',on_leave)
    pass_entry.place(relx=.45,rely=.32)
    
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.36)
    
    btn_recpass=Button(frm,font=('arial',9,'bold','underline'),text="Forgot Password",bg='white',cursor='hand2',fg='#0d6efd',width=15,border=0,command=recover_click)
    btn_recpass.place(relx=.7,rely=.42)
    
    btn_login=Button(frm,font=('arial',20,'bold'),text="Login",bg='#0d6efd',fg='white',width=21,pady=7,border=1,cursor="hand2",command=login_click)
    btn_login.place(relx=.45,rely=.5)
    
    lable=Label(frm,text="Don't have an account?",fg='black',bg='white',font=('arial',11,'bold'))
    lable.place(relx=.5,rely=.69)
    
    btn_new=Button(frm,font=('arial',9,'bold','underline'),text="Create account",bg='white',cursor='hand2',fg='#0d6efd',width=15,border=0,command=open_click)
    btn_new.place(relx=.67,rely=.69)
def openaccount_screen():
    frm=Frame(win) 
    frm.configure(bg="white")
    frm.place(relx=.1,rely=.2,relwidth=.8,relheight=.7)
    
    def home_click():
        frm.destroy()
        home_screen()
    
    heading=Label(frm,text='Create an Account', fg='#052c65',bg='white',font=('arial',23,'bold','underline'))
    heading.place(relx=.35,rely=0)
    
    f_name_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="First Name:")
    f_name_lbl.place(relx=.02,rely=.1)
    f_name_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    f_name_entry.place(relx=.19,rely=.10)
    f_name_entry.focus()
    Frame(frm,width=220,height=1,bg='black').place(relx=.19,rely=.16)
    
    l_name_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Last Name:")
    l_name_lbl.place(relx=.5,rely=.1)
    l_name_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    l_name_entry.place(relx=.7,rely=.10)
    Frame(frm,width=220,height=1,bg='black').place(relx=.7,rely=.16)
    
    dob_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Date of Birth:")
    dob_lbl.place(relx=.02,rely=.2)
    dob_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    dob_entry.place(relx=.19,rely=.20)
    Frame(frm,width=220,height=1,bg='black').place(relx=.19,rely=.26)
    
    def select_one(checkbox):
        if checkbox == "male":
            female_var.set(0)
            other_var.set(0)
        elif checkbox == "female":
            male_var.set(0)
            other_var.set(0)
        elif checkbox == "other":
            male_var.set(0)
            female_var.set(0)
    gender_lbl = Label(frm, font=('arial', 16, 'bold'), bg='white', fg='#000', border=0, text="Gender:")
    gender_lbl.place(relx=.5, rely=.2)
    male_var = IntVar()
    female_var = IntVar()
    other_var = IntVar()
    gen_btn1 = Checkbutton(frm, text="Male", variable=male_var, onvalue=1, offvalue=0, width=10,fg='#000',bg='white',command=lambda: select_one("male"))
    gen_btn2 = Checkbutton(frm, text="Female", variable=female_var, onvalue=1, offvalue=0, width=10, fg='#000',bg='white',command=lambda: select_one("female"))
    gen_btn3 = Checkbutton(frm, text="Other", variable=other_var, onvalue=1, offvalue=0, width=10, fg='#000',bg='white',command=lambda: select_one("other"))
    gen_btn1.place(relx=.68, rely=.20)
    gen_btn2.place(relx=.75, rely=.20)
    gen_btn3.place(relx=.83, rely=.20)

    father_name_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Father Name:")
    father_name_lbl.place(relx=.02,rely=.3)
    father_name_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    father_name_entry.place(relx=.19,rely=.30)
    Frame(frm,width=220,height=1,bg='black').place(relx=.19,rely=.36)
    
    mother_name_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Mother Name:")
    mother_name_lbl.place(relx=.5,rely=.3)
    mother_name_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    mother_name_entry.place(relx=.7,rely=.30)
    Frame(frm,width=220,height=1,bg='black').place(relx=.7,rely=.36)
 
    mob_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Mobile Numabr:")
    mob_lbl.place(relx=.02,rely=.4)
    mob_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    mob_entry.place(relx=.19,rely=.40)
    Frame(frm,width=220,height=1,bg='black').place(relx=.19,rely=.46)
    
    adh_num_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Aadhar Number:")
    adh_num_lbl.place(relx=.5,rely=.4)
    adh_num_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    adh_num_entry.place(relx=.7,rely=.40)
    Frame(frm,width=220,height=1,bg='black').place(relx=.7,rely=.46)
    
    nominee_name_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Nominee Name:")
    nominee_name_lbl.place(relx=.02,rely=.5)
    nominee_name_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    nominee_name_entry.place(relx=.19,rely=.50)
    Frame(frm,width=220,height=1,bg='black').place(relx=.19,rely=.56)
    
    acntype_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Account type:")  
    acntype_lbl.place(relx=.5,rely=.5)
    acntype_cb=Combobox(frm,font=('arial',16),values=['Select Account type','Saving','Current','Fixed Deposit'],width='17')
    acntype_cb.current(0)
    acntype_cb.place(relx=.7,rely=.50)
    
    add_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Address:")
    add_lbl.place(relx=.02,rely=.6)
    add_entry = Text(frm, font=('arial', 16), bg='white', border=1, width=18, height=3)
    add_entry.place(relx=.19, rely=.60)
    # Frame(frm,width=220,height=1,bg='black').place(relx=.18,rely=.76)
    
    password_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Password:")
    password_lbl.place(relx=.5,rely=.6)
    password_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    password_entry.place(relx=.7,rely=.60)
    Frame(frm,width=220,height=1,bg='black').place(relx=.7,rely=.66)
    
    con_password_lbl=Label(frm,font=('arial',16,'bold'),bg='white',fg='#000',border=0,text="Confirm Password:")
    con_password_lbl.place(relx=.5,rely=.7)
    con_password_entry=Entry(frm,font=('arial',16),bg='white',border=0,width=18)
    con_password_entry.place(relx=.7,rely=.70)
    Frame(frm,width=220,height=1,bg='black').place(relx=.7,rely=.76)
    
    btn_create=Button(frm,font=('arial',10,'bold'),text="Create Account",bg='#198754',fg='white',width=15,border=1,cursor="hand2")
    btn_create.place(relx=.35,rely=.83)
    btn_clear=Button(frm,font=('arial',10,'bold'),text="Clear",bg='#dc3545',fg='white',width=15,border=1,cursor="hand2")
    btn_clear.place(relx=.5,rely=.83)
    lable=Label(frm,text="I have an account.",fg='#000',bg='white',font=('arial',11,'bold'))
    lable.place(relx=.4,rely=.93)
    btn_old_act=Button(frm,font=('arial',9,'bold','underline'),text="Login hear",bg='white',cursor='hand2',fg='#0d6efd',width=15,border=0,command=home_click)
    btn_old_act.place(relx=.53,rely=.93)
    
    
def recoverpass_screen():
    frm=Frame(win) 
    frm.configure(bg="white")
    frm.place(relx=.1,rely=.2,relwidth=.8,relheight=.7)
    
    def home_click():
        frm.destroy()
        home_screen()
    img=PhotoImage(file='login.png')
    label_img = Label(frm, image=img, bg="white")
    label_img.image = img
    label_img.place(relx=.1,rely=.1)
    
    heading=Label(frm,text='Forgot your password?', fg='#052c65',bg='white',font=('arial',23,'bold','underline'))
    heading.place(relx=.45,rely=.08)
    heading_details=Label(frm,text='Please enter your details,you use to singin.', fg='#000',bg='white',font=('arial',8))
    heading_details.place(relx=.45,rely=.17)
    
    def on_enter(e):
        acn_entry.delete(0,'end')
    def on_leave(e):
        name=acn_entry.get()
        if name=='':
            acn_entry.insert(0,'Acount Number')
    acn_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='#000',border=0)
    acn_entry.insert(0,'Acount Number')
    acn_entry.bind('<FocusIn>',on_enter)
    acn_entry.bind('<FocusOut>',on_leave)
    acn_entry.place(relx=.45,rely=.22)
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.26)
    
    def on_enter(e):
        mob_entry.delete(0,'end')
    def on_leave(e):
        name=mob_entry.get()
        if name=='':
            mob_entry.insert(0,'Mobile Number')
    mob_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='#000',border=0)
    mob_entry.insert(0,'Mobile Number')
    mob_entry.bind('<FocusIn>',on_enter)
    mob_entry.bind('<FocusOut>',on_leave)
    mob_entry.place(relx=.45,rely=.32)    
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.36)
    
    def on_enter(e):
        email_entry.delete(0,'end')
    def on_leave(e):
        name=email_entry.get()
        if name=='':
            email_entry.insert(0,'Email Id')
    email_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='#000',border=0)
    email_entry.insert(0,'Email Id')
    email_entry.bind('<FocusIn>',on_enter)
    email_entry.bind('<FocusOut>',on_leave)
    email_entry.place(relx=.45,rely=.42)
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.46)
    def on_enter(e):
        pass_entry.delete(0,'end')
    def on_leave(e):
        name=pass_entry.get()
        if name=='':
            pass_entry.insert(0,'Password')    
    pass_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='#000',border=0)
    pass_entry.insert(0,'Password')
    pass_entry.bind('<FocusIn>',on_enter)
    pass_entry.bind('<FocusOut>',on_leave)
    pass_entry.place(relx=.45,rely=.52)    
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.56)
    
    def on_enter(e):
        con_pass_entry.delete(0,'end')
    def on_leave(e):
        name=con_pass_entry.get()
        if name=='':
            con_pass_entry.insert(0,'Confirm Password')    
    con_pass_entry=Entry(frm,font=('arial',11),bg='white',width=45,fg='#000',border=0)
    con_pass_entry.insert(0,'Confirm Password')
    con_pass_entry.bind('<FocusIn>',on_enter)
    con_pass_entry.bind('<FocusOut>',on_leave)
    con_pass_entry.place(relx=.45,rely=.62)   
    Frame(frm,width=362,height=2,bg='black').place(relx=.45,rely=.66)    
    btn_reset=Button(frm,font=('arial',20,'bold'),text="Reset Password",bg='#0d6efd',fg='white',width=21,border=1,cursor="hand2")
    btn_reset.place(relx=.45,rely=.7)
    btn_back=Button(frm,font=('arial',9,'bold','underline'),text="Back to Sing in",bg='white',cursor='hand2',fg='#0d6efd',width=15,border=0,command=home_click)
    btn_back.place(relx=.56,rely=.84)


    
    
def welcome_screen():
    frm=Frame(win) 
    frm.configure(bg="white")
    frm.place(relx=.0,rely=.2,relwidth=1,relheight=.8)
    def profile_screen():
        def welcome_click():
            frm.destroy()
            welcome_screen()
            
        def update_screen():
            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='white')
            ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
            title_lbl=Label(ifrm,text='This is Update Screen',font=('arial',20,'bold'),bg='white',fg='purple')
            title_lbl.pack()
        def update_click():
            ifrm.destroy()
            update_screen()
            
        def password_change_screen():
            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='white')
            ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
            title_lbl=Label(ifrm,text='This is Password change Screen',font=('arial',20,'bold'),bg='white',fg='purple')
            title_lbl.pack()
        def password_change_click():
            ifrm.destroy()
            password_change_screen()
        ifrm=Frame(frm) 
        ifrm.configure(bg="powder blue")
        ifrm.place(relx=.8,rely=0.07,relwidth=0.12,relheight=.2)
        btn_profile=Button(ifrm,width=12,font=('arial',8,'bold'),text="Profile Setting",fg='#0d6efd',border=1,cursor="hand2",command=update_click)
        btn_profile.place(relx=0.2,rely=0.02)    
        
        btn_profile_pass=Button(ifrm,width=15,font=('arial',8,'bold'),text="Password Change",fg='#0d6efd',border=1,cursor="hand2",command=password_change_click)
        btn_profile_pass.place(relx=0.12,rely=0.28)
        
        img=PhotoImage(file='cancle.png')
        img = img.subsample(8, 8)
        btn_can_img = Button(ifrm, image=img, bg="white", border=1,command=welcome_click)
        btn_can_img.image = img
        btn_can_img.place(relx=0.25, rely=0.53)
        btn_can_back=Button(ifrm,font=('arial',9,'bold'),text="Cancle",cursor='hand2',fg='#0d6efd',width=8,border=0,command=welcome_click)
        btn_can_back.place(relx=0.39,rely=0.53)    
       
    def profile_click():
        frm.destroy()
        profile_screen()
    
    
    def home_click():
        frm.destroy()
        home_screen()
    
    
    img=PhotoImage(file='images.png')
    img = img.subsample(7, 7)
    btn_pro_img = Button(frm, image=img, bg="white", border=1)
    btn_pro_img.image = img
    btn_pro_img.place(relx=0.829, rely=0.01)
    
    btn_back=Button(frm,font=('arial',12,'bold','underline'),text="Profile",bg='white',cursor='hand2',fg='#0d6efd',width=5,border=0,command=profile_screen)
    btn_back.place(relx=0.85,rely=0.01)
    
    img=PhotoImage(file='logout.png')
    img = img.subsample(10, 10)
    btn_log_img = Button(frm, image=img, bg="white", border=1,command=home_click)
    btn_log_img.image = img
    btn_log_img.place(relx=0.9, rely=0.01)
    btn_back=Button(frm,font=('arial',12,'bold','underline'),text="Logout",bg='white',cursor='hand2',fg='#0d6efd',width=6,border=0,command=home_click)
    btn_back.place(relx=0.92,rely=0.01)

    
    img=PhotoImage(file='bank.png')
    img = img.subsample(1, 1)
    label_img = Label(frm, image=img, bg="white")
    label_img.image = img
    label_img.place(relx=0.2,rely=.06)
    # btn_back=Button(frm,font=('arial',20,'bold'),text="Update Profile",bg='#6c757d',cursor='hand2',fg='white',width=15,border=0,command=home_click)
    # btn_back.place(relx=0.82,rely=0.1)
    def balance_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
        title_lbl=Label(ifrm,text='This is Check balance Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
    def deposit_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
        title_lbl=Label(ifrm,text='This is Deposit Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
    def withdraw_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
        title_lbl=Label(ifrm,text='This is Withdraw Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
    def mini_statement_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
        title_lbl=Label(ifrm,text='This is Mini Statement Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
    def transfer_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.07,rely=.13,relwidth=.7,relheight=.75)
        
        title_lbl=Label(ifrm,text='This is Transfer Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
    btn_bla=Button(frm,font=('arial',20,'bold'),text="Check balance",bg='#0dcaf0',cursor='hand2',fg='#000',width=15,border=0,command=balance_screen)
    btn_bla.place(relx=0.82,rely=0.15)
    
    btn_deposit=Button(frm,font=('arial',20,'bold'),text="Deposit",bg='#0dcaf0',cursor='hand2',fg='#000',width=15,border=0,command=deposit_screen)
    btn_deposit.place(relx=0.82,rely=0.30)
    
    btn_withdraw=Button(frm,font=('arial',20,'bold'),text="Withdraw",bg='#0dcaf0',cursor='hand2',fg='#000',width=15,border=0,command=withdraw_screen)
    btn_withdraw.place(relx=0.82,rely=0.45)
    
    btn_mini_statement=Button(frm,font=('arial',20,'bold'),text="Mini Statement",bg='#0dcaf0',cursor='hand2',fg='#000',width=15,border=0,command=mini_statement_screen)
    btn_mini_statement.place(relx=0.82,rely=0.60)
    
    btn_transfer=Button(frm,font=('arial',20,'bold'),text="Transfer",bg='#0dcaf0',cursor='hand2',fg='#000',width=15,border=0,command=transfer_screen)
    btn_transfer.place(relx=0.82,rely=0.75)




home_screen()
win.mainloop()
