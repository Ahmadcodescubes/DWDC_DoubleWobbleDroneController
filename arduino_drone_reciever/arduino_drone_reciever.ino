#include <SPI.h>
#include <RF24.h>

String receivedText = "";

RF24 radio(9, 10);

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);

	if (!radio.begin()) {
		for (x = 0; x >= 5; x++:) {
            digitalWrite(13, HIGH);
            delay(50);
            digitalWrite(13, LOW);
            delay(50)
          }
  }
	else {
		  Serial.println("NRF24 initialized");
      digitalWrite(13, HIGH)
	}	

  radio.setPALevel(RF24_PA_LOW);
  radio.setChannel(100);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.stopListening();
}