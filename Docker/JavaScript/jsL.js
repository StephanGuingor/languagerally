// Read app.js file
var fs = require('fs');
var state_map = require('/opt/state/game_state.json')

// Check syntax
var data = fs.readFileSync('/opt/external/app.js', 'utf8');
var patt = /console.log\([!\+\[\]\s]+\)/; // Regex
var r = /[!\+\[\]\s]+/
var res = patt.exec(data);

if (res) {
    code = r.exec(res[0]);
    var c = eval(code[0]);
    // Compare Output
    if (c == "false") {
        state_map.checkpoint = "intro_menu";
        state_map.language_phase.Javascript = true;
        const jsonString = JSON.stringify(state_map);

        fs.writeFile('/opt/state/game_state.json', jsonString, err => {
        })
    }
}
