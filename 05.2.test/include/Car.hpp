#pragma once

#include <string>
using namespace std;


class Car {

protected:
    int speed;
    int gear;
    string color;



public: // 함수의 원형만 지정, 실제 정의는 .cpp파일에서 정의
    Car(); //생성자 함수 <-- python:__init__()
    ~Car(); //파괴자 함수
    int getSpeed();
    void setSpeed(int s);


};