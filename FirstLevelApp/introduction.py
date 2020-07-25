import time
import sys
import random
import os
import threading
import queue
from modules import *
import json
import subprocess
import textwrap
import random

lines = 0


class COLORS:
    PINK = 199
    BLUE = 32
    GREEN = 119
    WHITE = 15


def b(m):
    m = u"\u001b[1m" + m + u"\u001b[0m"
    return m


def loading(d=0.05):
    c_m("Parsing into the matrix:  ", c=122, end="")
    for i in range(0, 100):
        time.sleep(d)
        v = str(i+1)
        print(f"\u001b[{len(str(i))+1}D" +
              f'{v}%', flush=True, end="", sep=" ")
    print()


def title():
    c_m("-"*20, c=COLORS.BLUE)
    c_m("Welcome to the trial!", c=COLORS.BLUE)
    c_m("A rally made by:", c=COLORS.BLUE, end="")
    c_m(b("Stephan"), c=COLORS.GREEN, sep="")
    c_m("-"*20, c=COLORS.BLUE)


def timer_thread(t, q):
    time.sleep(t)
    q.put(False)


def transition_effect():
    # print(u"\u001b[7A")
    print(u"\u001b[2J")
    time.sleep(0.1)

    q = queue.Queue()

    t = x = threading.Thread(target=timer_thread, args=(3, q), daemon=True)
    t.start()

    run = True

    w, h = os.get_terminal_size()
    while run:
        for i in range(h-1):
            for i in range(w):
                c_m(u"\u001b[48;5;46m"+str(random.randint(0, 1)),
                    c=0, end="", sep="")
            print()
        time.sleep(0.01)
        sys.stdout.write(f"\u001b[{w}D")
        sys.stdout.write(f"\u001b[{h}A")
        sys.stdout.flush()

        # When Other Thread Dies
        if not q.empty():
            run = q.get()
    t.join()


def show_options():
    pass


quiz = Quiz(("Do you believe in love?", "I find love very weird"), ("Sometimes I don't know if I'm alive", "Yeah I don't know"),
            intro="Before we begin, I need to know if you are worthy...",
            outro="Honestly I didn't care if you were capable or not, I just want to see you suffer",
            )


def js():
    print("\u001b[2J\u001b[H")
    if data["language_phase"]["Javascript"]:

        print_slow(
            "Common \u001b[38;5;69mjavascript\u001b[0m was already completed !", 0.04)
        time.sleep(0.5)
        return 1

    print_slow(
        "This language is known for it's interesting desing when handling operations between types!", 0.02)
    print_slow("It usually involves some type casting into a common type..", 0.02)

    print_slow(
        "The \u001b[38;5;119mJavascript challenge will be somewhat interesting...")
    blink_trans()
    print_slow(c_m("The task is as follow:", ret=True, c=32), 0.02)
    print_slow("\u001b[1m1)\u001b[0m "+c_m(
        "Go into the newly created directory called Javascript Lang", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m2)\u001b[0m "+c_m(
        "Inside the file app.js you can only use \u001b[3m`![(+`\u001b[38;5;119m inside the \u001b[1mconsole.log\u001b[38;5;198m method.", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m3)\u001b[0m "+c_m(
        "When you think you are ready run the \u001b[38;5;65mplay\u001b[0m command", ret=True, c=COLORS.GREEN), 0.02)

    print_slow("For a hint press h, else enter.")
    v = input('- ')
    if v == 'h':
        print_slow("An esoteric language called JSFuck might help.")

    # Create Directory
    path = "JavaScriptLang"
    path1 = "./JavaScriptLang/app.js"

    if not os.path.exists(path):
        try:
            os.mkdir(path)
            with open("./JavascriptLang/app.js", "w") as f:
                f.write("console.log('write here, only using `[!+()`')")

            data["checkpoint"] = "ljs"
            with open("../State/game_state.json", "w") as fw:
                json.dump(data, fw)
        except OSError:
            print("Creation of the directory %s failed" % path)
        except Exception:
            pass


def py():
    print("\u001b[2J\u001b[H")
    if data["language_phase"]["Python"]:

        print_slow(
            "Although python \u001b[38;5;69mrocks\u001b[0m, go and do ther things. !", 0.04)
        time.sleep(0.5)
        return 1

    print_slow(
        "I see you have chosen the language of the \u001b[38;5;69mgods\u001b[0m!", 0.02)
    print_slow("Perhaps I don't have to treat you that bad, we'll see..", 0.02)

    print_slow(
        "This is the python challenge, it should be as easy as importing the work.")
    blink_trans()
    print_slow(c_m("The task is as follow:", ret=True, c=32), 0.02)
    print_slow("\u001b[1m1)\u001b[0m "+c_m(
        "Go into the newly created directory called PythonLang", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m2)\u001b[0m "+c_m(
        "Open the python file and in just one line of code, make sure you print the python zen.", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m3)\u001b[0m "+c_m(
        "When you think you are ready run the \u001b[1mplay\u001b[38;5;119m command", ret=True, c=COLORS.GREEN), 0.02)

    # Create Directory
    path = "PythonLang"
    path1 = "./PythonLang/app.py"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            with open("./PythonLang/app.py", "w") as f:
                f.write("#Remember to only use one line, THIS LINE")

            data["checkpoint"] = "lpy"
            with open("../State/game_state.json", "w") as fw:
                json.dump(data, fw)
        except OSError:
            print("Creation of the directory %s failed" % path)
        except Exception:
            pass


def cpp():
    # Emojo Challenge
    print("\u001b[2J\u001b[H")
    if data["language_phase"]["C++"]:

        print_slow(
            "Move on \u001b[38;5;69mkiddo\u001b[0m!", 0.04)
        time.sleep(0.5)
        return 1

    print_slow(
        "I like that you have the \u001b[38;5;69mballs\u001b[0m!", 0.02)
    print_slow("After all this is basically python's dad...", 0.02)

    print_slow(
        "This is the C++ challenge, it will be weird!")
    blink_trans()
    print_slow(c_m("The task is as follow:", ret=True, c=32), 0.02)
    print_slow("\u001b[1m1)\u001b[0m "+c_m(
        "Go into the newly created directory called CPPLang", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m2)\u001b[0m "+c_m(
        "Open the cpp file and follow the instructions.", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m3)\u001b[0m "+c_m(
        "When you think you are ready run the \u001b[1mplay\u001b[38;5;119m command", ret=True, c=COLORS.GREEN), 0.02)

    print_slow("For a hint press h, else enter.")
    v = input('- ')
    if v == 'h':
        print_slow("Understanding what a preprocessor is might be a good start!")

    # Create Directory
    path = "CPPLang"
    path1 = "./CPPLang/app.hpp"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            with open("./CPPLang/app.hpp", "w") as f:
                f.write(textwrap.dedent("""\
                        #include <iostream>
                        // This should be a function that 
                        // When you run it, it print LOL
                        void 😂()👇🏻
                        🖨(🤣);
                        👆🏻
                                        """))

            data["checkpoint"] = "lcpp"
            with open("./State/game_state.json", "w") as fw:
                json.dump(data, fw)
        except OSError:
            print("Creation of the directory %s failed" % path)
        except Exception:
            pass


def java():
    # Emojo Challenge
    print("\u001b[2J\u001b[H")
    if data["language_phase"]["Java"]:

        print_slow(
            "Are you serious?! You want to do this again, because I can just change the variable that says you did it.", 0.04)
        print_slow(
            "You know what.", 0.04)
        print_slow(
            "I'll grab a random number from 0-100, if its 50. I guess you do it again.", 0.04)
        r = random.randint(0, 100)
        print_slow(
            "Lucky." if r == 50 else "You wanted this! It hurts my eyes. And I dont have eyes.", 0.04)
        blink_trans()

        if r == 50:
            data["language_phase"]["Java"] = False

        time.sleep(1)
        return 1

    print_slow(
        "Hopefully this is not your first pick, I refuse to believe that.", 0.02)
    print_slow(
        "This is the Java challenge, aka objects")
    blink_trans()
    print_slow(c_m("The task is as follow:", ret=True, c=32), 0.02)
    print_slow("\u001b[1m1)\u001b[0m "+c_m(
        "Go into the newly created directory called JavaLang", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m2)\u001b[0m "+c_m(
        "Open the Java file and follow the instructions.", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m3)\u001b[0m "+c_m(
        "When you think you are ready run the \u001b[1mplay\u001b[38;5;119m command", ret=True, c=COLORS.GREEN), 0.02)

    print_slow("For a hint press h, else enter.")
    v = input('- ')
    if v == 'h':
        print_slow("Everything is an object, internet has the answers!")

    # Create Directory
    path = "JavaLang"
    path1 = "./JavaLang/app.java"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            with open("./JavaLang/app.java", "w") as f:
                f.write(textwrap.dedent("""\
                    /** So heres the deal, I would give a fun example but this is java,
                    there is no fun, they are solely materialisic, and think that everything is an object.
                    Yes... even women. 
                    Those are a few reasons why I don't hang here.

                    But you have to help me.
                    I lost a file in one of those void containers and I dont want to come near here to get it out.

                    I need you to print the contents of the file located in: @param /opt/lost/notmydiary.txt
                    */

                    // import stuff here probably some objects
                    public class app{
                            public static void main(String[] args){
                            // write code using objects here
                            }
                        }
                                        """))

            data["checkpoint"] = "ljava"
            with open("./State/game_state.json", "w") as fw:
                json.dump(data, fw)
        except OSError:
            print("Creation of the directory %s failed" % path)
        except Exception:
            pass


def haskell():
    # Emojo Challenge
    print("\u001b[2J\u001b[H")
    if data["language_phase"]["Haskell"]:

        print_slow(
            "I know, this language is so satisfying. But no.", 0.04)
        time.sleep(0.5)
        return 1

    print_slow(
        "You will have an amazing time, it would be almost as if you weren't my slave.", 0.02)
    print_slow(
        "This is the Haskell challenge, aka functions")
    blink_trans()
    print_slow(c_m("The task is as follow:", ret=True, c=32), 0.02)
    print_slow("\u001b[1m1)\u001b[0m "+c_m(
        "Go into the newly created directory called HaskellLang", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m2)\u001b[0m "+c_m(
        "Open the Java file and follow the instructions. Its just some basic math, but purely functional.\n Like math.", ret=True, c=COLORS.GREEN), 0.02)
    print_slow("\u001b[1m3)\u001b[0m "+c_m(
        "When you think you are ready run the \u001b[1mplay\u001b[38;5;119m command", ret=True, c=COLORS.GREEN), 0.02)

    print_slow("For a hint press h, else enter.")
    v = input('- ')
    if v == 'h':
        print_slow(
            "http://learnyouahaskell.com/higher-order-functions might show you the way.")

    # Create Directory
    path = "HaskellLang"
    path1 = "./HaskellLang/App.hs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            with open("./HaskellLang/App.hs", "w") as f:
                f.write(textwrap.dedent("""\
                    -- so you need to complete this functions
                    -- it has to return the sum of even numbers that are 
                    -- multiples of 5 from 0 to n (inclusive)
                    module App where -- dont touch this

                    sumFiveEven :: Int -> Int -- it should be called sumFiveEven n and return the correct value  
                    sumFiveEven = -- You can write the solution here, or use a more space, just mantain the signature.
                                        """))

            data["checkpoint"] = "lhs"
            with open("./State/game_state.json", "w") as fw:
                json.dump(data, fw)
        except OSError:
            print("Creation of the directory %s failed" % path)
        except Exception:
            pass


def assembly():
    pass


def save_file():
    with open("State/game_state.json", "w") as fw:
        json.dump(data, fw)


menu = Menu(Item("Javascript", js),
            Item("Python", py),
            Item("C++", cpp),
            Item("Java", java),
            Item("Haskell", haskell),
            Item("Assembly", assembly),
            title="Language Challenge:")


if __name__ == "__main__":
    if not data["checkpoint"]:
        # title()
        # time.sleep(0.2)
        # blink_trans()
        # loading(0.1)
        # transition_effect()
        quiz.start()
        data["checkpoint"] = "intro_menu"

    if data["checkpoint"] == "intro_menu":
        menu.show()
    elif data["checkpoint"] == "lpy":
        py()
    elif data["checkpoint"] == "lcpp":
        cpp()
    elif data["checkpoint"] == "ljs":
        js()
    elif data["checkpoint"] == "ljava":
        java()
    elif data["checkpoint"] == "lhs":
        haskell()
    elif data["checkpoint"] == "lasm":
        assembly()

    save_file()
