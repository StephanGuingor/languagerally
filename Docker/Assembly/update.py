import subprocess
import json
import time

outputs = ''
outputse = ''

# Compile Asm
procces = subprocess.run(['nasm', '-felf64', '/opt/external/App.asm'],
                         capture_output=True)

err = procces.stderr.decode()

if err:
    print("You had a few errors!")
    print(err)

procces = subprocess.run(['gcc', '/opt/source-code/App.c', '/opt/external/App.o'],
                         capture_output=True)

err = procces.stderr.decode()

if err:
    print("You had a few errors!")
    print(err)

procces = subprocess.run(['./a.out'],
                         capture_output=True)


# use buf.getVale
outputs = procces.stdout.decode()

outputse = procces.stderr.decode()

if outputs:
    # Testing
    correct = 0
    vals = outputs.splitlines()
    res = ['10', '114', '2', '55', '39']
    correct = sum(filter(lambda x: x, map(
        lambda x, y: x.strip('\n').strip() == y, vals, res)))

    if correct == 5:
        print("Great Job! It was simple right!")
        print(
            "Remember \u001b[38;5;198mAssembly\u001b[0m,\nThe lower the better and the longer.")

        with open("/opt/state/game_state.json", "r") as fr:
            d = json.load(fr)
            d["checkpoint"] = "intro_menu"
            d["language_phase"]["Assembly"] = True

            with open("/opt/state/game_state.json", "w") as fw:
                json.dump(d, fw)
    else:
        print("This does not seem correct, here is your error! Maybe.")
        time.sleep(1)

        print("\tOutput,\u001b[38;5;32mExpected\u001b[0m")
        for i, j in zip(outputs.splitlines(), res):
            l = len(i)
            print(" -\t", f"\u001b[{l}D", i, " "*(3),
                  "\u001b[38;5;32m", j, '\u001b[0m')


if outputse:
    print("Error: \n" + outputse)
