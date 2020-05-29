from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Customer:
    def __init__(self,root):
        self.root = root
        self.root.title('Customer Billing System')
        self.root.geometry('1350x750+25+25') #25+25 open the window at top left corner of screen
        self.root.config(background='powder blue')

        #Frame Layout ------------------------------------------------------

        ABC = Frame(self.root,bg='powder blue', bd=20, relief=RIDGE)
        ABC.grid()
        
        ABC1 = Frame(ABC,bd=14,width=1350,height=100,padx=10,bg='powder blue',relief=RIDGE)
        ABC1.grid(row=0,column=0,columnspan=4,sticky=W)
        
        ABC2 = Frame(ABC,bd=14,width=450,height=488,padx=10,bg='cadet blue',relief=RIDGE)
        ABC2.grid(row=1,column=0,sticky=W)

        ABC3 = Frame(ABC,bd=14,width=450,height=488,padx=10,bg='powder blue',relief=RIDGE)
        ABC3.grid(row=1,column=1,sticky=W)

        ABC4 = Frame(ABC,bd=14,width=460,height=488,padx=10,bg='cadet blue',relief=RIDGE)
        ABC4.grid(row=1,column=2,sticky=W)

        ABC5 = Frame(ABC4,bd=14,width=370,height=340,padx=10,bg='cadet blue',relief=RIDGE)
        ABC5.grid(row=0,column=0,sticky=W)

        ABC6 = Frame(ABC4,bd=14,width=370,height=120,padx=10,bg='cadet blue',relief=RIDGE)
        ABC6.grid(row=1,column=0,columnspan=4,sticky=W)
        #---------------------------------------------------------------------------
        

        #setting up date and time---------------------------------------------------------

        Date1 = StringVar()
        Time1=StringVar()
        Date1.set(datetime.now().strftime('%d/%m/%y'))
        Time1.set(datetime.now().strftime('%H:%M:%S'))

        self.lblTitle = Label(ABC1, textvariable=Date1,font=('%Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue',fg='Cornsilk').grid(row=0,column=0)
        
        self.lblTitle = Label(ABC1, text='\tcustomer billing system\t\t',font=('Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue',fg='Cornsilk',justify=CENTER).grid(row=0,column=1)

        self.lblTitle = Label(ABC1, textvariable=Time1,font=('%Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue',fg='Cornsilk').grid(row=0,column=2)
        #----------------variables used--------------------------------------------------------

        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNO = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        CustomerRef.set(random.randint(1980,9875648))

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        E_Latta = StringVar()
        E_Espresso = StringVar()
        E_Iced_Latta = StringVar()
        E_Vale_Coffee = StringVar()
        E_Cappuccino = StringVar()
        E_African_Coffee = StringVar()
        E_American_Coffee = StringVar()
        E_Iced_Cappuccino = StringVar()

        E_Latta.set('0')
        E_Espresso.set('0')
        E_Iced_Latta.set('0')
        E_Vale_Coffee.set('0')
        E_Cappuccino.set('0')
        E_African_Coffee.set('0')
        E_American_Coffee.set('0')
        E_Iced_Cappuccino.set('0')

        #Button action--------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno('Customer Billing System',
                                                'Confirm if you want to exit')
            if iExit >0:
                root.destroy()
                return

        def Reset():
            self.txtReceipt.delete('1.0',END)
            E_Latta.set('0')
            E_Espresso.set('0')
            E_Iced_Latta.set('0')
            E_Vale_Coffee.set('0')
            E_Cappuccino.set('0')
            E_African_Coffee.set('0')
            E_American_Coffee.set('0')
            E_Iced_Cappuccino.set('0')

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            CustomerRef.set('')
            Firstname.set('')
            Surname.set('')
            Address.set('')
            PostCode.set('')
            Mobile.set('')
            Email.set('')
            Nationality.set('')
            DOB.set('')
            IDType.set('')
            Gender.set('')
            CheckInDate.set('')
            CheckOutDate.set('')
            Meal.set('')
            RoomType.set('')
            RoomNO.set('')
            RoomExtNo.set('')
            TotalCost.set('')
            SubTotal.set('')
            PaidTax.set('')
            TotalDays.set('')
            #----------------------------------------------

        def chkLatta():
            if(var1.get() == 1):
                self.txtLatta.configure(state=NORMAL)
                self.txtLatta.focus()
                self.txtLatta.delete('0',END)
                E_Latta.set('')
            elif var1.get() == 0:
                self.txtLatta.configure(state=DISABLE)
                self.txtLatta.set('0')


        def chkEspresso():
            if(var2.get() == 1):
                self.txtEspresso.configure(state=NORMAL)
                self.txtEspresso.focus()
                self.txtEspresso.delete('0',END)
                E_Espresso.set('')
            elif var2.get() == 0:
                self.txtEspresso.configure(state=DISABLE)
                self.txtEspresso.set('0')

        def chkIced_Latta():
            if(var3.get() == 1):
                self.txtIced_Latta.configure(state=NORMAL)
                self.txtIced_Latta.focus()
                self.txtIced_Latta.delete('0',END)
                E_Iced_Latta.set('')
            elif var3.get() == 0:
                self.Iced_Latta.configure(state=DISABLE)
                self.Iced_Latta.set('0')

        def chkVale_Coffee():
            if(var4.get() == 1):
                self.txtVale_Coffee.configure(state=NORMAL)
                self.txtVale_Coffee.focus()
                self.txtVale_Coffee.delete('0',END)
                E_Vale_Coffee.set('')
            elif var4.get() == 0:
                self.Vale_Coffee.configure(state=DISABLE)
                self.Vale_Coffee.set('0')

        def chkCappuccino():
            if(var5.get() == 1):
                self.txtCappuccino.configure(state=NORMAL)
                self.txtCappuccino.focus()
                self.txtCappuccino.delete('0',END)
                E_Cappuccino.set('')
            elif var5.get() == 0:
                self.txtCappuccino.configure(state=DISABLE)
                self.txtCappuccino.set('0')

        def chkAfrican_Coffee():
            if(var6.get() == 1):
                self.txtAfrican_Coffee.configure(state=NORMAL)
                self.txtAfrican_Coffee.focus()
                self.txtAfrican_Coffee.delete('0',END)
                E_African_Coffee.set('')
            elif var6.get() == 0:
                self.txtAfrican_Coffee.configure(state=DISABLE)
                self.txtAfrican_Coffee.set('0')

        def chkAmerican_Coffee():
            if(var7.get() == 1):
                self.txtAmerican_Coffee.configure(state=NORMAL)
                self.txtAmerican_Coffee.focus()
                self.txtAmerican_Coffee.delete('0',END)
                E_American_Coffee.set('')
            elif var7.get() == 0:
                self.txtAmerican_Coffee.configure(state=DISABLE)
                self.txtAmerican_Coffee.set('0')

        def chkIced_Cappuccino():
            if(var8.get() == 1):
                self.txtIced_Cappuccino.configure(state=NORMAL)
                self.txtIced_Cappuccino.focus()
                self.txtIced_Cappuccino.delete('0',END)
                E_Iced_Cappuccino.set('')
            elif var8.get() == 0:
                self.txtIced_Cappuccino.configure(state=DISABLE)
                self.txtIced_Cappuccino.set('0')
                    
        #--------------------------------------------
        #------------Total button action---------------------

        def costofItem():
            CustomerRef.set(random.randint(1980,9875648))
            Item1=float(E_Latta.get())
            Item2=float(E_Espresso.get())
            Item3=float(E_Iced_Latta.get())
            Item4=float(E_Vale_Coffee.get())
            Item5=float(E_Cappuccino.get())
            Item6=float(E_African_Coffee.get())
            Item7=float(E_American_Coffee.get())
            Item8=float(E_Iced_Cappuccino.get())

            PriceofDrinks = (Item1 * 100)+(Item2 * 150)+(Item3 * 120)+(Item4 * 130)+(Item5 * 200)+(Item6 * 180)+(Item7 * 170)+(Item8 * 130)

            SubTotalofItems="Rs",str('%.2f'%(PriceofDrinks))
            SubTotal.set(SubTotalofItems)

            Tax ="Rs",str('%.2f'%(PriceofDrinks*0.15))
            PaidTax.set(Tax)

            TTax = ((PriceofDrinks)*0.15)
            TCost = "Rs",str('%.2f'%(PriceofDrinks+TTax))
            TotalCost.set(TCost)

            self.txtReceipt.insert(END,'Items\t\t\t\t'+'Cost of Items \n')
            self.txtReceipt.insert(END,'Latta: \t\t\t\t'+E_Latta.get()+'\n')
            self.txtReceipt.insert(END,'Espresso: \t\t\t\t'+E_Espresso.get()+'\n')
            self.txtReceipt.insert(END,'Iced Latta: \t\t\t\t'+E_Iced_Latta.get()+'\n')
            self.txtReceipt.insert(END,'Vale Coffee: \t\t\t\t'+E_Vale_Coffee.get()+'\n')
            self.txtReceipt.insert(END,'Cappuccino: \t\t\t\t'+E_Cappuccino.get()+'\n')
            self.txtReceipt.insert(END,'African Coffee: \t\t\t\t'+E_African_Coffee.get()+'\n')
            self.txtReceipt.insert(END,'American Coffee: \t\t\t\t'+E_American_Coffee.get()+'\n')
            self.txtReceipt.insert(END,'Iced Cappuccino: \t\t\t\t'+E_Iced_Cappuccino.get()+'\n')

            self.txtReceipt.insert(END,'Tax: \t\t\t\t'+PaidTax.get()+'\n')
            self.txtReceipt.insert(END,'Sub Total: \t\t\t\t'+str(SubTotal.get())+'\n')
            self.txtReceipt.insert(END,'Total: \t\t\t\t'+str(TotalCost.get())+'\n')


        #----------Labels -------------------------------------------------
        


        self.lblCus_Ref=Label(ABC2,font=('aria',12,'bold'),text='Customer Ref:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblCus_Ref.grid(row=0,column=0,sticky=W)
        self.txtCus_Ref=Entry(ABC2,font=('arial',12,'bold'),textvariable=CustomerRef,width=20)
        self.txtCus_Ref.grid(row=0,column=1,pady=3,padx=20)

        self.lblFirstname=Label(ABC2,font=('aria',12,'bold'),text='First Name:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(ABC2,font=('arial',12,'bold'),textvariable=Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1,pady=3,padx=20)

        self.lblSurname=Label(ABC2,font=('aria',12,'bold'),text='Surname:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(ABC2,font=('arial',12,'bold'),textvariable=Surname,width=20)
        self.txtSurname.grid(row=2,column=1,pady=3,padx=20)

        self.lblAddress=Label(ABC2,font=('aria',12,'bold'),text='Address:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(ABC2,font=('arial',12,'bold'),textvariable=Address,width=20)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        self.lblPostCode=Label(ABC2,font=('aria',12,'bold'),text='PostCode:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(ABC2,font=('arial',12,'bold'),textvariable=PostCode,width=20)
        self.txtPostCode.grid(row=4,column=1,pady=3,padx=20)

        self.lblMobile=Label(ABC2,font=('aria',12,'bold'),text='Mobile:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(ABC2,font=('arial',12,'bold'),textvariable=Mobile,width=20)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail=Label(ABC2,font=('aria',12,'bold'),text='Email:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(ABC2,font=('arial',12,'bold'),textvariable=Email,width=20)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblNationality=Label(ABC2,font=('aria',12,'bold'),text='Naitionality:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblNationality.grid(row=7,column=0,sticky=W)
        #dropdown box
        self.cboN=ttk.Combobox(ABC2,font=('arial',12,'bold'),state='readonly',
                               textvariable=Nationality,width=18)
        self.cboN['value']=('','Indian','Other')
        self.cboN.current(0)
        self.cboN.grid(row=7,column=1,pady=3,padx=20)

        self.lblDOB=Label(ABC2,font=('aria',12,'bold'),text='DOB:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblDOB.grid(row=8,column=0,sticky=W)
        self.txtDOB=Entry(ABC2,font=('arial',12,'bold'),textvariable=DOB,width=20)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20)

        self.lblIDType=Label(ABC2,font=('aria',12,'bold'),text='IDType:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblIDType.grid(row=9,column=0,sticky=W)
        #dropdown box
        self.cboIDType=ttk.Combobox(ABC2,font=('arial',12,'bold'),state='readonly',
                               textvariable=IDType,width=18)
        self.cboIDType['value']=('','Pilot Licence','Driving Licence','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)

        self.lblGender=Label(ABC2,font=('aria',12,'bold'),text='Gender:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblGender.grid(row=10,column=0,sticky=W)
        #dropdown box
        self.cboGender=ttk.Combobox(ABC2,font=('arial',12,'bold'),state='readonly',
                               textvariable=Gender,width=18)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)

        self.lblCheckInDate=Label(ABC2,font=('aria',12,'bold'),text='CheckInDate:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblCheckInDate.grid(row=11,column=0,sticky=W)
        self.txtCheckInDate=Entry(ABC2,font=('arial',12,'bold'),textvariable=Date1,width=20)
        self.txtCheckInDate.grid(row=11,column=1,pady=3,padx=20)

        self.lblCheckOutDate=Label(ABC2,font=('aria',12,'bold'),text='CheckOutDate:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblCheckOutDate.grid(row=12,column=0,sticky=W)
        self.txtCheckOutDate=Entry(ABC2,font=('arial',12,'bold'),textvariable=Date1,width=20)
        self.txtCheckOutDate.grid(row=12,column=1,pady=3,padx=20)

        self.lblMeal=Label(ABC2,font=('aria',12,'bold'),text='Meal:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblMeal.grid(row=13,column=0,sticky=W)
        #dropdown box
        self.cboMeal=ttk.Combobox(ABC2,font=('arial',12,'bold'),state='readonly',
                               textvariable=Meal,width=18)
        self.cboMeal['value']=('','BreakFast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)

        self.lblRoomType=Label(ABC2,font=('aria',12,'bold'),text='RoomType:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.lblRoomType.grid(row=14,column=0,sticky=W)
        #dropdown box
        self.cboRoomType=ttk.Combobox(ABC2,font=('arial',12,'bold'),state='readonly',
                               textvariable=RoomType,width=18)
        self.cboRoomType['value']=('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)
        #--------------------------------------------------------------------------

        #check box ----------------------------------------------------------------

        self.Latta = Checkbutton(ABC3,text='Latta',variable=var1,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkLatta).grid(row=0,sticky=W)
        self.txtLatta = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Latta,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtLatta.grid(row=0,column=1)
        

        self.Espresso = Checkbutton(ABC3,text='Espresso',variable=var2,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkEspresso).grid(row=1,sticky=W)
        self.txtEspresso = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Espresso,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtEspresso.grid(row=1,column=1)
        

        self.Iced_Latta = Checkbutton(ABC3,text='Iced Latta',variable=var3,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkIced_Latta).grid(row=2,sticky=W)
        self.txtIced_Latta = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Iced_Latta,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtIced_Latta.grid(row=2,column=1)
        

        self.Vale_Coffee = Checkbutton(ABC3,text='Vale Coffee',variable=var4,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkVale_Coffee).grid(row=3,sticky=W)
        self.txtVale_Coffee = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Vale_Coffee,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtVale_Coffee.grid(row=3,column=1)
        

        self.Cappuccino = Checkbutton(ABC3,text='Cappuccino',variable=var5,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkCappuccino).grid(row=4,sticky=W)
        self.txtCappuccino = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Cappuccino,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtCappuccino.grid(row=4,column=1)
        

        self.African_Coffee = Checkbutton(ABC3,text='African Coffee',variable=var6,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkAfrican_Coffee).grid(row=5,sticky=W)
        self.txtAfrican_Coffee = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_African_Coffee,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtAfrican_Coffee.grid(row=5,column=1)
        

        self.American_Coffee = Checkbutton(ABC3,text='American Coffee',variable=var7,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkAmerican_Coffee).grid(row=6,sticky=W)
        self.txtAmerican_Coffee = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_American_Coffee,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtAmerican_Coffee.grid(row=6,column=1)
        

        self.Iced_Cappuccino = Checkbutton(ABC3,text='Iced Cappuccino',variable=var8,onvalue=1,offvalue=0,
                                 font=('arial',12,'bold'),bg='powder blue',command=chkIced_Cappuccino).grid(row=7,sticky=W)
        self.txtIced_Cappuccino = Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Iced_Cappuccino,bd=8,
                              width=20,justify='left',state=DISABLED)
        self.txtIced_Cappuccino.grid(row=7,column=1)
        

        self.lblspace = Label(ABC3,text='Tax and Total Sum',font=('arial',18,'bold'),pady=1,
                              bd=9,bg='cadet blue',fg='Cornsilk',width=26,justify=CENTER).grid(row=8,column=0,columnspan=4)


        self.PaidTax=Label(ABC3,font=('aria',12,'bold'),text='Paid Tax:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.PaidTax.grid(row=9,column=0,sticky=W)
        self.PaidTax=Entry(ABC3,font=('arial',12,'bold'),textvariable=PaidTax,width=20)
        self.PaidTax.grid(row=9,column=1,pady=3,padx=20)
        

        self.SubTotal=Label(ABC3,font=('aria',12,'bold'),text='Sub Total:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.SubTotal.grid(row=10,column=0,sticky=W)
        self.SubTotal=Entry(ABC3,font=('arial',12,'bold'),textvariable=SubTotal,width=20)
        self.SubTotal.grid(row=10,column=1,pady=3,padx=20)


        self.TotalCost=Label(ABC3,font=('aria',12,'bold'),text='Total Cost:',padx=2,fg='Cornsilk',
                              bg='cadet Blue')
        self.TotalCost.grid(row=11,column=0,sticky=W)
        self.TotalCost=Entry(ABC3,font=('arial',12,'bold'),textvariable=TotalCost,width=20)
        self.TotalCost.grid(row=11,column=1,pady=3,padx=20)

        
        #--------------------------------Text box-------------------------------------
        self.txtReceipt = Text(ABC5, height=19, width=43, bd=10, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)

        #-------------------------------------------------------------------------

        #Buttons---------------------------------------------------------
        self.btnTotal = Button(ABC6,padx=14,pady=7,bd=5,fg='black',font=('arial',16,'bold'),
                               width=5,height=2,bg='powder blue',text='Total',command=costofItem).grid(row=0,column=0)

        self.btnReset = Button(ABC6,padx=14,pady=7,bd=5,fg='black',font=('arial',16,'bold'),
                               width=5,height=2,bg='powder blue',text='Reset',command=Reset).grid(row=0,column=1)

        self.btnExit = Button(ABC6,padx=14,pady=7,bd=5,fg='black',font=('arial',16,'bold'),
                               width=5,height=2,bg='powder blue',text='Exit',command=iExit).grid(row=0,column=2)
        #-----------------------------------------------------------------------------------------

        



if __name__ == '__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
    
