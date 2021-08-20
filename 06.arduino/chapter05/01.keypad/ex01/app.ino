#include <MiniCom.h>
#include <Keypad.h>
#include "keymap.h"
MiniCom com;

// Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
String input="";

void setup() {

    com.init();
    com.print(0, "[[Keypad Test]]");

}

void loop() {

    char key = keypad.getKey();
 
    if (key) {         // NO_KEY(0)
    // String str(key);
    input += key; // 키 입력 누적
    com.print(1, input.c_str());
    }
}