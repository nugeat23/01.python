//문제

// 0.1초 간격으로 가변저항의 값을 읽음
// 가변저항 값의 범위는 0 ~ 255
// LCD 2번째 줄에 value: 24 형식으로 출력하세요.

#include <MiniCom.h>
#include <Analog.h>
#include <PWMLed.h>

Analog sensor(A0,255,0);
PWMLed led(9);
MiniCom com;

void setup(){
    com.init();
    com.print(0,"[[MiniCom]]");
    com.setInterval(100,check);

}

void loop(){

    com.run();

}

void check(){

    int value = sensor.read();
    led.setValue(value);
    com.print(1, "value: ", value);


}