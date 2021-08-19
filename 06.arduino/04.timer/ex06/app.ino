#include <Led.h>
Led led(8);
boolean led_state = HIGH;
void setup() {
 Serial.begin(115200); // 시리얼 포트 115200bps 통신 시작
}
void loop() {
 led.setValue(led_state);
 if(led_state == HIGH) Serial.println("LED ON!");
 else Serial.println("LED OFF!");
 led_state = !led_state; // 다음 출력할 LED 상태 업데이트
 delay(1000); // 1초 대기
}