import serial
import sys
import signal
import csv
from datetime import datetime

vib = []
temp = []
vol = []
cur = []
rpm = []

def format_datetime(dt):
    # Format the datetime object into a string without separators
    formatted_datetime = dt.strftime("%Y%m%d%H%M%S")
    return formatted_datetime

def avg(lst):
    numeric_values = [float(num_str) for num_str in lst if num_str.strip()]

    if numeric_values:
        average = sum(numeric_values) / len(numeric_values)
        return average
    else:
        return None

def main():
    directory = 'C:/Users/PC/OneDrive/Desktop/VAT/'
    c_t = directory + "Readings." + format_datetime(datetime.now()) + ".csv"
    fin = "C:/Users/PC/OneDrive/Desktop/VAT/FINAL REPORT.csv"
    serp = "COM3"
    baud = 9600
    t = 0
    c = 0
    
    ser = serial.Serial(serp, baud)
    print("Connected to Arduino Port: " + serp)
    
    with open(c_t, 'a', newline="") as filec:
        print("New File has been created....")
        csv_writer = csv.writer(filec)
        csv_writer.writerow(['Vibration', 'Temperature [C]', 'Voltage Drawn [V]', 'Current Drawn [mA]', 'RPM', 'Time [in s]'])
        
        def signal_handler(sig, frame):
            print("\nInterrupt received, closing serial connection and CSV file...")
            ser.close()
            
            # Aggregate and write to FINAL REPORT.csv upon interruption
            po = [
                format_datetime(datetime.now()),
                avg(vib),
                avg(temp),
                avg(vol),
                avg(cur),
                avg(rpm)
            ]
            
            # Open FINAL REPORT.csv in append mode and write aggregated data
            with open(fin, 'a', newline="") as aq:
                pp = csv.writer(aq)
                pp.writerow(po)
                
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        try:
            while True:
                getD = ser.readline().decode().strip()
                if getD:
                    reading = getD.split('\t')
                    if len(reading) >= 5:
                        reading.append(f"{t:.1f}")
                        vib.append(reading[0])
                        temp.append(reading[1])
                        vol.append(reading[2])
                        cur.append(reading[3])
                        rpm.append(reading[4])
                        
                        csv_writer.writerow(reading)
                        print(reading)
                
                c += 1
                t += 0.1
            
        except KeyboardInterrupt:
            print("\nInterrupt received, closing serial connection and CSV file...")
            ser.close()
            signal_handler(signal.SIGINT, None)  # Trigger the signal handler for cleanup

if __name__ == "__main__":
    main()
