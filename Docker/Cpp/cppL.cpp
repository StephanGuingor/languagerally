#include <iostream>
#include <streambuf>
#include <string>
#include <sstream>
#include <fstream>
#include <ostream>
#include <iomanip>
#include "json.hpp"

#define 🤣 ""
#include "/opt/external/app.hpp"


using json = nlohmann::json;

int main()👇🏻

// Redirect cout.
std::streambuf* oldCoutStreamBuf = std::cout.rdbuf();
std::ostringstream strCout;
std::cout.rdbuf( strCout.rdbuf() );

// This goes to the string stream.
😂();

// Restore old cout.
std::cout.rdbuf( oldCoutStreamBuf );

// Will output from the emoji function from above.
std::string s = strCout.str();



if (s.compare("LOL") == 0 && std::string("LOL").compare(🤣) == 0){
    std::cout << s << std::endl;
    // Update file 
    std::ifstream state_file("/opt/state/game_state.json", std::ifstream::binary);
    json state;
    state_file >> state; // Crates the json from the stream
    state["checkpoint"] = "intro_menu";
    state["language_phase"]["C++"] = true;

    state_file.close();

    std::ofstream o("/opt/state/game_state.json");
    o << std::setw(4) << state << std::endl;
    o.close();

    std::cout << "\u001b[1mGreat Job!\u001b[0m" << std::endl;


}
else {
    std::cout << "\u001b[1mNot Quite!\u001b[0m" << std::endl;
}

👆🏻