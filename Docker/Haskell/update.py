from io import StringIO  # Python3 use: from io import StringIO
from contextlib import redirect_stdout
import subprocess
import json
import time

outputs = ''
outputse = ''
with StringIO() as buf, redirect_stdout(buf):
    procces = subprocess.run(['runhaskell', '-i/opt/external', '/opt/source-code/HaskellL.hs'],
                             capture_output=True)

    # use buf.getVale
    outputs = procces.stdout.decode()

    outputse = procces.stderr.decode()


if outputs:
    # Testing
    correct = 0
    vals = outputs.splitlines()
    res = ['50500', '10', '100', '1900', '0']
    correct = sum(filter(lambda x: x, map(
        lambda x, y: x.strip('\n').strip() == y, vals, res)))

    if correct == 5:
        print("Great Job! It was simple right!")
        print("Remember \u001b[38;5;198mHaskell\u001b[0m")

        with open("/opt/state/game_state.json", "r") as fr:
            d = json.load(fr)
            d["checkpoint"] = "intro_menu"
            d["language_phase"]["Haskell"] = True

            with open("/opt/state/game_state.json", "w") as fw:
                json.dump(d, fw)
    else:
        print("This does not seem correct, here is your error!")
        time.sleep(1)

        if outputse:
            print("Error: \n" + outputse)
