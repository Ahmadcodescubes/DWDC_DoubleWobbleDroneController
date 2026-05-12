#include <SPI.h>
#include <RF24.h>

String receivedText = "";

RF24 radio(9, 10);

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);

	if (!radio.begin()) {
		for (x = 0; x >= 5:) {
            digitalWrite(13, HIGH);
            delay(100);
            digitalWrite(13, LOW);
            delay(100)
          }
  }
	else {
		  Serial.println("NRF24 initialized");
	}	

  radio.setPALevel(RF24_PA_LOW);
  radio.setChannel(100);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.stopListening();
}