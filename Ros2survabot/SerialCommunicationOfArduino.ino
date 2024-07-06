//distance variables
//setup a distance threshold to determin when to turn away
int cm = 0;

//sensor distance calculation function
long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT); //set trigger to output
  pinMode(echoPin, INPUT); //set echo to input
  
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2); 
  digitalWrite(triggerPin, HIGH); //set trigger pin to HIGH for 10 microseconds
  delayMicroseconds(10); //initiate the working time delay
  digitalWrite(triggerPin, LOW); //set trigger pin to Low
  
  return pulseIn(echoPin, HIGH); //return what the sensor detected
}


//setup function
void setup()
{
  Serial.begin(9600);
}


//loop function
void loop()
{
  //to calculate the distance in cm we need to multiply the time needed with 0.017
  cm = 0.01723 * readUltrasonicDistance(11, 6);  
  Serial.println(cm);;  
  //Get Serial feedback from the Sensor
  delay(10); //wait 10 milliseconds
}