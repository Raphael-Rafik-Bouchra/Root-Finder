from tkinter import *
import tkinter
from tkinter import ttk
from math import *
from tkinter import font
import time
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from sympy import Symbol, Derivative,parse_expr


def bisection(fun,a,b,N,e,list):
    def f(x): 
        f = eval(fun)
        return f

    f_a = f(a)
    f_b = f(b)
    if f_a*f_b >= 0:
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        f_a_n = f(a_n)
        f_b_n = f(b_n)
        list.insert('', 'end', text=str(n), values=(str(n), str(a_n), str(b_n),str(m_n),str(f_m_n)))
        if f_a_n*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f_b_n*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif abs(f_m_n) < e:
            return m_n
        else:
            return None
    return (a_n + b_n)/2



def callBisection(f,a,b,n,e,tab,button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = 50
    if len(e) == 0:
        e = 0.00001

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab,column=("c1", "c2", "c3", "c4", "c5"),show='headings',yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER,width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Xl")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Xu")
    tree.column("# 4", anchor=CENTER,width=75)
    tree.heading("# 4", text="Xr")
    tree.column("# 5", anchor=CENTER,width=125)
    tree.heading("# 5", text="f(Xr)")

    start_time = time.time()
    root = bisection(f,float(a),float(b),int(n),float(e),tree)
    end_time = time.time()


    er_label = ttk.Label(tab,text='Bisection Failed',font=("Courier",15))
    root_label = ttk.Label(tab,text='Approx. Root = ' + str(root),font=("Courier",10))
    time_label = ttk.Label(tab,text='Execution Time = ' + str(end_time-start_time),font=("Courier",10))
    iter_label = ttk.Label(tab,text='# of Iterations = ' + str(len(tree.get_children())),font=("Courier",10))

    if root == None:
        er_label.pack()
        er_label.place(x=500,y=250)
    else:  
        root_label.pack()
        root_label.place(x=475,y=150)
        time_label.pack()
        time_label.place(x=475,y=250)
        iter_label.pack()
        iter_label.place(x=475,y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50,y=100,height=300,width=400)
    iterations.place(x=450,y=100,height=300)
    iterations.config( command = tree.yview )


def falsePosition(fun,a,b,N,e,list):
    def f(x): 
        f = eval(fun)
        return f
    f_a = f(a)
    f_b = f(b)
    if f_a*f_b >= 0:
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        f_a_n = f(a_n)
        f_b_n = f(b_n)
        m_n = ((a_n*f_b_n)-(b_n*f_a_n))/(f_b_n-f_a_n)
        f_m_n = f(m_n)
        list.insert('', 'end', text=str(n), values=(str(n), str(a_n), str(b_n),str(m_n),str(f_m_n)))
        if f_a_n*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f_b_n*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif abs(f_m_n) < e:
            return m_n
        else:
            return None
    return ((a_n*f_b_n)-(b_n*f_a_n))/(f_b_n-f_a_n)


def callFalsePosition(f,a,b,n,e,tab,button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = 50
    if len(e) == 0:
        e = 0.00001

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab,column=("c1", "c2", "c3", "c4", "c5"),show='headings',yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER,width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER,width=75)
    tree.heading("# 2", text="Xl")
    tree.column("# 3", anchor=CENTER,width=75)
    tree.heading("# 3", text="Xu")
    tree.column("# 4", anchor=CENTER,width=75)
    tree.heading("# 4", text="Xr")
    tree.column("# 5", anchor=CENTER,width=125)
    tree.heading("# 5", text="f(Xr)")

    start_time = time.time()
    root = falsePosition(f,float(a),float(b),int(n),float(e),tree)
    end_time = time.time()


    er_label = ttk.Label(tab,text='False Position Failed',font=("Courier",15))
    root_label = ttk.Label(tab,text='Approx. Root = ' + str(root),font=("Courier",10))
    time_label = ttk.Label(tab,text='Execution Time = ' + str(end_time-start_time),font=("Courier",10))
    iter_label = ttk.Label(tab,text='# of Iterations = ' + str(len(tree.get_children())),font=("Courier",10))

    if root == None:
        er_label.pack()
        er_label.place(x=500,y=250)
    else:  
        root_label.pack()
        root_label.place(x=475,y=150)
        time_label.pack()
        time_label.place(x=475,y=250)
        iter_label.pack()
        iter_label.place(x=475,y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50,y=100,height=300,width=400)
    iterations.place(x=450,y=100,height=300)
    iterations.config( command = tree.yview )


def fixedPoint(g,xr,N,e,list):
    func=parse_expr(g)
    xi=Symbol('x')
    derivative=func.diff(xi)

    def f(x): 
        f = eval(g)
        return f

    def d(x): 
        f = eval(str(derivative))
        return f

    check = abs(d(xr))
    if(check >= 1):
        print(check)
        return None
    

    for n in range(1,N+1):
        xr_old = xr
        xr = f(xr_old)
        list.insert('', 'end', text=str(n), values=(str(n), str(xr_old), str(xr)))
        ea = abs((xr - xr_old)/xr) * 100
        if ea < e:
            return xr 
    return xr



def callFixedPoint(g,xi,n,e,tab,button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = 50
    if len(e) == 0:
        e = 0.00001

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab,column=("c1", "c2", "c3"),show='headings',yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER,width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER,width=125)
    tree.heading("# 2", text="X")
    tree.column("# 3", anchor=CENTER,width=125)
    tree.heading("# 3", text="f(x)")

    start_time = time.time()
    root = fixedPoint(g,float(xi),int(n),float(e),tree)
    end_time = time.time()


    er_label = ttk.Label(tab,text='Fixed Point will Diverge',font=("Courier",15))
    root_label = ttk.Label(tab,text='Approx. Root = ' + str(root),font=("Courier",10))
    time_label = ttk.Label(tab,text='Execution Time = ' + str(end_time-start_time),font=("Courier",10))
    iter_label = ttk.Label(tab,text='# of Iterations = ' + str(len(tree.get_children())),font=("Courier",10))


    if root == None:
        er_label.pack()
        er_label.place(x=500,y=250)
    else:  
        root_label.pack()
        root_label.place(x=475,y=150)
        time_label.pack()
        time_label.place(x=475,y=250)
        iter_label.pack()
        iter_label.place(x=475,y=350)
 
    tree.pack(fill=BOTH)
    tree.place(x=50,y=100,height=300,width=400)
    iterations.place(x=450,y=100,height=300)
    iterations.config( command = tree.yview )


def newton(fun,xr,N,e,list):
    func=parse_expr(fun)
    x=Symbol('x')
    derivative=func.diff(x)
    def f(x): 
        f = eval(fun)
        return f

    def d(x): 
        f = eval(str(derivative))
        return f
    

    for n in range(1,N+1):
        xr_old = xr
        xr = xr_old - (f(xr_old)/d(xr_old))
        list.insert('', 'end', text=str(n), values=(str(n), str(xr_old), str(f(xr_old))))
        ea = abs((xr - xr_old)/xr) * 100
        if ea < e:
            return xr 
    return xr



def callNewton(f,xi,n,e,tab,button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = 50
    if len(e) == 0:
        e = 0.00001

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab,column=("c1", "c2", "c3"),show='headings',yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER,width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER,width=125)
    tree.heading("# 2", text="X")
    tree.column("# 3", anchor=CENTER,width=125)
    tree.heading("# 3", text="f(x)")

    start_time = time.time()
    root = newton(f,float(xi),int(n),float(e),tree)
    end_time = time.time()


    root_label = ttk.Label(tab,text='Approx. Root = ' + str(root),font=("Courier",10))
    time_label = ttk.Label(tab,text='Execution Time = ' + str(end_time-start_time),font=("Courier",10))
    iter_label = ttk.Label(tab,text='# of Iterations = ' + str(len(tree.get_children())),font=("Courier",10))
 
    root_label.pack()
    root_label.place(x=475,y=150)
    time_label.pack()
    time_label.place(x=475,y=250)
    iter_label.pack()
    iter_label.place(x=475,y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50,y=100,height=300,width=400)
    iterations.place(x=450,y=100,height=300)
    iterations.config( command = tree.yview )


def secant(fun,x0,x1,N,e,list):
    def f(x): 
        f = eval(fun)
        return f
    
    xa = x0
    xb = x1

    for n in range(1,N+1):
        xr = xb - (f(xb)*(xa-xb))/(f(xa) - f(xb))
        list.insert('', 'end', text=str(n), values=(str(n), str(xa), str(xb), str(f(xa)), str(f(xb)), str(xr)))
        ea = abs((xb - xa)/xb) * 100
        if ea < e:
            return xr 
        xa = xb
        xb = xr
    return xr




def callSecant(f,a,b,n,e,tab,button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = 50
    if len(e) == 0:
        e = 0.00001

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab,column=("c1", "c2", "c3", "c4", "c5", "c6"),show='headings',yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER,width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER,width=70)
    tree.heading("# 2", text="Xi-1")
    tree.column("# 3", anchor=CENTER,width=70)
    tree.heading("# 3", text="Xi")
    tree.column("# 4", anchor=CENTER,width=70)
    tree.heading("# 4", text="f(Xi-1)")
    tree.column("# 5", anchor=CENTER,width=70)
    tree.heading("# 5", text="f(Xi)")
    tree.column("# 6", anchor=CENTER,width=70)
    tree.heading("# 6", text="Xi+1")

    start_time = time.time()
    root = secant(f,float(a),float(b),int(n),float(e),tree)
    end_time = time.time()


    root_label = ttk.Label(tab,text='Approx. Root = ' + str(root),font=("Courier",10))
    time_label = ttk.Label(tab,text='Execution Time = ' + str(end_time-start_time),font=("Courier",10))
    iter_label = ttk.Label(tab,text='# of Iterations = ' + str(len(tree.get_children())),font=("Courier",10))
 
    root_label.pack()
    root_label.place(x=475,y=150)
    time_label.pack()
    time_label.place(x=475,y=250)
    iter_label.pack()
    iter_label.place(x=475,y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50,y=100,height=300,width=400)
    iterations.place(x=450,y=100,height=300)
    iterations.config( command = tree.yview )
    
    

def MethodsWindow(function):
    newWindow = Toplevel(main)
    newWindow.title("Methods")
    newWindow.geometry("800x500")
    newWindow.resizable(False,False)
 
    tabControl = ttk.Notebook(newWindow)
  
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
  
    tabControl.add(tab1, text ='Bisection')
    tabControl.add(tab2, text ='False Postion')
    tabControl.add(tab3, text ='Fixed Point')
    tabControl.add(tab4, text ='Newton Raphson')
    tabControl.add(tab5, text ='Secant')
    tabControl.pack(expand = 1, fill ="both")

    #--------------Bisection--------------
    f_label = ttk.Label(tab1,text ='Function = ' + function,font=("Arial",18)).pack()
    m_i_label = ttk.Label(tab1,text='Enter Max Iterations:')
    e_label = ttk.Label(tab1,text='Enter Epsilon:')
    a_label = ttk.Label(tab1,text='Enter Interval From:')
    b_label = ttk.Label(tab1,text='To')
    max_iteration = ttk.Entry(tab1)
    epsilon = ttk.Entry(tab1)
    a_bis = ttk.Entry(tab1)
    b_bis = ttk.Entry(tab1)
    
    cal_button = ttk.Button(tab1,text='Calculate',command= lambda: callBisection(function,a_bis.get(),b_bis.get(),max_iteration.get(),epsilon.get(),tab1,cal_button))



    m_i_label.pack()
    m_i_label.place(x=40,y=50)
    max_iteration.pack()
    max_iteration.place(x=155,y=50,height=20,width=50)
    e_label.pack()
    e_label.place(x=220,y=50)
    epsilon.pack()
    epsilon.place(x=295,y=50,height=20,width=50)
    a_label.pack()
    a_label.place(x=370,y=50)
    a_bis.pack()
    a_bis.place(x=490,y=50,height=20,width=50)
    b_label.pack()
    b_label.place(x=545,y=50)
    b_bis.pack()
    b_bis.place(x=570,y=50,height=20,width=50)
    cal_button.pack()
    cal_button.place(x=675,y=50)

    #-------------------------------------

    #--------------False Position--------------
    f_label = ttk.Label(tab2,text ='Function = ' + function,font=("Arial",18)).pack()
    m_i_label2 = ttk.Label(tab2,text='Enter Max Iterations:')
    e_label2 = ttk.Label(tab2,text='Enter Epsilon:')
    a_label2 = ttk.Label(tab2,text='Enter Interval From:')
    b_label2 = ttk.Label(tab2,text='To')
    max_iteration2 = ttk.Entry(tab2)
    epsilon2 = ttk.Entry(tab2)
    a2 = ttk.Entry(tab2)
    b2 = ttk.Entry(tab2)
    
    cal_button2 = ttk.Button(tab2,text='Calculate',command= lambda: callFalsePosition(function,a2.get(),b2.get(),max_iteration2.get(),epsilon2.get(),tab2,cal_button2))



    m_i_label2.pack()
    m_i_label2.place(x=40,y=50)
    max_iteration2.pack()
    max_iteration2.place(x=155,y=50,height=20,width=50)
    e_label2.pack()
    e_label2.place(x=220,y=50)
    epsilon2.pack()
    epsilon2.place(x=295,y=50,height=20,width=50)
    a_label2.pack()
    a_label2.place(x=370,y=50)
    a2.pack()
    a2.place(x=490,y=50,height=20,width=50)
    b_label2.pack()
    b_label2.place(x=545,y=50)
    b2.pack()
    b2.place(x=570,y=50,height=20,width=50)
    cal_button2.pack()
    cal_button2.place(x=675,y=50)
    #------------------------------------------

    #--------------Fixed Point--------------
    f_label = ttk.Label(tab3,text ='Function = ' + function,font=("Arial",18)).pack()
    m_i_label3 = ttk.Label(tab3,text='Enter Max Iterations:')
    e_label3 = ttk.Label(tab3,text='Enter Epsilon:')
    a_label3 = ttk.Label(tab3,text='Enter G(x):')
    b_label3 = ttk.Label(tab3,text='Initial guess:')
    max_iteration3 = ttk.Entry(tab3)
    epsilon3 = ttk.Entry(tab3)
    g3 = ttk.Entry(tab3)
    xi3 = ttk.Entry(tab3)
    
    cal_button3 = ttk.Button(tab3,text='Calculate',command= lambda: callFixedPoint(g3.get(),xi3.get(),max_iteration3.get(),epsilon3.get(),tab3,cal_button3))



    m_i_label3.pack()
    m_i_label3.place(x=40,y=50)
    max_iteration3.pack()
    max_iteration3.place(x=155,y=50,height=20,width=50)
    e_label3.pack()
    e_label3.place(x=220,y=50)
    epsilon3.pack()
    epsilon3.place(x=295,y=50,height=20,width=50)
    a_label3.pack()
    a_label3.place(x=370,y=50)
    g3.pack()
    g3.place(x=430,y=50,height=20,width=90)
    b_label3.pack()
    b_label3.place(x=530,y=50)
    xi3.pack()
    xi3.place(x=600,y=50,height=20,width=50)
    cal_button3.pack()
    cal_button3.place(x=675,y=50)
    #---------------------------------------

    #--------------Newton--------------
    f_label = ttk.Label(tab4,text ='Function = ' + function,font=("Arial",18)).pack()
    m_i_label4 = ttk.Label(tab4,text='Enter Max Iterations:')
    e_label4 = ttk.Label(tab4,text='Enter Epsilon:')
    b_label4 = ttk.Label(tab4,text='Initial guess:')
    max_iteration4 = ttk.Entry(tab4)
    epsilon4 = ttk.Entry(tab4)
    xi4 = ttk.Entry(tab4)
    
    cal_button4 = ttk.Button(tab4,text='Calculate',command= lambda: callNewton(function,xi4.get(),max_iteration4.get(),epsilon4.get(),tab4,cal_button4))



    m_i_label4.pack()
    m_i_label4.place(x=40,y=50)
    max_iteration4.pack()
    max_iteration4.place(x=155,y=50,height=20,width=50)
    e_label4.pack()
    e_label4.place(x=220,y=50)
    epsilon4.pack()
    epsilon4.place(x=295,y=50,height=20,width=50)
    b_label4.pack()
    b_label4.place(x=375,y=50)
    xi4.pack()
    xi4.place(x=450,y=50,height=20,width=50)
    cal_button4.pack()
    cal_button4.place(x=675,y=50)
    #----------------------------------

    #--------------Secant--------------
    f_label = ttk.Label(tab5,text ='Function = ' + function,font=("Arial",18)).pack()
    m_i_label5 = ttk.Label(tab5,text='Enter Max Iterations:')
    e_label5 = ttk.Label(tab5,text='Enter Epsilon:')
    a_label5 = ttk.Label(tab5,text='X0:')
    b_label5 = ttk.Label(tab5,text='X1:')
    max_iteration5 = ttk.Entry(tab5)
    epsilon5 = ttk.Entry(tab5)
    a5 = ttk.Entry(tab5)
    b5 = ttk.Entry(tab5)
    
    cal_button5 = ttk.Button(tab5,text='Calculate',command= lambda: callSecant(function,a5.get(),b5.get(),max_iteration5.get(),epsilon5.get(),tab5,cal_button5))



    m_i_label5.pack()
    m_i_label5.place(x=40,y=50)
    max_iteration5.pack()
    max_iteration5.place(x=155,y=50,height=20,width=50)
    e_label5.pack()
    e_label5.place(x=220,y=50)
    epsilon5.pack()
    epsilon5.place(x=295,y=50,height=20,width=50)
    a_label5.pack()
    a_label5.place(x=370,y=50)
    a5.pack()
    a5.place(x=400,y=50,height=20,width=50)
    b_label5.pack()
    b_label5.place(x=455,y=50)
    b5.pack()
    b5.place(x=480,y=50,height=20,width=50)
    cal_button5.pack()
    cal_button5.place(x=675,y=50)
    #----------------------------------

def updateFunction(function,text ):
    function.set(function.get() + str(text))
    function_entry.icursor(len(function.get()))

def test(function):
    try:
        x = 0
        eval(function)
    except SyntaxError:
        label2.pack()
        label2.place(x=300,y=150)
        pass
    else:
        MethodsWindow(function)
    
def open_file(function):
   file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
   if file:
      content = file.readline().replace('\n', '')
      file.close()
      function.set(str(content))

main = Tk()
main.title('Root Finder Program')
main.geometry("500x200")
main.resizable(False,False)

label1 = Label(main,text='Enter Function',font=("Arial",18))
label2 = Label(main,text='Error: Invalid Function', fg='#f00',font=("Arial",13))
equation = tkinter.StringVar()
function_entry = Entry(main,textvariable=equation,font=("Arial",15))

browse_button = Button(main,text='Browse File',command=lambda: open_file(equation))
poly_button = Button(main,text='poly',command=lambda: updateFunction(equation,'x**'))
exp_button = Button(main,text='exp()',command=lambda: updateFunction(equation,'exp('))
cos_button = Button(main,text='cos()',command=lambda: updateFunction(equation,'cos('))
sin_button = Button(main,text='sin()',command=lambda: updateFunction(equation,'sin('))
next_button = Button(main,text='Next',command=lambda: test(function_entry.get()))


label1.pack()
function_entry.pack()
function_entry.place(x=100,y=50,height=30,width=300)
browse_button.pack()
browse_button.place(x=415,y=52)
poly_button.pack()
poly_button.place(x=150,y=100)
exp_button.pack()
exp_button.place(x=200,y=100)
cos_button.pack()
cos_button.place(x=250,y=100)
sin_button.pack()
sin_button.place(x=300,y=100)
next_button.pack()
next_button.place(x=225,y=150)

main.mainloop()