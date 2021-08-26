

#include <WifiMiniCom.h>
#include <PubSubClient.h>
#include <Led.h>

const char *ssid = "Campus7_Room4_2.4GHz";
const char *password = "12345678";
const char *mqtt_server = "172.20.10.3"; //Mosquitto 설치 된 컴퓨터 ,mqtt broker ip address

WifiMiniCom com;

WiFiClient espClient;
PubSubClient client(espClient);
Led led(BUILTIN_LED);

int value = 0;

void callback(char *topic, byte *payload, unsigned int length){

    char buf[128];
    memcpy(buf, payload, length);   // length 는 NULL 데이터
    buf[length] = "\0";

    Serial.print("Message arrived [");    
    Serial.print(topic);
    Serial.print("] ");
    Serial.println(buf);

    if (buf[0] =='1'){

        led.setValue(LOW);

    }

    else{

        led.setValue(HIGH);

    }

    com.print(0,topic);
    com.print(1,buf);

}

//MQTT 브로커에 연결
void reconnect(){

    while (!client.connected()) {

    Serial.print("Attempting MQTT connection...");

    if (client.connect("ESP8266Client")) {          // 클라이언트 ID 중복 주의

    Serial.println("connected");
    client.publish("outTopic", "hello world"); 
    client.subscribe("inTopic");                    // subscribe할 토픽 등록

    }

    else {                                          // 연결실패한 경우 5초 후 재시도
    Serial.print("failed, rc=");
    Serial.print(client.state());
    Serial.println(" try again in 5 seconds"); 
    delay(5000);

    }
    }
}

void publish() {

    char msg[50];
    ++value;
    sprintf(msg, 75, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);

}

void setup() {

    com.init(ssid, password);
    com.setInterval(2000, publish);

    client.setServer(mqtt_server, 1883);
    client.setCallback(callback); // 토픽 수신 시 호출할 함수 등록

}

void loop() {

    com.run();

    if (!client.connected()) {
    reconnect();
    }

    client.loop();

}
