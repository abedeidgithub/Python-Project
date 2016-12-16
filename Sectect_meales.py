from tkinter import *
import tkinter.messagebox as tm
import db2


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        i = db2.query_MEAL(db2.db)

        lblInfo = Label(self, font=('arial', 20, 'bold'), text="Restaurant List Meals", fg="steel Blue", bd=10,
                        bg="#cccccc", anchor='w')
        lblInfo.grid(row=0, column=0)
        lblInfo = Label(self, font=('arial', 14, 'bold'), text=i, fg="#111111", bd=8,
                        bg="#cccccc", anchor='w')
        lblInfo.grid(row=1, column=0)

        self.pack()


root = Tk()
LoginFrame(root)
root.resizable(False, False)


root.mainloop()
