#"Que nul n'entre ici s'il n'est géomètre" Platon, phrase gravée sur le fronton de l'Académie
"""Le Rubik's Cube"""


##Avis au lecteur: 
#Cher lecteur, vous vous aventurez ici dans un abîme insondable dont vous finirez peut être par en comprendre les moindres details, quelques rares sanctuaires (à vous d'en découvrir le nombre) ont été placés de telle manière à vous redonner de l'espoir car oui, il en faudra une quantité non négligeable. En voici un pour commencer:
#“Même sans espoir, la lutte est encore un espoir.” Romain Rolland, normalien du XIXe siècle
##Avis au lecteur souhaitant s'équiper pour ce périple:
#Corde de rappel: https://www.francocube.com/notation   #Strict minimum
#Connaissances de l'abîme: https://www.youtube.com/watch?v=k2rpG2yluzc&list=PL6fjca_ti7_AwfmtGzkR0PpoStaaVlDpc (série de 6 vidéos sur la methode Old Pochmann dite méthode Blind ou Blindfolded(à l'aveugle, car oui, il est possible de résoudre cet objet mystêrieux sans même le regarder))
#Casque: https://www.youtube.com/watch?v=pj_IsOCJS3k                    #Methode Roux partie 1 (cf ligne 1650 )
#Descendeur: https://www.youtube.com/watch?v=sfXOhSVoQHk                #Methode Roux partie 2
#Baudrier: https://www.youtube.com/watch?v=s86uyYftEaE                  #Methode Roux partie 3
#Mousqueton:  https://www.youtube.com/watch?v=YL55b8FljnE               #Methode Roux partie 4
#Et bien sur, un Rubik's Cube est fortement recommandé.
##Avis au lecteur ne souhaitant pas s'équiper:
#Bonne chance

#C'est ici que tout commence.
from numpy import *

#6 matrices: (R,V,O,Blanc,J,Bleu) 6 coefficients par case 
#18 mouvements: 2*9 (U,R,L,D,F,B,M,E,S) et leurs '
#1:rouge
#2:vert
#3:orange
#4:bleu
#5:jaune
#6:blanc

#cube résolu:
spec=array([[1,2,3],[4,5,6],[7,8,9]])
R=array([[1,1,1],[1,1,1],[1,1,1]])
V=array([[2,2,2],[2,2,2],[2,2,2]])
O=array([[3,3,3],[3,3,3],[3,3,3]])
Bleu=array([[4,4,4],[4,4,4],[4,4,4]])
J=array([[5,5,5],[5,5,5],[5,5,5]])
Blanc=array([[6,6,6],[6,6,6],[6,6,6]])
Cube=[R,V,O,Bleu,J,Blanc]
##
##                                         RESOLU
def resolu(Cube):   #Aprouvé par la science
    R,V,O,Bleu,J,Blanc=array([[1,1,1],[1,1,1],[1,1,1]]),array([[2,2,2],[2,2,2],[2,2,2]]),array([[3,3,3],[3,3,3],[3,3,3]]),array([[4,4,4],[4,4,4],[4,4,4]]),array([[5,5,5],[5,5,5],[5,5,5]]),array([[6,6,6],[6,6,6],[6,6,6]])
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    if all(Left==R) and all(Front==V) and all(Right==O) and all(Back==Bleu) and all(Up==J) and all(Down==Blanc) :
        return(True)
    return(False)
#print(resolu([R,V,O,Bleu,J,Blanc]))
##
##                                    LES MOUVEMENTS
def MouvU(Cube):    #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[0][i]=F[0][i]
        Front[0][i]=R[0][i]
        Right[0][i]=B[0][i]
        Back[0][i]=L[0][i]
        for j in range(3):  #rotation horaire
            Up[i][j]=U[2-j][i]
    return(Cube)
    
    
    
def MouvU1(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[0][i]=B[0][i]
        Front[0][i]=L[0][i]
        Right[0][i]=F[0][i]
        Back[0][i]=R[0][i]
        for j in range(3):  #rotation trigo
            Up[i][j]=U[j][2-i]
    return(Cube)



def MouvL(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Down[i][0]=F[i][0]
        Front[i][0]=U[i][0]
        Up[i][0]=B[2-i][2]
        Back[i][2]=D[2-i][0]
        for j in range(3):  #sens horaire
            Left[i][j]=L[2-j][i]
    return(Cube)
    
    
    
def MouvL1(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Down[i][0]=B[2-i][2]
        Front[i][0]=D[i][0]
        Up[i][0]=F[i][0]
        Back[i][2]=U[2-i][0]
        for j in range(3):  #sens trigo
            Left[i][j]=L[j][2-i]
    return(Cube)



def MouvD(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[2][i]=B[2][i]
        Front[2][i]=L[2][i]
        Right[2][i]=F[2][i]
        Back[2][i]=R[2][i]
        for j in range(3):
            Down[i][j]=D[2-j][i]
    return(Cube)



def MouvD1(Cube):    #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[2][i]=F[2][i]
        Front[2][i]=R[2][i]
        Right[2][i]=B[2][i]
        Back[2][i]=L[2][i]
        for j in range(3):
            Down[i][j]=D[j][2-i]
    return(Cube)



def MouvR(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Down[i][2]=B[2-i][0]
        Front[i][2]=D[i][2]
        Up[i][2]=F[i][2]
        Back[i][0]=U[2-i][2]
        for j in range(3):   #sens horaire des 3
            Right[i][j]=R[2-j][i]
    return(Cube)



def MouvR1(Cube):   #Aprouvé par la science    
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Down[i][2]=F[i][2]
        Front[i][2]=U[i][2]
        Up[i][2]=B[2-i][0]
        Back[i][0]=D[2-i][2]
        for j in range(3):   #sens trigo des 3
            Right[i][j]=R[j][2-i]
    return(Cube)
    


def MouvF(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Right[i][0]=U[2][i]
        Down[0][i]=R[2-i][0]
        Left[i][2]=D[0][i]
        Up[2][i]=L[2-i][2]
        for j in range(3):   #sens horaire des 2
            Front[i][j]=F[2-j][i]
    return(Cube)



def MouvF1(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Right[i][0]=D[0][2-i]
        Down[0][i]=L[i][2]
        Left[i][2]=U[2][2-i]
        Up[2][i]=R[i][0]
        for j in range(3):   #sens trigo des 2
            Front[i][j]=F[j][2-i]
    return(Cube)



def MouvB(Cube):   #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[i][0]=U[0][2-i]
        Down[2][i]=L[i][0]
        Right[i][2]=D[2][2-i]
        Up[0][i]=R[i][2]
        for j in range(3):   #sens horaire des 4
            Back[i][j]=B[2-j][i]
    return(Cube)
    
    
    
def MouvB1(Cube):   #Aprouvé par la science    
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[i][0]=D[2][i]
        Down[2][i]=R[2-i][2]
        Right[i][2]=U[0][i]
        Up[0][i]=L[2-i][0]
        for j in range(3):   #sens horaire des 4
            Back[i][j]=B[j][2-i]
    return(Cube)



def MouvE(Cube):        #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[1][i]=B[1][i]
        Front[1][i]=L[1][i]
        Right[1][i]=F[1][i]
        Back[1][i]=R[1][i]
    return(Cube)



def MouvE1(Cube):       #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[1][i]=F[1][i]
        Front[1][i]=R[1][i]
        Right[1][i]=B[1][i]
        Back[1][i]=L[1][i]
    return(Cube)
    


def MouvM(Cube):    #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Up[i][1]=B[2-i][1]
        Front[i][1]=U[i][1]
        Down[i][1]=F[i][1]   
        Back[i][1]=D[2-i][1]
    return(Cube)



def MouvM1(Cube):    #Aprouvé par la science
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Up[i][1]=F[i][1]
        Front[i][1]=D[i][1]
        Down[i][1]=B[2-i][1]
        Back[i][1]=U[2-i][1]
    return(Cube)
    
    
    
def MouvS(Cube):    
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[i][1]=D[1][i]
        Up[1][i]=L[2-i][1]
        Right[i][1]=U[1][i]
        Down[1][i]=R[2-i][1]
    return(Cube)
    
    
    
def MouvS1(Cube):  
    Left,Front,Right,Back,Up,Down=Cube[0],Cube[1],Cube[2],Cube[3],Cube[4],Cube[5]
    L,F,R,B,U,D=copy(Left),copy(Front),copy(Right),copy(Back),copy(Up),copy(Down)
    for i in range(3):
        Left[i][1]=U[1][2-i]
        Up[1][i]=R[i][1]
        Right[i][1]=D[1][2-i]
        Down[1][i]=L[i][1]
    return(Left,Front,Right,Back,Up,Down)
    
    
#print(MouvU(R,V,O,Bleu,J,Blanc)) #testeur: demander le mouvement voulu, la matrice cube resultant souhaitée, et spec=N


def x(Cube):    #Equivalent à R
    Cube=MouvR(MouvM1(MouvL1(Cube)))
    return(Cube)


def x1(Cube):   #Equivalent à r
    Cube=MouvR1(MouvM(MouvL(Cube)))
    return(Cube)
    
    
def y(Cube):    #Equivalent à U
    Cube=MouvU(MouvE1(MouvD1(Cube)))
    return(Cube)
    
    
def y1(Cube):   #Equivalent à u
    Cube=MouvU1(MouvE(MouvD(Cube)))
    return(Cube)
    
    
def z(Cube):    #Equivalent à F
    Cube=MouvF(MouvS(MouvB1(Cube)))
    return(Cube)
    
    
def z1(Cube):   #Equivalent à f
    Cube=MouvF1(MouvS1(MouvB(Cube)))
    return(Cube)



def MouvX(X,Cube):    #Fonction extrêmement utile, regroupe tous les mouvements possibles, la notation en  minuscule correspond au mouvement reciproque ( r equivaut à R' ), choix de simplicité puisque "r" compte pour un seul caractère dans une chaine alors que R' ou R1 compte pour 2
    if X=="U":
        return(MouvU(Cube))
    if X=="u":
        return(MouvU1(Cube))
    if X=="R":
        return(MouvR(Cube))
    if X=="r":
        return(MouvR1(Cube))
    if X=="D":
        return(MouvD(Cube))
    if X=="d":
        return(MouvD1(Cube))
    if X=="L":
        return(MouvL(Cube))
    if X=="l":
        return(MouvL1(Cube))
    if X=="F":
        return(MouvF(Cube))
    if X=="f":
        return(MouvF1(Cube))
    if X=="B":
        return(MouvB(Cube))
    if X=="b":
        return(MouvB1(Cube))
    if X=="M":
        return(MouvM(Cube))
    if X=="m":
        return(MouvM1(Cube))
    if X=="E":
        return(MouvE(Cube))
    if X=="e":
        return(MouvE1(Cube))
    if X=="S":
        return(MouvS(Cube))
    if X=="s":
        return(MouvS1(Cube))
    if X=="X":
        return(x(Cube))
    if X=="x":
        return(x1(Cube))
    if X=="Y":
        return(y(Cube))
    if X=="y":
        return(y1(Cube))
    if X=="Z":
        return(z(Cube))
    if X=="z":
        return(z1(Cube))
    if X=="":
        return(Cube)
        
        

##
##                                      FORMULES
#Vous pouvez toujours essayez de comprendre ces nomenclatures exotiques par rapport à leur influence sur le rubik's cube mais il est grandement conseillé de tester par soi même les formules, et ainsi de comprendre clairement leur impact sur le cube, ce passage reste cependant peu interessant mais requis pour simplifier grandement les notations futures (bien que la nomemclature des fonctions soit, certe très intuitive pour l'auteur, mais très peu pour vous, lecteur découvrant pas à pas ( ou plutot page à page) ce programme. Ne cherchez en aucun cas une explication sur le net aux noms donnés, ils ont été crées sur mesure et sont probablement unique au monde.

def Requin_Droit(Cube): #(L1 U1 L U1 L1 U1 U1 L) (R U R1 U R U U R1)  #Aprouvé
    L="luLuluuLRUrURUUr"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Requin_Gauche(Cube): #(R U R1 U R U U R1)  (L1 U1 L U1 L1 U1 U1 L) #Aprouvé
    L="RUrURUUrluLuluuL"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Kangourou_Droit(Cube): #(R U U R1 U1 R U1 R1) (L1 U1 U1 L U L1 U L) #Aprouvé
    L="RUUruRurluuLUlUL"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Kangourou_Gauche(Cube): # (L1 U1 U1 L U L1 U L)(R U U R1 U1 R U1 R1) #Aprouvé
    L="luuLUlULRUUruRur"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Switch(Cube): #(M1 U1 M1 U1 M1 U1 U1) (M U1 M U1 M U1 U1) #Aprouvé 
    L="mumumuuMuMuMuu"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
    
    
def Riviere_Droite(Cube): #nouvelle (RR U1 R1 U1 RURUR U1 R)       celle d'avant(RRURUR1U1R1U1R1UR1)   #Aprouvé 
    L="RRuruRURURuR"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
    #Ancienne
    L="RRURUrururUr"
    for i in L:
        MouvX(i,Cube)
    return(Cube)
    
    
#"La liberté ne peut être limitée que par la liberté." Rawls


def Riviere_Gauche(Cube): #nouvelle (R1 U R1 U1 R1 U1 R1 URU RR)  celle d'avant(RU1RURURU1R1U1RR)    #Aprouvé 
    L="rUrururURURR"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
    #Ancienne :
    L="RuRURURuruRR"
    for i in L:
        MouvX(i,Cube)
    return(Cube)


def Ninja(Cube):   #(MMU MMU M1UU MMUU M1UU)   non utilisé
    L="MMUMMUmUUMMUUmUU"
    for i in L:
        MouvX(i,Cube)
    return(Cube)


def Plus(Cube):     #(MMU MMUU MMU MM) 
    L="MMUMMUUMMUMM"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Fois(Cube):         #Aprouvé  non utilisé
    L="UU"
    for i in L:
        MouvX(i,Cube)
    return(Plus(Cube))


def Palette(Cube):          #Apouvé 
    L="UxRurDRUrdRUrDRurdXu"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)


def Finition(Cube):     #Aprouvé   
    L="UrufRUrurFRRuruRUrURu"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
    
    
def Pythagore_Bas(Cube):  #R1FR1BBRF1R1BBRR   #Aprouvé 
    L="rFrBBRfrBBRR"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
    
    
def Pythagore_Haut(Cube):  #RB1RFFR1BRFFRR   #Aprouvé 
    L="rrbbRFrbbRfR"
    #L="RbRFFrBRFFRR"
    for i in L:
        MouvX(i,Cube)
    return(Cube,L)
# print(Pythagore_Haut(Cube))


##
##                                          ORDRE
def Ordre(L):  #Renvoie l'odre de la sequence donnée, c'est à dire combien de fois il faut executer la sequence pour revenir à l'etat initial 
    R,V,O,Bleu,J,Blanc=array([[1,1,1],[1,1,1],[1,1,1]]),array([[2,2,2],[2,2,2],[2,2,2]]),array([[3,3,3],[3,3,3],[3,3,3]]),array([[4,4,4],[4,4,4],[4,4,4]]),array([[5,5,5],[5,5,5],[5,5,5]]),array([[6,6,6],[6,6,6],[6,6,6]])
    Cube_Ordre,ordre,l=[R,V,O,Bleu,J,Blanc],0,len(L)
    MouvX(L[0],Cube_Ordre)
    j=0
    while not resolu(Cube_Ordre):
        if j==0:
            for i in L[1:]:
                MouvX(i,Cube_Ordre)
        else:
            for i in L:
                MouvX(i,Cube_Ordre)
        ordre+=1
        j+=1
    return(ordre)
    
#print(Ordre("RRFLdr"))

#Faire un programme d'orientation des coins: Requin_Droit, Requin_Gauche, Kangourou_Droit, Kangourou_Gauche
#Coin orienté= Jaune ou blanc sur bas ou haut= 5 ou 6 sur Cube[4] ou Cube[5]
#Position des coin= Cube[4][0,2,6,8] et Cube[5][0,2,6,8]=Cube[4,5][0,2][0,2]
#Comment orienter: si Cube[4][2][0,2] ne sont pas 5 ou 6 alors KangG/ReqG et KangD/ReqD
#Pareil en Cube[5]
#Faire un U puis Orienter Cube[4][2][2] à droite puis pareil en Cube [5]
#Faire un F1 et orienter Cube[4][0][2] par le meme procédé puis remettre avec F
#Les coins sont orientés

#Fonctions requises : x // Orienteur qui prend en compte les req et kang



##
##                               FONCTIONS ANNEXES DE L'ORIENTATION
def Orient_Coin(N,Cube): #Oriente le coté Gauche si N=0 et le droit si N=1 (oriente seulement le coin en bas a gauche de la face du haut)
    L=""
    if N==0:
        if Cube[0][0][2]==5 or Cube[0][0][2]==6:  #Le sticker est a gauche
            L=Kangourou_Gauche(Cube)[1]
        if Cube[1][0][0]==5 or Cube[1][0][0]==6:  #Le sticker est devant
            L=Requin_Gauche(Cube)[1]
    if N==1:
        if Cube[2][0][0]==5 or Cube[2][0][0]==6:  #Le sticker est à droite
            L=Kangourou_Droit(Cube)[1]
        if Cube[1][0][2]==5 or Cube[1][0][2]==6:  #Le sticker est devant
            L=Requin_Droit(Cube)[1]
    return(Cube,L)

def Orient_Arrete(Cube):   #Aprouvé 
    L=""
    if Cube[1][0][1]==5 or Cube[1][0][1]==6:
        L=Switch(Cube)[1]
    if (Cube[1][0][1]==2 or Cube[1][0][1]==4) and (Cube[4][2][1]!=5 and Cube[4][2][1]!=6):
        L=Switch(Cube)[1]
    return(Cube,L)
def SuperMouvX(X,Cube):     #Aprouvé 
    Liste="UuRrDdLlBbFfEeSsMmXxYy"
    L=""
    for i in Liste:
        if X==i:
            MouvX(i,Cube)
            L=X
    if X=="A":
        L=Orient_Arrete(Cube)[1]
    if X=="0":
        L=Orient_Coin(0,Cube)[1]
    if X=="1":
        L=Orient_Coin(1,Cube)[1]        
    return(Cube,L)
##
##                                      ORIENTATION DES COINS
def Grand_Orient_Coin(Cube):      #tout le code mis en commentaire est la pour comprendre      #Aprouvé 
    #Orient_Coin(0,Cube)                        #Orientation à gauche
    #Orient_Coin(1,Cube)                        #Orientation à droite                Haut
    #MouvU1(Orient_Coin(1,MouvU(Cube)))         #Orientation du coin Haut_Droit
    #x(x(Cube))                                 #x2
    #Orient_Coin(0,Cube)                        #Orientation à gauche
    #Orient_Coin(1,Cube)                        #Orientation à droite                Bas
    #MouvU1(Orient_Coin(1,MouvU(Cube)))         #Orientation du coin Haut_Droit
    #x(x(Cube))                                 #x'2
    #MouvF1(y(MouvU(Orient_Coin(1,MouvU1(y1(MouvF(Cube)))))))  #(Fy1U1)(orient 1)(UyF1)  Finition 
    #return(Cube)
    #new
    L=""
    Liste="01U1uXX01U1uxxFyu1UYf"      
    for i in range(len(Liste)):
        l=SuperMouvX(Liste[i],Cube)[1]
        L=L+l
    return(Cube,L)
# L="01"
# print(CubeT[4])
# for i in L:                               #testeur du SuperMouvX
    # print(SuperMouvX(i,CubeT)[4])
    # print(i)

#Il faut maintenant orienter les arrêtes
#Seule la fonction Switch sera utilisée
#On fait d'abord les arretes du haut et du bas puis apres on fait la ceinture


##
##                                      ORIENTATION DES ARRETES
def Grand_Orient_Arrete(Cube):    #tout le code mis en commentaire est la pour comprendre      #Aprouvé
    # Orient_Arrete(Cube)                        # check direct
    # MouvU1(Orient_Arrete(MouvU(Cube)))     #check a droite
    # x(x(Cube))                             #on va en bas
    # Orient_Arrete(Cube)                    # 
    # MouvU1(Orient_Arrete(MouvU(Cube)))      #la meme                #Base sud est
    # MouvB(MouvR(MouvU(Orient_Arrete(MouvU1(MouvR1(MouvB1(Cube)))))))    #(B1 R1 U1 orient U R B)
    # x(x(Cube))                                                            #on revient en haut
    # MouvB(MouvR(MouvU(Orient_Arrete(MouvU1(MouvR1(MouvB1(Cube)))))))    #(B1 R1 U1 orient U R B)      double cross basse 
    # MouvF(MouvF(Orient_Arrete(MouvF(MouvF(Cube)))))                    #(FF  orient  FF)    trou haut fond
    # x1(MouvU(Orient_Arrete(MouvU1(x(Cube)))))                         # (x U1 orient U x1) Completion Front gauche
    # y(y(Cube))                                                         #on va deriere
    # x1(MouvU(Orient_Arrete(MouvU1(x(Cube)))))                         #la meme derriere
    # x1(MouvL1(MouvL1(MouvU1(Orient_Arrete(MouvU(MouvL(MouvL(x(Cube))))))))) # (x LL U orient U1 L1L1 X1) Back completed
    # y(y(Cube))                                            #on revient devant
    # MouvF1(MouvU(MouvU(x1(Orient_Arrete(x(MouvU(MouvU(MouvF(Cube)))))))))  #(F UU x orient x1 UU F1) Finition en ramenant le trou 
    # return(Cube)
    #new
    Liste="AUAuXXAUAubruAURBxxbruAURBFFAFFXuAUxyyXuAUxXLLUAullxYYFUUXAxUUf"        #compressé et aprouvé
    L=""
    for i in Liste:
        L=L+SuperMouvX(i,Cube)[1]
    return(Cube,L)


##
##                                      ORIENTATION TOTALE
def Orientation_Totale(Cube):                            #Aprouvé 
    l1=Grand_Orient_Coin(Cube)[1]       #On peut permuter ces 2 operations puisqu'elles sont independantes l'une de l'autre
    l2=Grand_Orient_Arrete(Cube)[1]
    return(Cube,l1+l2)


#Maintenant que toutes les pièces sont orientées,il faut permuter les pièces
#L'arrete Cube[4][0][1] fait office de buffer
#Il faut creer le cycle : Fonction "Creer_Cycle" qui prend en compte le cube orienté et renvoie une liste de Lettre  dans (ABCDEFGHIJKL) ou(123456789 10 11 12) où le buffer est C ou 3 
#Il va falloir appeler les pièces concernées par le cycle : Fonction "Appel_Arrete"
#Enfin il faut permuter les pièces à l'aide de Riviere_Droite, Riviere_Gauche, Ninja, Plus


##
def L_Arretes(Cube):
    L_Arretes=[]    #Liste des arretes          #Notation : [[Couleur orientée,l'autre],[    ,    ],...]=[a,b,c,...,k,l]
    L_Arretes=L_Arretes+[[Cube[4][2][1],Cube[1][0][1]]]+[[Cube[4][1][0],Cube[0][0][1]]]+[[Cube[4][0][1],Cube[3][0][1]]]+[[Cube[4][1][2],Cube[2][0][1]]]  #Arretes du haut: a,b,c,d
    L_Arretes=L_Arretes+[[Cube[1][1][0],Cube[0][1][2]]]+[[Cube[3][1][2],Cube[0][1][0]]]+[[Cube[3][1][0],Cube[2][1][2]]]+[[Cube[1][1][2],Cube[2][1][0]]]  #Arretes de la ceinture: e,f,g,h
    L_Arretes=L_Arretes+[[Cube[5][0][1],Cube[1][2][1]]]+[[Cube[5][1][0],Cube[0][2][1]]]+[[Cube[5][2][1],Cube[3][2][1]]]+[[Cube[5][1][2],Cube[2][2][1]]]  #Arretes du bas: i,j,k,l
    return(L_Arretes)
    
    
##
##                                       FONCTIONS EN STOCK

#L="ABCDEFGHIJKL"
#H="ABCDEK"
def Napas(i,L):  #Fonction qui renvoie True si i n'appartient pas à L
    for j in range(len(L)):
        if i==L[j]:
            return(False)
    return(True)
    
    
#print(Napas("F",H))
##
def Retireur(L,H): #fonction qui retire à L les elements de H et mets des 0 aux endroits retirés
    New=""
    for i in L:
        if Napas(i,H):
            New=New+i
        else:
            New=New+"0"
    return(New)
    
    
#print(Retireur(L,H))
##
def Checker(L,Dico):   #renvoie le nombre de caractères en commun
    Bon=""
    Checker=Retireur(Dico,L)
    for i in Checker:
        if i =="0":
            Bon=Bon+i
    return(len(Bon))
    
    
##
def Dispo(Arrete,Dico):   #Indique si l'arrete est disponible 
    for i in Dico:
        if Arrete==i:
            return(True)
    return(False)
    
    
#print(Dispo("A",Dico))
##
##                                  FONCTIONS ANNEXES DU CYCLE
def Creer_Dico(L):  #Crée le dictionaire d'arretes associé à la liste d'arretes
    Dico="ABCDEFGHIJKL"
    NewDico=""
    L_Arretes_Resolu=[[5,2],[5,1],[5,4],[5,3],[2,1],[4,1],[4,3],[2,3],[6,2],[6,1],[6,4],[6,3]]
    for i in range(12):
        for j in range(12):
            if L[i]==L_Arretes_Resolu[j]:
                NewDico=NewDico+Dico[j]
    return(NewDico)
    
    
#print(Creer_Dico(L_Arretes(Orientaton_Totale(CubeT))))
# print(L_Arretes(Orientaton_Totale(CubeT)))
##                             
def Liste(L): #Conversion d'une chaine en liste
    l=[]
    for i in L:
        l=l+[i]
    return(l)
    
    
#print(Liste("ABCD"))
def Chaine(l): #Conversion d'une liste en chaine
    L=""
    for i in range(len(l)):
        L=L+l[i]
    return(L)
    
    
##              
def Implementeur(Symbole,Place,L): #Permet d'assigner à une chaine de caractère
    L=Liste(L)                     #(Non inclus dans Python)
    L[Place]=Symbole
    L=Chaine(L)
    return(L)
    
    
##
##                                      LE CYCLE
def Creer_Cycle(Cube):     #Crée le cycle d'arretes associée au cube (orienté)  ##Operationel
    L="+"
    Dico="ABCDEFGHIJKL"
    Vide="000000000000"
    NewDico=Creer_Dico(L_Arretes(Cube))
    for i in range(12):              #Deblayage des pièces dejà bien mises
        if Dico[i]==NewDico[i]:
            Dico=Implementeur("0",i,Dico)   #Les pièces dejà mises obtiennent un 0
    while Dico!=Vide: #Tant qu'il n'y a pas toutes les pièces non resolu dans le cycle on continue       
        #recherche du buffer
        if Dico[2]!="0":     #la piece C n'est pas resolu
            Buffer=2
        if Dico[2]=="0":           #la piece C est deja resolu
            Buffer=0
            while Dico[Buffer]=="0":
                Buffer+=1
        L=L+Dico[Buffer]
        # Dico=Implementeur("0",Buffer,Dico)
        i=Buffer
        for j in range(len(NewDico)):       #Premier tour
            if NewDico[i]==Dico[j]:
                L=L+Dico[j]
                Dico=Implementeur("0",j,Dico)    #on met un 0 quand on utilise la pièce
                i=j
        while i!=Buffer:
            for j in range(len(NewDico)):       #recurrence cyclique
                if NewDico[i]==Dico[j]:
                    L=L+Dico[j]
                    Dico=Implementeur("0",j,Dico) #on met un 0 quand on utilise la pièce
                    i=j
        L=L[:len(L)-1]
        L=L+"+"                                 # + annonce d'un nouveau cycle
    return(L[:len(L)-1])


#print(Creer_Cycle(Orientaton_Totale(CubeT)))
##
def L_Coins(Cube):  #Renvoie la liste des coins du cube
    L_Coins=[]  #Liste des coins
    Cube=Orientation_Totale(Cube)[0]
    #Notation : [[Couleur orientée,Couleur sens horaire, Couleur sens trigo ],[    ,    ,   ],...]=[1,2,3,4,5,6,7,8]
    L_Coins=L_Coins+[[Cube[4][2][2],Cube[2][0][0],Cube[1][0][2]]]+[[Cube[4][2][0],Cube[1][0][0],Cube[0][0][2]]]+[[Cube[4][0][0],Cube[0][0][0],Cube[3][0][2]]]+[[Cube[4][0][2],Cube[3][0][0],Cube[2][0][2]]]  #Coins du haut:1,2,3,4
    L_Coins=L_Coins+[[Cube[5][0][2],Cube[1][2][2],Cube[2][2][0]]]+[[Cube[5][0][0],Cube[0][2][2],Cube[1][2][0]]]+[[Cube[5][2][0],Cube[3][2][2],Cube[0][2][0]]]+[[Cube[5][2][2],Cube[2][2][2],Cube[3][2][0]]]  #Coins du bas: 5,6,7,8
    return(L_Coins)
# print(L_Coins(Cube))


##
##                                      FONCTIONS ANNEXES D'APPEL
def Traqueur(A,L,Cube):  #Traque l'arrete A et donne sa nouvelle lettre après mouvement L  #Aprouvé par la science
    Cube=copy(Cube)
    L_Arretes_Resolu=[[5,2],[5,1],[5,4],[5,3],[2,1],[4,1],[4,3],[2,3],[6,2],[6,1],[6,4],[6,3]]
    Dico="ABCDEFGHIJKL"
    for i in range(len(Dico)):
        if A[0]==Dico[i]:        #decompression de la lettre en sa place chiffré
            place=i

    Copie_Flou=copy(L_Arretes(Cube)[place])      #on utilise la liste des arretes et on creer une copie
    Ombre=[Copie_Flou[0],Copie_Flou[1]]     #la fonction copy renvoie [5 3] si elle copie [5, 3] donc on reconstitue 
    for i in L:
         MouvX(i,Cube)          #mouvement
    New_L_Arretes=L_Arretes(Orientation_Totale(Cube)[0])   #on crée la nouvelle liste d'arretes 
    i=0
    while Ombre!=New_L_Arretes[i]:
        i+=1                            #Comparaison ancien/nouveau jusqu'à ce que la nouvelle place ait été trouvée
    return(Dico[i])                     #La traque est finie


#print(Traqueur("B","LL",CubeT))
##
def Tracoin(n1,L,Cube):   #Traque le coin et renvoie sa position après mouvement L  
    #Le mouvement L ne doit pas désorienter les coins : B/b/F/f/R/r/L/l interdit
    R=array([[1,1,1],[1,1,1],[1,1,1]])
    V=array([[2,2,2],[2,2,2],[2,2,2]])
    O=array([[3,3,3],[3,3,3],[3,3,3]])
    Bleu=array([[4,4,4],[4,4,4],[4,4,4]])
    J=array([[5,5,5],[5,5,5],[5,5,5]])
    Blanc=array([[6,6,6],[6,6,6],[6,6,6]])
    Cube=[R,V,O,Bleu,J,Blanc]
    L_Coins_Resolu=[[5,3,2],[5,2,1],[5,1,4],[5,4,3],[6,2,3],[6,1,2],[6,4,2],[6,3,4]]
    Dicoin="12345678"
    for i in range(len(Dicoin)):
        if n1[0]==Dicoin[i]:        #decompression du coin en sa place chiffré
            place=i

    Copie_Flou=copy(L_Coins(Cube)[place])      #on utilise la liste des coins et on creer une copie
    Ombre=[Copie_Flou[0],Copie_Flou[1],Copie_Flou[2]]     #la fonction copy renvoie [5 3 2] si elle copie [5, 3, 2] donc on reconstitue 
    for i in L:
         MouvX(i,Cube)          #mouvement
    New_L_Coins=L_Coins(Orientation_Totale(Cube)[0])   #on crée la nouvelle liste de coins 
    i=0
    while Ombre!=New_L_Coins[i]:
        i+=1                            #Comparaison ancien/nouveau jusqu'à ce que la nouvelle place ait été trouvée
    return(Dicoin[i])                     #La traque est finie
    
    
# print(Tracoin("2","LLBB",Cube))
##                                      
def Separateur(A,B):   #on sépare A et B et on met une sur la droite et l'autre sur la gauche   #Fonction longue mais fonctionnelle, les cas ont été determinés un par un à l'aide d'un rubik's cube et de deux mains
    L=""                    #Renvoie la liste des actions à effectuer pour séparer
    if A=="A":
        if B=="B":              
            L="LurU" 
        if B=="C":
            L="U"
        if B=="D":
            L="rULu"
        if B=="E" or B=="F" or B=="J":
            L="urU"
        if B=="G" or B=="H" or B=="L":
            L="ULu"
        if B=="I":
            L="DULu"
        if B=="K":
            L="dULu"
    if A=="B":
        if B=="A":
            L="LurU"
        if B=="C":
            L="LUru"
        if B=="E" or B=="F" or B=="J":
            L="UUrUU" 
        if B=="I":
            L="D"
        if B=="K":
            L="d"
    if A=="C":
        if B=="A":
            L="U"
        if B=="B":
            L="LUru" 
        if B=="D":
            L="ruLU"
        if B=="E" or B=="F" or B=="J":
            L="Uru"
        if B=="G" or B=="H" or B=="L":
            L="uLU"        
        if B=="I":
            L="dUru"
        if B=="K":
            L="DUru"
    if A=="D":
        if B=="A":
            L="rULu"
        if B=="C":
            L="ruLU"
        if B=="G" or B=="H" or B=="L":
            L="UULUU"
        if B=="I":
            L="d"
        if B=="K":
            L="D"
    if A=="E":
        if B=="A":
            L="urU"
        if B=="B":
            L="UUrUU"
        if B=="C":
            L="Uru"
        if B=="F":
            L="LDD"
        if B=="I":
            L="D"
        if B=="J":
            L="DD"
        if B=="K":
            L="d"
    if A=="F":
        if B=="A":
            L="urU"
        if B=="B":
            L="UUrUU"
        if B=="C":
            L="Uru"
        if B=="E":
            L="LDD"
        if B=="I":
            L="D"
        if B=="J":
            L="DD"
        if B=="K":
            L="d"
    if A=="G":
        if B=="A":
            L="ULu"
        if B=="C":
            L="uLU"
        if B=="D":
            L="UULUU"
        if B=="H":
            L="RDD"
        if B=="I":
            L="d"
        if B=="K":
            L="D"
        if B=="L":
            L="DD"
    if A=="H":
        if B=="A":
            L="ULu"
        if B=="C":
            L="uLU"
        if B=="D":
            L="UULUU"
        if B=="G":
            L="RDD"
        if B=="I":
            L="d"
        if B=="K":
            L="D"
        if B=="L":
            L="DD"
    if A=="I":
        if B=="A":
            L="DULu"
        if B=="C":
            L="dUru"
        if B=="B" or B=="E" or B=="F" or B=="K":
            L="D"
        if B=="D" or B=="G" or B=="H":
            L="d"
        if B=="J":
            L="LD"
        if B=="L":
            L="Rd"
    if A=="J":
        if B=="A":
            L="urU"
        if B=="B":
            L="UUrUU"
        if B=="C":
            L="Uru"
        if B=="E" or B=="F":
            L="DD"
        if B=="I":
            L="LD"
        if B=="K":
            L="Ld"
    if A=="K":
        if B=="A":
            L="dULu"
        if B=="C":
            L="DUru"
        if B=="B" or B=="E" or B=="F":
            L="d"
        if B=="D" or B=="G" or B=="H" or B=="I":
            L="D"
        if B=="J":
            L="Ld"
        if B=="L":
            L="RD"
    if A=="L":
        if B=="A":
            L="ULu"
        if B=="C":
            L="uLU"
        if B=="D":
            L="UULUU"
        if B=="G" or B=="H":
            L="DD"
        if B=="I":
            L="Rd"
        if B=="K":
            L="RD"
    return(L)
    
    
    
##
def Ascenseur(A,B):    #Fait monter deux arretes A et B en B et D sachant que A et B sont sur les faces L et R  #Nice
    L=""
    if A=="E" or B=="E":
        L="l"
    if A=="F" or B=="F":
        L="L"
    if A=="J" or B=="J":
        L="LL"
    if A=="G" or B=="G":
        L=L+"r"
    if A=="H" or B=="H":
        L=L+"R"
    if A=="L" or B=="L":
        L=L+"RR"
    return(L)
    
    
#print(Ascenseur("E","G"))
##
##                                          APPEL
def Appel_Arrete(A,B,Cube,n1,n2):    #Appel les arretes A et B en position B et D où A et B se suivent dans le cycle #Nice
#n1 et n2 sont ici pour la parité finale
    L=Separateur(A,B)                           #Séquence de la séparation
    Prem_n1,Prem_n2=Tracoin(n1,L,Cube),Tracoin(n2,L,Cube)
    TsA=Traqueur(A,L,Cube)                      #TsA=TraqueSeparationA
    TsB=Traqueur(B,L,Cube)                      #TsB=TraqueSeparationB
    for i in L:
        MouvX(i,Cube)
    Ascension=Ascenseur(TsA,TsB)                  #Sequence de l'ascension
    Deuz_n1=Tracoin(Prem_n1,Ascension,Cube)
    Deuz_n2=Tracoin(Prem_n2,Ascension,Cube)
    TaA=Traqueur(TsA,Ascension,Cube)              #TaA=TraqueAscensionA
    TaB=Traqueur(TsB,Ascension,Cube)              #Tab=TraqueAscensionB
    for i in Ascension:
        MouvX(i,Cube)
    return(L+Ascension,TaA,TaB,Cube,Deuz_n1,Deuz_n2)    #A mettre  pour avoir le tracé :A,B,TsA,TsB,TaA,TaB,
    
    
##
##                                     FONCTIONS ANNEXES DU CYCLOTRON
def Anti(L):  #renvoie l'inverse de la séquence L 
    H=""
    L1=""
    Bibli="UuRrDdLlFfBbMmEeSsXxYy"
    Anti_Bibli="uUrRdDlLfFbBmMeEsSxXyYy"
    for i in range(len(L)):    #Creation de H, Opposé de L
        H=H+L[len(L)-(i+1)]
    for i in H:
        for j in range(len(Bibli)):
            if i==Bibli[j]:
                L1=L1+Anti_Bibli[j]
    return(L1)
#print(Anti("URufFxYe"))


##
def Split_Cycle(Cycle): #Retourne la liste des Cycles de forme ["AB","CD","EF"]
    l=[]
    Liste_Cycles=[]
    for i in range(len(Cycle)):   #On balise les sous cycles
        if Cycle[i]=="+":
            l=l+[i]
    for i in range(len(l)):
        Liste_Cycles=Liste_Cycles+[""]  #Creation d'une liste adaptée au Cycle 
    l=l+[len(Cycle)+1]                  #["","",""] au maximum
    for x in range(len(l)-1):      #x=nombre de sous cycles
        j=l[x]                     #Depart de la variable à partir du debut du sous cycle
        while j<l[x+1]-1:          #Tourne jusqu'à atteindre la fin du sous cycle
            if j+1>=len(Cycle):    #Empecher la variable de dépasser la taillle du cycle
                break
            Liste_Cycles[x]=Liste_Cycles[x]+Cycle[j+1]    #Creation de la liste de chaines 
            j=j+1
    return(Liste_Cycles)
    

#print(Split_Cycle("+ABC+DE+FGHIJKL"))
# print(Split_Cycle("+2346+57"))
##
def Appel_Buffer(A,Cube): #Amène le buffer en position C et donne la liste des mouvements effectués
    if A=="A":
        L="UU"
    if A=="B":
        L="U"
    if A=="C":
        L=""
    if A=="D":
        L="u"
    if A=="E":
        L="lU"
    if A=="F":
        L="LU"
    if A=="G":
        L="ru"
    if A=="H":
        L="Ru"
    if A=="I":
        L="FFUU"
    if A=="J":
        L="LLU"
    if A=="K":
        L="BB"
    if A=="L":
        L="RRu"
    for i in L:
        MouvX(i,Cube)
    return(L)
    
    
##
def Recycleur_Arrete(A,B,C,D,Cube):  #On prend deux 2-cycles et on les permute ensemble  où +AB+CD
    Copie=copy(Cube)
    Info1=Appel_Arrete(A,B,Cube,"1","2")   #A et B sont en position TaA et TaB (B ou D
    L1,TaA,TaB=Info1[0]+"U",Info1[1],Info1[2]
    #où sont C et D
    MouvU(Cube)
    LocC=Traqueur(C,L1,Copie)
    LocD=Traqueur(D,L1,Copie)
    # print(TaA,TaB,LocC,LocD)
    Info2=Appel_Arrete(LocC,LocD,Cube,"1","2")
    L2=Info2[0]
    perm=Plus(Cube)[1]   #perm
    for i in Anti(L1+L2):   #Desetup
        MouvX(i,Cube)
    return(L1+L2+perm+Anti(L1+L2),Cube)
    

#"Le commencement de toutes les sciences, c'est l'étonnement de ce que les choses sont ce qu'elles sont". Aristote, Métaphysique

##
def Cyclozigouillage(A,B,Cube):   #Permute les pièces de A vers B    
    if A=="B" and B=="D":
        L=Riviere_Droite(Cube)[1]
        # print("Riviere_Droite")          #A ACTIVER
    if A=="D" and B=="B":
        L=Riviere_Gauche(Cube)[1]
        # print("Riviere_Gauche")           #A ACTIVER
    if (A!="B" and B!="D") and (A!="D" and B!="B"):
        print("MeydayMeyday")
    return(L)
    

##
##                                          CYCLOTRON
def Cyclotron(Cube):   #Le cyclotron ne prend en charge que les cubes orientés
    Mouvs=""
    Grand_Cycle=Creer_Cycle(Cube)
    # print(Grand_Cycle)      #A ACTIVER
    Sous_Cycles=Split_Cycle(Grand_Cycle)    #On casse le Grand Cycle en ses sous cycles
    # print(Sous_Cycles)
    for w in range(len(Sous_Cycles)):
        MouvsDuBuffer=Appel_Buffer(Sous_Cycles[w][0],Cube) #on pose le buffer en C
        Mouvs=Mouvs+MouvsDuBuffer
        # print(MouvsDuBuffer)          #A ACTIVER
        Cycle=Sous_Cycles[w]
        for i in range((len(Cycle)-1)//2):
            Cible1=Traqueur(Cycle[2*i+1],MouvsDuBuffer,Cube)    #Pieces cibles après Setup du buffer
            Cible2=Traqueur(Cycle[2*i+2],MouvsDuBuffer,Cube)
            Info=Appel_Arrete(Cible1,Cible2,Cube,"1","2")       #Setup   Info=[L,A,B,Cube]
            L,A,B=Info[0],Info[1],Info[2]
            # print(L)                 #A ACTIVER
            L1=Anti(L)
            Mouvs=Mouvs+L+Cyclozigouillage(A,B,Cube)+L1           #permutations
            # print(Traqueur(A,L1,Cube),Traqueur(B,L1,Cube),L1)   #A ACTIVER
            for j in L1:                                      #Desetup
                MouvX(j,Cube)
        for k in Anti(MouvsDuBuffer):                           #Desetup du buffer
            MouvX(k,Cube)
        Mouvs=Mouvs+Anti(MouvsDuBuffer)
        # print(Anti(MouvsDuBuffer))       #A ACTIVER
    return(Cube,Mouvs)            #Et un cube tout chaud, un!
    

##
def SuperCyclotron(Cube):    #Cyclotron écologique
    L=Cyclotron(Cube)[1]
    Cycle=Creer_Cycle(Cube)
    Dechets=Split_Cycle(Cycle)
    if len(Dechets)>1:
        if len(Dechets[0]+Dechets[1])==4:
            L=L+Recycleur_Arrete(Dechets[0][0],Dechets[0][1],Dechets[1][0],Dechets[1][1],Cube)[0]
    Nouveau_Cycle=Creer_Cycle(Cube)
    Dechets=Split_Cycle(Nouveau_Cycle)
    if len(Dechets)>1:  #Si il reste des dechets ça repart au tri
        if len(Dechets[0]+Dechets[1])==4:
            L=L+Recycleur_Arrete(Dechets[0][0],Dechets[0][1],Dechets[1][0],Dechets[1][1],Cube)[0]
    return(Cube,L)
    

##
##                                      FONCTIONS ANNEXES DU CYCLOCOIN
def Appel_Coin(n1,n2,Cube):            #Appel les coin n1 et n2 en position 2 et 3
    L=""
    if n1=="1":
        if n2=="2":
            L="UU"
        if n2=="3":
            L="BBDBBu"
        if n2=="4":
            L="u"
        if n2=="5":
            L="DDBBu"
        if n2=="6":
            L="dBBu"
        if n2=="7":
            L="BBu"
        if n2=="8":
            L="DBBu"
    if n1=="2":
        if n2=="3":
            L="LLdBB"
        if n2=="4":
            L="LLDLL"
        if n2=="5":
            L="DLLBB"
        if n2=="6":
            L="DDLLBB"
        if n2=="7":
            L="dLLBB"
        if n2=="8":
            L="LLBB"
    if n1=="3":
        if n2=="2":
            L="LLdBB"
        if n2=="5":
            L="LLDDBB"
        if n2=="6":
            L="DLLDDBB"
        if n2=="7":
            L="DDLLDDBB"
        if n2=="8":
            L="dLLDDBB"
    if n1=="4":
        if n2=="2":
            L="LLDLL"
        if n2=="5":
            L="dLL"
        if n2=="6":
            L="LL"
        if n2=="7":
            L="DLL"
        if n2=="8":
            L="DDLL"    
    if n1=="5":
        if n2=="2":
            L="DLLBB"
        if n2=="3":
            L="LLDDBB"
        if n2=="4":
            L="dLL"
        if n2=="6":
            L="DDBB"
        if n2=="7":
            L="BBdLL"
        if n2=="8":
            L="DBB"
    if n1=="6":
        if n2=="2":
            L="DDLLBB"
        if n2=="3":
            L="DLLDDBB"
        if n2=="4":
            L="LL"
        if n2=="5":
            L="DDBB"
        if n2=="7":
            L="dBB"
        if n2=="8":
            L="DBBdLL"
    if n1=="7":
        if n2=="2":
            L="dLLBB"
        if n2=="3":
            L="DDLLDDBB"
        if n2=="4":
            L="DLL"
        if n2=="5":
            L="BBdLL"
        if n2=="6":
            L="dBB"
        if n2=="8":
            L="BB"
    if n1=="8":
        if n2=="2":
            L="LLBB"
        if n2=="3":
            L="dLLDDBB"
        if n2=="4":
            L="DDLL"
        if n2=="5":
            L="DBB"
        if n2=="6":
            L="DBBdLL"
        if n2=="7":
            L="BB"
    Tn1=Tracoin(n1,L,Cube)                      #Tn1=Traque n1
    Tn2=Tracoin(n2,L,Cube)                      #Tn2=Traque n2
    return(L,Tn1,Tn2,Cube)


#print(Appel_Coin("7","4",Cube))
##
def Creer_Dicoin(L):  #Crée le dictionaire d'arretes associé à la liste de coins
    Dicoin="12345678"
    NewDicoin=""
    L_Coins_Resolu=[[5,3,2],[5,2,1],[5,1,4],[5,4,3],[6,2,3],[6,1,2],[6,4,1],[6,3,4]]
    for i in range(8):
        for j in range(8):
            if L[i]==L_Coins_Resolu[j]:
                NewDicoin=NewDicoin+Dicoin[j]
    return(NewDicoin)


##
def Creer_Cycle_Coins(Cube):     #Crée le cycle de coins associée au cube (orienté)  
    L="+"
    Dicoin="12345678"
    Vide="00000000"
    NewDicoin=Creer_Dicoin(L_Coins(Cube))
    for i in range(8):              #Deblayage des pièces dejà bien mises
        if Dicoin[i]==NewDicoin[i]:
            Dicoin=Implementeur("0",i,Dicoin)   #Les pièces dejà mises obtiennent un 0
    while Dicoin!=Vide: #Tant qu'il n'y a pas toutes les pièces non resolu dans le cycle on continue       
        #recherche du buffer
        if Dicoin[0]!="0":     #le coin 1 n'est pas resolu
            Buffer=0
        if Dicoin[0]=="0":           #le coin 1 est deja resolu
            Buffer=0
            while Dicoin[Buffer]=="0":
                Buffer+=1
        L=L+Dicoin[Buffer]
        i=Buffer
        for j in range(len(NewDicoin)):       #Premier tour
            if NewDicoin[i]==Dicoin[j]:
                L=L+Dicoin[j]
                Dicoin=Implementeur("0",j,Dicoin)    #on met un 0 quand on utilise la pièce
                i=j
        while i!=Buffer:
            for j in range(len(NewDicoin)):       #recurrence cyclique
                if NewDicoin[i]==Dicoin[j]:
                    L=L+Dicoin[j]
                    Dicoin=Implementeur("0",j,Dicoin) #on met un 0 quand on utilise la pièce
                    i=j
        L=L[:len(L)-1]
        L=L+"+"           # + annonce d'un nouveau cycle
    return(L[:len(L)-1])
# print(Creer_Cycle_Coins(Orientation_Totale(CubeT)[0]))


##
def Appel_Buffer_Coin(Buffer,Cube): #Amène le buffer en position 1 et donne la liste des mouvements effectués
    if Buffer=="1":
        L=""
    if Buffer=="2":
        L="u"
    if Buffer=="3":
        L="UU"
    if Buffer=="4":
        L="U"
    if Buffer=="5":
        L="RRU"
    if Buffer=="6":
        L="LLuu"
    if Buffer=="7":
        L="LLu"
    if Buffer=="8":
        L="RR"
    for i in L:
        MouvX(i,Cube)
    return(L)
##
def Cyclozigouillage_Coins(n1,n2,Cube):
    if n1=="3" and n2=="4":
        L=Pythagore_Bas(Cube)[1]
        # print("Pythagore_Bas")          #A ACTIVER
    if n1=="4" and n2=="3":
        L=Pythagore_Haut(Cube)[1]
        # print("Pythagore_Haut")           #A ACTIVER
    if (n1!="3" and n2!="4") and (n1!="4" and n2!="3"):
        print("MeydayMeyday")
    return(L)
    

##
##                                          LE CYCLOCOIN
def CycloCoin(Cube):
    Mouvs=""
    Grand_Cycle=Creer_Cycle_Coins(Cube)
    # print(Grand_Cycle)      #A ACTIVER
    Sous_Cycles=Split_Cycle(Grand_Cycle)    #On casse le Grand Cycle en ses sous cycles
    # print(Sous_Cycles)
    for w in range(len(Sous_Cycles)):
        MouvsDuBuffer=Appel_Buffer_Coin(Sous_Cycles[w][0],Cube) #on pose le buffer en C
        Mouvs=Mouvs+MouvsDuBuffer
        # print(MouvsDuBuffer)          #A ACTIVER
        Cycle=Sous_Cycles[w]
        for i in range((len(Cycle)-1)//2):
            Cible1=Tracoin(Cycle[2*i+1],MouvsDuBuffer,Cube)    #Pieces cibles après Setup du buffer
            Cible2=Tracoin(Cycle[2*i+2],MouvsDuBuffer,Cube)
            Info=Appel_Coin(Cible1,Cible2,Cube)       #Setup   Info=[L,A,B,Cube]
            L,n1,n2=Info[0],Info[1],Info[2]
            for m in L:
                MouvX(m,Cube)
            # print(L)                 #A ACTIVER
            L1=Anti(L)
            Mouvs=Mouvs+L+Cyclozigouillage_Coins(n1,n2,Cube)+L1           #permutations
            # print(Tracoin(n1,L1,Cube),Tracoin(n2,L1,Cube),L1)   #A ACTIVER
            for j in L1:                                      #Desetup
                MouvX(j,Cube)
        for k in Anti(MouvsDuBuffer):                           #Desetup du buffer
            MouvX(k,Cube)
        Mouvs=Mouvs+Anti(MouvsDuBuffer)
        # print(Anti(MouvsDuBuffer))       #A ACTIVER  
    return(Cube,Mouvs)            #Et un cube tout chaud, un!
    
    
##
def Apaireur(n1,n2): #Apaire les coins n1 et n2 en 3 4 sans impacter les coins 1 et 2 #Liste exhaustive, l'auteur a pris le temps de soigner chaque cas un par un de telle manière à obtenir un résultat cohérent, ce passage est long et peu intéressant d'un point de vue global, mais requis au bon fonctionnement de l'ensemble
    L=""
    if n1=="1":
        if n2=="2":
            L="UU"
        if n2=="3":
            L="FFDBB"
        if n2=="4":
            L="FFBB"
        if n2=="5":
            L="DDFF"
        if n2=="6":
            L="dFF"
        if n2=="7":
            L="FF"
        if n2=="8":
            L="DFF"
    if n1=="2":
        if n2=="1":
            L="UU"
        if n2=="3":
            L="FFBB"
        if n2=="4":
            L="FFdBB"
        if n2=="5":
            L="DFF"
        if n2=="6":
            L="DDFF"
        if n2=="7":
            L="dFF"
        if n2=="8":
            L="FF"
    if n1=="3":
        if n2=="1":
            L="FFDBB"
        if n2=="2":
            L="FFBB"
        if n2=="5":
            L="BB"
        if n2=="6":
            L="DBB"
        if n2=="7":
            L="DDBB"
        if n2=="8":
            L="dBB"
    if n1=="4":
        if n2=="1":
            L="FFBB"
        if n2=="2":
            L="FFdBB"
        if n2=="5":
            L="dBB"
        if n2=="6":
            L="BB"
        if n2=="7":
            L="DBB"
        if n2=="8":
            L="DDBB"
    if n1=="5":
        if n2=="1":
            L="DDFF"
        if n2=="2":
            L="DFF"
        if n2=="3":
            L="BB"
        if n2=="4":
            L="dBB"
        if n2=="7":
            L="BBdBB"
    if n1=="6":
        if n2=="1":
            L="dFF"
        if n2=="2":
            L="DDFF"
        if n2=="3":
            L="DBB"
        if n2=="4":
            L="BB"
        if n2=="8":
            L="BBDBB"
    if n1=="7":
        if n2=="1":
            L="FF"
        if n2=="2":
            L="dFF"
        if n2=="3":
            L="DDBB"
        if n2=="4":
            L="DBB"
        if n2=="5":
            L="BBdBB"
    if n1=="8":
        if n2=="1":
            L="DFF"
        if n2=="2":
            L="FF"
        if n2=="3":
            L="dBB"
        if n2=="4":
            L="DDBB"
        if n2=="6":
            L="BBDBB"
    return(L)


##
def Poseur(n1,n2): #Fait monter les coins n1 et n2(Apairés) en 3 4 sans impacter 1 2
    L=""
    if n1=="5":
        if n2=="6":
            L="DDBB"
        if n2=="8":
            L="DBB"
    if n1=="6":
        if n2=="7":
            L="dBB"
        if n2=="5":
            L="DDBB"
    if n1=="7":
        if n2=="8":
            L="BB"
        if n2=="6":
            L="dBB"
    if n1=="8":
        if n2=="5":
            L="DBB"
        if n2=="7":
            L="BB"
    return(L)

#Tout est pour le mieux dans le meilleur des mondes possibles" Leibniz
##
def Gentil_Appeleur_Coin(n1,n2,Cube):  # appel n1 et n2 en 3/4 sans bouger 1/2
    L=Apaireur(n1,n2)
    Pos_n1=Tracoin(n1,L,Cube)
    Pos_n2=Tracoin(n2,L,Cube)
    L=L+Poseur(Pos_n1,Pos_n2)
    return(L)
    

##
def Recycloin(n1,n2,n3,n4,Cube):   #Recycle les 2-Cycles
    l=Appel_Coin(n1,n2,Cube)[0]
    L=l+"UU"
    Fin_n1=Tracoin(n1,L,Cube)     
    Fin_n2=Tracoin(n2,L,Cube)
    Pos_n3=Tracoin(n3,L,Cube)     
    Pos_n4=Tracoin(n4,L,Cube)
    # print(Pos_n3,Pos_n4)
    for i in L:
        MouvX(i,Cube)               #n1/n2 en 1/2 
    Suite=Gentil_Appeleur_Coin(Pos_n3,Pos_n4,Cube)
    # print(Suite)
    Fin_n3=Tracoin(Pos_n3,Suite,Cube)
    Fin_n4=Tracoin(Pos_n4,Suite,Cube)
    # print(Fin_n1,Fin_n2,Fin_n3,Fin_n4)
    for j in Suite:
        MouvX(j,Cube)              #n3/n4 en 3,4  
    L=L+Suite
    perm=Palette(Cube)[1]
    L1=Anti(L)
    for g in L1:
        MouvX(g,Cube)
    return(L+perm+L1)


##
def SuperCycloCoin(Cube): #Cyclocoin ecologique
    L=CycloCoin(Cube)[1]
    Cycle=Creer_Cycle_Coins(Cube)
    Dechets=Split_Cycle(Cycle)
    # print(Dechets)
    if len(Dechets)>1:
        if len(Dechets[0]+Dechets[1])==4:
            L=L+Recycloin(Dechets[0][0],Dechets[0][1],Dechets[1][0],Dechets[1][1],Cube)
    Nouveau_Cycle=Creer_Cycle_Coins(Cube)
    # print(Nouveau_Cycle)
    Dechets=Split_Cycle(Nouveau_Cycle)
    if len(Dechets)>1:  #Si il reste des dechets ça repart au tri
        if len(Dechets[0]+Dechets[1])==4:
            L=L+Recycloin(Dechets[0][0],Dechets[0][1],Dechets[1][0],Dechets[1][1],Cube)
    return(Cube,L)


##
##                                         PARITE
#PLAN: Appeler les 2 arretes en B/D, Appeler gentillement les 2 coins en 3 et 4 puis faire la pll correspondante
##
def Parite(n1,n2,A,B,Cube):
    infos=Appel_Arrete(A,B,Cube,n1,n2)   #Arretes en B/D
    Mouv_A=infos[0]
    n1,n2=infos[4],infos[5]
    Mouv_C=Gentil_Appeleur_Coin(n1,n2,Cube)
    # print(n1,n2,L)
    setup=Mouv_A+Mouv_C
    for i in Mouv_C:
        MouvX(i,Cube)
    perm=Finition(Cube)[1]
    for p in perm:
        MouvX(p,Cube)
    L1=Anti(setup)
    for j in L1:
        MouvX(j,Cube)
    return(setup+perm+L1)



def La_Touche_Finale(Cube):
    L=""
    CycleA=Split_Cycle(Creer_Cycle(Cube))
    CycleC=Split_Cycle(Creer_Cycle_Coins(Cube))
    # print(CycleA,CycleC)
    if len(CycleA)>0 and len(CycleC)>0:
        L=Parite(CycleC[0][0],CycleC[0][1],CycleA[0][0],CycleA[0][1],Cube)
        for i in L:
            MouvX(i,Cube)
    return(Cube,L)
    
#"Vouloir le vrai, c'est s'avouer impuissant à le créer." Nietzsche
##
##                                          The Path
def ThePath(Cube): #donne le chemin à emprunter pour resoudre le cube
    Cube=copy(Cube) #Si on enlève cette ligne alors le cube sera resolu aussi
    Orientation=Orientation_Totale(Cube)[1]
    Arretes=SuperCyclotron(Cube)[1]
    Coins=SuperCycloCoin(Cube)[1]
    Parite=La_Touche_Finale(Cube)[1]     
    Path=Orientation+Arretes+Coins+Parite
    return(Path)     
    
     
##
##                                         COMPACTEUR 
def Compacteur(L):      #Compacte une liste de mouvements en une liste plus courte ayant le meme effet sur le cube   COMPACTEUR basique, peut faire mieux car Compacteur("Udu")="Udu" alors que "Udu"="d"
    n=len(L)
    L=L+5*"."
    Bibli="UuRrDdLlFfBbMmEeSsXxYy"
    AntiBibli="uUrRdDlLfFbBmMeEsSxXyY"
    for x in range(4):       #Nombre de nettoyages
        i=0        #i permet de ne pas depasser len(L)-3
        while i<len(L)-3:
            for j in range(len(Bibli)):
                if L[i]==Bibli[j] and L[i+1]==Bibli[j] and L[i+2]==Bibli[j] and L[i+3]==Bibli[j]:
                    L=L[:i]+L[i+4:]
                if L[i]==Bibli[j] and L[i+1]==AntiBibli[j]:
                    L=L[:i]+L[i+2:]
            i+=1
    L=L[:len(L)-5]
    #Petite amelioration pour la methode roux (Compacter le ZZZ en z qui apparait souvent au debut de la solution)
    if L[0]=="Z" and L[1]=="Z" and L[2]=="Z":
        L="z"+L[3:]
    return(L)
    
    
#PISTES D'UPGRADE: Split L en listes de mouvs independants ( (U,u) et D,d) sont indep  et ainsi les repasser dans le compacteur basique et recreer une liste toute neuve
#Mouvs indep:(U,u) avec (D,d) /// (D,d) avec (U,u)/// (R,r) avec (L,l)/// (L,l) avec (R,r)///(F,f) avec (B,b)///(B,b) avec (F,f)
#Aussi il faut transformer les RRR en r 
#A DEVELOPPER
# print(Compacteur("UuFfFfuuuuUuUFBFBFBuuuuFfff"))
# print(Compacteur("Udu"))
#Ce passage n'a pas été développé car considéré peu utile par rapport à l'effort requis pour en arriver à bout

##
##                                          CREATEUR
def Createur(L,Cube): 
    Cube=copy(Cube)
    for i in L:
        MouvX(i,Cube)
    return(Cube)
    
    
##
##                                      POSTE DE COMMANDES    
def melange(Chaine):
    import numpy.random as npr
    L=Liste(Chaine)
    npr.shuffle(L)
    return(L)
def Melange(L):
    return(Chaine(melange(L)))
# print(Melange("FUBLU"))


##                                 Données
Dico="ABCDEFGHIJKL"
Dicoin="12345678"
##                              Ecran de contrôle
def Ecran_de_controle(Cube,L):
    Cube=copy(Cube)
    CUBEE=Orientation_Totale(Cube)[0]
    print("Mélange:")
    print("        ",Compacteur(L))
    print("______________________________________________")
    print("Cycle de coins:")
    print("                          ",Creer_Cycle_Coins(CUBEE))
    # print()                          #A mettre si l'on veut aérer l'affichage
    print("Dicoin:")
    print("                          ",Dicoin)
    # print()
    print("Coins du cube:")
    print("                          ",Creer_Dicoin(L_Coins(CUBEE)))
    # print()
    print("Coins après résolution:")
    print("                          ",Creer_Dicoin(L_Coins(SuperCycloCoin(CUBEE)[0])))
    print("Cycle de coins résolu:")
    print("                           OK",Creer_Cycle_Coins(CUBEE))
    print("______________________________________________")
    print("Cycle d'arrêtes:")
    print("                          ",Creer_Cycle(CUBEE))
    # print()
    print("Dico:")
    print("                          ",Dico)
    # print()
    print("Arrêtes du cube:")
    print("                          ",Creer_Dico(L_Arretes(CUBEE)))
    # print()
    print("Arrêtes après résolution:")
    print("                          ",Creer_Dico(L_Arretes(SuperCyclotron(CUBEE)[0])))
    print("Cycle d'arretes résolu:")
    print("                           OK",Creer_Cycle(CUBEE))
    print("Parité résolu?")
    print("                  Coins    OK",Creer_Cycle_Coins(La_Touche_Finale(CUBEE)[0]))
    print("                  Arretes  OK",Creer_Cycle(CUBEE))
    print("Résolu?")
    print("                         ",resolu(CUBEE))
    if not resolu(CUBEE):
        print("ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE")  #petit message d'alerte
    for i in range(2):
        if not resolu(CUBEE):
            break
    return(CUBEE)



def Testeur(nb,Cube):
    for i in range(nb):
        L=Melange("UrufRUrurFRRuruRUrURu")
        CubeTest=Createur(L,Cube)
        Ecran_de_controle(CubeTest,L)
        


##
##                                   BOUTON ROUGE
# Le nombre à l'interieur du testeur correspond au nombre de cubes qui vont etre resolu, si ce nombre devient trop grand alors... A essayer c'est rigolo 
# # # Testeur(1,Cube) 
##
##                                    COMMENTAIRES
#REMARQUES:
#1: Si on met un melange à parité dans le testeur, le shuffle de celui la donnera toujours un melange à parité = La parité est invariante par le shuffle


##
##                  Sur commande
def Commande(L,Cube):
    CubeCommande=Createur(L,Cube)
    CubeCommandeCheck=Createur(L,Cube)
    Ecran_de_controle(CubeCommande,L)
##
##                              Commande de cube sauvage
# Cubeur=Createur("FUFUBUBURURULULU",Cube)
def EAsy_cube(L):
    Rt=array([[L[0],L[1],L[2]],[L[3],1,L[4]],[L[5],L[6],L[7]]])
    Vt=array([[L[8],L[9],L[10]],[L[11],2,L[12]],[L[13],L[14],L[15]]])
    Ot=array([[L[16],L[17],L[18]],[L[19],3,L[20]],[L[21],L[22],L[23]]])
    Bleut=array([[L[24],L[25],L[26]],[L[27],4,L[28]],[L[29],L[30],L[31]]])
    Jt=array([[L[32],L[33],L[34]],[L[35],5,L[36]],[L[37],L[38],L[39]]])
    Blanct=array([[L[40],L[41],L[42]],[L[43],6,L[44]],[L[45],L[46],L[47]]])
    easyCube=[Rt,Vt,Ot,Bleut,Jt,Blanct]
    return(easyCube)
Cubeur=Createur("brfdbruflddfudlfbbulrfl",Cube)   #probleme sur la liste avec parité mais ça marche dans le code
Cubeu=copy(Cubeur)
Compa=ThePath(Cubeu)
Comp=Compacteur(Compa)
# print(Comp)
# print(len(Comp))
# Ecran_de_controle(Cubeu,"Cube sauvage")
# for i in Comp:
    # MouvX(i,Cubeur)
# print(resolu(Cubeur))
##
##
##                                      Roux 
# La résolution est ici basée sur le principe de la methode Roux (du speedcuber français Gilles Roux né en 1971)
##
##
#Formules requises
#Orientations:
U_orient="FRUruf"
T_orient="RmUrurMFRf"
Pi_orient="FRUruRUruf"
Sune_orient="RUrURuur"
Antisune_orient="luLuluuL"
H_orient="RuuruRUruRur"
Sousmarin_orient="FRuruRUrf"
#Permutations:
Diag_perm="FRuruRUrfRUrurFRf"
Droite_perm="RUrfRUrurFRRur"
#Arrêtes finales:
Centres_final="eemeeM"
AngleB_final="uumuu"
AngleF_final="uuMuu"
Barres_final="uummuu"


#Pour commencer, il faut positionner le cube avec le centre blanc en bas et centre bleu à gauche:
def Positionnement(Cube):
    i=0
    L=""
    if Cube[5][1][1]==6 and Cube[1][1][1]==4:
        return(Cube)
    while Cube[5][1][1]!=6 and i<3:
        z(Cube)
        i+=1
        L=L+"Z"
    if i==3:     #Le blanc est donc soit devant ou derriere
        if not Cube[5][1][1]==6: #le blanc est deja sur la face du bas
            if Cube[1][1][1]==6:
                x1(Cube)
                L=L+"x"
            else :
                x(Cube)
                L=L+"X"
    while Cube[0][1][1]!=4 : #Le bleu est sur la ceinture, il suffit de tourner 
        y(Cube)
        L=L+"Y"
    return(Cube,L)


#Il faut desormais trouver l'arrete (Blanche,Bleu) et la placer, former la paire {(Bleu,Blanc,Rouge)+(Bleu,Rouge)} et la placer, et enfin la paire {(Bleu,Blanc,Orange)+(Bleu,Orange)] et la placer pour obtenir notre premier bloc!

##
##          Arrêtes Roux


def Creer_Dico_Universel(L):  #Crée le dictionaire d'arretes associé à la liste d'arretes + orientation des arretes (inversé par rapport au résolu = minuscule)  #Universel car il prend en compte l'orientation contrairement au précédent
    Dico="ABCDEFGHIJKL"
    Dico_Inv="abcdefghijkl"
    NewDico=""
    L_Arretes_Resolu=[[5,1],[5,4],[5,3],[5,2],[1,4],[3,4],[3,2],[1,2],[6,1],[6,4],[6,3],[6,2]]
    L_Arretes_Resolu_Inv=[[1,5],[4,5],[3,5],[2,5],[4,1],[4,3],[2,3],[2,1],[1,6],[4,6],[3,6],[2,6]]
    for i in range(12):
        for j in range(12):
            if L[i]==L_Arretes_Resolu[j]:
                NewDico=NewDico+Dico[j]
            if L[i]==L_Arretes_Resolu_Inv[j]:
                NewDico=NewDico+Dico_Inv[j]
    return(NewDico)
    
    
# L'arrete bleu blanc a donc pour denomination la lettre J ou j
#Vert,blanc=L,l
# Rouge,bleu=E,e     #Orange,bleu=F,f     #Vert,orange=G,g    #Vert,Rouge=H,h   



def Detector_Arrete(Arrête,Cube):  #Detecte l'arrete et renvoie sa lettre orienté de position (Exemple: Detector(E,Cube)=f indique que la E(Rouge,bleu)=[1,4] est en position f donc rouge,bleu est en F inv. La requete de l'arrete se fait toujours en MAJUSCULE      Arrête={A,B,C,D,E,F,G,H,I,J,K,L}
    Dico="ABCDEFGHIJKL"
    Dico_Inv="abcdefghijkl"
    Pos=0     #Cette variable va prendre l'indice de l'arrete commandée
    for j in range(len(Dico)):
        if Dico[j]==Arrête:
            Pos=j
    L_arretes=L_Arretes(Cube)
    Dico_Universel=Creer_Dico_Universel(L_arretes)
    for i in range(len(Dico_Universel)):
        if Dico_Universel[i]==Dico[Pos]:
            return(Dico[i])
        if Dico_Universel[i]==Dico_Inv[Pos]:
            return(Dico_Inv[i])
            
            
            
##
##              Coins Roux


def Chaineur(L):  #transforme la liste [1,2,3,4,5,6] en ["1","2","3","4","5","6"]    Fonction requise pour la prochaine fonction
    nombres_chaines=[]
    for i in L:
        if i==1:
            nombres_chaines=nombres_chaines+["1"]
        if i==2:
            nombres_chaines=nombres_chaines+["2"]
        if i==3:
            nombres_chaines=nombres_chaines+["3"]
        if i==4:
            nombres_chaines=nombres_chaines+["4"]
        if i==5:
            nombres_chaines=nombres_chaines+["5"]
        if i==6:
            nombres_chaines=nombres_chaines+["6"]
    return(nombres_chaines)



def L_Coins_Roux(Cube):  #Renvoie la liste des coins du cube   ##Attention ici les numeros des coins sont assignés différement par rapport à la précedente methode: le coin 1 correspond ici au précédent coin 2, le coin 2 au coin 3 etc.... et le coin 5 correspond au précédent coin 6 et de même. Sinon le codage des coins reste le même
    L_Coins=[]  #Liste des coins
    #Notation : [[Couleur orientée,Couleur sens horaire, Couleur sens trigo ],[    ,    ,   ],...]=[1,2,3,4,5,6,7,8] sous forme de liste de chaînes :["514",...,,"261"]
    L_Coins=L_Coins+[[Cube[4][2][0],Cube[1][0][0],Cube[0][0][2]]]+[[Cube[4][0][0],Cube[0][0][0],Cube[3][0][2]]]+[[Cube[4][0][2],Cube[3][0][0],Cube[2][0][2]]]+[[Cube[4][2][2],Cube[2][0][0],Cube[1][0][2]]]  #Coins du haut:1,2,3,4
    L_Coins=L_Coins+[[Cube[5][0][0],Cube[0][2][2],Cube[1][2][0]]]+[[Cube[5][2][0],Cube[3][2][2],Cube[0][2][0]]]+[[Cube[5][2][2],Cube[2][2][2],Cube[3][2][0]]]+[[Cube[5][0][2],Cube[1][2][2],Cube[2][2][0]]]  #Coins du bas: 5,6,7,8
    L_Coins_Roux=["","","","","","","",""]   #On souhaite maintenant convertir la lsite [[5,1,4]],...[2,6,1]] en ["514",...,,"261"]
    for i in range(8):
        for j in range(3):    
            coin_inter=Chaineur(L_Coins[i])  #[5,1,4] vers ["5","1","4"]
            coin=coin_inter[0]+coin_inter[1]+coin_inter[2]    #["5","1","4"] vers ["514"]
        L_Coins_Roux[i]=L_Coins_Roux[i]+coin       #formation de la liste en additionant les differents coins : ["514"]+["521"]+...=["514","521",...]
    return(L_Coins_Roux)



#on code o: orienté  t:trigo  h:horaire   Exemple1: "532" (Jaune,Orange,Vert) est codé [3,"o"]    Exemple2: "215" (Vert,Rouge,Jaune) est codé [4,"t"]: le coin est tourné dans le sens trigo par rapport a sa version orientée. Dans la liste Dicoin_Roux au dessus, les coins sont disposés selon l'ordre 1o,1t,1h ,2o,2t,2h etc...

##Codex des coins résolus: 
#l'ordre des couleures enoncées est pris en compte (o,t,h) cf un peu plus bas 

            #haut                         #bas
    #jaune,rouge,bleu : 1           #blanc,bleu,rouge  :5
       #jrb =[1,"o"]="514"              #bbr =[5,"o"]="641"
       #rbj =[1,"t"]="145"              #brb =[5,"t"]="416"
       #bjr =[1,"h"]="451"              #rbb =[5,"h"]="164"
    
    #jaune,bleu,orange: 2           #blanc,orange,bleu :6
       #jbo =[2,"o"]="543"              #bob =[6,"o"]="634"
       #boj =[2,"t"]="435"              #obb =[6,"t"]="346"
       #ojb =[2,"h"]="354"              #bbo =[6,"h"]="463"
        
    #jaune,orange,vert: 3           #blanc,vert,orange :7
       #jov =[3,"o"]="532"              #bvo =[7,"o"]="623"
       #ovj =[3,"t"]="325"              #vob =[7,"t"]="236"
       #vjo =[3,"h"]="253"              #obv =[7,"h"]="362"
    
    #jaune,vert,rouge : 4           #blanc,rouge,vert  :8
       #jvr =[4,"o"]="521"              #brv =[8,"o"]="612"
       #vrj =[4,"t"]="215"              #rvb =[8,"t"]="126"
       #rjv =[4,"h"]="152"              #vbr =[8,"h"]="261"
        



def Codeur_Coin(Coin): #Prend comme argument un coin de la forme "514" et le renvoie codé [1,"o"]
    Codage="oth"
    Liste=[["514","145","451"],  ["543","435","354"],  ["532","325","253"],  ["521","215","152"],  ["641","416","164"],  ["634","346","463"],  ["623","236","362"],  ["612","126","261"]]
    for i in range(8):
        for j in range(3):
            if Liste[i][j]==Coin:
                return([i+1,Codage[j]])
                


def L_Coins_Codes_Roux(Cube):  #Crée l'equivalent du  dictionaire d'arrêtes universel associé à la liste de coin, de la forme [[8,"h"],[1,"t"],[4,"o"],...] de longeur 8
    L_Coins=L_Coins_Roux(Cube)
    L_Coins_Codes=[]
    for i in range(8):    #Création de la liste des coins codés du cube de la forme [[1,"o"],[2,"o"],[3,"o"],[4,"o"],[5,"o"],[6,"o"][7,"o"],[8,"o"]]
        L_Coins_Codes=L_Coins_Codes+[Codeur_Coin(L_Coins[i])]
    return(L_Coins_Codes)



def Detecteur_De_Position_Coin(Coin_Code,Cube):  #donne la position du coin sur le cube   Exemple :  si je cherche le coin rouge,bleu,blanc orienté [5,"o"] et que celui ci est à la position 1 du cube (intersection des faces F,L,U  Devant,Gauche,Supérieure) la fonction renvoie 1
    Liste_des_Coins=L_Coins_Codes_Roux(Cube)   #on se donne la liste des coins du cube
    for i in range(len(Liste_des_Coins)):
        if Liste_des_Coins[i]==Coin_Code:
            return(i+1)    



def Detector_De_Position_Coin_Simple(Coin,Cube): #Même principe que le précédent Detector : Coin={1,2,3,4,5,6,7,8} (ici nombre) et renvoie sa position, la difference par rapport a la précédente fonction est que l'on ne se soucie pas de l'orientation
    Liste_des_Coins=L_Coins_Codes_Roux(Cube)
    for i in range(len(Liste_des_Coins)):
        if Liste_des_Coins[i][0]==Coin:
            return(i+1)



def Detector_Coin(Coin,Cube): #Même principe que le précédent Detector : Coin={1,2,3,4,5,6,7,8} (ici nombre) et renvoie le code associé [nombre,"orientation"] Exemple : si on veut savoir où est le coin 2 (de couleurs jaune,bleu,orange) et que la fonction renvoie [4,"h"], cela signifie que le coin jaune bleu orange est en orientation h et à la position 4
    Dico_o=[[1,"o"],[2,"o"],[3,"o"],[4,"o"],[5,"o"],[6,"o"],[7,"o"],[8,"o"]]
    Dico_t=[[1,"t"],[2,"t"],[3,"t"],[4,"t"],[5,"t"],[6,"t"],[7,"t"],[8,"t"]]
    Dico_h=[[1,"h"],[2,"h"],[3,"h"],[4,"h"],[5,"h"],[6,"h"],[7,"h"],[8,"h"]]
    L_Coins=L_Coins_Codes_Roux(Cube)
    Pos=Coin-1   #Cette variable va prendre l'indice du coin commandée
    for i in range(len(L_Coins)):
        if L_Coins[i]==Dico_o[Pos]:
            return(Dico_o[i])
        if L_Coins[i]==Dico_t[Pos]:
            return(Dico_t[i])
        if L_Coins[i]==Dico_h[Pos]:
            return(Dico_h[i])



## Fonctions annexes d'apairage

    
    
def Mettre_A_Niveau(Coin_Code,Cube): #renvoie la liste de mouvements qui permet de mettre le coin(qui respecte deja les conditions premieres d'apairage:etre en haut et non orienté) sur le bon niveau (niveau 1: 1 ou 4//niveau 2: 2 ou 3) selon la correspondance avec l'arrete et le nouveau code du coin mis à niveau
    Pos_Coin_Code=Detecteur_De_Position_Coin(Coin_Code,Cube)
    Sticker_Arrete_Visible=Cube[1][2][1]     #Visible = sur la face avant (face F)
    L=""
    if Pos_Coin_Code==1:   #obligé de faire 4 cas pour les positions 1,2,3,4, il aurait idéal de faire un boucle à 4 tours mais pas de motif regulier dans l'expression du sticker coin qui pointe vers le haut(hormis le fait qu'il soit sur la face du haut U)
    #OBJECTIF : Stickers concernées identiques implique Niveau 1 ----- Stickers concernés differents implique Niveau 2 
        if Sticker_Arrete_Visible!=Cube[4][2][0]:   #pas au bon niveau, il faut que le sticker du coin qui pointe vers le haut possède la meme couleur que le sticker visible de l'arrete en I                            #Niveau 1 vers niveau 2
            L="U"
    if Pos_Coin_Code==2:                            #Niveau 2 vers niveau 1
        if Sticker_Arrete_Visible==Cube[4][0][0]:  
            L="u"
    if Pos_Coin_Code==3:
        if Sticker_Arrete_Visible==Cube[4][0][2]: #Niveau 2 vers niveau 1
            L="U"
    if Pos_Coin_Code==4:
        if Sticker_Arrete_Visible!=Cube[4][2][2]: #Niveau 1 vers niveau 2
            L="u"
    return(L)
        
#"L'intelligence, envisagée dans ce qui en paraît être la démarche originelle, est la faculté de fabriquer des objets artificiels, en particulier des outils à faire des outils, et d'en varier indéfiniment la fabrication." Bergson, L'évolution créatrice
        
def TestOrientationExterne(Coin_Code,Cube): #renvoie True si le coin a le sticker blanc ou jaune vers l'exterieur et False sinon  #Fonction annexe de la fonction Apairage
    Pos_Coin_Code=Detecteur_De_Position_Coin(Coin_Code,Cube)  #on a besoin de connaitre où est le coin
    if Pos_Coin_Code==1 or Pos_Coin_Code==3:
        if Coin_Code[1]=="t":
            return(True)
    if Pos_Coin_Code==2 or Pos_Coin_Code==4:
        if Coin_Code[1]=="h":
            return(True)
    return(False)
    
    
    
def OrientationExterne(Coin_Code,MouvementPrecedent,Cube): #renvoie la liste de mouvements permetant d'orienter le coin vers l'exterieur sachant qu'il est deja au bon niveau, ainsi après cette fonction le coin est pret à etre apairé
    Cube=copy(Cube)  #Il ne faut pas encore modifier le cube
    MouvX(MouvementPrecedent,Cube)
    Pos_Coin_Code=Detecteur_De_Position_Coin(Coin_Code,Cube)
    L=""
    if not TestOrientationExterne(Coin_Code,Cube): #On agit seulement si il y a problème
        if Pos_Coin_Code==1:    #il faut aller en 4
            L="u"                                          #Dans le Niveau 1
        if Pos_Coin_Code==4:    #il faut aller en 1
            L="U"
        if Pos_Coin_Code==2:    #il faut aller en 3
            L="U"                                          #Dans le Niveau 2
        if Pos_Coin_Code==3:    #il faut aller en 2
            L="u"
    return(L)
        


def Apairage(Coin_Code,Cube): #Apaire (forme une paire) le coin et l'arrête qui sont dans des conditions favorables ( coin non orienté sur le haut et arrête en I), la strategie est la suivante: Mettre le coin à niveau, et ensuite lui donner l'orientation externe (sticker blanc/jaune qui pointe vers l'exterieur Note:un coin peut donc possèder cette fameuse "orientation externe" tout en étant non-orienté au premier sens du terme: sticker blanc/jaune vers le haut)
    #Observation importante: on remarque que la fonction apairage n'a point besoin de la variable arrete alors que pourtant l'apairage concerne le coin ET l'arrete, cependant nous savons que l'arrete se situe en I, donc elle n'est pas une variable à proprement parler, nous pouvons récupérer ses informations de couleur avec les commande Cube[1][2][1] pour le sticker visible et Cube[5][0][1] pour le sticker du bas
    Paire=0
    Premier_Mouv,DeuxiemeMouv,L="","",""
    PremierMouv=Mettre_A_Niveau(Coin_Code,Cube)
    DeuxiemeMouv=OrientationExterne(Coin_Code,PremierMouv,Cube)
    L=L+PremierMouv+DeuxiemeMouv
    CubeCopie=copy(Cube)
    for i in L:
        MouvX(i,CubeCopie)
    Position=Detecteur_De_Position_Coin(Coin_Code,CubeCopie)
    if Position==1:   #Apairage avec le coin 1, on note cette paire formée 1 de telle manière à connaitre l'emplacement de la paire pour la suite
        L=L+"m"
        Paire=1                                             
    if Position==2: 
        L=L+"mm"
        Paire=2
    if Position==3:
        L=L+"mm"
        Paire=3
    if Position==4:
        L=L+"m"
        Paire=4
    return(L,Paire)
    
    

##
##Partie 1 : Premier bloc


def Premier_Bloc_Roux(Cube):
    L=""
    Grand_Dico="ABCDEFGHIJKLabcdefghijkl"
    Bleu_Blanc=["ULL","LL","uLL","uuLL","L","l","Rdd","rdd","d","","D","dd","fL","ufL","Bl","UfL","fd","BD","bD","Fd","FL","lfd","bl","RFd"]
    Vers_I=["M","uM","mm","UM","luLM","LulM","rURM","RUrM","","Cas J impossible","m","RRUM","M","uM","mm","UM","luLM","LulM","rURM","RUrM","","Cas J impossible","m","RRUM"]
    Full_Coins_Codes=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    Vers_le_haut=["uurUR", "",  "",    "UrUR","",   "",    "rUR", "",  "",     "urUR",   "",  "",  "luL","lUL","luL",  "LUl","LUl","Lul",  "ruR","rUR","ruR",  "RUr","RUr","Rur"]
    Sol_PaireRougeBleu=["lmuL","uulUL","uulmuL","lUL"]
    ##Bleu--Blanc
    #il y a 24 cas possibles pour blanc,bleu(12*2), chacun se resout en moins de 3 mouvs HTM
    #Bleu_Blanc=["A","B","C","D","E","F","G","H","I","J","K","L","a","b","c","d","e","f","g",h",i",j","k","l"]
    bleublanc=Detector_Arrete("J",Cube)  #position de la bleublanc
    for i in range(len(Grand_Dico)):
        if bleublanc==Grand_Dico[i]:
            sol_bleublanc=i     #indice de la solution
    L=L+Bleu_Blanc[sol_bleublanc]   #compilation de la liste du premier bloc
    for i in Bleu_Blanc[sol_bleublanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    #il y a 22 cas possibles restants pour amener l'arrête vers I mais on fait une liste à 24 solutions pour que le lien avec Grand_Dico fonctionne
    #Vers_I=["A","B","C","D","E","F","G","H","I","J","K","L","a","b","c","d","e","f","g","h","i","j","k","l"]
    #on cherche juste à amener l'arrete en I mais pas besoin de porter attention à l'orientation, celle ci sera réglée dans l'apairage (ie la moitiée des solutions dans Vers_I sont identiques(A=a,B=b,...L=l))

    ##Rouge--Bleu
    rougebleu=Detector_Arrete("E",Cube)
    for i in range(len(Grand_Dico)):   #Recherche de la solution associée
        if rougebleu==Grand_Dico[i]:
            sol_rougebleu=i
    L=L+Vers_I[sol_rougebleu]     #Arrete rougebleu en I
    for i in Vers_I[sol_rougebleu]:  #On fait bouger le cube
        MouvX(i,Cube)
    #Amène le coin sur la face supérieure    
    # Vers_le_haut=["514","145","451",  "543","435","354",  "532","325","253",  "521","215","152",  "641","416","164",  "634","346","463",  "623","236","362",  "612","126","261"] 
    #ou encore Vers_le_haut=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    RougeBleuBlanc=Detector_Coin(5,Cube)
    for i in range(len(Full_Coins_Codes)):     #Recherche de la solution associée pour amener le coin en haut (et avec une "bonne" orientation ie pas orienté pour ensuite pouvoir être apairé avec l'arrête rougebleu deja mise en I
        if RougeBleuBlanc==Full_Coins_Codes[i]:
            sol_RougeBleuBlanc=i
    L=L+Vers_le_haut[sol_RougeBleuBlanc]     #Coin RougeBleuBlanc quelque part en haut et non orienté (très important)
    for i in Vers_le_haut[sol_RougeBleuBlanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    #IL FAUT DESORMAIS APAIRER ROUGE BLEU ET ROUGE BLEU BLANC
    #Etape 1 : le trouver
    RougeBleuBlancHaut=[5,Detector_Coin(5,Cube)[1]]
    #Etape 2 : Apairer
    ResultatsRBB=Apairage(RougeBleuBlancHaut,Cube)  #On s'assure de ne faire appel à cette fonction le minimum requis car ça commence à devenir assez complexe
    ApairageRougeBleu,PaireRougeBleu=ResultatsRBB[0],ResultatsRBB[1]
    L=L+ApairageRougeBleu
    for i in ApairageRougeBleu:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape3 : il faut placer la paire dans son emplacement, la paire à été formé en 1,2,3 ou 4, on crée donc la liste des solutions pour PaireRougeBleu:
    Placement_PaireRougeBleu=Sol_PaireRougeBleu[PaireRougeBleu-1]
    L=L+Placement_PaireRougeBleu
    for i in Placement_PaireRougeBleu:  #On fait bouger le cube, la paire RougeBleu est placée!! 
        MouvX(i,Cube)
    ##Orange--Bleu
    orangebleu=Detector_Arrete("F",Cube)
    for i in range(len(Grand_Dico)):   #Recherche de la solution associée
        if orangebleu==Grand_Dico[i]:
            sol_orangebleu=i
    L=L+Vers_I[sol_orangebleu]     #Arrete orangebleu en I
    for i in Vers_I[sol_orangebleu]:  #On fait bouger le cube
        MouvX(i,Cube)
    #Amène le coin sur la face supérieure    
    # Vers_le_haut=["514","145","451",  "543","435","354",  "532","325","253",  "521","215","152",  "641","416","164",  "634","346","463",  "623","236","362",  "612","126","261"] 
    #ou encore Vers_le_haut=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    Full_Coins_Codes=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    Vers_le_haut=["uurUR", "",  "",    "UrUR","",   "",    "rUR", "",  "",     "urUR",   "",  "",  "luL","lUL","luL",  "LUl","LUl","Lul",  "ruR","rUR","ruR",  "RUr","RUr","Rur"]
    OrangeBleuBlanc=Detector_Coin(6,Cube)
    for i in range(len(Full_Coins_Codes)):     #Recherche de la solution associée pour amener le coin en haut (et avec une "bonne" orientation ie pas orienté pour ensuite pouvoir être apairé avec l'arrête orangebleu deja mise en I
        if OrangeBleuBlanc==Full_Coins_Codes[i]:
            sol_OrangeBleuBlanc=i
    L=L+Vers_le_haut[sol_OrangeBleuBlanc]     #Coin OrangeBleuBlanc quelque part en haut et non orienté (très important)
    for i in Vers_le_haut[sol_OrangeBleuBlanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape 1 : le trouver
    OrangeBleuBlancHaut=[6,Detector_Coin(6,Cube)[1]]
    #Etape 2 : Apairer
    ResultatsOBB=Apairage(OrangeBleuBlancHaut,Cube)  #On s'assure de ne faire appel à cette fonction le minimum requis car ça commence à devenir assez complexe
    ApairageOrangeBleu,PaireOrangeBleu=ResultatsOBB[0],ResultatsOBB[1]
    L=L+ApairageOrangeBleu
    for i in ApairageOrangeBleu:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape 3 : il faut placer la paire dans son emplacement, la paire à été formé en 1,2,3 ou 4, on crée donc la liste des solutions pour PaireOrangeBleu:
    Sol_PaireOrangeBleu=["uuLul","LMUl","Lul","uuLMUl"] #liste de sols differente car emplacement d'arrivée different
    Placement_PaireOrangeBleu=Sol_PaireOrangeBleu[PaireOrangeBleu-1]
    L=L+Placement_PaireOrangeBleu
    for i in Placement_PaireOrangeBleu:  #On fait bouger le cube, la paire OrangeBleu est placée!! 
        MouvX(i,Cube)
    #TADAA!! Voici le premier bloc!
    return(L,Cube)
    
    
    
##Partie 2 : Second bloc


def Second_Bloc_Roux(Cube):   #C'est reparti pour un tour, globalement c'est pareil excépté les listes de Sol_Paire et la solution pour placer Vert_Blanc
    #Récupération des precieuses liste réutilisables fabriquées pour cela 
    Vers_I=["M","uM","mm","UM","luLM","LulM","rURM","RUrM","","Cas J impossible","m","RRUM","M","uM","mm","UM","luLM","LulM","rURM","RUrM","","Cas J impossible","m","RRUM"]
    Vers_le_haut=["uurUR", "",  "",    "UrUR","",   "",    "rUR", "",  "",     "urUR",   "",  "",  "luL","lUL","luL",  "LUl","LUl","Lul",  "ruR","rUR","ruR",  "RUr","RUr","Rur"]
    #Nouvelles listes: placer l'arrete vert blanche, comme la bleu blanche du premier bloc, sur le coté gauche cette fois, et sans detruire le travail précedent
    Vert_Blanc=["urr","uurr","Urr","rr","E impossible","F impossible","R","r","mmUrr","J impossible","mmurr","","mUrr","umUrr","Murr","UmUrr","e impossible","f impossible","rUmUrr","RUmUrr","murr","j impossible","MUrr","RRUmUrr"]
    Sol_PaireRougeVert=["Rur","UURmUr","uuRur","RmUr"]
    Sol_PaireOrangeVert=["uurMuR","rUR","rMuR","uurUR"]
    
    L=""
    Grand_Dico="ABCDEFGHIJKLabcdefghijkl"
    Full_Coins_Codes=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    ##Vert--Blanc
    vertblanc=Detector_Arrete("L",Cube)  #position de la vertblanc
    for i in range(len(Grand_Dico)):
        if vertblanc==Grand_Dico[i]:
            sol_vertblanc=i     #indice de la solution
    L=L+Vert_Blanc[sol_vertblanc]   #compilation de la liste du second bloc
    for i in Vert_Blanc[sol_vertblanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    ##Rouge--Vert
    rougevert=Detector_Arrete("H",Cube)
    for i in range(len(Grand_Dico)):   #Recherche de la solution associée
        if rougevert==Grand_Dico[i]:
            sol_rougevert=i
    L=L+Vers_I[sol_rougevert]     #Arrete rougevert en I
    for i in Vers_I[sol_rougevert]:  #On fait bouger le cube
        MouvX(i,Cube)
    RougeVertBlanc=Detector_Coin(8,Cube)
    for i in range(len(Full_Coins_Codes)):     #Recherche de la solution associée pour amener le coin en haut (et avec une "bonne" orientation ie pas orienté pour ensuite pouvoir être apairé avec l'arrête rougevert deja mise en I
        if RougeVertBlanc==Full_Coins_Codes[i]:
            sol_RougeVertBlanc=i
    L=L+Vers_le_haut[sol_RougeVertBlanc]     #Coin RougeVertBlanc quelque part en haut et non orienté (très important)
    for i in Vers_le_haut[sol_RougeVertBlanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    #IL FAUT DESORMAIS APAIRER ROUGE VERT ET ROUGE VERT BLANC
    #Etape 1 : le trouver
    RougeVertBlancHaut=[8,Detector_Coin(8,Cube)[1]]
    #Etape 2 : Apairer
    ResultatsRVB=Apairage(RougeVertBlancHaut,Cube)  #On s'assure de ne faire appel à cette fonction le minimum requis car ça commence à devenir assez complexe
    ApairageRougeVert,PaireRougeVert=ResultatsRVB[0],ResultatsRVB[1]
    L=L+ApairageRougeVert
    for i in ApairageRougeVert:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape3 : il faut placer la paire dans son emplacement, la paire à été formé en 1,2,3 ou 4, on crée donc la liste des solutions pour PaireRougeVert:
    Placement_PaireRougeVert=Sol_PaireRougeVert[PaireRougeVert-1]
    L=L+Placement_PaireRougeVert
    for i in Placement_PaireRougeVert:  #On fait bouger le cube, la paire RougeVert est placée!! 
        MouvX(i,Cube)
    ##Orange--Vert
    orangevert=Detector_Arrete("G",Cube)
    for i in range(len(Grand_Dico)):   #Recherche de la solution associée
        if orangevert==Grand_Dico[i]:
            sol_orangevert=i
    L=L+Vers_I[sol_orangevert]     #Arrete orangevert en I
    for i in Vers_I[sol_orangevert]:  #On fait bouger le cube
        MouvX(i,Cube)
    #Amène le coin sur la face supérieure    
    # Vers_le_haut=["514","145","451",  "543","435","354",  "532","325","253",  "521","215","152",  "641","416","164",  "634","346","463",  "623","236","362",  "612","126","261"] 
    #ou encore Vers_le_haut=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    Full_Coins_Codes=[[1,"o"],[1,"t"],[1,"h"],     [2,"o"],[2,"t"],[2,"h"],      [3,"o"],[3,"t"],[3,"h"],        [4,"o"],[4,"t"],[4,"h"],        [5,"o"],[5,"t"],[5,"h"],        [6,"o"],[6,"t"],[6,"h"],        [7,"o"],[7,"t"],[7,"h"],     [8,"o"],[8,"t"],[8,"h"]]
    Vers_le_haut=["uurUR", "",  "",    "UrUR","",   "",    "rUR", "",  "",     "urUR",   "",  "",  "luL","lUL","luL",  "LUl","LUl","Lul",  "ruR","rUR","ruR",  "RUr","RUr","Rur"]
    OrangeVertBlanc=Detector_Coin(7,Cube)
    for i in range(len(Full_Coins_Codes)):     #Recherche de la solution associée pour amener le coin en haut (et avec une "bonne" orientation ie pas orienté pour ensuite pouvoir être apairé avec l'arrête orangevert deja mise en I
        if OrangeVertBlanc==Full_Coins_Codes[i]:
            sol_OrangeVertBlanc=i
    L=L+Vers_le_haut[sol_OrangeVertBlanc]     #Coin OrangeVertBlanc quelque part en haut et non orienté (très important)
    for i in Vers_le_haut[sol_OrangeVertBlanc]:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape 1 : le trouver  
    OrangeVertBlancHaut=[7,Detector_Coin(7,Cube)[1]]
    #Etape 2 : Apairer
    ResultatsOVB=Apairage(OrangeVertBlancHaut,Cube)  #On s'assure de ne faire appel à cette fonction le minimum requis car ça commence à devenir assez complexe
    ApairageOrangeVert,PaireOrangeVert=ResultatsOVB[0],ResultatsOVB[1]
    L=L+ApairageOrangeVert
    for i in ApairageOrangeVert:  #On fait bouger le cube
        MouvX(i,Cube)
    #Etape 3 : il faut placer la paire dans son emplacement, la paire à été formé en 1,2,3 ou 4, on crée donc la liste des solutions pour PaireOrangeVert:
    Placement_PaireOrangeVert=Sol_PaireOrangeVert[PaireOrangeVert-1]
    L=L+Placement_PaireOrangeVert
    for i in Placement_PaireOrangeVert:  #On fait bouger le cube, la paire OrangeVert est placée!! 
        MouvX(i,Cube)
    #TADAA!! Voici le second bloc!
    return(L,Cube)



def Checker2(Cube): #Verifie si les deux blocs sont formés correctement
    if not (Cube[0][1][0],Cube[0][1][1],Cube[0][1][1],Cube[0][2][0],Cube[0][2][1],Cube[0][2][2])==(4,4,4,4,4,4):   #les bleus
        return(False)
    if not (Cube[2][1][0],Cube[2][1][1],Cube[2][1][1],Cube[2][2][0],Cube[2][2][1],Cube[2][2][2])==(2,2,2,2,2,2):   #les verts
        return(False)
    if not (Cube[5][0][0],Cube[5][2][0],Cube[5][0][2],Cube[5][2][2])==(6,6,6,6):   #les blancs
        return(False)
    if not (Cube[1][1][0],Cube[1][2][0],Cube[1][1][2],Cube[1][2][2])==(1,1,1,1):   #les rouges
        return(False)
    if not (Cube[3][1][0],Cube[3][2][0],Cube[3][1][2],Cube[3][2][2])==(3,3,3,3):   #les oranges
        return(False)
    return(True)



##Partie 3 : Les coins supérieurs



def Generateur_Seq(Cube):
    L_Coins=L_Coins_Codes_Roux(Cube)
    Seq=""
    for i in range(4):
        Seq=Seq+L_Coins[i][1]
    return(Seq)



def CheckerOrient(Cube):   #Verifie l'orientation des 4 coins du haut
    if not (Cube[4][0][0],Cube[4][2][0],Cube[4][0][2],Cube[4][2][2])==(5,5,5,5):   #les jaunes
        return(False)
    return(True)
    


def Generateur_Suite_Code(Cube):  #Creation de la liste de taille 8 qui indique si deux stickers des cotés sur la même face ont la même couleur (1 dans ce cas, 0 sinon)  Exemple: Le cube résolu a la liste [1,1,1,1,1,1,1,1] qu'il faut comprendre comme "les stickers des coins du haut sur la face gauche ont la même couleur et de même pour les 3 autres faces laterales
    Suite=(Cube[0][0][2],Cube[0][0][0],Cube[3][0][2],Cube[3][0][0],Cube[2][0][2],Cube[2][0][0],Cube[1][0][2],Cube[1][0][0])
    Suite_Code=[]
    for i in range(0,8,2):
        if Suite[i]==Suite[i+1]:
            Suite_Code=Suite_Code+[1,1]
        else:
            Suite_Code=Suite_Code+[0,0]
    return(Suite_Code)



def Checker_Coins_Roux(Cube):  #Verifie la partie 3 en entière (coins orientés et bonne position relative)
    if Generateur_Suite_Code(Cube)==[1,1,1,1,1,1,1,1]:
        return(True)
    return(False)
     
     
    
def Orientation_Coins_Roux(Cube):
    #On peut identifier les 7 cas possibles d'orientation à l'aide de la notation précédente sur les orientations, avec dans l'ordre les coins 1,2,3 et 4
    #U="thoo"   T="htoo"  Pi="thht"   Sune="ottt"  AntiSune="hhho"   H="htht"  Sousmarin="hoto"  id="oooo"
    L=""
    Banque=["thoo","htoo","thht","ottt","hhho","htht","hoto","oooo"]
    Sol_Banque=["FRUruf","RmUrurMFRf","FRUruRUruf","RUrURuur","luLuluuL","RuuruRUruRur","FRuruRUrf",""]
    Detecteur=27
    nb_tours=0
    while Detecteur!=1:
        nb_tours+=1
        if L=="":    #tour de passe passe pour régler un probleme de la boucle (le premier tour ne doit pas etre ajusté car c'est peu etre deja bon)
            L=L+"_"  
        else:
            L=L+"u"    #ajustement
            MouvU1(Cube) 
        Seq=Generateur_Seq(Cube)    #on genere la sequence d'orientation des coins
        for i in range(8):       #on regarde les 7 cas possibles
            if Banque[i]==Seq:   #le cube est bien ajusté
                Detecteur=1      #on ferme la boucle
                L=L+Sol_Banque[i]  #on prend la solution
    L=L[1:]  #liste réajusté (le _ en moins)
    for j in L[nb_tours-1:]:   #On fait tourner, mais on ne prend pas en compte les nb_tours-1 premiers termes car ils ont deja été utilisés plus haut(MouvU1)
        MouvX(j,Cube)
    return(L)



def Perm_Coin_Roux(Cube):
    #Soit c'est deja bon, soit c'est en condition de perm laterale (4 cas), soit c'est la perm diagoanle
    if Checker_Coins_Roux(Cube):
        return("")
    Suite_Code=Generateur_Suite_Code(Cube)
    Setup=["","u","uu","U"]
    for i in range(0,8,2):
        if Suite_Code[i]==1:
            L=Setup[i//2]+"RUrfRUrurFRRur"
            for j in L:
                MouvX(j,Cube)
            return(L)
    L="FRuruRUrfRUrurFRf"
    for i in L:
            MouvX(i,Cube)
    return(L)


            
##Partie 4: Orientation des 6 arrêtes restantes



def L_Six_Arretes(Cube): #renvoie la liste des 6 arretes ABCDIK en lettres
    L=Creer_Dico_Universel(L_Arretes(Cube))
    return(L[0]+L[1]+L[2]+L[3]+L[8]+L[10])



def Code_Orientation(Cube): #renvoie une liste de taille 6 avec 1 si l'arrete est orientée, et 0 sinon Exemple: [0,1,0,1,1,1] indique que A n'est pas orientée, et C non plus mais le reste est orienté. Remarque: les proprités du cube imposent que le nombre d'arretes orientées/on orientées soit pair : [0,1,0,0,1,1] n'existe pas(sauf si on à volontairement inversé une piece à la main)
    L=L_Six_Arretes(Cube)
    Code=""
    Dico="ABCDIK"
    Dico_Inv="abcdik"
    for i in range(6):
        for j in range(6):
            if L[i]==Dico[j]:
                Code=Code+"1"
            if L[i]==Dico_Inv[j]:
                Code=Code+"0"
    return(Code)
    
    

def Orientation_Arretes_Roux (Cube):  #Strategie : Etape 1 : rmettre un centre jaune ou blanc en haut  Etape 1': Verifier si c'est deja bon (6 arretes orientées  Etape 2:Se ramener à un cas à 4 arrete non orientées  Etape 3: 3 non orientés en haut, 1 en bas   Etape 4:  Orientation
    L=""
    if Cube[1][1][1]==5 or Cube[1][1][1]==6:    #Etape1
        Etape1="m"
        MouvM1(Cube)
        L=L+Etape1
    Etat=Code_Orientation(Cube) 
    if Etat=="111111":                         #Etape 1'
        return(L)
    #Etape2
    #Cas possibles de l'etape 2 : ab,ac,ad,ai,ak,bc,bd,bi,bk,cd,ci,ck,di,dk,ik et le reste passe à l'etape3 :16 cas(5+4+3+2+1+1)
    #on compte les 0, si il y en a 4 alors Etape2=""
    Compteur=0
    for i in range(6):                         #Etape 2
        if Etat[i]=="0":
            Compteur+=1
    if Compteur==4:
        Etape2=""
    if Compteur==6:  #Cas très particulier, les 6 arretes sont désorientés, on utilise pour cela une formule qui oriente les 6 d'un coup:
        for j in "RurMumURmUrM":
            MouvX(j,Cube)
        return(L+"RurMumURmUrM")
    #Cas non triviaux:15
    CasPossibles=["001111","010111","011011","011101","011110","100111","101011","101101","101110","110011","110101","110110","111001","111010","111100"]
    Sol_CasPossibles=["Umum","mum","umum","uumum","mum","mum","Umum","Umum","mum","mum","mum","umum","umum","mum","mum"]
    for i in range(15):
        if Etat==CasPossibles[i]:
            Etape2=Sol_CasPossibles[i]
    for i in Etape2:
        MouvX(i,Cube)
    L=L+Etape2
    #Etape 3: on veut qu'il y ai 3 orientées en haut et une non orientée en bas
    #Cas possibles :deja bon, 4 en haut, 2 en haut 2 en bas, et c'est tout 
    Etat2=Code_Orientation(Cube)     #On met à jour l'etat du cube
    Compteur3H,Compteur3B=0,0
    for i in range(4):
        if Etat2[i]=="0":
            Compteur3H+=1     #nb de non orientés en haut
    for i in range(4,6):
        if Etat2[i]=="0":
            Compteur3B+=1     #nb de non orientés en bas
    if Compteur3H==3 and Compteur3B==1:
        Etape3=""
    if Compteur3H==4 and Compteur3B==0:
        Etape3="muuM"
    if Compteur3H==2 and Compteur3B==2:  #dans ce cas la il y a 2 possibilités il y a toujours ik, et en haut il y a 6 configurations possibles: ab,ac,ad,bc,bd,cd
        Cas_Possibles=["001100","010100","011000","100100","101000","110000"]
        Sol_Cas_Possibles=["Muum","UMuum","Muum","muuM","Muum","muuM"]
        for i in range(6):
            if Etat2==Cas_Possibles[i]:
                Etape3=Sol_Cas_Possibles[i]
    for i in Etape3:
        MouvX(i,Cube)
    L=L+Etape3
    #Etape 4:Orientation
    #Cas possibles : les i:abc,abd,acd,bcd   les k:pareil  :8 cas possibles
    Etat3=Code_Orientation(Cube)
    CasPossiblesHaut=["0001","0010","0100","1000"]
    SolCasPossiblesI=["umum","mum","Umum","uumum"]
    SolCasPossiblesK=["UMum","uuMum","uMum","Mum"]
    Etape4=""
    if Etat3[4]=="0":  #les i
        for i in range(4):
            if Etat3[:4]==CasPossiblesHaut[i]:
                Etape4=SolCasPossiblesI[i]
    if Etat3[5]=="0":  #les k
        for i in range(4):
            if Etat3[:4]==CasPossiblesHaut[i]:
                Etape4=SolCasPossiblesK[i]
    for i in Etape4:
        MouvX(i,Cube)
    L=L+Etape4
    return(L)



def CheckerPartie4(Cube):
    L=[Cube[4][2][1],Cube[4][1][0],Cube[4][0][1],Cube[4][1][2],Cube[5][0][1],Cube[5][2][1]]
    Compteur_orientation=0
    for i in range(6):
        if L[i]==5 or L[i]==6:
            Compteur_orientation+=1
    if Compteur_orientation==6:
        return(True)
    return(False)
    


        
##Partie5: LSE (Last Six Edges) 

#Cette partie consiste à permuter les 6 dernieres arrêtes(qui sont deja orientées)
#Phase 1 : mettre la bleu jaune et la verte jaune à leur place
#Phase 2 : resoudre la fin

    

def CheckerPhase1(Cube):
    Suite=[[Cube[0][0][2],Cube[0][0][1],Cube[0][0][0]],[Cube[3][0][2],Cube[3][0][1],Cube[3][0][0]],[Cube[2][0][2],Cube[2][0][1],Cube[2][0][0]],[Cube[1][0][2],Cube[1][0][1],Cube[1][0][0]]] 
    
    if Suite[0]==[4,4,4] and Suite[2]==[2,2,2]:
        return(True)
    if Suite[1]==[4,4,4] and Suite[3]==[2,2,2]:
        return(True)
    if Suite[2]==[4,4,4] and Suite[1]==[2,2,2]:
        return(True)
    if Suite[3]==[4,4,4] and Suite[2]==[2,2,2]:
        return(True)
    return(False)
    
    
    
def Ajuster(Cube):  #Ajuste le cube à la fin de la phase 1 pour qu'il soit pret pour la phase 2
    if Cube[1][0][0]==1:
        Ajustement=""
    if Cube[1][0][0]==2: 
        Ajustement="u"
    if Cube[1][0][0]==3:
        Ajustement="uu"
    if Cube[1][0][0]==4:
        Ajustement="U"
    for i in Ajustement:
        MouvX(i,Cube)
    return(Ajustement)
    
    
    
def Phase1(Cube): #Strategie: Mettre BleuJaune en I et VertJaune en K  puis aligner (stickers verts à l'avant) et mm
    #Etape0:Verifier si c'est deja bon
    L=""
    if CheckerPhase1(Cube):
        U=Ajuster(Cube)
        L=L+U
        return(L)    
    #Etape1: BleuJaune en I
    #BleuJaune peut être en A,B,C,D,I,K et dans la liste L_Six_Arretes, BleuJaune correspond à B
    L_Arretes1=L_Six_Arretes(Cube)
    PossibilitesBleuJaune="ABCDIK"
    Sol_PossibilitesBleuJaune=["muuM","Umm","mm","umm","","MuuM"]
    for i in range(6):
        if L_Arretes1[i]=="B":
            Sol_BleuJaune=Sol_PossibilitesBleuJaune[i]
    for j in Sol_BleuJaune:
        MouvX(j,Cube)
    L=L+Sol_BleuJaune
    #Etape2:VertJaune en K
    #VertJaune peut être en A,B,C,D,K et dans la liste L_Six_Arretes, VertJaune correspond à D
    L_Arretes2=L_Six_Arretes(Cube)
    PossibilitesVertJaune="ABCDIK"
    Sol_PossibilitesVertJaune=["uuMuum","UMuum","Muum","uMuum","Cas impossible I",""]
    for i in range(6):
        if L_Arretes2[i]=="D":
            Sol_VertJaune=Sol_PossibilitesVertJaune[i]
    for j in Sol_VertJaune:
        MouvX(j,Cube)
    L=L+Sol_VertJaune
    #Maintenant, il faut aligner la face U puis faire mm
    ListeCouleurs=[Cube[1][0][0],Cube[0][0][0],Cube[3][0][0],Cube[2][0][0]]
    Sol_Couleur=["","u","uu","U"]
    Alignement=""
    for i in range(4):
        if ListeCouleurs[i]==2:    #le vert est trouvé
            Alignement=Sol_Couleur[i]
    for k in Alignement+"mm":
        MouvX(k,Cube)
    L=L+Alignement+"mm"  
    #Maintenant on ajuste simplement le cube pour la phase 2
    Ajustement=Ajuster(Cube)
    L=L+Ajustement
    return(L)



def CompteurLignesPointilles(Cube):  #une ligne pointillés de la tranche M est une ligne continue sans le centre, et une ligne continue est une ligne de meme couleur
    Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6]]
    CompteurPointille=0
    CouleursM=[1,3,5,6]
    for k in range(4):
        for j in CouleursM:    #Couleur autour du centre
            for i in CouleursM:     #Couleurs des centres
                if i!=j:    #sinon c'est une ligne continue
                    if Lignes[k]==[j,i,j]:
                        CompteurPointille+=1
    return(CompteurPointille)
    
    
    
def DetecteurAngleSolitaire(Cube): #Cet angle est forcement sur les arretes A,C,I,ou K
    Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]],[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6],[1,1,1]]   liste augmentée
    for i in range(4):
        if Lignes[i][2]!=Lignes[i][1] and Lignes[i][2]!=Lignes[i][0]:    
            if Lignes[i+1][0]!=Lignes[i+1][1]and Lignes[i+1][0]!=Lignes[i+1][2]:
                Position=i   #on recupere la position
                if Position==0:
                    return("A")
                if Position==1:
                    return("C")
                if Position==2:
                    return("K")
                if Position==3:
                    return("I")


#"Qui a une idée vraie sait en même temps qu'il a une idée vraie et ne peut douter de la vérité de la chose" (Spinoza, Éthique)
                    
                    
def DetecteurAngleTriple(Cube):    #Fonction miroir de DetecteurAngleSolitaire
    Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]],[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6],[1,1,1]]   liste augmentée
    for i in range(4):
        if Lignes[i][2]==Lignes[i][1] and Lignes[i][2]!=Lignes[i][0]:    
            if Lignes[i+1][0]==Lignes[i+1][1] and Lignes[i+1][0]!=Lignes[i+1][2]:
                Position=i   #on recupere la position
                if Position==0:
                    return("A")
                if Position==1:
                    return("C")
                if Position==2:
                    return("K")
                if Position==3:
                    return("I")

    
    
def Phase2(Cube): #Strategie: soit on est dans le cas des Centres et on finit, soit dans le cas des barres et on finit aussi, soit dans le cas des angles et on ajuste puis on finit
    #Observations: Dans le cas des angles, il n'y a pas de ligne continue, dans le cas des centres il y a 4 lignes pointillés et dans le cas des barres, il y a 2 lignes continues et 2 lignes pointillés
    #On va donc compter le nombre de lignes pointillés sur la tranche M et ainsi savoir quoi faire
    #On regarde d'abord si le cube est presque terminé (à quelques mouvements m ou deja terminé
    Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6]]
    L=""
    CubeTest=copy(Cube)
    if resolu(y(CubeTest)):
        return(L)
    if resolu(y(MouvM1(CubeTest))):
        MouvM1(Cube)
        return(L+"m")
    if resolu(y(MouvM1(MouvM1(CubeTest)))):   #Cas triviaux
        MouvM1(MouvM1(Cube))
        return(L+"mm")
    if resolu(y(MouvM(CubeTest))):
        MouvM(Cube)
        return(L+"M")
    NbLignesPointilles=CompteurLignesPointilles(Cube)
    if NbLignesPointilles==4:
        L=L+"eemeeM"
        for i in "eemeeM":
            MouvX(i,Cube)
    if NbLignesPointilles==2:  #Cas des barres :il faut placer les lignes continues sur le dessus et dessous 
        if Lignes[0][0]==Lignes[0][1] and Lignes[2][0]==Lignes[2][1]:
            L=L+"m" 
            MouvM1(Cube)
        L=L+"uummuu"
        for i in "uummuu":
            MouvX(i,Cube)
    if NbLignesPointilles==0: #Cas des angles: il faut placer l'angle solitaire sur la face superieure et s'assurer que l'angle triple soit en bas
        AngleSolitaire1=DetecteurAngleSolitaire(Cube)
        Vers_Face_Sup=["","","M","m"]  #Sol de [A,D,K,I] pour l'angle solitaire
        Liste=["A","D","K","I"]
        for i in range(4):
            if Liste[i]==AngleSolitaire1:
                L=L+Vers_Face_Sup[i]
                for j in Vers_Face_Sup[i]:   #L'angle est monté
                    MouvX(j,Cube)
        AngleSolitaire2,AngleTriple=DetecteurAngleSolitaire(Cube),DetecteurAngleTriple(Cube)  #Redetection des angles importants
        Finition=""
        Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]],[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6],[1,1,1]]   liste augmentée
        if AngleSolitaire2=="A" and AngleTriple=="C":
            Finition="m"
        if AngleSolitaire2=="C" and AngleTriple=="A":
            Finition="M"
        for i in Finition:
            MouvX(i,Cube)
        L=L+Finition
        AngleSolitaire3=DetecteurAngleSolitaire(Cube)
        Lignes=[[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]],[Cube[4][2][1],Cube[4][1][1],Cube[4][0][1]],[Cube[3][0][1],Cube[3][1][1],Cube[3][2][1]],[Cube[5][2][1],Cube[5][1][1],Cube[5][0][1]],[Cube[1][2][1],Cube[1][1][1],Cube[1][0][1]]]  #liste du cube resolu : [[1,1,1],[5,5,5],[3,3,3],[6,6,6],[1,1,1]]   liste augmentée
        if AngleSolitaire3=="C":    #Cas où l'angle solitaire et l'angle triple sont écartés
            L=L+"uumuu"                 #AngleB Final
            for i in "uumuu":
                MouvX(i,Cube)
        if AngleSolitaire3=="A":
            L=L+"uuMuu"                 #AngleF Final
            for i in "uuMuu":
                MouvX(i,Cube)
    #Voila, les cas sont terminés, mais il se peut qu'il reste un cas trivial à résoudre par m,M,ou mm, on refait donc la procédure du debut
    CubeTest=copy(Cube)
    # print(resolu(y(MouvM(CubeTest))),"                      ???????????????")
    if resolu(y(CubeTest)):
        return(L)
    CubeTest=copy(Cube)
    if resolu(y(MouvM1(CubeTest))):
        MouvM1(Cube)
        L=L+"m"
    CubeTest=copy(Cube)
    if resolu(y(MouvM1(MouvM1(CubeTest)))):   #Cas triviaux
        MouvM1(MouvM1(Cube))
        L=L+"mm"
    CubeTest=copy(Cube)
    if resolu(y(MouvM(CubeTest))):
        MouvM(Cube)
        L=L+"M"
    return(L)
    
#"La nature ne fait rien en vain" Aristote, Métaphysique
    
def Resolution_par_la_methode_Roux(Cube):
    L=Positionnement(Cube)[1]
    L=L+Premier_Bloc_Roux(Cube)[0]
    L=L+Second_Bloc_Roux(Cube)[0]
    L=L+Orientation_Coins_Roux(Cube)
    L=L+Perm_Coin_Roux(Cube)
    L=L+Orientation_Arretes_Roux(Cube)
    L=L+Phase1(Cube)
    L=L+Phase2(Cube)
    return(L)
    
    
    
def Resolu_Roux(Cube):
    Cube=copy(Cube)
    if resolu(y(Cube)):
        return(True)
    return(False)
    
    

def CheckerFinal(Cube,Liste):  #Verifie si la solution donnée est valide : la fonction prend la solution, le cube mélangé, et effectue simplement les mouvements et regarde si le cube est résolu
    Cube2=copy(Cube)
    for i in Liste:
        MouvX(i,Cube2)
    return(Resolu_Roux(Cube2))
    
    

def Testeur(nb,Cube):
    
    Total_Longueur=0   #on va compter la somme de tous les mouvements solutions pour en faire la moyenne
    for i in range(nb):
        L=Melange("RRRRRLLLLLMMMMMBBBBUUUUFFFFSSSSMMMMDDDD")    #on melange le cube selon une combinaison de ces mouvements, le lecteur est invité à mettre ce qu'il veut parmi les touches(Majuscules autorisées) {r,l,u,d,f,b,s,m,e,x,y,z} (Famille genératrice de 24 compasantes ( et en auncun cas libre car dim(Rubik'sCube)=5, le mouvement U pouvant  )
        print(L,"                     MELANGE")
        CubeTest=Createur(L,Cube)
        CubeX=copy(CubeTest)
        Solution=Resolution_par_la_methode_Roux(CubeX)
        Solution_Compacte=Compacteur(Solution)
        Longueur=len(Solution_Compacte)
        print(Longueur,"                                                   LONGUEUR")
        print(Solution_Compacte,"                SOLUTION")
        if not CheckerFinal(CubeTest,Solution_Compacte):
            print("Raté")
            print(CubeX,"           Voici le produit non fini")    #Ce message d'erreur n'a malheuresement jamais vu le jour...
            break
        Total_Longueur=Total_Longueur+Longueur  
    Moyenne=Total_Longueur/nb
    return(Moyenne)   #la moyenne tourne autour de 99 mais depend des mouvements mis dans Melange (la moyenne varie de 95 à 100mouvements)


#Pour les sceptiques qui voudraient constater par eux même que cela fonctionne : melangez un cube par vous même, inscrivez le sous forme matricielle dans les matrices ci dessous, enlevez les guillemets qui sont en haut et en bas du morceau de code ci dessous, et suivez les instructions qui vous être afficher à l'ecran 
"""
R=array([[1,1,6],[3,1,5],[2,2,6]])
V=array([[2,2,2],[3,2,2],[3,4,2]])
O=array([[5,3,4],[5,3,4],[5,2,5]])       #Ici un cas testé 
Bleu=array([[6,4,4],[1,4,4],[4,5,6]])
J=array([[5,5,1],[6,5,6],[1,1,1]])
Blanc=array([[4,6,3],[6,6,3],[3,1,3]])
CubeMélangé=[R,V,O,Bleu,J,Blanc]
print(CubeMélangé)
Sol=Compacteur(Resolution_par_la_methode_Roux(copy(CubeMélangé)))
print(Sol,"Voici une solution parmi tant d'autres pour vous. ")
for i in Sol:
    MouvX(i,CubeMélangé)
print(CubeMélangé,"                                 Résolu")"""

##Présentation:
ListeMelange="URLDFurlUmU"
CubePrez=Createur(ListeMelange,Cube)
print(CubePrez)
CopieCubePrez=copy(CubePrez)
L=Compacteur(Resolution_par_la_methode_Roux(CopieCubePrez))
print("Liste inbuvable",L)
print(len(L))
print(CheckerFinal(CubePrez,L))

Listepotable=L[:4]+"_____1ere paire_____"+L[4:15]+"______2eme paire_____"+L[15:29]+"_____3eme paire____"+L[29:46]+"_____4eme paire____"+L[46:59]+"_____uuu AntiSune____"+L[59:70]+"____u perm laterale____"+L[70:85]+"______Orientation Arrete_______"+L[85:97]+"______Phase1______"+L[97:109]+"____Cas 0 pré_____"+L[109:116]
#Verifié 3 fois 
print(Listepotable)
print("TADAA")

#Commande pour faire travailler Python ( Et oui, une fois le code achevé, il ne reste plus qu'à faire Ctrl+E et observer Python travailler) Note:Comptez aux alentours de 25 secondes pour 1000 cubes
##Commande Random
# print(Testeur(100,Cube),"        MOYENNE")
##
##Commentaire sur le choix des methodes employés:
#L'objectif de ce projet n'etant en auncun cas de recopier un travail dejà effectué par d'autres, mais de se confronter à un réel problème lié au Rubik's Cube, le choix de la methode adaptée à la résolution informatique a été rejetée (car beaucoup trop répandue pour résoudre informatiquement le cube), s'est donc imposé deux methode déjà partiellement étudiées auparavant : La méthode dite "OldPochmann" ou "blind" qui consiste à conserver les différentes pièces au cours de la résolution (d'où la longueur des solutions avoisinant les 350 mouvements)  et la methode dite "Roux", qui consiste cette fois à résoudre le cube de manière conventionnelle (vue autorisée, cependant avec un modification notable : l'utilisation de la tranche M qui rend la résolution plutot rapide, et différente de la methode la plus répandue dans le monde du SpeedCubing : la CFOP ou Fridrich ( de sa créatrice mathématicienne Jessica Fridrich). La methode Roux étant notablement plus difficile à coder que la methode Blind, à cause de la non conservation du cube (il faut aprendre à l'algorithme à reconnaitre les cas à chaque étape, ce qui n'est pas le cas lorsqu'il y a conservation du cube au cours de la resolution). 
#C'est également pour cela que la methode Roux est codée après la blind, cette première methode constituait une première approche, et ensuite a été abordé la seconde methode, avec des idées ayant pu émerger grâce à la première.

#"L'humanité ne se pose jamais que les problèmes qu'elle peut résoudre." Marx
#"Ce dont on ne peut pas parler, il faut le taire." Wittgenstein, Tractatus logico-philosophicus
