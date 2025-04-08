
from tkinter import *
from tkinter.messagebox import askokcancel

fenetre = Tk()
fenetre.geometry('840x768')
fenetre.resizable(width=False,height=False)
fenetre.maxsize(width=1024,height=768)
titre=Label(fenetre,text="Bienvenue sur la Banque GenMir",fg="black",font=("Times New Romans", 30, "bold"))
titre.place(x=210,y=20)

min_w = 50  # Largeur minimale du cadre
max_w = 200  # Largeur maximale du cadre
cur_width = min_w  # Largeur actuelle du cadre
expanded = False  # Vérifier s'il est complètement étendu

# les differentses photo a inserer pour le depot , retrait et transferer
# image pour le transfert



photo_transfert = PhotoImage(file ="transfert.png")
# image pour le  depot
photo_depot = PhotoImage(file="depot.png")
# image pour le retrait
photo_retrait = PhotoImage(file="retrait.png")
# solde
def fonction_solde():
    frame2 = Frame(fenetre, width=500, heigh=400, bg="blue")
    frame2.place(x=220, y=80)


# declaration de variables
argent = 0
argent_depot = DoubleVar()


    

    # les logos

  

#################
### Settings ####
#################

clair_mode = True
def setting():
    def customize():
        global clair_mode
        if clair_mode:
            clair.config(image=off,bg="black",activebackground="black")
            set_frame.config(bg="black")
            clair_mode=False
        else:
            clair.config(image=on,bg="#f5eeee",activebackground="white")
            set_frame.config(bg="#f5eeee")
            clair_mode=True
    set_frame=Frame(fenetre,bg='#f5eeee', width=700,height=580)
    Label(set_frame,text="Settings",font=("Bold",30)).place(x=0,y=0)
    set_frame.place(x=220,y=80)
    on=PhotoImage(file="light.png")
    off = PhotoImage(file="dark.png")
    clair = Button(set_frame, image=on, bd=0,bg="#f5eeee",activebackground="#f5eeee",command=customize)
    clair.place(x=20,y=80)
    #help_icon = PhotoImage(file='')
    Button(set_frame,bd=1,text="Help",).place(x=20,y=200)

##########
# depot###
##########

def deposer():
    global depot_argent, frame4
    
    
    frame4 = Frame(fenetre, width=600, heigh=400, bg="#7089e9")
    frame4.place(x=220, y=80)
    champ_solde = Label(frame4, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

    lab1 = Label(frame4, text="Veuillez rentrez la somme que vous voulez déposer",
                 font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
    lab1.place(x=60, y=20)
    depot_argent = Entry(frame4, bg="grey", fg="white", width=30, font=("Microsoft YaHei UI Light", 15, "bold"))
    depot_argent.place(x=50, y=100)
    bouton = Button(frame4, text="Valider", bg="#7089e9",border=1, fg="white", font=("Microsoft YaHei UI Light", 13, "bold"),
                    command=afficher_sommedepot)
    bouton.place(x=50, y=150)
    ok = Button(frame4, bd=1, text='Fermer', activebackground='white', bg="#7089e9",
                font=("Microsoft YaHei UI Light", 13, "bold"), fg='white', command=lambda: frame4.destroy())
    ok.place(x=150, y=150)


# cette fonction est appelé après le bouton valider
def afficher_sommedepot():
    global argent
    champ_solde = Label(frame4, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

   
    try:
        montant_depot = float(depot_argent.get())
        argent += montant_depot
        lab1 = Label(frame4, text=f"Vous venez de déposer {montant_depot},\nvotre nouveau solde est {argent}",
                     font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
        lab1.place(x=50, y=200)
    except:
        lab2 = Label(frame4, text=f"Vous n'avez rien deposé ,\nvotre nouveau solde : {argent}",
                     font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
        lab2.place(x=50, y=200)
    depot_argent.delete(0, 'end')  # Effacer le contenu de l'Entry


# retrait
def retirer():
    global frame3, retrait_argent
    champ_solde = Label(frame3, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

    frame3 = Frame(fenetre, width=600, heigh=400, bg="#7089e9")
    frame3.place(x=220, y=80)
    lab1 = Label(frame3, text="Veuillez rentrez la somme que vous voulez retirer",
                 font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
    lab1.place(x=20, y=20)
    retrait_argent = Entry(frame3, bg="grey", fg="white", width=30, font=("Microsoft YaHei UI Light", 15, "bold"))
    retrait_argent.place(x=50, y=100)
    bouton = Button(frame3, text="Valider", bg="#7089e9",fg="white", font=("Microsoft YaHei UI Light", 13, "bold"),
                    command=afficher_sommeretrait)
    bouton.place(x=50, y=150)
    ok = Button(frame3, text='Fermer', activebackground="white", bg="#7089e9",font=("Microsoft YaHei UI Light", 13, "bold"), fg='white', command=lambda: frame3.destroy())
    ok.place(x=150, y=150)


# cette fonction est appélé après validation

def afficher_sommeretrait():
    global argent, montant_retrait
    champ_solde = Label(frame3, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

    try:
        montant_retrait = float(retrait_argent.get())
        argent -= montant_retrait
        if argent >= 0:
            lab1 = Label(frame3, text=f"Vous venez de retirer {montant_retrait},\nvotre nouveau solde est {argent}",
                         font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
            lab1.place(x=50, y=200)
        else:
            lab1 = Label(frame3, text=f"le montant que voulez retirer depasse votre budget",
                         font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
            lab1.place(x=50, y=200)
    except:
        lab2 = Label(frame3, text=f"Vous n'avez rien retiré ,\nvotre nouveau solde : {argent}",
                     font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
        lab2.place(x=50, y=200)
        argent += montant_retrait
    retrait_argent.delete(0, 'end')  # Effacer le contenu de l'Entry


# place a la fonction transferer. c'est du copier collé de retirer
def transferer():
    global frame2, transfert_entree, adresse_entree
    champ_solde = Label(frame2, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

    frame2 = Frame(fenetre, width=600, heigh=400, bg="#7089e9")
    frame2.place(x=220, y=80)
    lab1 = Label(frame2, text="Veuillez  saisir \nle numero du compte du destinaire et la somme",
                 font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
    lab1.place(x=20, y=10)
    adresse_dest = Label(frame2, text="ID destinaire", font=("Microsoft YaHei UI Light", 15, "bold"), fg="white",
                         bg="#7089e9")
    adresse_dest.place(x=50, y=90)
    adresse_entree = Entry(frame2, font=("Microsoft YaHei UI Light", 15, "bold"), fg="white", bg="grey")
    adresse_entree.place(x=190, y=90)
    transfert_argent = Label(frame2, text="somme", font=("Microsoft YaHei UI Light", 15, "bold"), fg="white",
                             bg="#7089e9")
    transfert_argent.place(x=50, y=140)
    transfert_entree = Entry(frame2, font=("Microsoft YaHei UI Light", 15, "bold"), fg="white", bg="grey")
    transfert_entree.place(x=190, y=140)
    bouton = Button(frame2, text="Valider", bd=1,bg="#7089e9", fg="white", font=("Microsoft YaHei UI Light", 13, "bold"),
                    command=afficher_sommetransfert)
    bouton.place(x=190, y=190)
    ok = Button(frame2, bd=1, text='Fermer', activebackground='white', bg='#7089e9',
                font=("Microsoft YaHei UI Light", 13, "bold"), fg='white', command=lambda: frame2.destroy())
    ok.place(x=290, y=190)


# fonction pour afficher la somme après transfert

def afficher_sommetransfert():
    global argent
    champ_solde = Label(frame1, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

   
    try:
        montant_transfert = float(transfert_entree.get())
        argent -= montant_transfert
        if argent >= 0:
            lab1 = Label(frame2,
                         text=f"Vous venez de transférer {montant_transfert},au compte \n{adresse_entree.get()}\nvotre nouveau solde est {argent}",
                         font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
            lab1.place(x=50, y=250)
        else:
            lab1 = Label(frame2, text=f"le montant que voulez \ntransférerr depasse votre budget",
                         font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
            lab1.place(x=50, y=250)
            argent += montant_transfert
    except:
        lab2 = Label(frame2, text=f"Vous n'avez rien retiré ,\nvotre nouveau solde : {argent}",
                     font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9")
        lab2.place(x=50, y=200)
    transfert_entree.delete(0, 'end')  # Effacer le contenu de l'Entry
    adresse_entree.delete(0, 'end')  # Effacer le contenu de l'Entry


def expand():
    global cur_width, expanded
    cur_width += 2 # Augmenter la largeur de 10
    rep = fenetre.after(5, expand)  # Répéter cette fonction toutes les 5 ms
    frame.config(width=cur_width)  # Changer la largeur à la nouvelle largeur augmentée
    if cur_width >= max_w:  # Si la largeur est supérieure à la largeur maximale
        expanded = True  # Le cadre est étendu
        fenetre.after_cancel(rep)  # Arrêter de répéter la fonction
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 6  # Réduire la largeur de 10
    rep = fenetre.after(5, contract)  # Appeler cette fonction toutes les 5 ms
    frame.config(width=cur_width)  # Changer la largeur à la nouvelle largeur réduite
    if cur_width <= min_w:  # Si c'est de retour à la largeur normale
        expanded = False  # Le cadre n'est pas étendu
        fenetre.after_cancel(rep)  # Arrêter de répéter la fonction
        fill()

def fill():
    if expanded:  # Si le cadre est étendu
        # Afficher un texte, et supprimer l'image
        dashboard_b.config(text='Dashboard', image='', font=(0, 21), command=dashborder)
        set_b.config(text='Setting', image='', font=(0, 21),command=setting)
        logout_b.place(x=0, y=fenetre.winfo_height() - 150)
    else:
        # Ramener l'image
        dashboard_b.config(image=dashboard, font=(0, 21))
        set_b.config(image=settings, font=(0, 21))
        logout_b.place_forget()

def Logout():
    rep=askokcancel("Alerte de déconnexion","Souhaitez-vous vraiment quitter ???")
    if rep :
        fenetre.quit()

# fonction pour le dashbord
def dashborder():
    global frame1
    frame1 = Frame(fenetre, width=800, heigh=900, bg="white")
    frame1.place(x=220, y=80)
    # les boutons de depot , retrait
    # label et bouton pour les depots
    label_depot = Label(frame1, text="depot", font=("Microsoft YaHei UI Light", 13, "bold"), width=10, bg="white", fg="black")
    label_depot.place(x=80, y=300)
    bouton_depot = Button(frame1, border=0,image=photo_depot,highlightthickness=0, font=("Microsoft YaHei UI Light", 13, "bold"), fg="white", bg="#7089e9", command=deposer)
    bouton_depot.place(x=100, y=230)
    # label et bouton  pour les retrait
    label_retrait = Label(frame1, text="Retirer", font=("Microsoft YaHei UI Light", 13, "bold"), width=10, bg="white",
                          fg="black")
    label_retrait.place(x=240, y=300)
    bouton_retrait = Button(frame1, image=photo_retrait, border=0,highlightthickness=0, font=("Microsoft YaHei UI Light", 13, "bold"),
                            fg="white", bg="#7089e9", command=retirer)
    bouton_retrait.place(x=260, y=230)
    # labels et boutons pour transférer
    label_transfert = Label(frame1, text="Transférer", font=("Microsoft YaHei UI Light", 13, "bold"), width=10,
                            bg="white", fg="black")
    label_transfert.place(x=407, y=300)
    bouton_transfert = Button(frame1, image=photo_transfert, border=0,highlightthickness=0, font=("Microsoft YaHei UI Light", 13, "bold"),
                              fg="white", bg="#7089e9", command=transferer)
    bouton_transfert.place(x=430, y=230)
    # barre du solde
   
    champ_solde = Label(frame1, width=25, text=f"{argent}$", state='disabled', bg='white', fg='black',
                        font=("Microsoft YaHei UI Light", 30, "bold"))
    champ_solde.place(x=5, y=120)

# Définir les icônes à afficher et les redimensionner
dashboard = PhotoImage(file='dashboard.png')
settings = PhotoImage(file='setting.png')
help_icon = PhotoImage(file='help.png')
transf=PhotoImage(file='help.png')

fenetre.update()  # Pour que la largeur soit mise à jour
frame = Frame(fenetre, bg='#7089e9', width=50, height=fenetre.winfo_height())
frame.place(x=0, y=0)  # Utiliser le gestionnaire de géométrie place

# Créer les boutons avec les icônes à afficher
dashboard_b = Button(frame, image=dashboard,fg="white", bg='#7089e9', relief='flat')
set_b = Button(frame, image=settings,fg="white", bg='#7089e9', relief='flat',command=setting)
logout_b = Button(frame, text='Log-out', compound='left', command=Logout)

# Les placer sur le cadre en utilisant place
dashboard_b.place(x=0, y=70)
set_b.place(x=0, y=125)

# Lier au cadre, si survolé ou quitté
frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())

# Pour qu'il ne dépende pas des widgets à l'intérieur du cadre
frame.grid_propagate(False)

fenetre.mainloop()
