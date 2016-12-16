from tkinter import *
import tkinter.messagebox as tm
import db2

root = Tk()
root.title("Home ")
root.resizable(False, False)

logo = PhotoImage(file="download.png")
logo2 = PhotoImage(file="giphy.gif")  

logo1 = PhotoImage(file="giphy.gif")
root.label_Logo = Label(root, image=logo1)
root.label_Logo.pack()


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.logbtn = Button(self, text="Buying", command=self._login_btn_clickked_1,width=30,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Update User", command=self._login_btn_clickked_2,width=32,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Delete User", command=self._login_btn_clickked_3,width=34,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Add User", command=self._login_btn_clickked_4,width=36,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Menu", command=self._login_btn_clickked_5,width=38,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Total price", command=self._login_btn_clickked_6,width=40,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Update Meals", command=self._login_btn_clickked_7,width=42,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),bd=3)
        self.logbtn.grid(columnspan=2)
        self.pack()

    def _login_btn_clickked_1(self):
        root.destroy()
        import Python;

    def _login_btn_clickked_2(self):
        root.destroy()
        import update;

    def _login_btn_clickked_3(self):
        root.destroy()
        import delete;

    def _login_btn_clickked_4(self):
        root.destroy()
        import insert_user;

    def _login_btn_clickked_5(self):
        root.destroy()
        import Sectect_meales;

    def _login_btn_clickked_6(self):
        root.destroy()
        import Sectect_TotalPrices;

    def _login_btn_clickked_7(self):
        root.destroy()
        import update_Meals_Sal;


lf = LoginFrame(root)
root.mainloop()
