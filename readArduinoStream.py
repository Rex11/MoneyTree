##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial
import datetime

serial_port = 'COM3';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "F:\DarlingDoesItAll\MoneyTree\soil_saturation.txt";


ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    line = line[:-2] # Remove \n from the end. It's added later, but when left in here there's an extra newline for some reason
    
    timestamp = datetime.datetime.now();
    date_time = timestamp.strftime("%Y/%m/%d, %H:%M:%S")
    #print(date_time + ": " + line)
    
    output_file = open(write_to_file_path, "a+");
    output_file.write(date_time);
    output_file.write(": ")
    output_file.write(line)
    output_file.write("\n")
    
    output_file.close();