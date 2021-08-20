#include <MiniCom.h>
#include <Keypad.h>
#include <Led.h>
#include "keymap.h"


MiniCom com;
Led beep(13);
// Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);


String input="";
bool b_Input = false; // 키 입력 상태 변수, * 누르면 true, # 누르면 false



void setup() {

    com.init();
    com.print(0, "[[Keypad Test]]");

}

void loop() {

    char key = keypad.getKey();
 
    if (key) {         
        process(key);
    }
}

void process(char key){
    tick();
    if(key == '*' && b_Input==false){ // 키입력 시작     
                 
      input="";
      b_Input=true;
      com.print(1,"start");     

    }



    else if(key =='#'){ // 키입력 완료
        b_Input =false;
        check();    // 마지막 처리


    }

    else if(b_Input){

        input += key;

    }

}

void check(){

    com.print(1,input.c_str());
    delay(3000);
    com.print(1,"");

}

void tick(){

    beep.on();
    delay(100);
    beep.off();


}











