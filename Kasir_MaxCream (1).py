#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;

#Membuat Frame aplikasi
root = Tk()

root.geometry("1355x768+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("Maxcream Cashier") # nama aplikasi

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Maxcream',font=('Castellar',39,'bold'),fg='#fde4c3',bg='#302a18', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#784c12') # warna dasar / background
# batas Frame aplikasi


# VARIABLE
# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

# variabel menu mxcream
e_original=StringVar()
e_boba=StringVar()
e_oreo = StringVar()
e_jasmine = StringVar()
e_peppermint = StringVar()
e_caramel = StringVar()
e_strawberry = StringVar()
e_mocca = StringVar()
e_mango = StringVar()



# variabel Harga dalam struk
hargadarimxcreamvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_original.set('0')
e_boba.set('0')
e_oreo.set('0')
e_jasmine.set('0')
e_peppermint.set('0')
e_caramel.set('0')
e_strawberry.set('0')
e_mocca.set('0')
e_mango.set('0')


# FUNGSI
# Awal fungsi perhitungan harga total
tax=(11/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadarimxcream,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or         var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0:

        item1=int(e_original.get())
        item2=int(e_boba.get())
        item3=int(e_oreo.get())
        item4=int(e_jasmine.get())
        item5=int(e_peppermint.get())
        item6=int(e_caramel.get())
        item7=int(e_strawberry.get())
        item8=int(e_mocca.get())
        item9=int(e_mango.get())



        hargadarimxcream=(item1*8000) + (item2*16000) + (item3*16000) + (item4*15000) + (item5*15000) + (item6*20000) + (item7*16000)         + (item8*16000) + (item9*24000)


        hargadarimxcreamvar.set(str(hargadarimxcream))


        subtotalItems=hargadarimxcream
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# awal fungsi cetak struk
def struk():
    global billnumber,date
    if hargadarimxcreamvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'----------------------------------------------------------\n')
        textStruk.insert(END,'Varian\t\t          Harga Eskrim (Rp)\n')
        textStruk.insert(END,'-----------------------------\n\n')
        if e_original.get()!='0':
            textStruk.insert(END,f'Original\t\t\tRp. {int(e_original.get())*8000}\n\n')

        if e_boba.get()!='0':
            textStruk.insert(END,f'Boba Sundae\t\t\tRp. {int(e_boba.get())*16000}\n\n')

        if e_oreo.get()!='0':
            textStruk.insert(END,f'Oreo Sundae\t\t\tRp. {int(e_oreo.get())*16000}\n\n')

        if e_jasmine.get() != '0':
            textStruk.insert(END, f'Jasmine Tea MC\t\t\tRp. {int(e_jasmine.get()) * 15000}\n\n')

        if e_peppermint.get() != '0':
            textStruk.insert(END, f'Peppermint Tea MC\t\t\tRp. {int(e_peppermint.get()) * 15000}\n\n')

        if e_caramel.get() != '0':
            textStruk.insert(END, f'Caramel Sundae\t\t\tRp. {int(e_caramel.get()) * 20000}\n\n')

        if e_strawberry.get() != '0':
            textStruk.insert(END, f'Strawberry Sundae\t\t\tRp. {int(e_strawberry.get()) * 16000}\n\n')

        if e_mocca.get() != '0':
            textStruk.insert(END, f'Mocca Sundae\t\t\tRp. {int(e_mocca.get()) * 16000}\n\n')

        if e_mango.get() != '0':
            textStruk.insert(END, f'Mango Boba MC\t\t\tRp. {int(e_mango.get()) * 24000}\n')



        textStruk.insert(END,'----------------------------------------------------------\n')
        if hargadarimxcreamvar.get()!='Rp 0':
            textStruk.insert(END,f'Sub Total\t\t\tRp. {hargadarimxcream}\n\n')

        textStruk.insert(END, f'PPN\t\t\tRp. {totaltax}\n')
        textStruk.insert(END,'-----------------------------\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {hargadarimxcream+totaltax}\n')
        textStruk.insert(END,'----------------------------------------------------------\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')
# Batas fungsi simpan dalam perangkat 

# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_original.set('0')
    e_boba.set('0')
    e_oreo.set('0')
    e_jasmine.set('0')
    e_peppermint.set('0')
    e_caramel.set('0')
    e_strawberry.set('0')
    e_mocca.set('0')
    e_mango.set('0')


    # batas untuk variables

    textoriginal.config(state=DISABLED)
    textboba.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textjasmine.config(state=DISABLED)
    textpeppermint.config(state=DISABLED)
    textcaramel.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)
    textmocca.config(state=DISABLED)
    textmango.config(state=DISABLED)


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

    hargadarimxcreamvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')

# batas fungsi reset

# mengaktifkan fungsi entry menu
def original():
    if var1.get()==1:
        textoriginal.config(state=NORMAL)
        textoriginal.delete(0,END)
        textoriginal.focus()
    else:
        textoriginal.config(state=DISABLED)
        e_original.set('0')

def boba():
    if var2.get()==1:
        textboba.config(state=NORMAL)
        textboba.delete(0,END)
        textboba.focus()
    else:
        textboba.config(state=DISABLED)
        e_boba.set('0')

def oreo():
    if var3.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def jasmine():
    if var4.get()==1:
        textjasmine.config(state=NORMAL)
        textjasmine.delete(0,END)
        textjasmine.focus()

    else:
        textjasmine.config(state=DISABLED)
        e_jasmine.set('0')

def peppermint ():
    if var5.get()==1:
        textpeppermint.config(state=NORMAL)
        textpeppermint.delete(0,END)
        textpeppermint.focus()
    else:
        textpeppermint.config(state=DISABLED)
        e_peppermint.set('0')

def caramel():
    if var6.get()==1:
        textcaramel.config(state=NORMAL)
        textcaramel.delete(0,END)
        textcaramel.focus()
    else:
        textcaramel.config(state=DISABLED)
        e_caramel.set('0')

def strawberry():
    if var7.get()==1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0,END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')

def mocca():
    if var8.get()==1:
        textmocca.config(state=NORMAL)
        textmocca.delete(0,END)
        textmocca.focus()
    else:
        textmocca.config(state=DISABLED)
        e_mocca.set('0')

def mango():
    if var9.get()==1:
        textmango.config(state=NORMAL)
        textmango.delete(0,END)
        textmango.focus()
    else:
        textmango.config(state=DISABLED)
        e_mango.set('0')
# batas mengaktifkan entry menu makanan


# FRAME KIRI

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=12)
hargaFrame.pack(side=BOTTOM)

mxcreamFrame=LabelFrame(menuFrame,text=' MENU ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
mxcreamFrame.pack(side=LEFT)

calculatorFrame=Frame(menuFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu eskrim
original=Checkbutton(mxcreamFrame,text=' Original ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=original, bg='#f6f6f6')
original.grid(row=0,column=0,sticky=W)

boba=Checkbutton(mxcreamFrame,text=' Boba Sundae ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=boba, bg='#f6f6f6')
boba.grid(row=1,column=0,sticky=W)

oreo=Checkbutton(mxcreamFrame,text=' Oreo Sundae ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=oreo, bg='#f6f6f6')
oreo.grid(row=2,column=0,sticky=W)

jasmine=Checkbutton(mxcreamFrame,text=' Jasmine Tea MC ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=jasmine, bg='#f6f6f6')
jasmine.grid(row=3,column=0,sticky=W)

peppermint=Checkbutton(mxcreamFrame,text=' Peppermint Tea MC',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=peppermint, bg='#f6f6f6')
peppermint.grid(row=4,column=0,sticky=W)

caramel=Checkbutton(mxcreamFrame,text= ' Caramel Sundae',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=caramel, bg='#f6f6f6')
caramel.grid(row=5,column=0,sticky=W)

strawberry=Checkbutton(mxcreamFrame,text=' Strawberry Sundae ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=strawberry, bg='#f6f6f6')
strawberry.grid(row=6,column=0,sticky=W)

mocca=Checkbutton(mxcreamFrame,text=' Mocca Sundae',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=mocca, bg='#f6f6f6')
mocca.grid(row=7,column=0,sticky=W)

mango=Checkbutton(mxcreamFrame,text=' Mango Boba MC ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=mango, bg='#f6f6f6')
mango.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item eskrim
textoriginal=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_original)
textoriginal.grid(row=0,column=1)

textboba=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_boba)
textboba.grid(row=1,column=1)

textoreo=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_oreo)
textoreo.grid(row=2,column=1)

textjasmine=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_jasmine)
textjasmine.grid(row=3,column=1)

textpeppermint=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_peppermint)
textpeppermint.grid(row=4,column=1)

textcaramel=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7, width=8,state=DISABLED,textvar=e_caramel)
textcaramel.grid(row=5,column=1)

textstrawberry=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_strawberry)
textstrawberry.grid(row=6,column=1)

textmocca=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_mocca)
textmocca.grid(row=7,column=1)

textmango=Entry(mxcreamFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_mango)
textmango.grid(row=8,column=1)



# membuat tampilan daftar menu kalkulator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''


# menambahkan fields entri untuk item dessert
calculatorField=Entry(calculatorFrame,font=('arial',25,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',25,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',25,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',25,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',25,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',25,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadarimxcream=Label(hargaFrame,text='    HARGA ESKRIM', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadarimxcream.grid(row=0,column=0)

textHargadarimxcream=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadarimxcreamvar)
textHargadarimxcream.grid(row=0,column=1,padx=41)



LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()


# In[ ]:





# In[ ]:




