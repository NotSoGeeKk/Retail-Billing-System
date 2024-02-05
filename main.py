from tkinter import *
from tkinter import messagebox
import random
import os,tempfile
# functions

if not os.path.exists('bills'):
    os.mkdir('bills')
billno=random.randint(100,1000)
def total():
    global gljprice,oxjprice,jimjprice,cusjprice,s9jprice,lvjprice
    global csprice,slprice,gvprice,d4price,snprice,mfprice
    global slrprice,slcprice,tagprice,tagfprice,bsprice,tsprice
    global totalbill
    gljprice = int(gljEntry.get())*1300
    oxjprice = int(OxjEntry.get())*2500
    jimjprice = int(JimjEntry.get())*1000
    cusjprice = int(CusjEntry.get())*2300
    s9jprice = int(S9jEntry.get())*1000
    lvjprice = int(LVjEntry.get())*3000
    totaljeanprice = gljprice+oxjprice+jimjprice+cusjprice+s9jprice+lvjprice
    jeans_priceEntry.insert(0,totaljeanprice)
    totaljeantax = totaljeanprice*0.15
    jeans_taxEntry.delete(0,END)
    jeans_taxEntry.insert(0,totaljeantax)

    csprice = int(CsEntry.get())*1000
    slprice = int(slEntry.get())*1200
    gvprice = int(gvEntry.get())*700
    d4price = int(D4Entry.get())*600
    snprice = int(SNEntry.get())*800
    mfprice = int(MfEntry.get())*1000
    totalshirtprice = csprice+slprice+gvprice+d4price+snprice+mfprice
    shirt_priceEntry.insert(0,totalshirtprice)
    totalshirttax = totalshirtprice*0.15
    shirt_taxEntry.delete(0,END)
    shirt_taxEntry.insert(0,totalshirttax)

    slrprice = int(slrEntry.get())*700
    slcprice = int(slcEntry.get())*850
    tagprice = int(tagEntry.get())*600
    tagfprice = int(tagfEntry.get())*900
    bsprice = int(bsEntry.get())*1000
    tsprice = int(TSEntry.get())*1000
    totaltshirtprice = slcprice+slcprice+tagprice+tagfprice+bsprice+tsprice
    tshirt_priceEntry.insert(0,totaltshirtprice)
    totaltshirttax = totaltshirtprice*0.15
    tshirt_taxEntry.delete(0,END)
    tshirt_taxEntry.insert(0,totaltshirttax)
    totalbill = totaltshirtprice+totaltshirttax+totaljeanprice+totaljeantax+totaltshirtprice+totaltshirttax

def bill_area():
    if nameEntry.get() == '' or PhoneEntry.get() == '':
        messagebox.showerror('ERROR','Customer Details Are Required')
    elif jeans_priceEntry.get() == '' and shirt_priceEntry.get() == '' and tshirt_priceEntry.get()=='':
        messagebox.showerror('ERROR','No Products Are Selected')
    elif jeans_priceEntry.get() == 0 and shirt_priceEntry.get() == 0 and tshirt_priceEntry.get()==0:
        messagebox.showerror('ERROR', 'No Products Are Selected')
    else:
        textarea.insert(END,'\t\t** WELCOME CUSTOMER **\n\n')
        textarea.insert(END,f'      Bill Number:{billno}\n')
        textarea.insert(END, f'      Customer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'      Phone Number:{PhoneEntry.get()}\n')
        textarea.insert(END, ' =========================================================\n')
        textarea.insert(END,'\t\tProduct\t\tQuantity\t\tPrice\n')
        textarea.insert(END, ' =========================================================\n')
        if gljEntry.get() !='0':
            textarea.insert(END,f'\t\tGLZ J\t\t{gljEntry.get()}\t\t{gljprice}\n')
        if OxjEntry.get() != '0':
            textarea.insert(END, f'\t\tOXF J\t\t{OxjEntry.get()}\t\t{oxjprice}\n')
        if JimjEntry.get() != '0':
            textarea.insert(END, f'\t\tJIM J\t\t{JimjEntry.get()}\t\t{jimjprice}\n')
        if CusjEntry.get() != '0':
            textarea.insert(END, f'\t\tCUS J\t\t{CusjEntry.get()}\t\t{cusjprice}\n')
        if S9jEntry.get() != '0':
            textarea.insert(END, f'\t\tS9 J\t\t{S9jEntry.get()}\t\t{s9jprice}\n\n')
        if LVjEntry.get() != '0':
            textarea.insert(END, f'\t\tLEVIS J\t\t{LVjEntry.get()}\t\t{lvjprice}\n')
        if CsEntry.get()!='0':
            textarea.insert(END,f'\t\tCS\t\t{CsEntry.get()}\t\t{csprice}\n')
        if slEntry.get() != '0':
            textarea.insert(END, f'\t\tSL\t\t{slEntry.get()}\t\t{slprice}\n')
        if gvEntry.get() != '0':
            textarea.insert(END, f'\t\tGV\t\t{gvEntry.get()}\t\t{gvprice}\n')
        if D4Entry.get() != '0':
            textarea.insert(END, f'\t\tD4\t\t{D4Entry.get()}\t\t{d4price}\n')
        if SNEntry.get() != '0':
            textarea.insert(END, f'\t\tS9\t\t{SNEntry.get()}\t\t{snprice}\n')
        if MfEntry.get() != '0':
            textarea.insert(END, f'\t\tMF\t\t{MfEntry.get()}\t\t{mfprice}\n')
        if slrEntry.get() != '0':
            textarea.insert(END, f'\t\tSL R\t\t{slrEntry.get()}\t\t{slrprice}\n')
        if slcEntry.get() != '0':
            textarea.insert(END, f'\t\tSL C\t\t{slcEntry.get()}\t\t{slcprice}\n')
        if tagEntry.get() != '0':
            textarea.insert(END, f'\t\tTAG\t\t{tagEntry.get()}\t\t{tagprice}\n')
        if tagfEntry.get() != '0':
            textarea.insert(END, f'\t\tTAG F\t\t{tagfEntry.get()}\t\t{tagfprice}\n')
        if bsEntry.get() != '0':
            textarea.insert(END, f'\t\tBOSS\t\t{bsEntry.get()}\t\t{bsprice}\n')
        if TSEntry.get() != '0':
            textarea.insert(END, f'\t\tTS\t\t{TSEntry.get()}\t\t{tsprice}\n')
        textarea.insert(END, ' ---------------------------------------------------------\n')
        if jeans_taxEntry != '0.0':
            textarea.insert(END,f'\n \t\t\t\tJEANS TAX\t\t{jeans_taxEntry.get()}')
        if shirt_taxEntry != '0.0':
            textarea.insert(END, f'\n \t\t\t\tSHIRT TAX\t\t{shirt_taxEntry.get()}')
        if tshirt_taxEntry != '0.0':
            textarea.insert(END, f'\n \t\t\t\tTSHIRT TAX\t\t{tshirt_taxEntry.get()}')
        textarea.insert(END,f'\n\t\t\t\tTotal Bill: \t\t{totalbill}')
        save_bill()
def save_bill():
    global billno
    result = messagebox.askyesno('CONFIRM','Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0,END)
        file=open(f'bills/{billno}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('SUCCESS',f'BILL:{billno} IS SAVED')
        billno=random.randint(100,1000)

def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == BillEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('ERROR','Invalid Bill Number')

def print():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('ERROR','Bill Is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file, 'print')
def clear():
    gljEntry.insert(0,0)
    OxjEntry.insert(0,0)
    JimjEntry.insert(0,0)
    CusjEntry.insert(0,0)
    S9jEntry.insert(0,0)
    LVjEntry.insert(0,0)
    CsEntry.insert(0,0)
    slEntry.insert(0,0)
    gvEntry.insert(0,0)
    D4Entry.insert(0,0)
    SNEntry.insert(0,0)
    MfEntry.insert(0,0)
    slrEntry.insert(0,0)
    slcEntry.insert(0,0)
    tagEntry.insert(0,0)
    tagfEntry.insert(0,0)
    bsEntry.insert(0,0)
    TSEntry.insert(0,0)
    tshirt_priceEntry.delete(0,END)
    shirt_priceEntry.delete(0,END)
    jeans_priceEntry.delete(0,END)
    jeans_taxEntry.delete(0,END)
    shirt_taxEntry.delete(0,END)
    tshirt_taxEntry.delete(0,END)
    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    BillEntry.delete(0,END)

    textarea.delete(0,END)

# gui

root = Tk()
root.title("BILLING SYSTEM")
root.geometry('1270x550')
root.iconbitmap("icon.ico")

# heading
headingLabel=Label(root,text="SSQUARE COLLECTION",font=('times new roman',30,'bold'),
                   bg='black',fg='red')
headingLabel.pack(fill=X)

# customer details frame
customer_details_frame=LabelFrame(root,text='CUSTOMER DETAILS',font=('times new roman',15,'bold'),bg='black',fg='red')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='black',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=10)

nameEntry=Entry(customer_details_frame,font=('arial',15))
nameEntry.grid(row=0,column=1,pady=10,padx=5)

PhoneLabel=Label(customer_details_frame,text='Phone No.',font=('times new roman',15,'bold'),bg='black',fg='white')
PhoneLabel.grid(row=0,column=2,padx=20,pady=10)

PhoneEntry=Entry(customer_details_frame,font=('arial',15))
PhoneEntry.grid(row=0,column=3,pady=10,padx=5)

BillLabel=Label(customer_details_frame,text='Bill No.',font=('times new roman',15,'bold'),bg='black',fg='white')
BillLabel.grid(row=0,column=4,padx=20,pady=10)

BillEntry=Entry(customer_details_frame,font=('arial',15))
BillEntry.grid(row=0,column=5,pady=10,padx=5)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),command=search)
searchButton.grid(row=0,column=6,padx=50,pady=8)

productFrame=Frame(root)
productFrame.pack(fill=X)

# jeans frame
jeansFrame=LabelFrame(productFrame,text='JEANS',font=('times new roman',15,'bold'),bg='black',fg='red')
jeansFrame.grid(row=0,column=0)

# glitz jeans
gljLabel=Label(jeansFrame,text='GLITZ',font=('times new roman',15,'bold'),bg='black',fg='white')
gljLabel.grid(row=1,column=0,)

gljEntry=Entry(jeansFrame,font=('arial',15),width=10)
gljEntry.grid(row=1,column=1,pady=5,padx=20)
gljEntry.insert(0,0)

# oxford jeans
OxjLabel=Label(jeansFrame,text='Oxford',font=('times new roman',15,'bold'),bg='black',fg='white')
OxjLabel.grid(row=2,column=0)

OxjEntry=Entry(jeansFrame,font=('arial',15),width=10)
OxjEntry.grid(row=2,column=1,pady=5,padx=5)
OxjEntry.insert(0,0)

# jimmy
JimjLabel=Label(jeansFrame,text='JIMMY',font=('times new roman',15,'bold'),bg='black',fg='white')
JimjLabel.grid(row=3,column=0)

JimjEntry=Entry(jeansFrame,font=('arial',15),width=10)
JimjEntry.grid(row=3,column=1,pady=5,padx=5)
JimjEntry.insert(0,0)

# custom
CusjLabel=Label(jeansFrame,text='CUSTOM',font=('times new roman',15,'bold'),bg='black',fg='white')
CusjLabel.grid(row=4,column=0)

CusjEntry=Entry(jeansFrame,font=('arial',15),width=10)
CusjEntry.grid(row=4,column=1,pady=5,padx=5)
CusjEntry.insert(0,0)

#s9
S9jLabel=Label(jeansFrame,text='S9',font=('times new roman',15,'bold'),bg='black',fg='white')
S9jLabel.grid(row=5,column=0)

S9jEntry=Entry(jeansFrame,font=('arial',15),width=10)
S9jEntry.grid(row=5,column=1,pady=5,padx=5)
S9jEntry.insert(0,0)

#Levis
LVjLabel=Label(jeansFrame,text='LEVIS',font=('times new roman',15,'bold'),bg='black',fg='white')
LVjLabel.grid(row=6,column=0)

LVjEntry=Entry(jeansFrame,font=('arial',15),width=10)
LVjEntry.grid(row=6,column=1,pady=5,padx=5)
LVjEntry.insert(0,0)

# shirt frame

shirtFrame=LabelFrame(productFrame,text='Shirt',font=('times new roman',15,'bold'),bg='black',fg='red')
shirtFrame.grid(row=0,column=1)


# cs shirts
CsLabel=Label(shirtFrame,text='CS',font=('times new roman',15,'bold'),bg='black',fg='white')
CsLabel.grid(row=0,column=1)

CsEntry=Entry(shirtFrame,font=('arial',15),width=10)
CsEntry.grid(row=0,column=2,pady=5,padx=20)
CsEntry.insert(0,0)

# sl shirts
slLabel=Label(shirtFrame,text='SL',font=('times new roman',15,'bold'),bg='black',fg='white')
slLabel.grid(row=1,column=1)

slEntry=Entry(shirtFrame,font=('arial',15),width=10)
slEntry.grid(row=1,column=2,pady=5,padx=5)
slEntry.insert(0,0)

# gv shirts

gvLabel=Label(shirtFrame,text='GV',font=('times new roman',15,'bold'),bg='black',fg='white')
gvLabel.grid(row=2,column=1)

gvEntry=Entry(shirtFrame,font=('arial',15),width=10)
gvEntry.grid(row=2,column=2,pady=5,padx=5)
gvEntry.insert(0,0)

#d4 shirts
D4Label=Label(shirtFrame,text='D4',font=('times new roman',15,'bold'),bg='black',fg='white')
D4Label.grid(row=3,column=1)


D4Entry=Entry(shirtFrame,font=('arial',15),width=10)
D4Entry.grid(row=3,column=2,pady=5,padx=5)
D4Entry.insert(0,0)

#snitch
SNLabel=Label(shirtFrame,text='Snitch',font=('times new roman',15,'bold'),bg='black',fg='white')
SNLabel.grid(row=4,column=1)


SNEntry=Entry(shirtFrame,font=('arial',15),width=10)
SNEntry.grid(row=4,column=2,pady=5,padx=5)
SNEntry.insert(0,0)
#mf
MfLabel=Label(shirtFrame,text='MaF',font=('times new roman',15,'bold'),bg='black',fg='white')
MfLabel.grid(row=5,column=1)

MfEntry=Entry(shirtFrame,font=('arial',15),width=10)
MfEntry.grid(row=5,column=2,pady=5,padx=5)
MfEntry.insert(0,0)
# tees frame

teesFrame=LabelFrame(productFrame,text='T-SHIRT',font=('times new roman',15,'bold'),bg='black',fg='red')
teesFrame.grid(row=0,column=2)

# sl round
slrLabel=Label(teesFrame,text='SL ROUND',font=('times new roman',15,'bold'),bg='black',fg='white')
slrLabel.grid(row=0,column=2)

slrEntry=Entry(teesFrame,font=('arial',15),width=10)
slrEntry.grid(row=0,column=3,pady=5,padx=5)
slrEntry.insert(0,0)

# sl collar
slcLabel=Label(teesFrame,text='SL COLLAR',font=('times new roman',15,'bold'),bg='black',fg='white')
slcLabel.grid(row=1,column=2)

slcEntry=Entry(teesFrame,font=('arial',15),width=10)
slcEntry.grid(row=1,column=3,pady=5,padx=20)
slcEntry.insert(0,0)
# tag
tagLabel=Label(teesFrame,text='TAG',font=('times new roman',15,'bold'),bg='black',fg='white')
tagLabel.grid(row=2,column=2)

tagEntry=Entry(teesFrame,font=('arial',15),width=10)
tagEntry.grid(row=2,column=3,pady=5,padx=5)
tagEntry.insert(0,0)

# tag full
tagfLabel=Label(teesFrame,text='Full Sleeves',font=('times new roman',15,'bold'),bg='black',fg='white')
tagfLabel.grid(row=3,column=2)

tagfEntry=Entry(teesFrame,font=('arial',15),width=10)
tagfEntry.grid(row=3,column=3,pady=5,padx=5)
tagfEntry.insert(0,0)

#BOSS
bsLabel=Label(teesFrame,text='BOSS',font=('times new roman',15,'bold'),bg='black',fg='white')
bsLabel.grid(row=4,column=2)

bsEntry=Entry(teesFrame,font=('arial',15),width=10)
bsEntry.grid(row=4,column=3,pady=5,padx=5)
bsEntry.insert(0,0)

#TS
TSLabel=Label(teesFrame,text='TS',font=('times new roman',15,'bold'),bg='black',fg='white')
TSLabel.grid(row=5,column=2)

TSEntry=Entry(teesFrame,font=('arial',15),width=10)
TSEntry.grid(row=5,column=3,pady=5,padx=5)
TSEntry.insert(0,0)

#bill frame

billframe=Frame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billareaLabel=Label(billframe,text='BILL AREA',font=('times new roman',15,'bold' ),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

sb=Scrollbar(billframe,orient=VERTICAL)
sb.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=12,width=60,yscrollcommand=sb.set)
textarea.pack()
sb.config(command=textarea.yview)


# bill menu frame

bill_menu_frame=LabelFrame(root,text='BILLING DETAILS',font=('times new roman',15,'bold'),bg='black',fg='red')
bill_menu_frame.pack()

jeans_pricelabel=Label(bill_menu_frame,text='JEANS PRICE',font=('times new roman',15,'bold'),bg='black',fg='white')
jeans_pricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

jeans_priceEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
jeans_priceEntry.grid(row=0,column=1,pady=9,padx=10)

shirt_pricelabel=Label(bill_menu_frame,text='SHIRT PRICE',font=('times new roman',15,'bold'),bg='black',fg='white')
shirt_pricelabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

shirt_priceEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
shirt_priceEntry.grid(row=1,column=1,pady=9,padx=10)

tshirt_pricelabel=Label(bill_menu_frame,text='T-SHIRT PRICE',font=('times new roman',15,'bold'),bg='black',fg='white')
tshirt_pricelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

tshirt_priceEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
tshirt_priceEntry.grid(row=2,column=1,pady=9,padx=10)

jeans_taxlabel=Label(bill_menu_frame,text='JEANS TAX',font=('times new roman',15,'bold'),bg='black',fg='white')
jeans_taxlabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

jeans_taxEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
jeans_taxEntry.grid(row=0,column=3,pady=9,padx=10)


shirt_taxlabel=Label(bill_menu_frame,text='SHIRT TAX',font=('times new roman',15,'bold'),bg='black',fg='white')
shirt_taxlabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

shirt_taxEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
shirt_taxEntry.grid(row=1,column=3,pady=9,padx=10)

tshirt_taxlabel=Label(bill_menu_frame,text='T-SHIRT TAX',font=('times new roman',15,'bold'),bg='black',fg='white')
tshirt_taxlabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

tshirt_taxEntry=Entry(bill_menu_frame,font=('arial',15),width=10)
tshirt_taxEntry.grid(row=2,column=3,pady=9,padx=10)

# buttons

buttonFrame=Frame(bill_menu_frame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)


totalButton=Button(buttonFrame,text='TOTAL',font=('arial',16,'bold'),bg='black',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=25)

billButton=Button(buttonFrame,text='BILL',font=('arial',16,'bold'),bg='black',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=25)

printButton=Button(buttonFrame,text='PRINT',font=('arial',16,'bold'),bg='black',fg='white',bd=5,width=8,pady=10,command=print)
printButton.grid(row=0,column=2,pady=20,padx=25)

clearButton=Button(buttonFrame,text='CLEAR',font=('arial',16,'bold'),bg='black',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=3,pady=20,padx=25)

root.mainloop()
