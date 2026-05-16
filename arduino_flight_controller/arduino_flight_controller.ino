#include <SPI.h>
#include <RF24.h>

String receivedText = "";

RF24 radio(9, 10);

void setup() {
  Serial.begin(115200);

	if (!radio.begin()) {
    Serial.println("404/rf");
  }
	else {
		  Serial.println("NRF24 initialized");
	}	

  radio.setPALevel(RF24_PA_LOW);
	//NOTE FOR SELF: set everything under this curly braket the same for the receiving arduino
	//{
  radio.setChannel(100);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.stopListening();
	//}
}

void loop() {

  // Check if data exists
  if (Serial.available() > 0) {

    receivedText = Serial.readStringUntil('\n');

    receivedText.trim();
		if (receivedText = "REPLY"){
			Serial.println("YES");
		}

		if (receivedText == "DSCNT") {
			Serial.println("CONTROLLER DISCONNECTED");
			Serial.println("ENTERING SAFETY LANDING MODE");
			char Safety[32] = {0};
			receivedText = "0";
			receivedText.toCharArray(Safety, 32);
			radio.write(&Safety, sizeof(Safety));
			Serial.println("SAFETY PROTOCOL ACTIVATED, CONNECT A CONTROLLER WITHIN 5 SECONDS");
		}
		char buffer[32] = {0};
		receivedText.toCharArray(buffer, 32);
		radio.write(&buffer, sizeof(buffer));
  }
}