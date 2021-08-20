#include <SimpleTimer.h>

SimpleTimer timer;
int timerId;

void reset(){

    Serial.print("reset----------------------");

}

void setup(){

    Serial.begin(115200);
    timerId = timer.setTimeout(2000,reset);

    delay(1000);
    timer.restartTimer(timerId);

}

void loop(){

    timer.run();

}