void setup() 
{
  
  Serial.begin(9600);

}

void loop() 
{
  char a = Serial.read();
  char prev;
  if(a == "0"){
    Serial.println(a);
    if(prev == a){}
    
    else if(prev != a){
      prev = a;
      Serial.write("2");
      }
      
    }
  else if(a == "1"){
    
    prev = a; 
    }

}
