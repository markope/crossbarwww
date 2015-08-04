



```cpp
static const int PIN_LED1 = 11;

void setup() {
  pinMode(PIN_LED1, OUTPUT);
}

void loop() {
  digitalWrite(PIN_LED1, HIGH);
  delay(500);
  digitalWrite(PIN_LED1, LOW);
  delay(500);
}
```

https://store.arduino.cc/product/T020010

Pin 11 on the Arduino is O0 on the shield.
Pin 10 on the Arduino is O1 on the shield.
Pin 9 on the Arduino is O2 on the shield.
Pin 6 on the Arduino is O3 on the shield.
Pin 5 on the Arduino is O4 on the shield.
Pin 3 on the Arduino is O5 on the shield.
