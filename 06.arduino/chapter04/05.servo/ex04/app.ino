// 문제
// 버튼을 한번 누른 경우 서보 모터 90도 회전
// 버튼을 한번 더 누르면 서보 모터 0도 회전

#include <Button.h>
#include <Servo.h>
#include <MiniCom.h>

MiniCom com;
Button btn(2);
Servo myServo;
const int servo_pin = 5;
bool bOpen = false;

void open(){

    myServo.write(90);
    com.print(1, "Open");

}

void close(){

    myServo.write(0);
    com.print(1, "Close");


}

void check(){

    bOpen = !bOpen;
    if(bOpen){      //열림
        open();
    }
    else{
        close();
    }


}

void setup(){

    com.init();
    com.print(0, "Servo Test3");
    myServo.attach(servo_pin);

}

void loop(){


}