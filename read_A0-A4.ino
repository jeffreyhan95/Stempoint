void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly
  // read A0
  int val0 = analogRead(0);
  // read A1
  int val1 = analogRead(1);
  // read A2
  int val2 = analogRead(2);
  // read A3
  int val3 = analogRead(3);
  // print to serial
  Serial.print(val0);
  Serial.print(" ");
  Serial.print(val1);
  Serial.print(" ");
  Serial.print(val2);
  Serial.print(" ");
  Serial.print(val3);
  Serial.print("\n");
  // wait 
  delay(1000);
}
