# Basic False Data injection simulation

This code is used to simulate basic False data injection attacks between devices

You can run this code either on local host or multiple devices

To run this initially you need to have a couple of python packages:

numpy
mathlib

Then initially run the master connecting device (which collects all the data)

e.g:
```Bash
python3 DER_master 127.0.0.1 8081 10
```

Then run the connecting devices

e.g:
```Bash
python3 DER_device 127.0.0.1 8081 9
```

Then run the sus device to simulate false data injections

e.g:
```Bash
python3 DER_sus 127.0.0.1 8081 9
```
