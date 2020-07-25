from typing import Union
import time
import sys
import pickle
import json
import subprocess
import threading

from functools import wraps


def music_play_thread(m):
    subprocess.run(['say', '-v', 'Paulina', m, ])


def create_thread(f, deamon=True, args=None, **kwargs):
    return threading.Thread(target=f, args=args, daemon=deamon, **kwargs)


def music_t_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=music_play_thread,
                             args=(args[0],), daemon=True)
        t.start()
        d = func(*args, **kwargs)
        t.join()
        return d
    return wrapper


data = ''
with open("State/game_state.json") as f:
    data = json.load(f)


def c_m(*args, c=15, ret=False, **kwargs):
    c_code = u"\u001b[38;5;{}m"
    reset_code = u"\u001b[0m"

    if ret:
        return c_code.format(c) + "".join(args) + reset_code
    print(c_code.format(c), *args, reset_code, **kwargs)


def s_cbar():
    print("\033[6 q", end="\r", sep="")


def blink_trans(c=7):
    m = " "
    s_cbar()
    for i in range(3):
        print(f"\033[48;5;{c}m"+m+"\033[0m", end="\r", sep="")
        time.sleep(0.2)
        c_m(m, end="\r", sep="")
        time.sleep(0.2)
    print()


def print_slow(m, d=0.03, **kwargs):
    l = len(m)

    for i in range(l):
        print(m[i], end="", sep="", flush=True)
        time.sleep(d)
    print(**kwargs)


class Test:
    PASSED = 0

    def __init__(self, title):
        self.title = title
        self.completed = False

    def start(self):
        pass


class Quiz:
    def __init__(self, *prompts: Union[str, str], intro, outro):
        self.prompts = prompts
        self.intro = intro
        self.outro = outro

    def start(self):
        print("\u001b[2J\u001b[H")
        print_slow(c_m(self.intro, c=32, ret=True), end="\n\r")
        for p in self.prompts:
            print_slow(p[0])
            res = input('\u001b[1m- \u001b[0m')
            print_slow(p[1])
            time.sleep(0.1)
            blink_trans()
        print_slow(self.outro)
        time.sleep(0.8)


class Item:
    def __init__(self, t, callback):
        self.t = t
        self.completed = False
        self.callback = callback


class Menu:
    def __init__(self, *items, title="Options:"):
        self.options = items
        self.load_completion()
        self.t = title

    def load_completion(self):
        global data
        for i in self.options:
            v = data.get("language_phase", False)
            if v:
                i.completed = v.get(i.t, False)
            else:
                i.completed = v

    def show(self):
        print("\u001b[2J\u001b[H")
        print_slow("\u001b[1m"+self.t+"\u001b[0m", 0.05)
        for i, p in enumerate(self.options):
            print_slow(c_m(str(i+1)+') ', ret=True, c=32), end="")
            comp = "[" + "\u001b[1m X \u001b[0m" + \
                "]" if p.completed else "[" + "\u001b[1m   \u001b[0m" + "]"
            print_slow(p.t + " "*(20-len(p.t)) + comp, 0.02)
            time.sleep(0.1)
        blink_trans()
        print_slow("Choose your already determined fate.", 0.01)
        self._handleInput()

    def _handleInput(self):
        try:
            res = int(input('\u001b[1m - \u001b[0m').strip("\n"))
            if self.options[res-1].callback() == 1:
                self.show()
        except Exception:
            print_slow("I thought you could at least read...")
            self.show()
