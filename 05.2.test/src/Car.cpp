#include "Car.hpp"





// 생성자 함수 정의
Car::Car() {

}


// 파괴자 함수 정의
Car::~Car() {

}

// 리턴타입 클래스명::메서드명(인자) { }
int Car::getSpeed(){

    return speed;

}

void Car::setSpeed(int s){

    speed = s;

}