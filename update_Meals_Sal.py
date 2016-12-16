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

        self.label_1 = Label(self,font =('arial', 10 , 'bold'), text="Name ")


        self.entry_1 = Entry(self,font =('arial', 8 , 'bold'),bd=10,width=60)
        self.label_3 = Label(self,font =('arial', 10 , 'bold'),bd=10, text="new salary")


        self.entry_3 = Entry(self,width=60,font =('arial', 8 , 'bold'),bd=10)


        self.label_1.grid(row=0, sticky=E,padx=5,pady=5)
        self.entry_1.grid(row=0, column=1,padx=5,pady=5)
        self.label_3.grid(row=2, sticky=E,padx=5,pady=5)
        self.entry_3.grid(row=2, column=1,padx=5,pady=5)

        self.logbtn = Button(self,image=butt, command=self._login_btn_clickked,width=200,bg="#32c3ff",
                             fg="black",font =('arial', 16 , 'bold'),padx=5,pady=5)
        self.logbtn.grid(columnspan=2)
        self.pack()

    def _login_btn_clickked(self):
        db2.query_MEAL(db2.db)
        name = self.entry_1.get()
        price = self.entry_3.get()
        i=int(db2.select_MEAL_ID(db2.db, dict(MEAL_NAME = name)))
        tm.showerror("Login error", i)
        if i > 0:
            db2.update_MEAL(db2.db,dict(PRICE=price,MEAL_ID=i))
            db2.query_MEAL(db2.db)

            tm.showinfo("Login info", "تمام ")

        else:
             tm.showerror("Login error", "مش موجود")

lf = LoginFrame(root)
root.mainloop()
