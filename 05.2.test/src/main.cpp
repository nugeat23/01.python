#include <iostream>
#include <string>
#include "Car.hpp"
using namespace std;


int main() {
    
    Car myCar;

    myCar.setSpeed(100);

    cout << "속도 : " << myCar.getSpeed() << endl;

    return 0;
    

}