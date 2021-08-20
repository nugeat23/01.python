#include <Button.h>

Button btn(2);

const int relay_pin = 12;
boolean relay_out = LOW;

void check(){                            //Button callback -> interrupt 방식

    if(!btn.debounce()) return;

    relay_out = !relay_out;             // 릴레이 제어핀 출력값 반전
    digitalWrite(relay_pin, relay_out); //릴레이 제어핀 새 출력값 출력


}

void setup() {
    btn.attachInterrupt(check, FALLING);         // 인터럽트 연결
    pinMode(relay_pin, OUTPUT); 
}

void loop() {

}