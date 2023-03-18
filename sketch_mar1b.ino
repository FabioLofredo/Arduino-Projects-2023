#include <HCSR04.h>
 
#define TRIGGER   9
#define ECHO      8

UltraSonicDistanceSensor distanceSensor(TRIGGER, ECHO);  
void setup () {
    Serial.begin(9600);  
    pinMode (2, OUTPUT);
    pinMode (3, OUTPUT);
    pinMode (4, OUTPUT);    
}
void loop () {
  
    int distancia = 0;
    distancia = distanceSensor.measureDistanceCm();

    Serial.println(distancia);
    if(distancia >=30)
    {digitalWrite (2, HIGH);}
    else{digitalWrite (2, LOW);}
    if(distancia >=60)
    {digitalWrite (3, HIGH);}
    else{digitalWrite (3, LOW);}
    if(distancia >=90)
    {digitalWrite (4, HIGH);}
    else{digitalWrite (4, LOW);}
    
    delay(100);
}