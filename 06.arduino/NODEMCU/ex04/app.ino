#include <ArduinoJson.h>


void setup(){

    Serial.begin(115200);
    StaticJsonDocument<256> doc;

    doc["value"] = 42;
    doc["lat"] = 42.748010;
    doc["lon"] = 2.293491;
    
    char output[256];

    serializeJson(doc, output);
    Serial.prinln(output);


}

void loop(){




}