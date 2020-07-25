# Run imported file
import subprocess
import json

output = subprocess.check_output(['python3', '/opt/external/app.py'])
answer = subprocess.check_output(['python3', '-c', 'import this'])

# Compare it and return a veredict
if output == answer:
    # update game_state
    with open("/opt/state/game_state.json", "r") as fr:
        d = json.load(fr)
        d["checkpoint"] = "intro_menu"
        d["language_phase"]["Python"] = True
        print("Great Job! It was simple right!")
        with open("/opt/state/game_state.json", "w") as fw:
            json.dump(d, fw)
else:
    print("Not quite, but keep trying! or not")
