#include "Led.h"

Led led(3); // 3번 핀에 연결

void setup(){



}

void loop(){
    // Led Blink
    led.toggle();
    delay(1000);

}