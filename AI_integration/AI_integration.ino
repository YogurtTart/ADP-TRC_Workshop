void setup() {
    Serial.begin(9600);  // Start serial communication
    Serial.println("Enter a message:");
}

void loop() {
    if (Serial.available()) {  // Check if data is available
        String input = Serial.readStringUntil('\n');  // Read input until newline
        input.trim();  // Remove extra spaces/newlines
        
        if (input.length() > 0) {  // Ensure input is not empty
            Serial.print("Received: ");
            Serial.println(input);  // Send it back
        }
    }
}
