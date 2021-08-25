#include <ArduinoJson.h>

void setup(){

    Serial.begin(115200);

    String buf = "{\"sensor\":\"temp\",\"value\":20.5}";    //네트워크 수신 문자열

    StaticJsonDocument<256> doc;

    auto error = deserializeJson(doc, buf);
    if (error){

        Serial.print("deserializeJson() failed with code");
        Serial.println(error.c_str());
        return;
    }
    const char* sensor = doc["sensor"];
    // const char* value = doc["value"];
    float value = doc["value"].as<float>(); //float 타입으로 캐스팅

    Serial.println(sensor);
    Serial.println(value);

}

void loop(){



}