import time


def println(s):
    print(s, end="")


Game = True


class Gender:
    pass


class Player:
    def __init__(self, name: str, gender: Gender, alive: bool = True):
        self.alive = alive
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"Player('{self.name}', {self.gender}, alive={self.alive})"


def approachedBy(p):
    if (p.gender == "m"):
        return "You are in a middle of the street and is approached by a tall dragonic girl..."
    elif (p.gender == "f"):
        return "You are in a middle of the street and is approached by a small pitty boy..."
    else:
        return "Ahhhh"
    return "What do you want to do?"


def twoAnsPrompt(question: str, answer1: str, answer2: str, a: str, b: str):
    input = input(question)
    if (input == answer1):
        print(a)
    elif (input == answer2):
        print(b)


def twoAnsPromptWithOut(question: str, answers1: list[str], answers2: list[str], print1: str, print2: str, r1, r2):
    i = input(question + "\n")  # Ska vara lista på answers
    if i in answers1:
        print(print1)
        return r1
    elif i in answers2:
        print(print2)
        return r2
    else:
        badAnswer()
        twoAnsPromptWithOut(question, answers1, answers2, print1, print2, r1, r2)


def basicResponsWithOut(question, out1, out2):
    answer = input(question + "\n")
    print(out1 + answer + out2)
    return answer


# def basicDependentPrompt(prompt, a):
#     i = input(prompt + "\n")
#     if i in

def badAnswer():
    print("You cannot answer that... Maybe typo?\n")


def newLife():
    i = input("\nDo you wish to start a new life? Type your answer:\n")
    if i in ["Y", "yes", "Yes", "y"]:
        n = basicResponsWithOut("What is your name?", "Hello ", "!")  # ChooseName
        g = twoAnsPromptWithOut("Do you wish to be 'male' or 'female'?", ["male", "Male"], ["female", "Female"],
                                "You are now male!",
                                "You are now female", "Male", "Female")

        return Player(n, g)
    elif i in ["N", "n", "no", "No"]:
        println("No?")
        time.sleep(0.5)
        for i in range(3):
            println(".")
            time.sleep(0.5)
        print()
        return False
    else:
        badAnswer()
        newLife()


while Game:
    player = newLife()
    if not player:
        Game = False
        print("\nGame has ended...")
        break
    if player.alive == True:
        print(player)
        print("Life begins...")
        input()
        print(approachedBy(player))

        input()

    print("\nGame has ended...")
