from tkinter import *
from tkinter import messagebox
import glob 

def corpus():
    fichiers = glob.glob(edit1V.get()+'/*.txt')
    textes.delete(0,END)
    textes.insert(END,*fichiers)
    
def clique(evenement):
    selection = evenement.widget.curselection()
    t = open(evenement.widget.get(selection),'r').read()
    contenu.delete('1.0',END)
    contenu.insert(END,t)

#police1 = Font(family='Helvetica', size=36, weight='bold')

def fermerf():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
        f.destroy()

f = Tk()
f.protocol("WM_DELETE_WINDOW", fermerf)
f.title('Analyseur de textes')

edit1V = StringVar()
edit1 = Entry(f,width=30,textvariable=edit1V,font=('Verdana',12))
edit1.grid(column=0,row=0,sticky='we',padx=10,pady=10)

cadre2 = Frame(f)
cadre2.grid(column=1,row=0,sticky='nsew')
boutonA  = Button(cadre2,width=12,text='OK', command=corpus) 
boutonA.grid(column=0,row=0,sticky='w',padx=10,pady=10)
boutonB  = Button(cadre2,width=12,text='OK2') 
boutonB.grid(column=1,row=0,sticky='w',padx=10,pady=10)

#texte    = Text(f,width=40,wrap='word')
#texte.grid(column=0,row=1,sticky='nswe',padx=10,pady=10)
textes = Listbox(f,width=30,relief=RIDGE,borderwidth=4)
textes.grid(column=0,row=1,sticky='nswe',padx=10,pady=10)
textes.bind('<<ListboxSelect>>',clique)

cadre3 = Frame(f)
cadre3.grid(column=1,row=1)
contenu = Text(cadre3,width=40,wrap='word')
contenu.grid(column=0,row=0,sticky='nswe',padx=(10,0),pady=10)
bardef1 = Scrollbar(cadre3,orient=VERTICAL)
bardef1.grid(column=1,row=0,sticky='ns',pady=10)
bardef1.config(command = contenu.yview)
contenu.configure(yscrollcommand=bardef1.set)




cadre = Frame(f,width=150)
cadre.grid(column=2,row=1,sticky='nswe')
boutonCdr1 = Button(cadre,width=12,text='Opération 1')
boutonCdr1.grid(column=0,row=0,sticky='w',padx=(10,10),pady=(10,0))
boutonCdr2 = Button(cadre,width=12,text='Opération 2')
boutonCdr2.grid(column=0,row=1,sticky='w',padx=(10,10),pady=(10,0))


f.columnconfigure(0,weight=1)
f.rowconfigure(1,weight=1)
f.columnconfigure(1,weight=2)

bm = Menu(f)
bm1 = Menu(bm,tearoff=0)
bm1.add_command(label='Ouvrir')
bm1.add_command(label='Quitter', command= f.quit)
bm.add_cascade(label='Fichier', menu= bm1)

f.config(menu=bm)

def fermerf2():
    f2.withdraw()
    



f2 = Toplevel()
f2.protocol("WM_DELETE_WINDOW", fermerf2)
f2.title('Affichage')
# Ici, on crée les composants
f2.withdraw()
f2.deiconify()


f.mainloop()


