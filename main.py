Game = True
Life = True

class Player():
    def __init__(self, life, name, gender):
        self.life = life
        self.name = name
        self.gender = gender

def approachedBy(p):
    if (p.gender == "m"):
        print("You are in a middle of the street and is approached by a tall dragonic girl...")
    elif (p.gender == "f"):
        print("You are in a middle of the street and is approached by a small pitty boy...")
    print("What do you want to do?")

def twoAnsPrompt(question, answer1, answer2, a, b):
    input = input(question)
    if (input == answer1):
        print(a)
    elif (input == answer2):
        print(b)

def twoAnsPromptWithOut(question, answers1, answers2, print1, print2, r1, r2):
    i = input(question + "\n")
    if i in answers1:
        print(print1)
        return r1
    elif i in answers2:
        print(print2)
        return r2
    else:
        badAnswer()
        twoAnsPromptWithOut(question, answer1, answer2, print1, print2, r1, r2)

def basicResponsWithOut(question, out1, out2):
    answer = input(question + "\n")
    print(out1 + answer + out2)
    return answer

# def basicDependentPrompt(prompt, a):
#     i = input(prompt + "\n")
#     if i in

def badAnswer():
    print("You cannot answer that... Maybe typo?")

def newLife():
    newLife = input("Start new life?: Type 'Y' or 'N'\n");
    if (newLife == 'Y'):
        n = basicResponsWithOut("What is your name?", "Hello ", "!")  # ChooseName
        g = twoAnsPromptWithOut("Do you with to 'male' or 'female'?", ["male"], ["female"], "You are now male!",
                                "You are now female", "Male", "Female")
        player = Player("Alive", n, g)
        return player
    elif (newLife == "N"):
        print("No?")
        player = Player("Dead", "u", "u")
        return player
    else:
        badAnswer()
        newLife()

while Game:
    player = newLife()
    if player.life == "Alive":
        print("Life begins...")
        input()


    print("Game has ended...")