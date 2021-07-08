#PROJECT BY MANTHAN
from tkinter import * 
from tkinter import messagebox
import random 
import time
import datetime
import math

root=Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background="peach puff")
#--------------------------------------------------------------------------------------------------------------------------------

Tops=Frame(root,bg="peach puff",bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lbTitle=Label(Tops,font=("arial",60,"bold"),text="Restaurant Management System",bd=21,bg="sky blue",fg="Cornsilk",justify=CENTER)
lbTitle.grid(column=0,row=0)
#--------------------------------------------------------------------------------------------------------------------------------

ReceiptCal_f=Frame(root,bg="peach puff",bd=10,relief=RIDGE)
ReceiptCal_f.pack(side=RIGHT)
button_f=Frame(ReceiptCal_f,bg="peach puff",bd=3,relief=RIDGE)
button_f.pack(side=BOTTOM)
cal_f=Frame(ReceiptCal_f,bg="peach puff",bd=6,relief=RIDGE)
cal_f.pack(side=TOP)
receipt_f=Frame(ReceiptCal_f,bg="peach puff",bd=4,relief=RIDGE)
receipt_f.pack(side=BOTTOM)

#-------------------------------------------------------------------------------------------------------------------------------

Menuframe=Frame(root,bg="peach puff",bd=10,relief=RIDGE)
Menuframe.pack(side=LEFT)
Drinks_f=Frame(Menuframe,bg="peach puff",bd=10)
Drinks_f.pack(side=TOP)
cost_f=Frame(Menuframe,bg="alice blue",bd=4)
cost_f.pack(side=BOTTOM)

Drinks_f=Frame(Menuframe,bg="alice blue",bd=10,relief=RIDGE)
Drinks_f.pack(side=LEFT)
cake_f=Frame(Menuframe,bg="alice blue",bd=10,relief=RIDGE)
cake_f.pack(side=RIGHT)

#_________________________________________________VARIABLES_______________________________________________________________________________________

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DATEOFORDER=StringVar()
RECEIPT_REF=StringVar()
PAIDTAX=StringVar()
SUBTOTAL=StringVar()
TOTALCOST=StringVar()
COSTOFCAKES=StringVar()
COSTOFDRINKS=StringVar()
SERVICECHARGE=StringVar()

text_Input=StringVar()
operator=""

E_MAGGIE=StringVar()
E_MAKNHI=StringVar()      
E_BURGER=StringVar()
E_VEG_PIZZA=StringVar()
E_PIRI_FRIES=StringVar()
E_VEG_FRANKY=StringVar()
E_NOODLES=StringVar()
E_MOMOS=StringVar()

E_MAGGIE.set("0")
E_MAKNHI.set("0")    
E_BURGER.set("0")
E_VEG_PIZZA.set("0")
E_PIRI_FRIES.set("0")
E_VEG_FRANKY.set("0")
E_NOODLES.set("0")
E_MOMOS.set("0")

E_PASTA_R=StringVar()
E_PASTA_W=StringVar()
E_BREAD=StringVar()
E_M_GARLIC=StringVar()
E_VEG_SANDWICH=StringVar()
E_C_BREAD=StringVar()
E_ORIEO=StringVar()
E_CHAPPAN=StringVar()

E_PASTA_R.set("0")
E_PASTA_W.set("0")
E_BREAD.set("0")
E_M_GARLIC.set("0")
E_VEG_SANDWICH.set("0")
E_C_BREAD.set("0")
E_ORIEO.set("0")
E_CHAPPAN.set("0")

DATEOFORDER.set(time.strftime("%d/%m/%Y"))

#----------------------------------------------FUNCTION---------------------------------------------------------------------------------------
def iExit():
	iExit=messagebox.askyesno("Exit Restaurant System","Confirm If You Want To Exit")
	if iExit > 0:
		root.destroy()
		return

def Reset():
	E_MAGGIE.set("0")
	E_MAKNHI.set("0")    
	E_BURGER.set("0")
	E_VEG_PIZZA.set("0")
	E_PIRI_FRIES.set("0")
	E_VEG_FRANKY.set("0")
	E_NOODLES.set("0")
	E_MOMOS.set("0")
	E_PASTA_R.set("0")
	E_PASTA_W.set("0")
	E_BREAD.set("0")
	E_M_GARLIC.set("0")
	E_VEG_SANDWICH.set("0")
	E_C_BREAD.set("0")
	E_ORIEO.set("0")
	E_CHAPPAN.set("0")
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	var12.set(0)
	var13.set(0)
	var14.set(0)
	var15.set(0)
	var16.set(0)
	TXT_MAGGIE.configure(state=DISABLED)
	TXT_MAKNHI.configure(state=DISABLED)
	TXT_BURGER.configure(state=DISABLED)
	TXT_VEG_PIZZA.configure(state=DISABLED)
	TXT_PIRI_PIRI_FRIES.configure(state=DISABLED)
	TXT_VEG_FRANKY.configure(state=DISABLED)
	TXT_VEG_FRANKY.configure(state=DISABLED)
	TXT_MOMOS.configure(state=DISABLED)
	TXT_PASTA_R.configure(state=DISABLED)
	TXT_PASTA_W.configure(state=DISABLED)
	TXT_BREAD.configure(state=DISABLED)
	TXT_M_GARLIC.configure(state=DISABLED)
	TXT_VEG_SANDWICH.configure(state=DISABLED)
	TXT_C_BREAD.configure(state=DISABLED)
	TXT_ORIEO.configure(state=DISABLED)
	TXT_CHAPPAN.configure(state=DISABLED)	
	PAIDTAX.set("0")
	SUBTOTAL.set("")
	TOTALCOST.set("")
	COSTOFCAKES.set("")
	COSTOFDRINKS.set("")
	SERVICECHARGE.set("")
	TXT_RECEIPT.delete("1.0",END)

def CostOfItem():
	item1=float(E_MAGGIE.get())
	item2=float(E_MAKNHI.get())
	item3=float(E_BURGER.get())
	item4=float(E_VEG_PIZZA.get())
	item5=float(E_PIRI_FRIES.get())
	item6=float(E_VEG_FRANKY.get())
	item7=float(E_NOODLES.get())
	item8=float(E_MOMOS.get())
	item9=float(E_PASTA_R.get())
	item10=float(E_PASTA_W.get())
	item11=float(E_BREAD.get())
	item12=float(E_M_GARLIC.get())
	item13=float(E_VEG_SANDWICH.get())
	item14=float(E_C_BREAD.get())
	item15=float(E_ORIEO.get())
	item16=float(E_CHAPPAN.get())
	PriceOfDrinks=(item1*35)+(item2*45)+(item3*30)+(item4*80)+(item5*40)+(item6*30)+(item7*50)+(item8*60)
	PriceOfCakes=(item9*40)+(item10*45)+(item11*30)+(item12*40)+(item13*50)+(item14*45)+(item15*50)+(item16*50)
	DrinksPrice="₹",str("%.2f"%(PriceOfDrinks))
	CakesPrice="₹",str("%.2f"%(PriceOfCakes))
	COSTOFDRINKS.set(DrinksPrice)
	COSTOFCAKES.set(CakesPrice)
	SC="₹",str("%.2f"%(2.23))
	SERVICECHARGE.set(SC)
	SubTotalOfItems="₹",str("%.2f"%(PriceOfDrinks+PriceOfCakes+2.23))
	SUBTOTAL.set(SubTotalOfItems)
	T=float(txtPAIDTAX.get())
	Tax="₹",T
	PAIDTAX.set(Tax)
	#D=Tax
	TT=((PriceOfDrinks+PriceOfCakes+2.23-T))
	#TC="₹",str("%.2f"%(PriceOfDrinks+PriceOfCakes+2-float(Tax)))
	TC="₹",str(TT)
	TOTALCOST.set(TC)
    
#------------------------------------------------CHECKBUTTONS--------------------------------------------------------------------------------

def ChkMAGGIE():
	if(var1.get()==1):
		TXT_MAGGIE.configure(state=NORMAL)
		TXT_MAGGIE.focus()
		TXT_MAGGIE.delete("0",END)
		E_MAGGIE.set("")
	elif(var1.get()==0):
		TXT_MAGGIE.configure(state=DISABLED)
		E_MAGGIE.set("0")

def ChkMAKHNI():
	if(var2.get()==1):
		TXT_MAKNHI.configure(state=NORMAL)
		TXT_MAKNHI.focus()
		TXT_MAKNHI.delete("0",END)
		E_MAKNHI.set("")
	elif(var2.get()==0):
		TXT_MAKNHI.configure(state=DISABLED)
		E_MAKNHI.set("0")

def ChkBURGER():
	if(var3.get()==1):
		TXT_BURGER.configure(state=NORMAL)
		TXT_BURGER.focus()
		TXT_BURGER.delete("0",END)
		E_BURGER.set("")
	elif(var3.get()==0):
		TXT_BURGER.configure(state=DISABLED)
		E_BURGER.set("0")
    	
def ChkVEGPIZZA():
	if(var4.get()==1):
		TXT_VEG_PIZZA.configure(state=NORMAL)
		TXT_VEG_PIZZA.focus()
		TXT_VEG_PIZZA.delete("0",END)
		E_VEG_PIZZA.set("")
	elif(var4.get()==0):
		TXT_VEG_PIZZA.configure(state=DISABLED)
		E_VEG_PIZZA.set("0")   	


def ChkPIRIPIRIFRIES():
	if(var5.get()==1):
		TXT_PIRI_PIRI_FRIES.configure(state=NORMAL)
		TXT_PIRI_PIRI_FRIES.focus()
		TXT_PIRI_PIRI_FRIES.delete("0",END)
		E_PIRI_FRIES.set("")
	elif(var5.get()==0):
		TXT_PIRI_PIRI_FRIES.configure(state=DISABLED)
		E_PIRI_FRIES.set("0")	

def ChkVEGFRANKY():
	if(var6.get()==1):
		TXT_VEG_FRANKY.configure(state=NORMAL)
		TXT_VEG_FRANKY.focus()
		TXT_VEG_FRANKY.delete("0",END)
		E_VEG_FRANKY.set("")
	elif(var6.get()==0):
		TXT_VEG_FRANKY.configure(state=DISABLED)
		E_VEG_FRANKY.set("0")


def ChkNOODLES():
	if(var7.get()==1):
		TXT_NOODLES.configure(state=NORMAL)
		TXT_NOODLES.focus()
		TXT_NOODLES.delete("0",END)
		E_NOODLES.set("")
	elif(var7.get()==0):
		TXT_NOODLES.configure(state=DISABLED)
		E_NOODLES.set("0")    
    
def ChkMOMOS():
	if(var8.get()==1):
		TXT_MOMOS.configure(state=NORMAL)
		TXT_MOMOS.focus()
		TXT_MOMOS.delete("0",END)
		E_MOMOS.set("")
	elif(var8.get()==0):
		TXT_MOMOS.configure(state=DISABLED)
		E_MOMOS.set("0")   
    
def ChkPASTAR():
	if(var9.get()==1):
		TXT_PASTA_R.configure(state=NORMAL)
		TXT_PASTA_R.focus()
		TXT_PASTA_R.delete("0",END)
		E_PASTA_R.set("")
	elif(var9.get()==0):
		TXT_PASTA_R.configure(state=DISABLED)
		E_PASTA_R.set("0")      

def ChkPASTAW():
	if(var10.get()==1):
		TXT_PASTA_W.configure(state=NORMAL)
		TXT_PASTA_W.focus()
		TXT_PASTA_W.delete("0",END)
		E_PASTA_W.set("")
	elif(var10.get()==0):
		TXT_PASTA_W.configure(state=DISABLED)
		E_PASTA_W.set("0")   
    
def ChkBREAD():
	if(var11.get()==1):
		TXT_BREAD.configure(state=NORMAL)
		TXT_BREAD.focus()
		TXT_BREAD.delete("0",END)
		E_BREAD.set("")
	elif(var11.get()==0):
		TXT_BREAD.configure(state=DISABLED)
		E_BREAD.set("0")   

def ChkMGARLIC():
	if(var12.get()==1):
		TXT_M_GARLIC.configure(state=NORMAL)
		TXT_M_GARLIC.focus()
		TXT_M_GARLIC.delete("0",END)
		E_M_GARLIC.set("")
	elif(var12.get()==0):
		TXT_M_GARLIC.configure(state=DISABLED)
		E_M_GARLIC.set("0")    
    
def ChkVEGSANDWICH():
	if(var13.get()==1):
		TXT_VEG_SANDWICH.configure(state=NORMAL)
		TXT_VEG_SANDWICH.focus()
		TXT_VEG_SANDWICH.delete("0",END)
		E_VEG_SANDWICH.set("")
	elif(var13.get()==0):
		TXT_VEG_SANDWICH.configure(state=DISABLED)
		E_VEG_SANDWICH.set("0")    
    
def ChkCBREAD():
	if(var14.get()==1):
		TXT_C_BREAD.configure(state=NORMAL)
		TXT_C_BREAD.focus()
		TXT_C_BREAD.delete("0",END)
		E_C_BREAD.set("")
	elif(var14.get()==0):
		TXT_C_BREAD.configure(state=DISABLED)
		E_C_BREAD.set("0")   

def ChkORIEO():
	if(var15.get()==1):
		TXT_ORIEO.configure(state=NORMAL)
		TXT_ORIEO.focus()
		TXT_ORIEO.delete("0",END)
		E_ORIEO.set("")
	elif(var15.get()==0):
		TXT_ORIEO.configure(state=DISABLED)
		E_ORIEO.set("0")

def ChkCHAPPAN():
	if(var16.get()==1):
		TXT_CHAPPAN.configure(state=NORMAL)
		TXT_CHAPPAN.focus()
		TXT_CHAPPAN.delete("0",END)
		E_CHAPPAN.set("")
	elif(var16.get()==0):
		TXT_CHAPPAN.configure(state=DISABLED)
		E_CHAPPAN.set("0")   
    

def RECEIPT():
	TXT_RECEIPT.delete("1.0",END)
	x=random.randint(1,10000)
	randomRef=str(x)
	RECEIPT_REF.set("BILL" + randomRef)
	#m=str(datetime.datetime.now())
	TXT_RECEIPT.insert(END,"RECEIPT REF:\t\t" + RECEIPT_REF.get()+"\t\t"+DATEOFORDER.get()+"\n")
	#TXT_RECEIPT.insert(END,"TIME:\t\t" + m + "\n")
	TXT_RECEIPT.insert(END,"ITEM:\t\t\t" + " " + "  " + "NUMBER OF ITEMS: \n")
	TXT_RECEIPT.insert(END,"\n")
	if(var1.get()==1):
		TXT_RECEIPT.insert(END,"MAGGIE:\t\t\t\t" + E_MAGGIE.get() + "  x ₹35" + "\n")
	if(var2.get()==1):
		TXT_RECEIPT.insert(END,"MAKHNI MAGGIE:\t\t\t\t" + E_MAKNHI.get() + "  x ₹45" + "\n")
	if(var3.get()==1):
		TXT_RECEIPT.insert(END,"BURGER:\t\t\t\t" + E_BURGER.get() + "  x ₹30" + "\n")
	if(var4.get()==1):
		TXT_RECEIPT.insert(END,"VEG PIZZA:\t\t\t\t" + E_VEG_PIZZA.get() + "  x ₹80" + "\n")
	if(var5.get()==1):
		TXT_RECEIPT.insert(END,"PIRI PIRI FRIES:\t\t\t\t" + E_PIRI_FRIES.get() + "  x ₹40" + "\n")
	if(var6.get()==1):
		TXT_RECEIPT.insert(END,"VEG FRANKY:\t\t\t\t" + E_VEG_FRANKY.get() + "  x ₹30" + "\n")
	if(var7.get()==1):
		TXT_RECEIPT.insert(END,"HAKKA NOODLES:\t\t\t\t" + E_NOODLES.get() + "  x ₹50" + "\n")
	if(var8.get()==1):
		TXT_RECEIPT.insert(END,"VEG MOMOS:\t\t\t\t" + E_MOMOS.get() + "  x ₹60" + "\n")
	if(var9.get()==1):
		TXT_RECEIPT.insert(END,"RED SAUCE PASTA:\t\t\t\t" + E_PASTA_R.get() + "  x ₹40" + "\n")
	if(var10.get()==1):
		TXT_RECEIPT.insert(END,"WHITE SAUCE PASTA:\t\t\t\t" + E_PASTA_W.get() + "  x ₹45" + "\n")
	if(var11.get()==1):
		TXT_RECEIPT.insert(END,"GARLIC BREAD:\t\t\t\t" + E_BREAD.get() + "  x ₹30" + "\n")
	if(var12.get()==1):
		TXT_RECEIPT.insert(END,"MASALA GARLIC BREAD:\t\t\t\t" + E_M_GARLIC.get() + "  x ₹40" + "\n")
	if(var13.get()==1):
		TXT_RECEIPT.insert(END,"VEG GRILLED SANDWICH:\t\t\t\t" + E_VEG_SANDWICH.get() + "  x ₹50" + "\n")
	if(var14.get()==1):
		TXT_RECEIPT.insert(END,"CHOCOLATE BREAD:\t\t\t\t" + E_C_BREAD.get() + "  x ₹45" + "\n")
	if(var15.get()==1):
		TXT_RECEIPT.insert(END,"ORIEO COOKIE DELIGHT:\t\t\t\t" + E_ORIEO.get() + "  x ₹50" + "\n")
	if(var16.get()==1):
		TXT_RECEIPT.insert(END,"CHAPPAN BHOJ:\t\t\t\t" + E_CHAPPAN.get() + "  x ₹50" + "\n")
	T=txtPAIDTAX.get()
	Tax=T
	TXT_RECEIPT.insert(END,"DISCOUNT:\t\t\t\t" + "-" + str(Tax) + "\n")
	TXT_RECEIPT.insert(END,"_____________________________________________" + "\n")
	TXT_RECEIPT.insert(END,"GRAND TOTAL:\t\t\t\t" + TOTALCOST.get() + "\n")
	TXT_RECEIPT.insert(END, "\n")
	TXT_RECEIPT.insert(END, "\t\t\t\t\t\t" + "THANK YOU!" + "\t\t\t\t VISIT AGAIN!" + "\n")
	TXT_RECEIPT.insert(END, "-мαηтнαη")


	
	
	
	
	



#--------------------------------------------DRINKS----------------------------------------------------------------------------------------------------------
MAGGIE=Checkbutton(Drinks_f,text="MAGGIE",variable=var1,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkMAGGIE).grid(row=0,sticky=W)
MAKNHI=Checkbutton(Drinks_f,text="MAKHNI MAGGIE",variable=var2,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkMAKHNI).grid(row=1,sticky=W)
BURGER=Checkbutton(Drinks_f,text="BURGER",variable=var3,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkBURGER).grid(row=2,sticky=W)
VEG_PIZZA=Checkbutton(Drinks_f,text="VEG PIZZA",variable=var4,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkVEGPIZZA).grid(row=3,sticky=W)
PIRI_PIRI_FRIES=Checkbutton(Drinks_f,text="PIRI PIRI FRIES",variable=var5,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkPIRIPIRIFRIES).grid(row=4,sticky=W)
VEG_FRANKY=Checkbutton(Drinks_f,text="VEG FRANKY",variable=var6,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkVEGFRANKY).grid(row=5,sticky=W)
NOODLES=Checkbutton(Drinks_f,text="HAKKA NOODLES",variable=var7,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkNOODLES).grid(row=6,sticky=W)
MOMOS=Checkbutton(Drinks_f,text="VEG MOMOS",variable=var8,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkMOMOS).grid(row=7,sticky=W)
#-------------------------------------------END DRINKS--------------------------------------------------------------------------------------------------------

TXT_MAGGIE=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_MAGGIE)
TXT_MAGGIE.grid(row=0,column=1)
TXT_MAKNHI=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_MAKNHI)
TXT_MAKNHI.grid(row=1,column=1)
TXT_BURGER=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_BURGER)
TXT_BURGER.grid(row=2,column=1)
TXT_VEG_PIZZA=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_VEG_PIZZA)
TXT_VEG_PIZZA.grid(row=3,column=1)
TXT_PIRI_PIRI_FRIES=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_PIRI_FRIES)
TXT_PIRI_PIRI_FRIES.grid(row=4,column=1)
TXT_VEG_FRANKY=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_VEG_FRANKY)
TXT_VEG_FRANKY.grid(row=5,column=1)
TXT_NOODLES=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_NOODLES)
TXT_NOODLES.grid(row=6,column=1)
TXT_MOMOS=Entry(Drinks_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_MOMOS)
TXT_MOMOS.grid(row=7,column=1)



#--------------------------------------------------CAKE--------------------------------------------------------------------------------------------
PASTA_R=Checkbutton(cake_f,text="RED SAUCE PASTA",variable=var9,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkPASTAR).grid(row=0,sticky=W)
PASTA_W=Checkbutton(cake_f,text="WHITE SAUCE PASTA",variable=var10,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkPASTAW).grid(row=1,sticky=W)
BREAD=Checkbutton(cake_f,text="GARLIC BREAD",variable=var11,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkBREAD).grid(row=2,sticky=W)
M_GARLIC=Checkbutton(cake_f,text="MASALA GARLIC BREAD",variable=var12,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkMGARLIC).grid(row=3,sticky=W)
VEG_SANDWICH=Checkbutton(cake_f,text="VEG GRILLED SANDWICH",variable=var13,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkVEGSANDWICH).grid(row=4,sticky=W)
C_BREAD=Checkbutton(cake_f,text="CHOCOLATE BREAD",variable=var14,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkCBREAD).grid(row=5,sticky=W)
ORIEO=Checkbutton(cake_f,text="ORIEO COOKIE DELIGHT",variable=var15,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkORIEO).grid(row=6,sticky=W)
CHAPPAN=Checkbutton(cake_f,text="CHAPPAN BHOJ",variable=var16,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg="alice blue",command=ChkCHAPPAN).grid(row=7,sticky=W)

#------------------------------------------------END CAKE-------------------------------------------------------------------------------------------

TXT_PASTA_R=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_PASTA_R)
TXT_PASTA_R.grid(row=0,column=1)
TXT_PASTA_W=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_PASTA_W)
TXT_PASTA_W.grid(row=1,column=1)
TXT_BREAD=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_BREAD)
TXT_BREAD.grid(row=2,column=1)
TXT_M_GARLIC=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_M_GARLIC)
TXT_M_GARLIC.grid(row=3,column=1)
TXT_VEG_SANDWICH=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_VEG_SANDWICH)
TXT_VEG_SANDWICH.grid(row=4,column=1)
TXT_C_BREAD=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_C_BREAD)
TXT_C_BREAD.grid(row=5,column=1)
TXT_ORIEO=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_ORIEO)
TXT_ORIEO.grid(row=6,column=1)
TXT_CHAPPAN=Entry(cake_f,font=("arial",16,"bold"),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_CHAPPAN)
TXT_CHAPPAN.grid(row=7,column=1)

#----------------------------------------------TOTAL COST-------------------------------------------------------------------------------------------

lbCOSTOFDRINKS=Label(cost_f,font=("arial",14,"bold"),text="MENU-I",bg="alice blue",fg="black").grid(column=0,row=0,sticky=W)
txtCOSTOFDRINKS=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=COSTOFDRINKS)
txtCOSTOFDRINKS.grid(row=0,column=1)

lbCOSTOFCAKES=Label(cost_f,font=("arial",14,"bold"),text="MENU-II",bg="alice blue",fg="black").grid(column=0,row=1,sticky=W)
txtCOSTOFCAKES=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=COSTOFCAKES)
txtCOSTOFCAKES.grid(row=1,column=1)

lbSERVICECHARGE=Label(cost_f,font=("arial",14,"bold"),text="SERVICE CHARGE",bg="alice blue",fg="black").grid(column=0,row=2,sticky=W)
txtSERVICECHARGE=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=SERVICECHARGE)
txtSERVICECHARGE.grid(row=2,column=1)

#---------------------------------------------PAYMENT INFORMATION---------------------------------------------------------------------------------

lbPAIDTAX=Label(cost_f,font=("arial",14,"bold"),text="DISCOUNT",bd=7,bg="alice blue",fg="black").grid(column=2,row=0,sticky=W)
txtPAIDTAX=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=PAIDTAX)
txtPAIDTAX.grid(row=0,column=3)

lbSUBTOTAL=Label(cost_f,font=("arial",14,"bold"),text="SUB TOTAL",bd=7,bg="alice blue",fg="black").grid(column=2,row=1,sticky=W)
txtSUBTOTAL=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=SUBTOTAL)
txtSUBTOTAL.grid(row=1,column=3)

lbTOTALCOST=Label(cost_f,font=("arial",14,"bold"),text="TOTAL COST",bd=7,bg="alice blue",fg="black").grid(column=2,row=2,sticky=W)
txtTOTALCOST=Entry(cost_f,font=("arial",14,"bold"),bg="white",bd=7,justify=RIGHT,insertwidth=2,textvariable=TOTALCOST)
txtTOTALCOST.grid(row=2,column=3)



#---------------------------------------------- TEXT RECEIPT----------------------------------------------------------------------

TXT_RECEIPT=Text(receipt_f,width=46,height=12,bg="pink",bd=4,font=("arial",12,"bold"))
TXT_RECEIPT.grid(row=0,column=0)

btnTOTAL=Button(button_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="TOTAL",bg="light pink",command=CostOfItem).grid(row=0,column=0)
btnRECEIPT=Button(button_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="RECEIPT",bg="light pink",command=RECEIPT).grid(row=0,column=1)
btnRESET=Button(button_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="RESET",bg="light pink",command=Reset).grid(row=0,column=2)
btnEXIT=Button(button_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="EXIT",bg="light pink",command=iExit).grid(row=0,column=3)


#----------------------------------------------CALCULATOR DISPLAY-------------------------------------------------------------------------
def btnclick(numbers):
	global operator
	operator=operator+str(numbers)
	text_Input.set(operator)

def btnClear():
	global operator
	operator=""
	text_Input.set("")

def btnEquals():
	try:
		global operator
		sumup=str(eval(operator))
		text_Input.set(sumup)
		operator=""
	except:
		text_Input.set("ERROR")
		operator=""	



txt_DISPLAY=Entry(cal_f,width=45,bg="white",bd=4,font=("arial",12,"bold"),justify=RIGHT,textvariable=text_Input)
txt_DISPLAY.grid(row=0,column=0,columnspan=4,pady=1)
txt_DISPLAY.insert(0,"0")
#--------------------------------------------CALCULATOR BUTTONS----------------------------------------------------------------------------

btn7=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="7",bg="alice blue",command=lambda:btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="8",bg="alice blue",command=lambda:btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="9",bg="alice blue",command=lambda:btnclick(9))
btn9.grid(row=2,column=2)
btnADD=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="+",bg="powder blue",command=lambda:btnclick("+"))
btnADD.grid(row=2,column=3)

btn4=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="4",bg="alice blue",command=lambda:btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="5",bg="alice blue",command=lambda:btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="6",bg="alice blue",command=lambda:btnclick(6))
btn6.grid(row=3,column=2)
btnSUB=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="-",bg="powder blue",command=lambda:btnclick("-"))
btnSUB.grid(row=3,column=3)


btn1=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="1",bg="alice blue",command=lambda:btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="2",bg="alice blue",command=lambda:btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="3",bg="alice blue",command=lambda:btnclick(3))
btn3.grid(row=4,column=2)
btnMULT=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="*",bg="powder blue",command=lambda:btnclick("*"))
btnMULT.grid(row=4,column=3)

btn0=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="0",bg="alice blue",command=lambda:btnclick(0))
btn0.grid(row=5,column=0)
btnCLEAR=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="C",bg="powder blue",command=btnClear)
btnCLEAR.grid(row=5,column=1)
btnEQUALS=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="=",bg="powder blue",command=btnEquals)
btnEQUALS.grid(row=5,column=2)
btnDIV=Button(cal_f,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),width=4,text="/",bg="powder blue",command=lambda:btnclick("/"))
btnDIV.grid(row=5,column=3)





root.mainloop()