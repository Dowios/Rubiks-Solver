#define TOP 31
#define BTM 32
#define RGT 33
#define LFT 34
#define FRT 35
#define BCK 36
#define DIR 37
#define DELAY 700
void setup() {
  pinMode(TOP, OUTPUT);
  pinMode(BTM, OUTPUT);
  pinMode(RGT, OUTPUT);
  pinMode(LFT, OUTPUT);
  pinMode(FRT, OUTPUT);
  pinMode(BCK, OUTPUT);
  pinMode(DIR, OUTPUT);
  digitalWrite(TOP, LOW);
  digitalWrite(BTM, LOW);
  digitalWrite(RGT, LOW);
  digitalWrite(LFT, LOW);
  digitalWrite(FRT, LOW);
  digitalWrite(BCK, LOW);
  digitalWrite(DIR, LOW);
  Serial.begin(9600);
}

void loop() {
  char moves = Serial.read();
  selectMove(moves);
  delay(500);
}

void selectMove(char str) {
  switch(str) {
    case 'U':
      moveMotor(TOP, HIGH);
      break;
    case 'u':
      moveMotor(TOP, LOW);
      break;
    case 'D':
      moveMotor(BTM, HIGH);
      break;
    case 'd':
      moveMotor(BTM, LOW);
      break;
    case 'L':
      moveMotor(LFT, HIGH);
      break;
    case 'l':
      moveMotor(LFT, LOW);
      break;
    case 'R':
      moveMotor(RGT, HIGH);
      break;
    case 'r':
      moveMotor(RGT, LOW);
      break;
    case 'F':
      moveMotor(FRT, HIGH);
      break;
    case 'f':
      moveMotor(FRT, LOW);
      break;
    case 'B':
      moveMotor(BCK, HIGH);
      break;
    case 'b':
      moveMotor(BCK, LOW);
      break;
  }
}

void moveMotor(int face, bool dir) {
  digitalWrite(DIR, dir);
  for(int x = 0; x < 50; x++) {
    digitalWrite(face,HIGH); 
    delayMicroseconds(DELAY); 
    digitalWrite(face,LOW); 
    delayMicroseconds(DELAY);
  }
}
