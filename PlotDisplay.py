import pandas as pd
import matplotlib.pyplot as plt

try:
    file_path = r"C:\Users\PC\OneDrive\Desktop\VAT\Readings.20240425145857.csv"
    df=pd.read_csv(file_path, encoding='latin-1')
    vib=df['Vibration']
    temp=df['Temperature [C]']
    vol=df['Voltage Drawn [V]']
    curr=df['Current Drawn [mA]']
    rpm=df['RPM']
    tim=df['Time [in s]']
    fig, ((ax1, ax2), (ax3, ax4), (ax5, _)) = plt.subplots(nrows=3, ncols=2, figsize=(12, 18))

    # Plot 1: Sinusoidal wave
    ax1.plot(tim,vib,marker='o', linestyle='-', color='b', label='Vibration')
    ax1.set_title('Plot 1: Vibration vs Time')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.grid(True)
    ax1.legend()

    # Plot 2: Exponential decay
    ax2.plot(tim,temp,marker='o', linestyle='dotted', color='r', label='Temperature')
    ax2.set_title('Plot 2: Temperature vs Time')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.grid(True)
    ax2.legend()

    # Plot 3: Random noise
    ax3.scatter(tim,vol,marker='o', linestyle='--', color='g', label='Voltage')
    ax3.set_title('Plot 3: Voltage vs Time')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.grid(True)
    ax3.legend()

    # Plot 4: Quadratic function
    ax4.plot(tim,curr,marker='o', linestyle='-.', color='m', label='Current')
    ax4.set_title('Plot 4: Current vs Time')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.grid(True)
    ax4.legend()

    # Plot 5: Sigmoid function
    ax5.plot(tim,rpm,marker='o', linestyle=':', color='k', label='RPM')
    ax5.set_title('Plot 5: RPM vs Time')
    ax5.set_xlabel('X')
    ax5.set_ylabel('Y')
    ax5.grid(True)
    ax5.legend()

    # Hide the unused subplot (ax6)
    ax6 = fig.add_subplot(3, 2, 6)
    ax6.axis('off')

    # Adjust layout
    plt.tight_layout()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)  # Show gridlines
    plt.legend()  # Show legend based on 'label' in plot function
    plt.show()
except FileNotFoundError as e:
    print(f"Error: CSV file not found - {e}")
except KeyError as e:
    print(f"Error: Column not found in DataFrame - {e}")
except Exception as e:
    print(f"Error: An unexpected error occurred - {e}")
