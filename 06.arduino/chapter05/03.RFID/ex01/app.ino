#include <MFRC522.h>
#include <Buzzer.h>

#define RST_PIN 9       //reset 핀은 9번으로 설정
#define SS_PIN  10      //SS핀은 10번으로 설정
                        //SS핀은 데이터를 주고받는 역할의 핀(SS=Slave Selector)

MFRC522 mfrc(SS_PIN, RST_PIN);  //MFR522 객체 생성
Buzzer buzzer(8);

byte myId[4] = {    // 등록된 ID

    9,180,145,85

};

bool checkId(byte id[]){    // 배열 인자 선언

    for(int i=0; i<4; i++){

        if(myId[i] != id[i]){   // 한 개의 값이 다르면 --> 두 id가 다름

            return false;

        }

    }
    // 루프를 끝냈음 --> 두 id가 같음
    return true;

}

void setup(){
    Serial.begin(9600);
    SPI.begin();
    mfrc.PCD_init();

}


void loop(){

    if (!mfrc.PICC_IsNewCardPresent()||!mfrc.PICC_ReadCardSerial()){
    // 태그 접촉이 되지 않았을때 또는 ID가 읽혀지지 않았을 때
    delay(500);
    return;
}
buzzer.beep();      // 비프음, Led 효과 출력

// 등록된 id(myID)와 동일한 ID인지 검사
// if(myId==mfrc.uid.uidByte){     //일치하면 myId는 byte배열 타입, mfrc.uid.uidByte는 byte배열 타입

if(checkId(mfrc.uid.uidByte)){

    greenLed.on();
    delay(1000);
    greenLed.off();


}

else{       //일치하지 않으면

    buzzer.beep(1000); // 지정한 초동안 beep음 내도록

}

// Serial.print("Card UID:");      // 태그의 ID 출력

// 태그의 ID 출력하는 반복문. 태그의 ID사이즈(4)까지
// for (byte i = 0; i <4;, i++){

//     // mfrc.uid.uidByte[0] ~ mfrc.uid.uidByte[3]까지 출력
//     Serial.print(mfrc.uid.uidByte[i]);
//     Serial.print(" ");      // id 사이의 간격 출력

//     Serial.println();
// }