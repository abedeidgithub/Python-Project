from tkinter import*
import random
import time;
import db2;
import tkinter.messagebox as tm


root=Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Resaurant management system")
root.configure(backgroun='#CCCCCC')

text_Input=StringVar()
operator =""

Tops=Frame(root,width=1600, height =50, bg="#1fa5d2" , relief =SUNKEN)
Tops.pack(side=TOP)


f1=Frame(root,width=800, height =700 , relief =SUNKEN)
f1.pack(side=LEFT)
f1.configure(backgroun='#CCCCCC')
f2=Frame(root,width=300, height =700 , relief =SUNKEN)
f2.pack(side=RIGHT)
f2.configure(backgroun='#CCCCCC')

#=================================time=======================
localtime=time.asctime(time.localtime(time.time()))
#=================================info==============================
lblInfo=Label(Tops, font =('arial',50,'bold'), text="Restaurant Mangement system ", fg="steel Blue",bd=10,bg="#cccccc", anchor='w')
lblInfo.grid(row =0 ,column=0)

lblInfo=Label(Tops, font =('arial',20,'bold'), text= localtime, fg="steel Blue",bd=10,bg="#cccccc", anchor='w')
lblInfo.grid(row =1 ,column=0)


#=================================cal==================
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Coffee.set("")
    Total.set("")
    Cakes.set("")
    Salmon.set("")
    pepsi.set("")
    SideDishes.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Juices.set("")
    IcedDrinks.set("")
    IceCream.set("")
    Cocktails.set("")
    tea.set("")
    Sandwiches.set("")
    Combos.set("")
    Tuna.set("")
    Pizza.set("")
    Pasta.set("")
    Macaroni .set("")
    Fish.set("")
    SeaFood.set("")
    Beef.set("")
    SIMPLESALAD.set("")
    Soups.set("")
    T_Bone.set("")
def Reset_Total():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Coffee.set("")
    Cakes.set("")
    Salmon.set("")
    pepsi.set("")
    SideDishes.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Juices.set("")
    IcedDrinks.set("")
    IceCream.set("")
    Cocktails.set("")
    tea.set("")
    Sandwiches.set("")
    Combos.set("")
    Tuna.set("")
    Pizza.set("")
    Pasta.set("")
    Macaroni .set("")
    Fish.set("")
    SeaFood.set("")
    Beef.set("")
    SIMPLESALAD.set("")
    Soups.set("")
    T_Bone.set("")



def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)



    if ((Fries.get())== ''):
        costofFries = 0
        Fries.set("0")

    if (Burger.get()== ''):
        costofBurger = 0
        Burger.set("0")

    if (Coffee.get() == ''):
        costofCoffee = 0
        Coffee.set("0")

    if (Cakes.get() == ''):
        costofCakes = 0
        Cakes.set("0")

    if (Salmon.get() == ''):
        costofSalmon = 0
        Salmon.set("0")

    if (pepsi.get() == ''):
        costofpepsi = 0
        pepsi.set("0")

    if (SideDishes.get() == ''):
        costofSideDishes = 0
        SideDishes.set("0")

    if (Chicken_Burger.get() == ''):
        costofChicken_Burger = 0
        Chicken_Burger.set("0")

    if (Cheese_Burger.get() == ''):
        costofCheese_Burger = 0
        Cheese_Burger.set("0")

    if (IcedDrinks.get() == ''):
        costofIcedDrinks = 0
        IcedDrinks.set("0")

    if (Juices.get() == ''):
        costofJuices = 0
        Juices.set("0")

    if (IceCream.get() == ''):
        costofIceCream= 0
        IceCream.set("0")

    if (Cocktails.get() == ''):
        costofCocktails= 0
        Cocktails.set("0")

    if (tea.get() == ''):
        costoftea = 0
        tea.set("0")

    if (Sandwiches.get() == ''):
        costofSandwiches = 0
        Sandwiches.set("0")

    if (Combos.get() == ''):
        costofCombos = 0
        Combos.set("0")

    if (Tuna.get() == ''):
        costofTuna = 0
        Tuna.set("0")

    if (Pizza.get() == ''):
        costofPizza = 0
        Pizza.set("0")

    if (Pasta.get() == ''):
        costofPasta = 0
        Pasta.set("0")

    if (Macaroni.get() == ''):
        costofMacaroni= 0
        Macaroni.set("0")

    if (Fish.get() == ''):
        costofFish = 0
        Fish.set("0")
    if (SIMPLESALAD.get() == ''):
        costofSIMPLESALAD = 0
        SIMPLESALAD.set("0")
    if (Soups.get() == ''):
        costofSoups= 0
        Soups.set("0")

    if (SeaFood.get() == ''):
        costofSeaFood = 0
        SeaFood.set("0")
    if (Beef.get() == ''):
        costofBeef = 0
        Beef.set("0")

    if (T_Bone.get() == ''):
        costofT_Bone = 0
        T_Bone.set("0")

    if (Filet.get() == ''):
        costofFilet = 0
        Filet.set("0")











        costofFries =float(Fries.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofBurger = float(Burger.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofFilet = float(Filet.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofCoffee =float(Coffee.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofCakes = float(Cakes.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofSalmon = float(Salmon.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofpepsi = float(pepsi.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofSideDishes = float(SideDishes.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofChicken_Burger = float(Chicken_Burger.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofCheese_Burger = float(Cheese_Burger.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofJuices = float(Juices.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofIcedDrinks = float(IcedDrinks.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofIceCream=float(IceCream.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofCocktails=float(Cocktails.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costoftea=float(tea.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofSandwiches=float(Sandwiches.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofCombos=float(Combos.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofTuna=float(Tuna.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofPizza=float(Pizza.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofPasta=float(Pasta.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofMacaroni=float(Macaroni.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofFish=float(Fish.get())*float(db2.select(db2.db, dict(MEAL_NAME='Fries')))
        costofSeaFood=float(SeaFood.get())*float(db2.select(db2.db, dict(MEAL_NAME='SeaFood')))
        costofBeef=float(Beef.get())*float(db2.select(db2.db, dict(MEAL_NAME='Beef')))
        costofSIMPLESALAD=float(SIMPLESALAD.get())*float(db2.select(db2.db, dict(MEAL_NAME='SIMPLESALAD')))
        costofSoups=float(Soups.get())*float(db2.select(db2.db, dict(MEAL_NAME='Soups')))
        costofT_Bone=float(T_Bone.get())*float(db2.select(db2.db, dict(MEAL_NAME='T_Bone')))

    OverAllCost= str(costofT_Bone + costofSIMPLESALAD+costofFries+ costofBurger+costofFilet+costofCoffee+costofCakes+costofSalmon
                     +costofpepsi+costofSideDishes+costofChicken_Burger+costofCheese_Burger+costofJuices+costofIcedDrinks+costofIceCream
                     +costofCocktails+costoftea+costofSandwiches+costofCombos+costofTuna+costofPizza+costofPasta+costofMacaroni+costofFish+costofSeaFood
                     +costofBeef+costofSoups)
    Total.set(OverAllCost)
    Reset_Total()
    c=float(OverAllCost)
    db2.insert_total(db2.db,dict(TOTAL_NAME = "",TOTAL_PRICE = c))
    db2.query_total(db2.db)
    tm.showinfo("Login info", c)
def qExit():
    root.destroy()



txtDisplay=Entry(f2,font =('arial', 20 , 'bold'),textvariable=text_Input,bd=20, insertwidth=4, bg="#32c3ff", justify = "right" )
txtDisplay.grid(columnspan=4)
#---------------------------------------------------------------------------
btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text="7",bg="#32c3ff", command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16, bd=8,fg="black", font =('arial', 20 , 'bold'),text="8",bg="#32c3ff", command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16, bd=8,fg="black", font =('arial', 20 , 'bold'),text="9",bg="#32c3ff", command=lambda: btnClick(9)).grid(row=2 ,column=2)
Addition=Button(f2,padx=16,pady=16, bd=8,fg="black", font =('arial', 20 , 'bold'),text="+",bg="#32c3ff", command=lambda: btnClick("+")).grid(row=2 ,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="4",bg="#32c3ff", command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="5",bg="#32c3ff", command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="6",bg="#32c3ff", command=lambda: btnClick(6)).grid(row=3 ,column=2)
Subtraction=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="-",bg="#32c3ff", command=lambda: btnClick("-")).grid(row=3 ,column=3)
#---------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="1",bg="#32c3ff", command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="2",bg="#32c3ff", command=lambda: btnClick(2)).grid(row=4,column=1)
btn6=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="3",bg="#32c3ff", command=lambda: btnClick(3)).grid(row=4 ,column=2)
Multiply=Button(f2,padx=16,pady=16, bd=8,fg="black", font =('arial', 20 , 'bold'),text="*",bg="#32c3ff", command=lambda: btnClick("*")).grid(row=4 ,column=3)
#-------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="0",bg="#32c3ff", command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="C",bg="#32c3ff" , command=lambda: btnClearDisplay()).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="=",bg="#32c3ff" ,  command=lambda: btnEqualsInput()).grid(row=5 ,column=2)
Division=Button(f2,padx=16,pady=16, bd=8,fg="black",font =('arial', 20 , 'bold'),text="/",bg="#32c3ff", command=lambda: btnClick("/")).grid(row=5 ,column=3)
#-------------------
#--------------------------------Restaurent info  1------------------------------------
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
Coffee=StringVar()
Total=StringVar()
Cakes=StringVar()
Salmon=StringVar()
pepsi=StringVar()
SideDishes=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()
Juices=StringVar()
IcedDrinks=StringVar()
IceCream=StringVar()
Cocktails=StringVar()
tea=StringVar()
Sandwiches=StringVar()
Combos=StringVar()
Tuna=StringVar()
Pizza=StringVar()
Pasta=StringVar()
Macaroni =StringVar()
Fish =StringVar()
SeaFood  =StringVar()
Beef =StringVar()
SIMPLESALAD =StringVar()
Soups=StringVar()
T_Bone=StringVar()

lplReference=Label(f1,font =('arial', 10 , 'bold'),text="Reference",anchor='w',bg="#cccccc")
lplReference.grid(row=0,column=0)
txtReference=Entry(f1,font =('arial', 8 , 'bold'),textvariable=rand,bd=10,insertwidth=4,bg="#ffffff",justify='right',state=DISABLED)
txtReference.grid(row=0,column=1)

lplPrice=Label(f1,font =('arial', 10 , 'bold'),text="Large Fries",anchor='w',bg="#cccccc")
lplPrice.grid(row=1,column=0)
txtPrice=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtPrice.grid(row=1,column=1)

lplBurger=Label(f1,font =('arial', 10 , 'bold'),text=" Burger",anchor='w',bg="#cccccc")
lplBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtBurger.grid(row=2,column=1)

lplFilet=Label(f1,font =('arial', 10 , 'bold'),text=" Filet",anchor='w',bg="#cccccc")
lplFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Filet,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtFilet.grid(row=3,column=1)

lplChicken=Label(f1,font =('arial', 10 , 'bold'),text=" Chicken",anchor='w',bg="#cccccc")
lplChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=4,column=1)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="Soups ",anchor='w',bg="#cccccc")
lplCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Soups ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=5,column=1)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text=" Cheese",anchor='w',bg="#cccccc")
lplCheese.grid(row=6,column=0)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=6,column=1)


lplChicken=Label(f1,font =('arial', 10 , 'bold'),text="Pasta ",anchor='w',bg="#cccccc")
lplChicken.grid(row=7,column=0)
txtChicken=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Pasta ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=7,column=1)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="Pizza",anchor='w',bg="#cccccc")
lplCheese.grid(row=8,column=0)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Pizza,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=8,column=1)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="Tuna",anchor='w',bg="#cccccc")
lplCheese.grid(row=9,column=0)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Tuna,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=9,column=1)

#--------------------------------Restaurent info  2------------------------------------



lplReference=Label(f1,font =('arial', 10 , 'bold'),text="SIMPLE SALAD",anchor='w',bg="#cccccc")
lplReference.grid(row=0,column=2)
txtReference=Entry(f1,font =('arial', 8 , 'bold'),textvariable=SIMPLESALAD,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtReference.grid(row=0,column=3)

lplPrice=Label(f1,font =('arial', 10 , 'bold'),text="Beef ",anchor='w',bg="#cccccc")
lplPrice.grid(row=1,column=2)
txtPrice=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Beef ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtPrice.grid(row=1,column=3)

lplBurger=Label(f1,font =('arial', 10 , 'bold'),text="Sea Food",anchor='w',bg="#cccccc")
lplBurger.grid(row=2,column=2)
txtBurger=Entry(f1,font =('arial', 8 , 'bold'),textvariable=SeaFood,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtBurger.grid(row=2,column=3)

lplFilet=Label(f1,font =('arial', 10 , 'bold'),text="Fish",anchor='w',bg="#cccccc")
lplFilet.grid(row=3,column=2)
txtFilet=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Fish,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtFilet.grid(row=3,column=3)

lplChicken=Label(f1,font =('arial', 10 , 'bold'),text="Mac Macaroni",anchor='w',bg="#cccccc")
lplChicken.grid(row=4,column=2)
txtChicken=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Macaroni,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=4,column=3)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="Salmon Combo",anchor='w',bg="#cccccc")
lplCheese.grid(row=5,column=2)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Salmon,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=5,column=3)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text=" Side Dishes",anchor='w',bg="#cccccc")
lplCheese.grid(row=6,column=2)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=SideDishes,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=6,column=3)



lplChicken=Label(f1,font =('arial', 10 , 'bold'),text="Chicken Combos",anchor='w',bg="#cccccc")
lplChicken.grid(row=7,column=2)
txtChicken=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Combos,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=7,column=3)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="T-Bone ",anchor='w',bg="#cccccc")
lplCheese.grid(row=8,column=2)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=T_Bone ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=8,column=3)

lplCheese=Label(f1,font =('arial', 10 , 'bold'),text="Sandwiches",anchor='w',bg="#cccccc")
lplCheese.grid(row=9,column=2)
txtCheese=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Sandwiches,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=9,column=3)

#--------------------------------Restaurent info  3------------------------------------

lplDrinks=Label(f1,font =('arial', 10 , 'bold'),text="Coffee ",anchor='w',bg="#cccccc")
lplDrinks.grid(row=0,column=4)
txtDrinks=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Coffee ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtDrinks.grid(row=0,column=5)

lplCost=Label(f1,font =('arial', 10 , 'bold'),text="Cakes ",anchor='w',bg="#cccccc")
lplCost.grid(row=1,column=4)
txtCost=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Cakes ,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtCost.grid(row=1,column=5)

lplService=Label(f1,font =('arial', 10 , 'bold'),text="pepsi",anchor='w',bg="#cccccc")
lplService.grid(row=2,column=4)
txtService=Entry(f1,font =('arial', 8 , 'bold'),textvariable=pepsi,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtService.grid(row=2,column=5)

lplStateTax=Label(f1,font =('arial', 10 , 'bold'),text="Juices",anchor='w',bg="#cccccc")
lplStateTax.grid(row=3,column=4)
txtStateTax=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Juices,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtStateTax.grid(row=3,column=5)

lplSubTotal=Label(f1,font =('arial', 10 , 'bold'),text="Iced Drinks",anchor='w',bg="#cccccc")
lplSubTotal.grid(row=4,column=4)
txtSubTotal=Entry(f1,font =('arial', 8 , 'bold'),textvariable=IcedDrinks,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtSubTotal.grid(row=4,column=5)

lplTotalCost=Label(f1,font =('arial', 10 , 'bold'),text="Ice Cream",anchor='w',bg="#cccccc")
lplTotalCost.grid(row=5,column=4)
txtTotalCost=Entry(f1,font =('arial', 8 , 'bold'),textvariable=IceCream,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtTotalCost.grid(row=5,column=5)




lplService=Label(f1,font =('arial', 10 , 'bold'),text="Cocktails",anchor='w',bg="#cccccc")
lplService.grid(row=6,column=4)
txtService=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Cocktails,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtService.grid(row=6,column=5)

lplStateTax=Label(f1,font =('arial', 10 , 'bold'),text="Tea",anchor='w',bg="#cccccc")
lplStateTax.grid(row=7,column=4)
txtStateTax=Entry(f1,font =('arial', 8 , 'bold'),textvariable=tea,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtStateTax.grid(row=7,column=5)



lplTotalCost=Label(f1,font =('arial', 10 , 'bold'),text="Total Cost",anchor='w',bg="#cccccc")
lplTotalCost.grid(row=9,column=4)
txtTotalCost=Entry(f1,font =('arial', 8 , 'bold'),textvariable=Total,bd=10,insertwidth=4,bg="#ffffff",justify='right',state=DISABLED)
txtTotalCost.grid(row=9,column=5)


#------------------------------------------------buttons--------------------------------------------
btnTotal=Button(f1,padx=40,pady=8,bd=3,activeforeground="#ffffff",fg="black",font =('arial', 16 , 'bold'),width=10,text="Total",bg="#32c3ff",command=Ref).grid(row=16,column=1)

btnReset=Button(f1,padx=40,pady=8,bd=3,fg="black",font =('arial', 16 , 'bold'),width=10,text="Reset",bg="#32c3ff",command=Reset).grid(row=16,column=2)

btnExit=Button(f1,padx=40,pady=8,bd=3,fg="black",font =('arial', 16 , 'bold'),width=10,text="Exit",bg="#32c3ff",command=qExit).grid(row=16,column=3)



root.mainloop()
