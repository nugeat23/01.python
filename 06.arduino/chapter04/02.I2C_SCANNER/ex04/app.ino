#include <LiquidCrystal_I2C.h>
// '김' 패턴
uint8_t name_k[8] = {
  B11101,
  B00101,
  B00101,
  B01001,
  B10001,
  B11111,
  B10001,
  B11111
}; 
// 'T' 패턴
uint8_t name_t[8] = {  
  B11111,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100
}; 
// 'G' 패턴
uint8_t name_g[8] = { 
  B00000,
  B01110,
  B11011,
  B10001,
  B10000,
  B10111,
  B10001,
  B01110
};

LiquidCrystal_I2C lcd(0x27, 16, 2); // lcd 객체 생성
void setup() 
{
 lcd.backlight();
 // put your setup code here, to run once:
 lcd.init();
 lcd.createChar(0, name_k); // '신' 패턴 코드 0으로 저장
 lcd.createChar(1, name_t); // '동' 패턴 코드 1으로 저장
 lcd.createChar(2, name_g); // '욱' 패턴 코드 2으로 저장 
}

void loop() 
{
 // put your main code here, to run repeatedly: 
 lcd.setCursor(0, 0); // 커서 2행 1열(0, 1)
 lcd.print("Hello, Arduino!"); // 문자열 표시
 lcd.setCursor(0, 1); // 커서 2행 1열(0, 1)
 lcd.print("My name is "); // 문자열 표시
 lcd.write(0);
 lcd.write(1);
 lcd.write(2);
}