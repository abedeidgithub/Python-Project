from tkinter import *
import tkinter.messagebox as tm
import db2
root = Tk()
root.title("Login ")
root.resizable(False, False)
butt = PhotoImage(file="0b73bb37.png")
root.label_Logo = Label(root,image=butt)
root.label_Logo.pack()
logo = PhotoImage(file="1458916845_cloud-upload.png")
root.label_Logo = Label(root,image=logo)
root.label_Logo
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username",font =('arial', 10 , 'bold'),)
        self.label_2 = Label(self, text="Password",font =('arial', 10 , 'bold'),)

        self.entry_1 = Entry(self,font =('arial', 8 , 'bold'),bd=10,width=60)
        self.entry_2 = Entry(self, show="*",font =('arial', 8 , 'bold'),bd=10,width=60)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.logbtn = Button(self, command=self._login_btn_clickked,text="Log In",width=30,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),padx=5)
        self.logbtn.grid(columnspan=2)
        self.pack()

    def _login_btn_clickked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        i=db2.select_item(db2.db, dict(USER_NAME = username, PASSWORD = password))
        print(i)


        if i > 0:
            tm.showinfo("Login info", "Found ")
            root.destroy()
            import home;


        else:
             tm.showerror("Login error", "Not Found")





lf = LoginFrame(root)
root.mainloop()
