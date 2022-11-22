# DER-sim-modbus
Simulation of a DER system using modbus communication

These scripts attempt to simulate a small component of the DER architecture, mainly the communication between the DERMS and DER devices using the modbus communication protocol

The code contained in `Server.py` contains the code required to simulate 3 DER smart meters in seperate threads and 1 load device simulating the power network load requirements

The code contained in `Client.py` simulates the DERMS device, sequentially telling DER devices to either provide more or less power depending on the requirements sent by the load.

# Usage:

## Basic usage:
To use this code you must have the required packages installed to install these use:

`pip install -r requirements.txt`

Once the packages are installed run the code using

`python3 Client.py`

`python3 Server.py` 

in 2 seperate terminals, they will output the logs of whats being sent between the 2 devices

## Mangle modbus communication:
To use mangled_burp.py you need to install burpsuite with and extension

To download burpsuite: https://portswigger.net/burp/communitydownload

To download burpsuite extension: https://github.com/summitt/Burp-Non-HTTP-Extension

BurpSuite is a tool used to intercept network communication between devices, in which you can modify these communication to resemble how you like
The Burp-Non-HTTP-Extension allows you to capture TCP communication between devices, without it we cant intercept and change modbus communications to what we want

Once inside Burpsuite go to the NoPE Proxy tab at the top bar:

![NoPE Proxy Tab](https://raw.githubusercontent.com/TeddyCom1/DER-sim-modbus/main/Pictures/NoPE_proxy_top_bar.jpg)

And add a proxy listener and enable it with the configuration in the following image:

![NoPE Proxy Settings](https://raw.githubusercontent.com/TeddyCom1/DER-sim-modbus/main/Pictures/NoPE_proxy_proxy_setting.jpg)

Once you have enabled the proxy listener go to the automation tab at the top and import `mangle_burp.py` and enable the script

![Python Mangler](https://raw.githubusercontent.com/TeddyCom1/DER-sim-modbus/main/Pictures/import_python_mangler.jpg)

After completing these steps run the 2 python scripts using:

`python3 Client.py y`

`python3 Server.py`

Make sure you also have installed the python script requirements with:

`pip install -r requirements.txt`

