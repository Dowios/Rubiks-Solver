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
}

void selectMove(char str) {
  switch(str) {
    case 'U':
      moveMotor(TOP, LOW);
      break;
    case 'u':
      moveMotor(TOP, HIGH);
      break;
    case 'D':
      moveMotor(BTM, LOW);
      break;
    case 'd':
      moveMotor(BTM, HIGH);
      break;
    case 'L':
      moveMotor(LFT, LOW);
      break;
    case 'l':
      moveMotor(LFT, HIGH);
      break;
    case 'R':
      moveMotor(RGT, LOW);
      break;
    case 'r':
      moveMotor(RGT, HIGH);
      break;
    case 'F':
      moveMotor(FRT, LOW);
      break;
    case 'f':
      moveMotor(FRT, HIGH);
      break;
    case 'B':
      moveMotor(BCK, LOW);
      break;
    case 'b':
      moveMotor(BCK, HIGH);
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
