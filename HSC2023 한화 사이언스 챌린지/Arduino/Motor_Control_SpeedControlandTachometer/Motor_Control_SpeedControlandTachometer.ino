#include <Wire.h>
#include <Servo.h>

Servo ESC;

int speed = 1; // meter/second

float rotor_rev=0.0;
int rotor_rpm;

float water_rev=0.0;
int water_rpm;
float water_rotorradius = 10; // in centimeters
float water_speed;

int oldtime=0;
int time;

bool CW = true;
int pulsew = 1000; // CW false -> 1500 

int ESC_pin = 9;
int rotor_pin = 18;
int water_pin = 19; // on board mega


void calcspeed(){ //changes water_rpm into m/s of water
  float pi = 3.14;
  float metertocm = 100;

  water_speed = water_rpm * water_rotorradius / metertocm * 2 * pi / 60;
}

void adjustESC(){
  if (waterspeed <= speed) {
    pulsew += 5;
  }
  else if (waterspeed >= speed){
    pulsew -= 5;
  }
}


void rotor_isr() //interrupt service routine
{
  rotor_rev++;
}

void water_isr() //interrupt service routine
{
  water_rev++;
}


void setup() {
  ESC.attach(9);  // ESC를 9번 핀에 연결
  Serial.begin(9600);

  attachInterrupt(digitalPinToInterrupt(rotor_pin) ,rotor_isr,RISING); 
  attachInterrupt(digitalPinToInterrupt(water_pin) ,water_isr,RISING);
}

void loop() {
  //indrek's arduspreadsheet , seperated by /t
  delay(1000);
  noInterrupts();
  time=millis()-oldtime;        //finds the time 
  rotor_rpm = (rotor_rev/time)*60000; 
  water_rpm=(water_rev/time)*60000;         //calculates rpm
  calcspeed();
  adjustESC();

  /*

  
  */
  Serial.println(rotor_rpm);
  Serial.println(water_speed);
  Serial.println(speed);

  Serial.print("/t");

  oldtime=millis();             //saves the current time
  rotor_rev=0;
  water_rev = 0;  
  interrupts();
}

