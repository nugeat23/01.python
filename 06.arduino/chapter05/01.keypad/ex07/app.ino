#include "storage.h"

// String writeRom(int address, String value){ // 기록할 주소, 값

//     int length = value.length();
    
//     EEPROM.write(address,length);   // 문자열 길이 저장

//     for(int ix=1; ix <= length; ix++){
        
//         EEPROM.write(address+1, value.charAt(ix-1));
//         delay(100);
//     }
// }

// String readRom(int address){


//     String value ="";
//     int length = EEPROM.read(address);

//     for(int ix=1; ix<=length; ix++){

//         value += (char)EEPROM.read(address+ix); // (char): 캐스트 연산자, char 타입으로 형 변환
//         delay(100);
//     }

//     return value;
// }

void setup(){

    Serial.begin(115200);   // door lock 비밀번호의 공장 초기화 값

    writeRom(100,"1234");

    String password = readRom(100);
    Serial.println(password);


}

void loop(){

}
