#include <MqttCom.h>
#include <DHT.h>
#include <Analog.h>

const char *ssid = "nugeat";
const char *password = "asdf6292";
const char *mqtt_server = "192.168.0.159"; // mqtt broker ip address
MqttCom com;
DHT dht11(D6, DHT11); // DHT11 객체 생성
Analog cds(A0, 0, 1023, 0, 100);

void publish() {
 char msg[50];
 float fh, fc;
 fh = dht11.readHumidity(); // 습도 측정
 fc = dht11.readTemperature(); // 섭씨 온도 측정
 int illu = cds.read(); // 조도 측정
 if (isnan(fh) || isnan(fc)) { // 측정 실패시에는 출력없이 리턴
 Serial.println("DHT11 read failed!!");
 return;
 }
 
 com.publish("iot/temp", fc);
 com.publish("iot/humi", fh);
 com.publish("iot/illu", illu);
}

void setup() {
 com.init(ssid, password);
 com.setServer(mqtt_server, NULL, NULL);
 com.setInterval(2000, publish);
 dht11.begin();
}
void loop() {
 com.run();
}