import os
import ctypes
import sys
import tkinter as tk
from tkinter.ttk import *

chemin_script = os.path.dirname(os.path.abspath(__file__))  
chemin_ico_sauvegarde = os.path.join(chemin_script, 'icon_sauvegarde.ico')
chemin_ico_nouvelle_partie = os.path.join(chemin_script, 'icon_nouvelle_partie.ico')
chemin_image_fond = os.path.join(chemin_script, 'image_fond.png')
chemin_ico_combat = os.path.join(chemin_script, 'icon_combat.ico')
chemin_sauvegarde = os.path.join(chemin_script, 'sauvegarde.csv')
chemin_informaticien = os.path.join(chemin_script, 'image_informaticien.png')
chemin_attention = os.path.join(chemin_script, 'image_attention.ico')
chemin_iconphoto = os.path.join(chemin_script, 'image_epee.png')
chemin_fond_ecran_2 = os.path.join(chemin_script, 'image_fond_ecran_sauvegarde.png')

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("mon_application")

if sys.platform == "win32":
    myappid = "mon.application.id"  # Changer pour un ID unique
    os.system(f'powershell -command "[System.Reflection.Assembly]::LoadWithPartialName(\'System.Windows.Forms\') | Out-Null;'
              f'[System.Windows.Forms.Application]::EnableVisualStyles()"')

Sauvegarde_Ligne = []

import csv
Sauvegarde_Reader = open(chemin_sauvegarde, newline='')
spamreader = csv.reader(Sauvegarde_Reader, delimiter=' ', quotechar='|')
try:
    Sauvegarde_Ligne = next(spamreader)
except StopIteration:
    print(".")
Longeur_Sauvegarde_Ligne = len(Sauvegarde_Ligne)

class Infirmier():
    def __init__(self, DNIVEAU = 1, DXP = 0, DARGENT = 1000):
        self.PV = 60
        self.DGT = 10
        self.TITRE = 'Infirmier'
        self.ARGENT = DARGENT
        self.NIVEAU = DNIVEAU
        self.XP = DXP
        self.CAPACITE1 = 'Attaque DDOS'
        self.CAPACITE2 = 'Protection Parefeu'
        self.CAPACITE1_PRIX = 300
        self.CAPACITE2_PRIX = 300
    
    def attaque(self, adversaire):
        Nouveau_PV_Adversaire = adversaire.PV - self.DGT
        if Nouveau_PV_Adversaire < 0:
            Nouveau_PV_Adversaire = 0
        adversaire.PV = Nouveau_PV_Adversaire
    def capacite1(self, adversaire):
        Nouveau_PV_Adversaire = adversaire.PV - 2*self.DGT
        if Nouveau_PV_Adversaire < 0:
            Nouveau_PV_Adversaire = 0
        adversaire.PV = Nouveau_PV_Adversaire
    def capacite2(self, adversaire):
        print('oui')        


class Informaticien():
    def __init__(self, DNIVEAU = 1, DXP = 0, DARGENT = 1000):
        self.PV = 50
        self.DGT = 10
        self.TITRE = 'Informaticien'
        self.ARGENT = DARGENT
        self.NIVEAU = DNIVEAU
        self.XP = DXP
        self.CAPACITE1 = 'Attaque DDOS'
        self.CAPACITE2 = 'Protection Parefeu'
        self.CAPACITE1_PRIX = 300
        self.CAPACITE2_PRIX = 300

class Alchimiste():
    def __init__(self, DNIVEAU = 1, DXP = 0, DARGENT = 1000):
        self.PV = 40
        self.DGT = 20
        self.TITRE = 'Alchimiste'
        self.ARGENT = DARGENT
        self.NIVEAU = DNIVEAU
        self.XP = DXP
        self.CAPACITE1 = 'Attaque DDOS'
        self.CAPACITE2 = 'Protection Parefeu'
        self.CAPACITE1_PRIX = 300
        self.CAPACITE2_PRIX = 300

class Magicien():
    def __init__(self, DNIVEAU = 1, DXP = 0, DARGENT = 1000):
        self.PV = 50
        self.DGT = 20
        self.TITRE = 'Magicien'
        self.ARGENT = DARGENT
        self.NIVEAU = DNIVEAU
        self.XP = DXP
        self.CAPACITE1 = 'Attaque DDOS'
        self.CAPACITE2 = 'Protection Parefeu'
        self.CAPACITE1_PRIX = 300
        self.CAPACITE2_PRIX = 300

class Guerrier():
    def __init__(self, DNIVEAU = 1, DXP = 0, DARGENT = 1000):
        self.PV = 30
        self.DGT = 20
        self.TITRE = 'Guerrier'
        self.ARGENT = DARGENT
        self.NIVEAU = DNIVEAU
        self.XP = DXP
        self.CAPACITE1 = 'Attaque DDOS'
        self.CAPACITE2 = 'Protection Parefeu'
        self.CAPACITE1_PRIX = 300
        self.CAPACITE2_PRIX = 300

#******************
#* Fenêtre Combat *
#******************

def Supprimer_Sauvegarde():
    Root_Confirmation = tk.Tk()
    Root_Confirmation.title('Confirmation')
    Root_Confirmation.iconbitmap(chemin_attention)

    def Confirmer():
        Sauvegarde_Writer2 = open(chemin_sauvegarde, 'w', newline='')
        Writer = csv.writer(Sauvegarde_Writer2,  delimiter=' ')
        Writer.writerow([])
        Root.destroy()
        Root_Confirmation.destroy()

    def Annuler():
        Root_Confirmation.destroy()

    Root_Confirmation_Confirmer_Button = tk.Button(Root_Confirmation, text='Confirmer', command=Confirmer)
    Root_Confirmation_Confirmer_Button.grid(column=1, row=2)
    Root_Confirmation_Annuler_Button = tk.Button(Root_Confirmation, text='Annuler', command=Annuler)
    Root_Confirmation_Annuler_Button.grid(column=3, row=2)
    Root_Confirmation_Label = tk.Label(Root_Confirmation, text='Êtes-vous sûr ?')
    Root_Confirmation_Label.grid(column=2, row=1)
    Root_Confirmation.mainloop()

def Quitter():
    Root.destroy()

def Root_Combat(ancien_menu='Sauvegarde', personnage='Erreur'):
    global Cbt_Image_Fond
    global Sauvegarde_Ligne
    personnages = {
        'Informaticien': Informaticien,
        'Guerrier': Guerrier,
        'Infirmier': Infirmier,
        'Alchimiste': Alchimiste,
    }
    if ancien_menu == 'Nouvelle_Partie':
        Personnage = personnages.get(personnage, Magicien)()
        Sauvegarde_Writer = open(chemin_sauvegarde, 'w', newline='')
        Writer = csv.writer(Sauvegarde_Writer,  delimiter=' ')
        Sauvegarde_Creation = ['0', Pseudo, Personnage.TITRE, Personnage.NIVEAU, Personnage.XP, Personnage.ARGENT]
        Writer.writerow(Sauvegarde_Creation)
        Sauvegarde_Ligne = Sauvegarde_Creation
        Root_NP_ValidationPseudo_Button.destroy()
        Root_NP_ValidationFinale_Button.destroy()
        Root_NP_ChoixPersonnage_Label.destroy()
        Root_NP_Pseudo_Entry.destroy()
        Root_NP_Pseudo_Label.destroy()
        Root_NP_ChoixPersonnage_Button['Infirmier'].destroy()
        Root_NP_ChoixPersonnage_Button['Magicien'].destroy()
        Root_NP_ChoixPersonnage_Button['Informaticien'].destroy()
        Root_NP_ChoixPersonnage_Button['Guerrier'].destroy()
        Root_NP_ChoixPersonnage_Button['Alchimiste'].destroy()
        Root_NP_ChoixPersonnage_IAIGM_Label
        Canvas.delete('lignes')
    elif ancien_menu == 'Sauvegarde':
        Fond_Ecran_Label.destroy()
        Personnage = personnages.get(Sauvegarde_Ligne[2], Magicien)(Sauvegarde_Ligne[3], Sauvegarde_Ligne[4], Sauvegarde_Ligne[5])
        Root_Sauvegarde_Nouvelle_Sauvegarde_Label.destroy()
        Root_Sauvegarde_Nouvelle_Sauvegarde_Button.destroy()
        Root_Sauvegarde_Aucune_Sauvegarde_Label.destroy()
        Root_Sauvegarde_Reprise_Sauvegarde_Button.destroy()

    Root.title(f'Combat | {Sauvegarde_Ligne[1]}')
    Root.iconbitmap(chemin_ico_combat)

    #*************************
    #Zone combat

    Canvas.create_line(0, 300, 800, 300)
    Canvas.create_line(650, 300, 650, 450)
    Canvas.create_line(420, 300, 420, 450)
    Canvas.create_line(0, 350, 420, 350, tags='ligne_avant_combat')

    Cbt_Image_Fond = tk.PhotoImage(file=chemin_image_fond, width=802, height=356)
    Cbt_Image_Fond_Label = tk.Label(Root, image=Cbt_Image_Fond)
    Cbt_Image_Fond_Label.place(x='-2', y='-60')

    def Debut_Combat():
        Cbt_Boutique_Capacite1_Button.config(cursor='arrow', state='disabled')
        Cbt_Boutique_Capacite2_Button.config(cursor='arrow', state='disabled')
        Cbt_Boutique_Label.config(fg='grey')
        Cbt_Boutique_Valider.destroy()
        Cbt_J__Attaque.config(cursor='hand2', state='normal')
        Cbt_J__Capacite1.config(cursor='hand2', state='normal')
        Cbt_J__Capacite2.config(cursor='hand2', state='normal')

    def Initier_Combat():
        global Cbt_Boutique_Valider
        Cbt_Boutique_Capacite1_Button.config(cursor='hand2', state='normal')
        Cbt_Boutique_Capacite2_Button.config(cursor='hand2', state='normal')
        Cbt_Boutique_Label.config(fg='black')
        Cbt_Boutique_Valider = tk.Button(Root, text='Valider', command=Debut_Combat, relief='groove', font=('Helvetica', 11))
        Cbt_Boutique_Valider.place(x='510', y='305')
        Cbt_J__Combat.place_forget()
        Canvas.delete('ligne_avant_combat')
        Canvas.create_line(0, 380, 420, 380, tags='ligne_en_combat')

    Cbt_J__Combat = tk.Button(Root, text='Combat !', command=Initier_Combat, font=('Helvetica', 13, 'bold'), relief='groove', cursor='hand2')
    Cbt_J__Combat.place(x='10', y='360')

    Cbt_J__Attaque = tk.Button(Root, text=f'Attaque ({Personnage.DGT})', font=('Helvetica', 13, 'bold'), relief='groove', state='disabled')
    Cbt_J__Attaque.place(x='10', y='400')

    Cbt_J__Capacite1 = tk.Button(Root, text=f'{Personnage.CAPACITE1}', font=('Helvetica', 13, 'bold'), relief='groove', state='disabled')
    Cbt_J__Capacite1.place(x='122', y='400')

    Cbt_J__Capacite2 = tk.Button(Root, text=f'{Personnage.CAPACITE2}', font=('Helvetica', 13, 'bold'), relief='groove', state='disabled')
    Cbt_J__Capacite2.place(x='252', y='400')

    #**************************
    #Zone Sauvegarde

    Cbt_Sauvegarde_Button = tk.Button(Root, text='Sauvegarder', font=('Helvetica', 13, 'bold'), relief='groove', cursor='hand2')
    Cbt_Sauvegarde_Button.place(x='665', y='400')

    Cbt_Infos_Joueur_Label = tk.Label(Root, text=f'Pseudo : {Sauvegarde_Ligne[1]}\nTitre : {Sauvegarde_Ligne[2]}\nNiveau : {Sauvegarde_Ligne[3]}\nXP : {Sauvegarde_Ligne[4]}/{int(Sauvegarde_Ligne[3])*500}\nArgent : {Sauvegarde_Ligne[5]}$', justify='left')
    Cbt_Infos_Joueur_Label.place(x='665', y='310')

    #***************************
    #Menu

    Cbt_Menu = tk.Menu(Root)
    Cbt_Menu_Parametres = tk.Menu(Cbt_Menu, tearoff=0)
    Cbt_Menu_Parametres.add_command(label='Supprimer Sauv.', command=Supprimer_Sauvegarde)
    Cbt_Menu_Parametres.add_separator()
    Cbt_Menu_Parametres.add_command(label='Sauv. et Quitter')
    Cbt_Menu_Parametres.add_command(label='Quitter', command=Quitter)
    Cbt_Menu.add_cascade(label='Paramètres', underline=0, menu=Cbt_Menu_Parametres)
    Cbt_Menu_Configuration = tk.Menu(Cbt_Menu, tearoff=0)
    Cbt_Menu_Configuration.add_command(label='Pseudo')
    Cbt_Menu.add_cascade(label='Configuration',underline=0, menu=Cbt_Menu_Configuration)
    Root.config(menu=Cbt_Menu)

    #**********************
    #Boutique

    Cbt_Boutique_Label = tk.Label(Root, text='Boutique :', fg='gray', font=('Helvetica', 13))
    Cbt_Boutique_Label.place(x='425', y='307')

    Cbt_Boutique_Capacite1_Button = tk.Button(Root, text=f'{Personnage.CAPACITE1} ({Personnage.CAPACITE1_PRIX}$)', relief='groove', state='disabled', font=('Helvetica', 13, 'bold'))
    Cbt_Boutique_Capacite1_Button.place(x='425', y='350')

    Cbt_Boutique_Capacite2_Button = tk.Button(Root, text=f'{Personnage.CAPACITE2} ({Personnage.CAPACITE2_PRIX}$)', relief='groove', state='disabled', font=('Helvetica', 13, 'bold'))
    Cbt_Boutique_Capacite2_Button.place(x='425', y='410')

    #***********************
    #Info Joueur et Adversaire

    Cbt_IJ_Label = tk.Label(text=f"Infos Joueur : {Personnage.PV} PV, {Personnage.DGT} D'attaque...", font=('Helvetica', 13))
    Cbt_IJ_Label.place(x='25', y='315')

Root = tk.Tk()
iconphoto = tk.PhotoImage(file=chemin_iconphoto)
Root.wm_iconphoto(False, iconphoto)
Canvas = tk.Canvas(Root, width=800, height=450)
Canvas.place(x='0', y='0')

#***************************
#* Fenêtre Nouvelle Partie *
#***************************

Root_NP_ChoixPersonnage_Button = {}

def Nouvelle_Partie():
    global Root_NP_ValidationPseudo_Button
    global Root_NP_ValidationFinale_Button
    global Root_NP_ChoixPersonnage_Label
    global Root_NP_Pseudo_Entry
    global Root_NP_Pseudo_Label
    global Root_NP_ChoixPersonnage_Button
    global Root_NP_ChoixPersonnage_IAIGM_Label

    Fond_Ecran_Label.destroy()
    Root_Sauvegarde_Nouvelle_Sauvegarde_Label.destroy()
    Root_Sauvegarde_Nouvelle_Sauvegarde_Button.destroy()
    Root_Sauvegarde_Aucune_Sauvegarde_Label.destroy()
    if Longeur_Sauvegarde_Ligne != 0:
        Root_Sauvegarde_Reprise_Sauvegarde_Button.destroy()


    def Root_NP_ValidationPseudo_Def():
        global Pseudo
        Pseudo = Root_NP_Pseudo_Entry.get()
        Root_NP_ValidationPseudo_Button.config(bg='lightgreen')

    def modifier_personnage(personnage_ = 'erreur'):
        global Type_Personnage
        Type_Personnage = personnage_
        if Root_NP_ValidationPseudo_Button.cget('bg') == 'lightgreen':
            Root_NP_ValidationFinale_Button.config(bg='lightgreen')

    def Root_NP_ValidationFinale_Def(personnage='erreur'):
        if Root_NP_ValidationFinale_Button.cget('bg') == 'lightgreen': 
            Root_Combat('Nouvelle_Partie', personnage)

    Root_NP_ValidationPseudo_Button = tk.Button(Root, text='Valider', command=Root_NP_ValidationPseudo_Def, font=('Helvetica', 13, 'bold'), relief='groove', cursor='hand2')
    Root_NP_ValidationPseudo_Button.place(x='270', y='77')

    Root_NP_ValidationFinale_Button = tk.Button(Root, text='Valider', command=lambda: Root_NP_ValidationFinale_Def(Type_Personnage), font=('Helvetica', 18, 'bold'), bg='#ff7276', relief='groove', cursor='hand2')
    Root_NP_ValidationFinale_Button.place(x='20', y='380')

    Root.title('Combat | Nouvelle Partie')
    Root.iconbitmap(chemin_ico_nouvelle_partie)

    Root_NP_Pseudo_Label = tk.Label(Root, text='Pseudo :', font=('Helvetica', 25, 'bold'))
    Root_NP_Pseudo_Label.place(x='20', y='20')

    def valider_texte(saisie):
        return len(saisie) <= 10

    vcmd = Root.register(valider_texte)

    Root_NP_Pseudo_Entry = tk.Entry(Root, font=('Helvetica', 14), validate="key", validatecommand=(vcmd, "%P"))
    Root_NP_Pseudo_Entry.place(x='25', y='80')

    Root_NP_ChoixPersonnage_Label = tk.Label(Root, text='Choisissez votre personnage :', font=('Helvetica', 25, 'bold'))
    Root_NP_ChoixPersonnage_Label.place(x='20', y='125')

    Root_NP_ChoixPersonnage_Button['Informaticien'] = tk.Button(Root, command=lambda: [Root_NP_ChoixPersonnage_UpdateColor('Informaticien'), modifier_personnage('Informaticien')], text='Informaticien', relief='groove', cursor='hand2', font=('Helvetica', 13, 'bold'))
    Root_NP_ChoixPersonnage_Button['Informaticien'].place(x='25', y='180')
    Root_NP_ChoixPersonnage_IAIGM_Label = tk.Label(Root, text='- Attaque DDOS\n- Protection Parefeu', justify='left')
    Root_NP_ChoixPersonnage_IAIGM_Label.place(x='25', y='220')

    Root_NP_ChoixPersonnage_Button['Alchimiste'] = tk.Button(Root, command=lambda: [Root_NP_ChoixPersonnage_UpdateColor('Alchimiste'), modifier_personnage('Alchimiste')], text='Alchimiste', relief='groove', cursor='hand2', font=('Helvetica', 13, 'bold'))
    Root_NP_ChoixPersonnage_Button['Alchimiste'].place(x='160', y='180')
    Root_NP_ChoixPersonnage_IAIGM_Label = tk.Label(Root, text='- Potion Regen\n- Potion attaque', justify='left')
    Root_NP_ChoixPersonnage_IAIGM_Label.place(x='160', y='220')

    Root_NP_ChoixPersonnage_Button['Infirmier'] = tk.Button(Root, command=lambda: [Root_NP_ChoixPersonnage_UpdateColor('Infirmier'), modifier_personnage('Infirmier')], text='Infirmier', relief='groove', cursor='hand2', font=('Helvetica', 13, 'bold'))
    Root_NP_ChoixPersonnage_Button['Infirmier'].place(x='276', y='180')
    Root_NP_ChoixPersonnage_IAIGM_Label = tk.Label(Root, text='- Regen Ultra', justify='left')
    Root_NP_ChoixPersonnage_IAIGM_Label.place(x='276', y='220')

    Root_NP_ChoixPersonnage_Button['Guerrier'] = tk.Button(Root, command=lambda: [Root_NP_ChoixPersonnage_UpdateColor('Guerrier'), modifier_personnage('Guerrier')], text='Guerrier', relief='groove', cursor='hand2', font=('Helvetica', 13, 'bold'))
    Root_NP_ChoixPersonnage_Button['Guerrier'].place(x='378', y='180')
    Root_NP_ChoixPersonnage_IAIGM_Label = tk.Label(Root, text='- Bouclier Ultra', justify='left')
    Root_NP_ChoixPersonnage_IAIGM_Label.place(x='378', y='220')

    Root_NP_ChoixPersonnage_Button['Magicien'] = tk.Button(Root, command=lambda: [Root_NP_ChoixPersonnage_UpdateColor('Magicien'), modifier_personnage('Magicien')], text='Magicien', relief='groove', cursor='hand2', font=('Helvetica', 13, 'bold'))
    Root_NP_ChoixPersonnage_Button['Magicien'].place(x='482', y='180')
    Root_NP_ChoixPersonnage_IAIGM_Label = tk.Label(Root, text='?', justify='left')
    Root_NP_ChoixPersonnage_IAIGM_Label.place(x='482', y='220')

    Canvas.create_line(150, 180, 150, 350, tags='lignes')
    Canvas.create_line(265, 180, 265, 350, tags='lignes')
    Canvas.create_line(366, 180, 366, 350, tags='lignes')
    Canvas.create_line(469, 180, 469, 350, tags='lignes')

Dictionnaire_Couleur_Personnage = {
    'Informaticien': 'lightgreen',
    'Guerrier': '#638ecb',
    'Infirmier': '#ff7276',
    'Alchimiste': '#f1b04c',
    'Magicien': '#ca5cdd'
}

def Root_NP_ChoixPersonnage_UpdateColor(personnage):
    for btn in Root_NP_ChoixPersonnage_Button.values():
        btn.config(bg='SystemButtonFace') 

    if personnage in Root_NP_ChoixPersonnage_Button:
        Root_NP_ChoixPersonnage_Button[personnage].config(bg=Dictionnaire_Couleur_Personnage[personnage])
    

#**********************
#* Fenêtre Sauvegarde *
#**********************

Root.title('Combat | Sauvegarde')
Root.iconbitmap(chemin_ico_sauvegarde)
Root.resizable(False, False)
Root.geometry('800x450')

Fond_ecran = tk.PhotoImage(file=chemin_fond_ecran_2, width=805, height=455)
Fond_Ecran_Label = tk.Label(Root, image=Fond_ecran)
Fond_Ecran_Label.place(x='-2', y='-2')



if Longeur_Sauvegarde_Ligne != 0:
    Root_Sauvegarde_Aucune_Sauvegarde_Label = tk.Label(Root, text='1 Sauvegarde détectée', font=('Helvetica', 11, 'bold'))
    Root_Sauvegarde_Aucune_Sauvegarde_Label.place(x='0', y='430')

    Root_Sauvegarde_Nouvelle_Sauvegarde_Label = tk.Label(Root, text='Sauvegarde :', font=('Helvetica', 25, 'bold'))
    Root_Sauvegarde_Nouvelle_Sauvegarde_Label.place(x='20', y='150')

    Root_Sauvegarde_Reprise_Sauvegarde_Button = tk.Button(Root, command=Root_Combat, text=f'{Sauvegarde_Ligne[1]}', relief='groove', cursor='hand2', font=('Helvetica', 25, 'bold'))
    Root_Sauvegarde_Reprise_Sauvegarde_Button.place(x='25', y='200')

    Decal_Pseudo = 0
    Longeur_Pseudo = len(Sauvegarde_Ligne[1])
    if Longeur_Pseudo > 7:
        Decal_Pseudo += Longeur_Pseudo - 7 

    def get_pseudo_button_position():
        global Root_Sauvegarde_Reprise_Sauvegarde_Button
        global Root_Sauvegarde_Nouvelle_Sauvegarde_Button
        Root_Sauvegarde_Nouvelle_Sauvegarde_Button = tk.Button(Root, command=Nouvelle_Partie, text='+', relief='groove', cursor='hand2', font=('Helvetica', 25, 'bold'))
        Root_Sauvegarde_Nouvelle_Sauvegarde_Button.place(x=f'{Root_Sauvegarde_Reprise_Sauvegarde_Button.winfo_x()+Root_Sauvegarde_Reprise_Sauvegarde_Button.winfo_width()+20}', y='200')

    Root.after(100, get_pseudo_button_position) 
else:
    Root_Sauvegarde_Aucune_Sauvegarde_Label = tk.Label(Root, text='Aucune sauvegarde détectée...', font=('Helvetica', 11, 'bold'))
    Root_Sauvegarde_Aucune_Sauvegarde_Label.place(x='0', y='430')

    Root_Sauvegarde_Nouvelle_Sauvegarde_Label = tk.Label(Root, text='Nouvelle sauvegarde ?', font=('Helvetica', 25, 'bold'))
    Root_Sauvegarde_Nouvelle_Sauvegarde_Label.place(x='20', y='150')

    Root_Sauvegarde_Nouvelle_Sauvegarde_Button = tk.Button(Root, command=Nouvelle_Partie, text='+', relief='groove', cursor='hand2', font=('Helvetica', 25, 'bold'))
    Root_Sauvegarde_Nouvelle_Sauvegarde_Button.place(x='25', y='200')

dictionnaire_niveaux = {
    1:500,
    2:1000,
    3:1500
}

Root.mainloop()