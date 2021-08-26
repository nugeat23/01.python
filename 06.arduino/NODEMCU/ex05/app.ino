#include <WifiMiniCom.h>
#include <ArduinoJson.h>

const char *ssid = "Campus7_Room4_2.4GHz";
// const char *password = "12345678"
const char *password =NULL;

String host = "api.openweathermap.org";
String url = "/data/2.5/weather?q=seoul&APPID=8bf29d04be249c169416af30176d94c9&units=metric";

// 디폴트는 켈빈 온도
// 섭씨온도는 켈빈 온도 - 273.15

WifiMiniCom com;

bool request(WiFiClient &client) { 

    const int port = 80;
    if (!client.connect(host, port))
    {
    Serial.println("connection failed");
    return false;
    }
    
    Serial.print("Requesting URL: ");
    Serial.println(url);
    
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +       //GET 뒤에 반드시 space, HTTP앞에 space, 요청라인
                            "Host: " + host + "\r\n" +          // 헤더
                            "Connection: close\r\n\r\n");       // 헤더 끝을 나타내는 빈줄

    // client.println();
    // client.println();
    // client.println();
    // client.println();

    return true;

}

void deserialize(String line) {

    // DynamicJsonDocument doc(800); 
    StaticJsonDocument<800> doc; 
    auto error = deserializeJson(doc, line);
    if (error) {
    Serial.print("deserializeJson() failed with code ");
    Serial.println(error.c_str());
    return;

 }
    String w_main = doc["weather"][0]["main"];
    double temp = doc["main"]["temp"].as<double>();     //온도
    double humi = doc["main"]["humidity"].as<double>(); //습도

    String msg = "weather: " + w_main;
    com.print(0, msg.c_str());
    msg = String("T:") + temp + ", H:" + humi;
    com.print(1, msg.c_str());


}

String response(WiFiClient &client) {

    int timeout = millis() + 5000;
    while (client.available() == 0) {

    if (timeout - millis() < 0) {
    Serial.println(">>> Client Timeout !");
    client.stop();
    return "";

        }
    } 

    bool isBody = false;
    String body ="";

    while(client.available()) {

            String line = client.readStringUntil('\r');    // 1줄 읽기
            line.trim();                                   // 공백 제거
            if(line == "") {
            isBody = true;
            continue;
            }

        Serial.println(line);
        if(isBody) {
        body = line;                                   //json 문자열
        break;
            }
        }

        Serial.println();
        Serial.println("closing connection");

        return body;
}

void setup(){

    com.init(ssid,NULL);
    
}

void loop(){

    WiFiClient client;

    if(request(client)) {

    String body = response(client);
    deserialize(body);

    }
    
    delay(100000);


}