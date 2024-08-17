#include <Wire.h>
#include <Servo.h>

Servo ESC;

const int escpin = 9;

const int upbuttonpin = 5;
const int downbuttonpin = 6;
const int ledpin = 13;

int power = 0; 
int waterspeed = 0;

void servobyms(int ms){
  ESC.write(map(ms, 1, 2, 0, 180));
}

void initesc () {
  // (1) connect the esc ground -> by switching on, it turns on
  // give esc 1ms or 2ms which means maximum speed
  servobyms(1);
  delay(1000);
  //give esc neutral signal
  servobyms(1.5);
  delay(1000);
  //initial end
}


void setup() {
  ESC.attach(9);  // 서보를 9번 핀에 연결
  initesc();

  pinMode(upbuttonpin, INPUT);
  pinMode(downbuttonpin, INPUT);
  pinMode(ledpin, OUTPUT);
  
  
  Serial.begin(9600);
}

void loop() {
  bool up = digitalRead(upbuttonpin);
  bool down  = digitalRead(downbuttonpin);
  
  int angle = map(power, 0, 100, 90, 0);  // 0~1023 범위를 0~180 범위로 매핑
  
  digitalWrite(ledpin, LOW);
  if (up && power <= 100) power += 1;
  if (down && power >=0) power -=1;
  
  
  ESC.write(angle);  // 서보 각도 제어
  
  Serial.print(up);
  Serial.print("\t");
  Serial.print(down);
  Serial.print("\t");
  Serial.print(angle);
  Serial.print("\t");
  Serial.println(power);

  delay(100);  // 갱신 속도 제어를 위한 지연
}

