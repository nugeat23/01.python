// 스위치 풀업/풀다운 동작 확인
#include <Led.h>

const int pu_sw_pin = 2;    // 풀다운 스위치 연결핀(SW1)
Led led1(4);                // 풀다운 스위치 확인용

const int pd_sw_pin = 3;    // 풀업 스위치 연결핀(SW2)
Led led2(5);                // 풀업 스위치 확인용

void setup(){

    pinMode(pd_sw_pin, INPUT);  // 풀다운 스위치 연결핀 입력
    pinMode(pu_sw_pin, INPUT);  // 풀업 스위치 연결핀 입력

}

void loop(){

    boolean pd_sw, pu_sw;

    pu_sw = digitalRead(pu_sw_pin); // 풀업 스위치 상태 읽기
    led1.setValue(pu_sw);           // 풀업 스위치 상태 LED 출력

    pd_sw = digitalRead(pd_sw_pin); // 풀다운 스위치 상태 읽기
    led2.setValue(pd_sw);           // 풀다운 스위치 상태 LED 출력


}