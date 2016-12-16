from tkinter import *
import tkinter.messagebox as tm
import db2


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username",font =('arial', 10 , 'bold'))
        self.label_2 = Label(self, text="Password",font =('arial', 10 , 'bold'))

        self.entry_1 = Entry(self,width=60,font =('arial', 8 , 'bold'),bd=10)
        self.entry_2 = Entry(self, show="*",width=60,font =('arial', 8 , 'bold'),bd=10)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)


        self.logbtn = Button(self, text="DELETE_USER",width=30,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3, command=self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        i = db2.select_item(db2.db, dict(USER_NAME=username, PASSWORD=password))
        print(i)

        if i > 0:
            db2.delete(db2.db, username)
            db2.query(db2.db)
            tm.showerror("Login error", "تم المسح ")

        else:
            tm.showerror("Login error", "مش موجود")









root = Tk()
lf = LoginFrame(root)
root.mainloop()
