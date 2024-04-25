#include <dht11.h>
#include<Wire.h>
const int vib=2,ir=3,vs=A2,curr=A1,temp=7;
int rpm,oldT=0,time,sec;
float vIn,sensitivity=0.185,current=0.0,vSV,rev=0,l;
const float fact= 5.128,vCC=5.00;
dht11 DHT11;
void isr()
{
  rev++;
}
void setup()
{
  pinMode(vib,INPUT);
  pinMode(ir,INPUT);
  pinMode(temp,INPUT);
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(ir),isr,RISING);
}
void loop()
{
  int mes=vibra();
  int poV=analogRead(curr);
  int chk=DHT11.read(temp);
  int vSV=analogRead(vs);
  vIn=vSV*(25.0/1024.0);
  float mv=(poV/1024.0);
  current=(mv/sensitivity);
  int t=(float)DHT11.temperature;
  detachInterrupt(digitalPinToInterrupt(ir));
  time=millis()-oldT;
  rpm=(rev/time)*600;
  oldT=millis();
  rev=0;
  delay(10);
  Serial.print(mes);
  Serial.print("\t" );
  Serial.print(t);
  Serial.print("\t" );
  Serial.print(vIn);
  Serial.print("\t" );
  Serial.print(current,2);
  Serial.print("\t" );
  Serial.print(rpm);  
  Serial.println("");
  attachInterrupt(digitalPinToInterrupt(ir),isr,RISING);
}
int vibra()
{
  int mes=pulseIn(vib,HIGH);
  return mes;
}