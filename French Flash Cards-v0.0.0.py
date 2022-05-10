import random


#avoir, -er verb endings, the (m/f/pl), days of the week, months of the year, etre, accents, colours, de la food thing.
print("\n\n")

def erVerbEndings():
  def je_func():                              #je function

    print("\033[0;36mwhat is the -er ending for 'Je' (I)\n")
    answerJe = "e"
    answerJeIn = input("\033[1;34m")
    if answerJeIn == answerJe:
      print("\033[1;32mcorrect!\n\n")
    elif answerJeIn != answerJe:
      print("\033[1;31mincorrect, answer is 'e'\n\n")
  
  def nous_func():                             #nous function

    print("\033[0;36mwhat is the -er ending for 'Nous' (We)\n")
    answerNous = "ons"
    answerNousIn = input("\033[1;34m")
    if answerNousIn == answerNous:
      print("\033[1;32mcorrect!\n\n")
    elif answerNousIn != answerNous:
      print("\033[1;31mincorrect, answer is 'ons'\n\n")

  def tu_func():                              #tu function

    print("\033[0;36mwhat is the -er ending for 'Tu' (You(inf))\n")
    answerTu = "es"
    answerTuIn = input("\033[1;34m")
    if answerTuIn == answerTu:
      print("\033[1;32mcorrect!\n\n")
    elif answerTuIn != answerTu:
      print("\033[1;31mincorrect, answer is 'es'\n\n")

  def vous_func():                              #vous function

    print("\033[0;36mwhat is the -er ending for 'Vous' (You(pl/form))\n")
    answerVous = "ez"
    answerVousIn = input("\033[1;34m")
    if answerVousIn == answerVous:
      print("\033[1;32mcorrect!\n\n")
    elif answerVousIn != answerVous:
      print("\033[1;31mincorrect, answer is 'es'\n\n")

  def ieo_func():                              #Il/Elle/On function

    print("\033[0;36mwhat is the -er ending for 'Il/Elle/On' (Him/Her/We(inf))\n")
    answerIeo = "e"
    answerIeoIn = input("\033[1;34m")
    if answerIeoIn == answerIeo:
      print("\033[1;32mcorrect!\n\n")
    elif answerIeoIn != answerIeo:
      print("\033[1;31mincorrect, answer is 'e'\n\n")

  def ie_func():                              #Ils/Elles function

    print("\033[0;36mwhat is the -er ending for 'Ils/Elles' (they m/f)\n")
    answerIe = "ent"
    answerIeIn = input("\033[1;34m")
    if answerIeIn == answerIe:
      print("\033[1;32mcorrect!\n\n")
    elif answerIeIn != answerIe:
      print("\033[1;31mincorrect, answer is 'ent'\n\n")



 
  def rand():
    x = [je_func, nous_func, tu_func, vous_func, ieo_func, ie_func]                 #runs random function
    random.choice(x)()
  def randloop():
   for a in range(12):
     rand()
  randloop()






def etre():

  def je():
    
    print("\033[0;36mwhat is the Etre verb ending for 'Je' (I (am))?\n")
    answerJe = "suis"
    answerJeIn = input("\033[1;34m")
    if answerJeIn == answerJe:
      print("\033[1;32mcorrect!\nJe suis = I am\n\n")
    elif answerJeIn != answerJe:
      print("\033[1;31mincorrect, answer is 'es'\nJe suis = I am\n\n")

  def tu():
  
    
    print("\033[0;36mwhat is the Etre verb ending for 'Tu' (You (are) (inf))\n")
    answerTu = "es"
    answerTuIn = input("\033[1;34m")
    if answerTuIn == answerTu:
      print("\033[1;32mcorrect!\nTu es = You are\n\n")
    elif answerTuIn != answerTu:
      print("\033[1;31mincorrect, answer is 'es'\nTu es = You are\n\n")

  def ilElle():


    print("\033[0;36mwhat is the Etre verb ending for 'Il/Elle' (He/She (is) ((inf))\n")
    answerIe = "est"
    answerIeIn = input("\033[1;34m")
    if answerIeIn == answerIe:
      print("\033[1;32mcorrect!\nIl/Elle est = He/She is\n\n")
    elif answerIeIn != answerIe:
      print("\033[1;31mincorrect, answer is 'est'\nIl/Elle est = He/She is\n\n")

  
  def nous():

    print("\033[0;36mwhat is the Etre verb ending for 'Nous' (We (are))\n")
    answerNous = "sommes"
    answerNousIn = input("\033[1;34m")
    if answerNousIn == answerNous:
      print("\033[1;32mcorrect!\nNous sommes = We are\n\n")
    elif answerNousIn != answerNous:
      print("\033[1;31mincorrect, answer is 'sommes'\nNous sommes = We are\n\n")

  def vous():

    print("\033[0;36mwhat is the Etre verb ending for 'Vous' (You (are) (pl/form))\n")
    answerVous = "etes"
    answerVousIn = input("\033[1;34m")
    if answerVousIn == answerVous:
      print("\033[1;32mcorrect!\nVous êtes = You are (pl/inf)\n\n")
    elif answerVousIn != answerVous:
      print("\033[1;31mincorrect, answer is 'es'\nVous êtes = You are (pl/inf)\n\n")
  
  def ilsElles():
    
    print("\033[0;36mwhat is the Etre ending for 'Ils/Elles' (They (are) (m/f)\n")
    answerIe = "sont"
    answerIeIn = input("\033[1;34m")
    if answerIeIn == answerIe:
      print("\033[1;32mcorrect!\nIls/Elles sont = They are (m/f)\n\n")
    elif answerIeIn != answerIe:
      print("\033[1;31mincorrect, answer is 'sont'\nIls/Elles sont = They are (m/f)\n\n")

  def rand():
      x = [je, tu, ilElle, nous, vous, ilsElles]                 #runs random function
      random.choice(x)()
  def randloop():
    for a in range(12):
      rand()
  randloop()





def quantArtFood():

  def du():

    print("\033[0;36mWhat should go in the gaps: Jaime manger ____ poulet (I like to eat chicken). \nWhat is the dally la thing for Masculine Singular?\n")
    answerDu = "du"
    answerDuIn = input("\033[1;34m")
    if answerDuIn == answerDu:
      print("\033[1;32mcorrect!\nDe + le = du\nJaime manger \033[1;31mdu \033[0;36mpoulet (I like to eat chicken)\nPoulet is masculine.\n\n")
    elif answerDuIn != answerDu:
      print("\033[1;31mincorrect, answer is 'du'\n\033[0;36mDe + le = du\nJaime manger \033[1;31mdu \033[0;36mpoulet (I like to eat chicken)\nPoulet is masculine.\n\n")



  def deLa():

    print("\033[0;36mWhat should go in the gaps: Vous aimez boire ____ limonade? \nWhat is the dally la thing for Feminine Singular?\n")
    answerdeLa = "de la"
    answerdeLaIn = input("\033[1;34m")
    if answerdeLaIn == answerdeLa:
      print("\033[1;32mcorrect!\nDe + la = de la\nVous aimez boire\033[1;31mde la \033[0;36mlimonade? (Do you like to drink lemonade?)\nlimonade is feminine.\n\n")
    elif answerdeLaIn != answerdeLa:
      print("\033[1;31mincorrect, answer is 'de la'\n\033[0;36mDe + la = de la\nVous aimez boire\033[1;31mde la \033[0;36mlimonade? (Do you like to drink lemonade?)\nlimonade is feminine.\n\n")


  def deL():


    print("\033[0;36mWhat should go in the gaps: Il n'aime pas boire ____eau minérale (He does not like to drink mineral water) \nWhat is the dally la thing for before a vowel?\n")
    answerdeL = "de l'"
    answerdeLIn = input("\033[1;34m")
    if answerdeLIn == answerdeL:
      print("\033[1;32mcorrect!\n\033[0;36mDe + l' = de l'\nIl n'aime pas boire\033[1;31mde l'\033[0;36meau minérale (He does not like to drink mineral water)\nEau minérale is feminine.\n\n")
    elif answerdeLIn != answerdeL:
      print("\033[1;31mincorrect, answer is 'de l'\n\033[0;36mDe + l' = de l'\nIl n'aime pas boire\033[1;31mde l'\033[0;36meau minérale (He does not like to drink mineral water)\nEau minérale is feminine.\n\n")

  def des():


    print("\033[0;36mWhat should go in the gaps: Tu aimes manger ____ cuisses de grenouille? (Do you like to eat frog legs?)\nWhat is the dally la thing for Feminine Singular?\n")
    answerdes = "des"
    answerdesIn = input("\033[1;34m")
    if answerdesIn == answerdes:
      print("\033[1;32mcorrect!\nDe + les = des\nTu aimes manger\033[1;31mdes\033[0;36mcuisses de grenouilles? (Do you like to eat frog legs?)\nCuisses de grenouilles is feminine and plural.\n\n")
    elif answerdesIn != answerdes:
      print("\033[1;31mincorrect, answer is 'de la'\n\033[0;36mDe + les = des\nTu aimes manger\033[1;31mdes\033[0;36mcuisses de grenouilles? (Do you like to eat frog legs?)\nCuisses de grenouilles is feminine and plural.\n\n")


  def rand():
      x = [du, deLa, deL, des]                 #runs random function
      random.choice(x)()
  def randloop():
    for a in range(12):
      rand()
  randloop()

card = input("For: -er verb endings, Être, Quantative articles food; type: -er, etre, qaf, respectively. " )
if card == '-er':
  erVerbEndings()
elif card == 'etre':
  etre()
elif card == 'qaf':
  quantArtFood()


print("\n\n")

