<ZINE>
<img width="551" height="788" alt="image" src="https://github.com/user-attachments/assets/6165940e-1fb5-4d81-9e86-503c6038dce4" />

  The cloud keyboard is a simple cloud-shaped 3x3 keyboard designed using KiCAD and Onshape. It connects with a USB, and runs a simple micropython code that prints a designated number on the coding shell for each key when pressed.

## ***Inspiration~***
I made this keyboard because I wanted a to build a personalized cute keyboard completely from scratch. It was my first ever PCB I ever designed, and it helped me learn a LOT. 

## ***Full Instructions~***

**getting the pcb**
1. go to https://jlcpcb.com/. click "get instant quote".
2. download the gerber zip file from the pcb folder and upload it.
3. you can change the color of the PCB if you'd like, but keep all the other settings the same.
4. order your PCB by following the steps on the website.

**getting the parts**
1. To find all the suitable parts needed for this pcb, open the BOM file. This lists all the necessary parts needed for the PCB-- you'll see several links leading to product pages.

**printing the case**
1. download the STL files, or go open this onshape link: https://cad.onshape.com/documents/30ca1b2b31257d2650154877/w/6a6ce5b2935f39e9888c6e90/e/9cf32ad964649424d66e1c2f?renderMode=0&uiState=6a1fb2345d12723005a9a689.
2. follow the directions on your own 3D printer's manufacturer's website/app to upload the STL files in and print them. support for the prints are not neeeded, as long as you have the models sitting on the correct side.

**soldering and putting everything together**
1. solder the pieces together in their designated spots. You can use the .step file to see how it should look like in the end (the battery cell is optional). Make sure to sandwich the keys together with the top of the case, putting the keys in from the top.
2. After you're done soldering it, plug the ESP32 into your device using a USB-C.
3. Import micropython onto your ESP32 by uploading the ESP32_GENERIC_C3-20260406-v1.28.0.bin into the adafruit webserial bootloader (https://adafruit.github.io/Adafruit_WebSerial_ESPTool/)(to start this, click the "connect" button on the upper right corner. no offset is needed.). 
4. Run keys.py on Thonny after connecting to the ESP32 by selecting the suitable option on the lower left corner.


## ***GALLERY~***
<details>
  <summary>3D model, PCB design, schematic, etc</summary>
<img width="891" height="653" alt="image" src="https://github.com/user-attachments/assets/7323a848-ede7-4593-80b1-8ce7abd7586a" />
<img width="1007" height="833" alt="image" src="https://github.com/user-attachments/assets/b3f32099-1b07-4e01-99a3-6a676b3562ed" />
<img width="719" height="487" alt="image" src="https://github.com/user-attachments/assets/bac06c70-8b7d-4e91-b26e-29bfaa08ae4b" />
<img width="738" height="744" alt="image" src="https://github.com/user-attachments/assets/43ed9a53-5819-492b-8f3b-27e9059a4014" />
<img width="1281" height="924" alt="image" src="https://github.com/user-attachments/assets/d1daff77-2d7d-426e-9703-4416e9e301b2" />

<img width="539" height="303" alt="image" src="https://github.com/user-attachments/assets/b36119f6-1f06-4e04-8963-c042a19a32e7" />
<img width="799" height="540" alt="image" src="https://github.com/user-attachments/assets/045d28ca-455b-4cb7-b8ee-a7835cb4b26d" />
</details>

## ***Credits~***
This project used:
- [KiCAD](https://www.kicad.org/) (for PCB design)
- [Onshape](https://www.onshape.com/en/platform) (for case design) 
