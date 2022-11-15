from tkinter import *
def fat(n):
    if n == 0:
        f=1
        return f  
    elif n<0:
        return "não pode numero negativo"
    else:
        f = 1
        for c in range(n, 0, -1):
            f*=c
        return f

def pers(n):
    return fat(n)

def perr(n,a=0,b=0,c=0):
    if n < 0 or a < 0 or b < 0 or c < 0 or n<a+b+c:
        return "valores negativos ou as repetições são maiores que N"
    else:
        return int(fat(n)/((fat(a))*(fat(b))*(fat(c))))

def comb(n,k):
    if n<0 or k<  0 or n-k < 0:
        return "valores negativos ou P maior que N"
    else:
        return fat(n)/((fat(k)*fat(n-k)))
def arran(n,k):
    if n <0 or k < 0 or n-k < 0:
        return "valores negativos ou P é maior que N"
    else:
        return fat(n)/(fat(n-k))
        

root = Tk()

class Application():
    def __init__(self):
       self.root = root
       self.tela()
       self.frames_tela()
       self.widgets()
       root.mainloop() 
    def tela(self):
        self.root.title("Analise conbinatoria.")
        self.root.configure(background='#B0E0E6')
        self.root.geometry("1080x720")
        self.root.resizable(True,True)
    def frames_tela(self):
        self.frame = Frame(self.root,bd="4",bg="#F5FFFA")
        self.frame.place(relx=0.1,rely=0.08,relwidth=0.8 ,relheight=0.99)
    def widgets(self):        
               
        # permutação simples 
        def permsimples():
            n = self.lb_perms.get()
            try:
                n = int(n)
                try:
                    self.a = Label(self.frame,text= f'a permutação é {int(fat(n))}',  bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.07,relwidth=0.9,relheight=0.05)
                except:
                    self.a = Label(self.frame,text= f'{fat(n)}', bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.07,relwidth=0.9,relheight=0.05)
            except:
                self.a = Label(self.frame,text= f'valores invalidos ou nulos', bd="4",bg="#F5FFFA",font="arial 10 ")
                self.a.place(relx=0.155,rely=0.07,relwidth=0.9,relheight=0.05)
                
        self.lb_permsimples = Label(self.frame,text='P',bd="4",bg="#F5FFFA",font="arial 40 ")
        self.lb_permsimples.place(relx=0.0,rely=0.0,relwidth=0.1,relheight=0.1)  
        
        self.lb_permsimplesN = Label(self.frame,text='n =',bd="4",bg="#F5FFFA",font="arial 20 ")
        self.lb_permsimplesN.place(relx=0.05,rely=0.07,relwidth=0.05,relheight=0.05)
        
        self.lb_perms = Entry(self.frame,background="#F5FFFA",font="arial 20")
        self.lb_perms.place(relx=0.1,rely=0.07,relwidth=0.05,relheight=0.05) 
        
        self.bt_calcular = Button(self.frame,text="Calcular",command=permsimples)
        self.bt_calcular.place(relx=0.8,rely=0.0,relwidth=0.09,relheight=0.02)
        
        
        
        #permutação com repetição 
        
        def permRepeticao():
            n,a,b,c = self.lb_permrepeticaoN.get(), self.lb_permrepeticaoA.get(),           self.lb_permrepeticaoB.get(), self.lb_permrepeticaoC.get()
            try:
                n = int(n)
                try : 
                    a = int(a) 
                    if a == 1:
                        a=0
                except: a = 0
                
                try : 
                    b = int(b) 
                    if b == 1:
                        b=0
                except: b = 0
                
                try : 
                    c = int(c) 
                    if c == 1:
                        c=0
                except: c = 0
                
                try:
                    self.a = Label(self.frame,text= f'a permutação é {int(perr(n,a,b,c))}', bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.28,relwidth=0.9,relheight=0.05)  
        
                except:
                    self.a = Label(self.frame,text= f'{perr(n,a,b,c)}',          bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.28,relwidth=0.9,relheight=0.05)
            except:
                self.a = Label(self.frame,text= f'valores invalidos ou nulos',bd="4",bg="#F5FFFA",font="arial 10 ")
                self.a.place(relx=0.155,rely=0.28,relwidth=0.9,relheight=0.05)
        
        self.lb_permrepeticao = Label(self.frame,text='P',bd="4",bg="#F5FFFA",font="arial 40 ")
        self.lb_permrepeticao.place(relx=0.0,rely=0.20,relwidth=0.1,relheight=0.1)  
        
        self.lb_permrepeticaoNl = Label(self.frame,text='n =',bd="4",bg="#F5FFFA",font="arial 20 ")
        self.lb_permrepeticaoNl.place(relx=0.05,rely=0.28,relwidth=0.05,relheight=0.05)
        
        self.lb_permrepeticaoN = Entry(self.frame,background="#F5FFFA",font="arial 20")
        self.lb_permrepeticaoN.place(relx=0.095,rely=0.28,relwidth=0.05,relheight=0.05)
        
        self.lb_permrepeticaoAl = Label(self.frame,text='a=',bd="4",bg="#F5FFFA",font="arial 15 ")
        self.lb_permrepeticaoAl.place(relx=0.07,rely=0.19,relwidth=0.05,relheight=0.05)  
        
        self.lb_permrepeticaoA = Entry(self.frame,background="#F5FFFA",font="arial 10")
        self.lb_permrepeticaoA.place(relx=0.11,rely=0.20,relwidth=0.03,relheight=0.03)
        
        self.lb_permrepeticaoBl = Label(self.frame,text='b=',bd="4",bg="#F5FFFA",font="arial 15 ")
        self.lb_permrepeticaoBl.place(relx=0.14,rely=0.19,relwidth=0.05,relheight=0.05)
        
        self.lb_permrepeticaoB = Entry(self.frame,background="#F5FFFA",font="arial 10")
        self.lb_permrepeticaoB.place(relx=0.18,rely=0.20,relwidth=0.03,relheight=0.03)
        
        self.lb_permrepeticaoCl = Label(self.frame,text='c=',bd="4",bg="#F5FFFA",font="arial 15 ")
        self.lb_permrepeticaoCl.place(relx=0.21,rely=0.19,relwidth=0.05,relheight=0.05)
        
        self.lb_permrepeticaoC = Entry(self.frame,background="#F5FFFA",font="arial 10")
        self.lb_permrepeticaoC.place(relx=0.25,rely=0.20,relwidth=0.03,relheight=0.03)
        
        self.bt_calcularPR = Button(self.frame,text="Calcular",command=permRepeticao)
        self.bt_calcularPR.place(relx=0.8,rely=0.19,relwidth=0.09,relheight=0.02)

        #combinação simples  
        def combinação():
            n = self.lb_combCE.get()
            p = self.lb_combPE.get()
            try:
                n = int(n)
                p = int(p)
                try:
                    self.a = Label(self.frame,text= f'a permutação é {int(comb(n, p))}',  bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.48,relwidth=0.9,relheight=0.05)
                except:
                    self.a = Label(self.frame,text= f'{comb(n, p)}', bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.48,relwidth=0.9,relheight=0.05)
            except:
                self.a = Label(self.frame,text= f'valores invalidos ou nulos', bd="4",bg="#F5FFFA",font="arial 10 ")
                self.a.place(relx=0.155,rely=0.48,relwidth=0.9,relheight=0.05)
        
    
        self.lb_combC = Label(self.frame,text='C',bd="4",bg="#F5FFFA",font="arial 40 ")
        self.lb_combC.place(relx=0.0,rely=0.40,relwidth=0.1,relheight=0.1)  
        
        self.lb_combN = Label(self.frame,text='n =',bd="4",bg="#F5FFFA",font="arial 20 ")
        self.lb_combN.place(relx=0.05,rely=0.48,relwidth=0.05,relheight=0.05)
        
        self.lb_combP = Label(self.frame,text='p=',bd="4",bg="#F5FFFA",font="arial 15 ")
        self.lb_combP.place(relx=0.07,rely=0.39,relwidth=0.05,relheight=0.05)  
        
        self.lb_combPE = Entry(self.frame,background="#F5FFFA",font="arial 10")
        self.lb_combPE.place(relx=0.11,rely=0.40,relwidth=0.03,relheight=0.03)
        
        self.lb_combCE = Entry(self.frame,background="#F5FFFA",font="arial 20")
        self.lb_combCE.place(relx=0.095,rely=0.48,relwidth=0.05,relheight=0.05)
        
        self.bt_calcularC = Button(self.frame,text="Calcular",command=combinação)
        self.bt_calcularC.place(relx=0.8,rely=0.39,relwidth=0.09,relheight=0.02)
        
        
         #arranjo simples  
        def arranjo():
            n = self.lb_arrbNE.get()
            p = self.lb_arrbPE.get()
            try:
                n = int(n)
                p = int(p)
                try:
                    self.a = Label(self.frame,text= f'a permutação é {int(arran(n, p))}',  bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.68,relwidth=0.9,relheight=0.05)
                except:
                    self.a = Label(self.frame,text= f'{arran(n, p)}', bd="4",bg="#F5FFFA",font="arial 10 ")
                    self.a.place(relx=0.155,rely=0.68,relwidth=0.9,relheight=0.05)
            except:
                self.a = Label(self.frame,text= f'valores invalidos ou nulos', bd="4",bg="#F5FFFA",font="arial 10 ")
                self.a.place(relx=0.155,rely=0.68,relwidth=0.9,relheight=0.05)
            
            
            
        self.lb_arrbA = Label(self.frame,text='A',bd="4",bg="#F5FFFA",font="arial 40 ")
        self.lb_arrbA.place(relx=0.0,rely=0.60,relwidth=0.1,relheight=0.1)  
        
        self.lb_arrbN = Label(self.frame,text='n =',bd="4",bg="#F5FFFA",font="arial 20 ")
        self.lb_arrbN.place(relx=0.05,rely=0.68,relwidth=0.05,relheight=0.05)
        
        self.lb_arrbP = Label(self.frame,text='p=',bd="4",bg="#F5FFFA",font="arial 15 ")
        self.lb_arrbP.place(relx=0.07,rely=0.59,relwidth=0.05,relheight=0.05)  
        
        self.lb_arrbPE = Entry(self.frame,background="#F5FFFA",font="arial 10")
        self.lb_arrbPE.place(relx=0.11,rely=0.60,relwidth=0.03,relheight=0.03)
        
        self.lb_arrbNE = Entry(self.frame,background="#F5FFFA",font="arial 20")
        self.lb_arrbNE.place(relx=0.095,rely=0.68,relwidth=0.05,relheight=0.05)
        
        self.bt_calcularA = Button(self.frame,text="Calcular",command=arranjo)
        self.bt_calcularA.place(relx=0.8,rely=0.59,relwidth=0.09,relheight=0.02)
         
         
         
         
        
Application()