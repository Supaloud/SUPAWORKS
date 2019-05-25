#include <Servo.h>

#include <Wire.h>
#include <Adafruit_PN532.h>

#define PN532_IRQ   (2)
#define PN532_RESET (3)

Adafruit_PN532 nfc(PN532_IRQ, PN532_RESET);

Servo myservo;

void setup() {
  myservo.attach(9);
  delay(100);
  myservo.write(0);
  delay(100);
  myservo.detach();
  Serial.begin(115200);
  Serial.println("Hello!");
  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1);
  }
  Serial.print("Found chip PN5");
  
  nfc.SAMConfig();
  
  Serial.println("Waiting for an ISO14443A Card ...");
}

void loop() {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
  uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
  
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  
  if (success) {
    Serial.println("Found an ISO14443A card");
    nfc.PrintHex(uid, uidLength);
    myservo.attach(9);
    delay(1000);
    
    if (uidLength == 4) {
      uint32_t cardid = uid[0];
      cardid <<= 8;
      cardid |= uid[1];
      cardid <<= 8;
      cardid |= uid[2];  
      cardid <<= 8;
      cardid |= uid[3]; 
      Serial.print("#");
      Serial.println(cardid);
    }
    char a;
    a = Serial.read();
    if(a!=0){
      myservo.write(90);
      delay(2000);
      
      uint8_t success;
      uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
      uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
 
      success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
      if (success) {
        Serial.println("Found an ISO14443A card");
        nfc.PrintHex(uid, uidLength);
        if (uidLength == 4) {
          uint32_t cardid = uid[0];
          cardid <<= 8;
          cardid |= uid[1];
          cardid <<= 8;
          cardid |= uid[2];  
          cardid <<= 8;
          cardid |= uid[3]; 
          Serial.print("#");
          Serial.println(cardid);
          Serial.println("0");
          char a;
          a = Serial.read(); 
          if(a==0){
            myservo.write(0);
            myservo.detach();
            delay(2000);
          }
        }
      }
    }
  }
}

  
