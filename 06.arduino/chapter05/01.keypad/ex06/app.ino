//EEPROM

#include <EEPROM.h>

int randomNumber;

void setup(){

    Serial.begin(115200);
    randomSeed(analogRead(0));

}

void loop(){

    Serial.println("Random Numbers");

        for(int i = 0; i <10; i++){     //EEPROM에 데이터 쓰기
            randomNumber = random(256);
            EEPROM.write(i, randomNumber); // write(주소,값)
            delay(100);

        }

    Serial.println();

        
        for(int i = 0; i <10; i++){     //EEPROM에 데이터 읽기
            randomNumber = EEPROM.read(i);  //read(주소)
            EEPROM.write(i, randomNumber); // write(주소,값)

            Serial.println("EEPROM Address : " + String(i) + "\t Value : " + 
            randomNumber);


            delay(100);

        }

    while(true); //1회만 시행 후 대기

}