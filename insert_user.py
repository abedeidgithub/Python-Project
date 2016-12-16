from tkinter import *
import tkinter.messagebox as tm
import db2
root = Tk()
root.title("insert  User")
root.resizable(False, False)

logo = PhotoImage(file="we.gif")
butt = PhotoImage(file="1458916838_Save.png")
root.label_Logo = Label(root,image=logo)
root.label_Logo.pack()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username",font =('arial', 10 , 'bold'),bd=10,)
        self.label_2 = Label(self, text="Password",font =('arial', 10 , 'bold'),bd=10,)

        self.entry_1 = Entry(self,width=50,font =('arial', 8 , 'bold'),bd=10)
        self.entry_2 = Entry(self,width=50,font =('arial', 8 , 'bold'),bd=10, show="*")


        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(row=2, sticky=E)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)

        self.logbtn = Button(self,text="save", command=self._login_btn_clickked,width=30,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),padx=5,pady=0)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        if username=='' or password=='':
            tm.showinfo("Login info", "ادخل الحقول  ")
        else:
           db2.insert_record(db2.db,dict(USER_NAME=username, PASSWORD = password ))
           tm.showinfo("Login info", "تمام  ")

        db2.query(db2.db)


lf = LoginFrame(root)
root.mainloop()
