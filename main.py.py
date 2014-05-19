#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from random import choice

# ------------ Variables utiles au programme ------------ #

quitter=['quitter', 'arret']
listeQuestion=['Qui est le créateur de PyQuestionnaire ?:Thomas', 'Qui est le créateur de Microsoft ?:Bill Gates', 'Qui est le fondateur de "GNU" ?:Richard Stallman', 'Qui est le créateur d\'Apple ?:Steve Jobs', 'Qui est le "Condor":Kevin Mitnick', 'Donnez l\'acronynme de la communauté de hackers en Allemagne:CCC']



# ------------ Fonctions ------------ #

def lancerPartie():
	nom=nomVariable.get().lower()
	if nom!='' and nom!='saisir ici votre nom':
		echangeTXT.insert(END,'Bienvenue sur PyQuestion {}, une partie est lancée... \n\n'.format(nom.capitalize()))
		genererQuestion()

def about():
	showinfo('About', 'PyQuestionnaire réalisé par Linuxien Barbu')

def genererQuestion():
	global choix 
	choix = choice(listeQuestion)
	question=choix.split (':')[0]
	echangeTXT.insert(END, question)

def verifierReponse():
	reponse=reponseVariable.get().lower()
	if reponse not in quitter:
		if reponse == choix.split(':')[1].lower():
			echangeTXT.insert(END,'\nBonne réponse !\n\n')
			genererQuestion()
		elif reponse =='':
			pass
		else:
			echangeTXT.insert(END, '\nMauvaise réponse !\n\n')

def ouvrirQuestionnaire():
	echangeTXT.delete(0.0,END)
	echangeTXT.insert(END, 'Ouverture du questionnaire "{}"\n\n\n'.format(questionnaireVariable.get().capitalize()))
	del(listeQuestion[:])
	with open(questionnaireVariable.get()+'.txt', 'r') as fichier:
		for ligne in fichier:
			listeQuestion.append(ligne.strip('\n'))
	genererQuestion()




# ------------ Graphical User Interface ------------ #

mainWindow=Tk() # instanciation d'un objet Tkinter
mainWindow.title('PyQuestionnaire') # Attribution  d'un titre
mainWindow.resizable(width=FALSE, height=FALSE) # Empêche l'utilisateur de redéfinir les dimensions de la fenêtre 

# Création d'un menu 

menuConteneur=Menu(mainWindow)
menuFichier=Menu(menuConteneur, tearoff=0)
menuFichier.add_command(label='Quitter', command=mainWindow.destroy)
menuConteneur.add_cascade(label='Fichier', menu=menuFichier)
menuAbout=Menu(menuConteneur, tearoff=0)
menuAbout.add_command(label='About', command=about)
menuConteneur.add_cascade(label='Help', menu=menuAbout)
mainWindow.config(menu=menuConteneur)

# --> Cadre n° 1 : informations  relatives au joueur et bouton pour démarrer une partie

infoFRM=Frame(mainWindow, borderwidth=2, relief=GROOVE)
nomVariable=StringVar()
nomVariable.set('Saisir ici votre nom')

nomLBL=Label(infoFRM, text='Nom du joueur')
nomLBL.grid(row=0, column=0, padx=5, pady=5)
nomETY=Entry(infoFRM, textvariable=nomVariable)
nomETY.grid(row=0, column=1, padx=5, pady=5)
lancerBTN=Button(infoFRM, text='Lancer partie',command=lancerPartie)
lancerBTN.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

infoFRM.grid(row=0, column=0, padx=5, pady=5)

# cadre n°2 : Zone réceptive des questions et réponses 

echangeFRM=Frame(mainWindow, borderwidth=2, relief=GROOVE)
echangeTXT=Text(echangeFRM, width=60, height=30)
echangeTXT.grid(row=0, column=0, padx=5, pady=5)
echangeFRM.grid(row=1, column=0, padx=5, pady=5)

# cadre n°3 : zone dédiée à la saisie des réponse de l'utilisateur 
reponseVariable=StringVar()
reponseVariable.set('Ecrire ici votre réponse')
reponseFRM=Frame(mainWindow, borderwidth=2, relief=GROOVE)
reponseETY=Entry(reponseFRM, textvariable=reponseVariable)
reponseETY.grid(row=0, column=0, padx=5, pady=5)
reponseBTN=Button(reponseFRM, text='Valider réponse', command=verifierReponse)
reponseBTN.grid(row=0, column=1, padx=5, pady=5)

reponseFRM.grid(row=3, column=0, padx=5, pady=5)


# cadre n°4 : changer de questionnaire
questionnaireFRM=Frame(mainWindow, borderwidth=2, relief=GROOVE)
questionnaireVariable=StringVar()
questionnaireETY=Entry(questionnaireFRM, textvariable=questionnaireVariable)
questionnaireETY.grid(row=0, column=0, padx=5, pady=5)
questionnaireBTN=Button(questionnaireFRM, text='Changer questionnaire', command=ouvrirQuestionnaire)
questionnaireBTN.grid(row=0, column=1, padx=5, pady=5)
questionnaireFRM.grid(row=4, column=0, padx=5,pady=5)


mainWindow.mainloop() # boucle réceptive des évènements de l'utilisateur 
