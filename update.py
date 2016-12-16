from tkinter import *
import tkinter.messagebox as tm
import db2
root = Tk()
root.title("Update ")
root.resizable(False, False)

logo = PhotoImage(file="0b73bb37.png")
butt = PhotoImage(file="1458916771_Sync.png")
root.label_Logo = Label(root,image=logo)
root.label_Logo.pack()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self,font =('arial', 10 , 'bold'), text="old Username")
        self.label_2 = Label(self,font =('arial', 10 , 'bold'), text="old Password")

        self.entry_1 = Entry(self,width=60,font =('arial', 8 , 'bold'),bd=10)
        self.entry_2 = Entry(self, show="*",width=60,font =('arial', 8 , 'bold'),bd=10)
        self.label_3 = Label(self,font =('arial', 10 , 'bold'), text="new Username")
        self.label_4 = Label(self,font =('arial', 10 , 'bold'), text="new Password")

        self.entry_3 = Entry(self,width=60,font =('arial', 8 , 'bold'),bd=10)
        self.entry_4 = Entry(self, show="*",width=60,font =('arial', 8 , 'bold'),bd=10)

        self.label_1.grid(row=0, sticky=E,padx=5,pady=5)
        self.label_2.grid(row=1, sticky=E,padx=5,pady=5)
        self.entry_1.grid(row=0, column=1,padx=5,pady=5)
        self.entry_2.grid(row=1, column=1,padx=5,pady=5)
        self.label_3.grid(row=2, sticky=E,padx=5,pady=5)
        self.label_4.grid(row=3, sticky=E,padx=5,pady=5)
        self.entry_3.grid(row=2, column=1,padx=5,pady=5)
        self.entry_4.grid(row=3, column=1,padx=5,pady=5)

        self.logbtn = Button(self,image=butt,width=200,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3,
                             command=self._login_btn_clickked,padx=5,pady=5)
        self.logbtn.grid(columnspan=2)
        self.pack()

    def _login_btn_clickked(self):
        db2.query(db2.db)
        username = self.entry_1.get()
        password = self.entry_2.get()
        i=db2.select_item(db2.db, dict(USER_NAME = username, PASSWORD = password))
        print(i)
        if i > 0:
            new_username = self.entry_3.get()
            new_password = self.entry_4.get()
            db2.update(db2.db,dict(USER_NAME=new_username, PASSWORD= new_password ,USER_ID=i))
            db2.query(db2.db)

            tm.showinfo("Login info", "تمام ")

        else:
             tm.showerror("Login error", "مش موجود")

lf = LoginFrame(root)
root.mainloop()
