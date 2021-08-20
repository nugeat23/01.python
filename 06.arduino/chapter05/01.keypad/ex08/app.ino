#include <MiniCom.h>
#include <Keypad.h>
#include <Led.h>
#include <Servo.h>
#include "keymap.h"
#include <Button.h>

#include <storage.h>

// 키 입력 누를때 마다 LCD에 *가 출력
// 키 입력 완료시 LCD 지움

//평상시에는 LCD --> 백라이트 오프
//입력 시작되면 -->백라이트 온
//입력 완료되면 -->백라이트 오프

//EEPROM을 활용한 비밀번호 관리

const int BASE_ADDRESS = 100;   // 초기 비밀번호 저장 주소
MiniCom com;
Led beep(13);
Servo lock;
Button btn(2);  // 비밀번호 설정 버튼


// Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);


String input="";
String inputStar=""; //입력할 때 출력할 *문자열
String password = ""; // 도어락 비밀번호



bool b_Input = false; // 키 입력 상태 변수, * 누르면 true(입력 시작), # 누르면 false(입력 중지) 
int timerId = -1;       // 타임 아웃 용 타이머 ID

bool bSetPassword = false;  // 비밀번호 설정 모드 여부


void setup() {

    com.init();
    com.offLcd();
    // com.print(0, "[[Door Lock]]");

    password = readRom(BASE_ADDRESS);   // EEPROM에서 비밀번호 읽기


    lock.attach(3);
    lock.write(0);

    btn.setCallback(setpassword);

}

void loop() {

    btn.check();

    com.run();      //com::run()에서 timer.run() 호출
    char key = keypad.getKey();
 
    if (key) {         
        process(key);
    }
}

void setpassword(){

    bSetPassword = !bSetPassword;   // 상태 반전
    if(bSetPassword){   // 새 비밀번호 입력 시작

        input="";
        inputStar="";
        b_Input = true;
        com.onLcd();        
        

    }

    else{   // 새 비밀번호 입력 완료

        // ROM에 비밀번호 저장
        password = input;
        password = writeRom(BASE_ADDRESS, password);
        com.print(1,"");
        com.offLcd();


    }

}


void process(char key){
    tick();
    SimpleTimer& timer = com.getTimer();
    if(key == '*' && b_Input==false){ // 키입력 시작     
                 
      input="";
      inputStar="";
      b_Input=true;
      com.onLcd();

      com.print(0,"[[Insert]]");
      timerId = timer.setTimeout(5000, reset);    

    }



    else if(key =='#' ||key =='*'){ // 키입력 완료
        timer.deleteTimer(timerId);
        b_Input =false;
        
        check();    // 마지막 처리
        com.offLcd();


    }

    else if(b_Input){

        input += key;
        inputStar += '*';
        com.print(1,inputStar.c_str());
        if(!bSetPassword){
            timer.restartTimer(timerId);
        }
    }

}

void check(){
    if(input==password) {   //비밀번호 일치
        lock.write(90);
        delay(3000);
        lock.write(0);
    }
    else {

        for(int i=0; i<4; i++){
            tick();
            delay(100);
        }
                     //비밀번호 불일치
    }

    // com.print(1,input.c_str());
    delay(1000);
    com.print(0,"[[Door Lock]]");
    delay(1000);
    com.print(0,"");
    com.print(1,"");

}

void tick(){

    beep.on();
    delay(100);
    beep.off();


}

void reset(){

    // com.print(0,"[[Door Lock]]");
    
    input = "";
    b_Input = false;
    com.offLcd();


}










