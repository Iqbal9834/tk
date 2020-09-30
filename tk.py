import tkinter.messagebox
from tkinter import *
import sqlite3 as sq
# try:
    # conn = sq.connect()
    # cursor = conn.cursor()
    # cursor.execute( & quot; & quot; & quot; CREATE TABLE IF NOT EXISTS tours(
    #     To_place text,
    #     From_place text,
    #     Interval text,
    #     Amount text,
    #     Tour_code text PRIMARY KEY); & quot; & quot; & quot; )


def res():
    if(v.get() == 2):
        w.destroy()

        def show():
            list1.delete(0, END)
            cursor = conn.cursor()
            cursor.execute(&quot; SELECT * FROM tours&quot; )
            a = cursor.fetchall()  # fetches whole data from the db for
        i in a:
        list1.insert(END, i)


if list1.size() == 0:

tkinter.messagebox.showinfo(&quot; Underflow&quot; , & quot; Oops!! Nothing to show&quot; )


def search():


t = str(e1.get()) f = str(e2.get())
dt = str(e3.get()) a = str(e4.get())
c = str(e5.get()) if(t == &quot; & quot; and f == &quot; & quot; and dt == &quot; & quot; and
a == &quot; & quot; and c == &quot; & quot;):

tkinter.messagebox.showinfo(&quot; Error&quot; , & quot; None of the fields are filled&quot; )

else: m = [] if(t != &quot; & quot;):
f1 = &quot; To_place =? and & quot;
m.append(t)

else:
if(f != &quot; & quot;):

f1 = &quot; & quot;
f2 = &quot; From_place =? and & quot;
m.append(f) else:


if(dt != &quot; & quot;):
f2 = &quot; & quot;
f3 = &quot; Interval =? and & quot;
m.append(dt) else:

f3 = &quot; & quot;

if(a != &quot; & quot;):

f4 = &quot; Amount =? and & quot;
m.append(a) else:
f4 = &quot; & quot;

if(c != &quot; & quot;):

f5 = &quot; Tour_code =?&quot;
m.append(c) else:
f5 = &quot; Tour_code !=?&quot;

m.append(c) cursor = conn.cursor()

cursor.execute(f & quot; & quot; & quot; SELECT * FROM tours WHERE {f1} {f2} {f3} {f4}

{f5}&quot; & quot; & quot; , m)

rows = cursor.fetchall()

if(rows == []):
else:
for i in rows:
def close():


tkinter.messagebox.showinfo(&quot; Alert&quot;, & quot; No record found&quot; )
list1.delete(0, END)
list1.insert(END, i)

answer = tkinter.messagebox.askquestion(&quot; Exit&quot;, & quot; Are you sure you want to exit ?& quot; )

The following packages have unmet dependencies:
 npm : Depends: node-gyp ( >= 0.10.9) but it is not going
if answer == &quot; yes&quot; : w1.destroy() else:

pass
def set(m):


i = list1.curselection()
if(len(i) == 0):
pass

else:

b = i[0]
j1, j2, j3, j4, j5 = list1.get(b)
e1.delete(0, END)
e1.insert(END, j1)
e2.delete(0, END)
e2.insert(END, j2)
e3.delete(0, END)
e3.insert(END, j3)
e4.delete(0, END)

10

e4.insert(END, j4)
e5.delete(0, END)
e5.insert(END, j5) def
clear1(): e1.delete(0, END)
e2.delete(0, END)
e3.delete(0, END)
e4.delete(0, END)
e5.delete(0, END)
w1 = Tk()
w1.title(&quot; TOURS AND TRAVELS (USER MODULE)&quot; )
w1.configure(background=&quot; light green&quot; )
l1 = Label(w1, text=&quot; TO&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l1.grid(row=0, column=0)
l2 = Label(w1, text=&quot; FROM&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l2.grid(row=0, column=3)
l3 = Label(w1, text=&quot; INTERVAL&quot;, bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l3.grid(row=1, column=0)
l4 = Label(w1, text=&quot; AMOUNT&quot;, bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l4.grid(row=1, column=3)
l5=Label(w1, text=&quot; TOUR CODE&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l5.grid(row=2, column=0)
l6=Label(w1, text=&quot; == ==To\tFrom\tInterval\tAmount\tTour code == ==&quot;, bg= &  # 39;yellow&#39;
, font=(&quot; Comic Sans MS&quot; , 16))
l6.grid(row=4, column=0)
from_text=StringVar()
e1 = Entry(w1, textvariable=from_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))
e1.grid(row=0, column=1)
to_text=StringVar()
e2 = Entry(w1, textvariable=to_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))
e2.grid(row=0, column=4)
traveldt_text=StringVar()

10

e3 = Entry(w1, textvariable=traveldt_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))
e3.grid(row=1, column=1)
amount_text=StringVar()
e4= Entry(w1, textvariable=amount_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))
e4.grid(row=1, column=4)
tourcode_id=StringVar()
e5=Entry(w1, textvariable=tourcode_id, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))
e5.grid(row=2, column=1)
list1 = Listbox(w1, height=7, width=35, bg=&quot; light blue&quot; , fg=&quot; red&quot; , font=(&quot; Calibri&quot; , 20))
list1.bind(&#39;&lt;&lt;ListboxSelect&gt;&gt;&#39;, set)
list1.grid(row=5, column=0, rowspan=6, columnspan=1)
sb1=Scrollbar(w1)
sb1.grid(row=3, column=1, rowspan=6)
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)
b1 = Button(w1, text=&quot; SHOW DATA&quot; ,
width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=show)
b1.grid(row=4, column=3)
b4 = Button(w1, text=&quot; SEARCH DATA&quot; ,
width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=search)
b4.grid(row=5, column=3)
b6 = Button(w1, text=&quot; CLOSE&quot; ,
width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=close)
b6.grid(row=6, column=3)
w1.mainloop()
if(v.get() == 1): def check():
p=e.get() if(p == &quot; Hello&quot; ):
window1.destroy()
w.destroy()
window=Tk() def
set(m):
i=list1.curselection()
if(len(i) == 0):
pass else:

10

b=i[0]
j1, j2, j3, j4, j5=list1.get(b)
e1.delete(0, END)
e1.insert(END, j1)
e2.delete(0, END)
e2.insert(END, j2)
e3.delete(0, END)
e3.insert(END, j3)
e4.delete(0, END)
e4.insert(END, j4)
e5.delete(0, END)
e5.insert(END, j5) def
clear1():

e1.delete(0, END)

e2.delete(0, END) e3.delete(0, END)
e4.delete(0, END) e5.delete(0, END)

def
show():
list1.delete(0, END)
cursor=conn.cursor()

cursor.execute(&quot; SELECT * FROM tours&quot; )

a=cursor.fetchall()  # fetches whole data from the db for
i in a:
if list1.size() == 0:

list1.insert(END, i)
tkinter.messagebox.showinfo(&quot; Underflow&quot; , & quot; Oops!! Nothing to show&quot; )

def add(): t=str(e1.get()) f=str(e2.get())
dt=str(e3.get()) a=str(e4.get()) c=str(e5.get())
if(t == &quot; & quot; or f == &quot; & quot; or dt == &quot; & quot; or a == &quot; & quot; or c == &quot; & quot;):
tkinter.messagebox.showinfo(&quot; Error&quot; , & quot; All fields not filled&quot; ) else:

cursor=conn.cursor()
cursor.execute(&quot; SELECT * FROM tours WHERE Tour_code=?& quot; , [c])

a1=cursor.fetchone() if(a1 == None):
k=[t, f, dt, a, c] cursor=conn.cursor()

cursor.execute(&quot; INSERT INTO tours VALUES(?, ?, ?, ?, ?); & quot;, k)

conn.commit()show()

tkinter.messagebox.showinfo(&quot; Alert&quot; , & quot; Data Added&quot; )

clear1() else:

tkinter.messagebox.showinfo(&quot; Error&quot;, & quot; Tour_code cannot be same&quot; )
def update(): upd=list1.curselection() if

10

upd == (): show()
tkinter.messagebox.showinfo(&quot; Alert&quot; , & quot; Entry not selected&quot; ) else:

upd=list1.get(upd[0])

cd=upd[4]

tkinter.messagebox.showinfo(&quot; Alert&quot;, & quot; Updation would be done in

accordance with Tour_code&quot;)

t=str(e1.get()) f=str(e2.get())

dt=str(e3.get()) a=str(e4.get())
c=str(e5.get()) if(t == &quot; & quot; or f == &quot; & quot; or dt == &quot; & quot; or a == &quot; & quot; or c == &quot; & quot;):
tkinter.messagebox.showinfo(&quot; Error&quot; , & quot; All fields not filled&quot; )
else:

Tour_code=?& quot;, [cd])
if(rows == None):

cursor=conn.cursor()
cursor.execute(& quot; SELECT Tour_code FROM tours WHERE
rows=cursor.fetchone()
tkinter.messagebox.showinfo(&quot; Alert&quot;, & quot; Given Tour_code do not

exist&quot;) else:

cursor.execute(& quot; & quot; & quot; UPDATE tours SET
To_place=?, From_place=?, Interval=?, Amount=?, Tour_code=?
WHERE Tour_code=?& quot; & quot; & quot; , [t, f, dt, a, c, cd])

conn.commit()show()

tkinter.messagebox.showinfo(&quot; Alert&quot;, & quot; Data Updated&quot; )

clear1() def search():

t=str(e1.get()) f=str(e2.get())

dt=str(e3.get()) a=str(e4.get())
c=str(e5.get()) if(t == &quot; & quot; and f == &quot; & quot; and dt == &quot; & quot; and
a == &quot; & quot; and c == &quot; & quot;):

tkinter.messagebox.showinfo(&quot; Error&quot; , & quot; None of the fields are filled&quot; )

else: m=[] if(t != &quot; & quot;):

f1= & quot; To_place=? and &quot;
m.append(t) else:
f1= & quot; & quot;

if(f != &quot; & quot;):

else:
if(dt != &quot; & quot;):

f2= & quot; From_place=? and &quot;
m.append(f)
f2= & quot; & quot;

10
f3= & quot; Interval=? and &quot;
m.append(dt) else:

f3= & quot; & quot;

if(a != &quot; & quot;):

f4= & quot; Amount=? and &quot;
m.append(a) else:
f4= & quot; & quot;

if(c != &quot; & quot;):

f5= & quot; Tour_code=?& quot;
m.append(c) else:
f5= & quot; Tour_code !=?&quot;

m.append(c) cursor=conn.cursor()

cursor.execute(f & quot; & quot; & quot; SELECT * FROM tours WHERE {f1} {f2} {f3} {f4}

{f5}&quot; & quot; & quot; , m)
if(rows == []):
else:
for i in rows:
def delete():

rows=cursor.fetchall()
tkinter.messagebox.showinfo(&quot; Alert&quot; , & quot; No record found&quot; )
list1.delete(0, END)
list1.insert(END, i)
dele=list1.curselection()
if dele == (): show()

tkinter.messagebox.showinfo(&quot; Alert&quot;, & quot; Select item from list box that you wist to

delete&quot;) else:
r=dele[::-1]

for x in r:
code=delete[4]

delete=list1.get(x)

cursor=conn.cursor()

cursor.execute(&quot; DELETE FROM tours WHERE Tour_code=?& quot; , [code])

conn.commit()show()

tkinter.messagebox.showinfo(&quot; Alert&quot; , & quot; Data deleted&quot; )

clear1() def close():

answer=tkinter.messagebox.askquestion(&quot; Exit&quot;, & quot; Are you sure you want to exit ?& quot; )
if answer == &quot; yes&quot; : window.destroy() else: pass

window.title(&quot; TOURS AND TRAVELS (ADMIN MODULE)&quot; )

window.configure(background=&quot; light green&quot; )

10

l1 = Label(window, text=&quot; TO&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))

l1.grid(row=0, column=0)

l2 = Label(window, text=&quot; FROM&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))

l2.grid(row=0, column=3)

l3 = Label(window, text=&quot; INTERVAL&quot;, bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))

l3.grid(row=1, column=0)

l4 = Label(window, text=&quot; AMOUNT&quot;, bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))

l4.grid(row=1, column=3)

l5=Label(window, text=&quot; TOUR CODE&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))

l5.grid(row=2, column=0)

l6=Label(window, text=& quot; == ==To\tFrom\tInterval\tAmount\tTour

code == ==&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,16))
l6.grid(row=4, column=0)

from_text=StringVar()
e1 = Entry(window, textvariable=from_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))

e1.grid(row=0, column=1)
to_text=StringVar()
e2 = Entry(window, textvariable=to_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))

e2.grid(row=0, column=4)

traveldt_text=StringVar()
e3 = Entry(window, textvariable=traveldt_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))

e3.grid(row=1, column=1)

amount_text=StringVar()
e4= Entry(window, textvariable=amount_text, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))

e4.grid(row=1, column=4)

tourcode_id=StringVar()
e5=Entry(window, textvariable=tourcode_id, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 20))

e5.grid(row=2, column=1)

list1=Listbox(window, height=7, width=35, bg= & quot; light

10

blue&quot;, fg=&quot; red&quot; , font=(&quot; Calibri&quot; , 20), selectmode=MULTIPLE)

list1.bind(&#39;&lt;&lt;ListboxSelect&gt;&gt;&#39;, set)
list1.grid(row=4, column=0, rowspan=6, columnspan=1)
sb1=Scrollbar(window)
sb1.grid(row=3, column=1, rowspan=6)
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

b1 = Button(window, text=&quot; SHOW DATA&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=show)
b1.grid(row=4, column=3)

b2 = Button(window, text=&quot; ADD DATA&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=add) # no bracket with function

b2.grid(row=5, column=4)
b3 = Button(window, text=&quot; UPDATE DATA&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=update)
b3.grid(row=6, column=3)

b4 = Button(window, text=&quot; SEARCH DATA&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=search)
b4.grid(row=7, column=4)

b5 = Button(window, text=&quot; DELETE DATA&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=delete)
b5.grid(row=8, column=3)

b6 = Button(window, text=&quot; CLOSE&quot; ,

width=16, bg=&quot; black&quot;, fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 20), command=close)
b6.grid(row=9, column=4)
window.mainloop()
conn.commit() else:

tkinter.messagebox.showinfo(&quot; Status&quot;, & quot; Wrong password&quot; )
window1=Tk() window1.geometry(&quot; 430x120+300+400&quot; )
window1.configure(background=&quot; light green&quot; )
window1.title(&quot; TOURS AND TRAVELS ADMIN LOGIN&quot; )
l1=Label(window1, text=&quot; Enter password: & quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,15))
l1.grid(row=0, column=0) s=StringVar()

10

e=Entry(window1, textvariable=s, bg=&quot; pink&quot;, font=(&quot; Calibri&quot; , 15), width=10)
e.grid(row=1, column=1) b=Button(window1, text=& quot; Login as
admin&quot;, command=check, bg=&quot; teal&quot; , fg=&quot; white&quot; , font=(&quot; Calibri&quot; , 18))
b.grid(row=2, column=2) window1.mainloop() else:
tkinter.messagebox.showinfo(&quot; Alert&quot; , & quot; Select one&quot; )
w=Tk()
w.geometry(&quot; 380x200&quot;)  # width x height(small x)
w.title(&quot; TOURS AND TRAVELS&quot; )
w.configure(background=&quot; light green&quot; ) l1=Label(w, text=&quot; Login
page&quot; , bg= &  # 39;yellow&#39; ,font=(&quot;Comic Sans MS&quot;,20))
l1.grid(row=0, column=2)
l2=Label(w, text=&quot; Select one: & quot; , bg= &  # 39;pink&#39; ,font=(&quot;Comic Sans MS&quot;,15))
l2.grid(row=1, column=2)
v=IntVar()
l3=Label(w, text=&quot; & quot; , padx=10, bg=&quot; light green&quot; )
l3.grid(row=2, column=0)
r1=Radiobutton(w, text=&quot; Admin&quot; , value=1, variable=v, bg= &  # 39;light blue&#39;
, font=(&quot; Comic Sans MS&quot; , 15))
r1.grid(row=2, column=1)
r2=Radiobutton(w, text=&quot; User&quot; , value=2, variable=v, bg= &  # 39;light blue&#39; ,font=(&quot;Comic Sans
MS&quot; , 15))
r2.grid(row=2, column=3)
l4=Label(w, text=&quot; & quot; , padx=10, bg=&quot; light green&quot; )
l4.grid(row=3, column=2)
b=Button(w, text=&quot; Submit choice&quot; , command=res, fg=&quot; white&quot; , bg= &  # 39;teal&#39; ,font=(&quot;Comic Sans
MS&quot; , 15))
b.g rid(row=4, column=2)
w.mainloop()
conn.commit() except:
tkinter.messagebox.showerror(&quot; Error&quot; , & quot; Some error occured&quot; )
finally: conn.commit() conn.close()

10

SCREENSHOTS:
