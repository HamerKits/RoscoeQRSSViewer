# RoscoeQRSSViewer  
Roscoe QRSS Viewer  
MIT License - See LICENSE.md  
Copyright 2023 John Hamer  

My name is John Hamer. I enjoy experimenting with low-frequency radio. I run the lowfer station JH in Conway SC FM03mw at frequency 181818Hz. For more information on LF stations in North America, visit www.lwca.org.

Roscoe QRSS Viewer is an open source python script to display a slow waterfall. The input is taken from the computers sound card. This script is similar to the popular program ARGO, but is not intended to be a replacement.

I wrote this script for my personal experiments, but made available as a base for other peoples experiments or as an alternative to available software that does not have cross platform support. 

One of the main things I wanted to do with this software is run it on Android. This is so I can monitor my staion from the Android head unit/radio in my car. I have run a variant of this software using pydroid, which does not currently support PySide2, with PyQt5. I switched to PySide2 for the license agreement, but plan to make this support PySide2 or 6 by default and use PyQt5 as a backup with a disclaimer stating the package will be licensed under a GPL license. I will still keep the code under MIT, as PyQt5 is not a requirement to use this software. PyAudio is not supported by Android, so I will have to add support for audiostream. This should also make it compatable with iOS devices.

This software currently uses the FFT heavily with certain settings. This is due to the open nature of the span/frequency/QRSS settings. I think this is a nice feature of this script. Argo reduces this issue by limiting the span to pre-determined values based on the QRSS settings and limiting the monitorable frequency range. This makes it impossible to monitor VLF frequencies directly from the sound card without downconverting hardware. 

I plan to reduce the FFT load by using software downconverting techniques for higher frequency really slow QRSS speeds in combination with averaging the output from multiple FFT results. This should lower the FFT bin size and move much of the calculations to simple additions and multiplications from Numpys fast C++ libraries. For large frequency spans, I will average the sample to smaller samples to reduce the FFT bin size. This is probably not an issue on fast computers, but I use a slower Windows 7 computer for my monitoring because it is electrically quieter than my faster computers. This causes issues with my SDR so I have to play with settings to make it not sputter/skip. This skipping makes the data into the FFT inaccurate and smears the signals displayed making them harder to decipher. Soapy support will further reduce CPU load be eliminating the need to run the SDR software. These changes need to be made before adding Soapy support due to the large sample rates of SDR devices.

![](./images/RoscoeQRSSViewer.jpg)

Advantages:  
1. Open source - Can be modified/customized  
2. Cross platform - Not limited to windows  

Disadvantages:  
1. If using windows, requires windows 7 (I think)  
2. CPU/memory hog compared to comparable software written in non-interpreted languages  

Future plans (somewhat in order):  
1. Better AGC techniques to increase visibility of weaker signals
2. Reduce FFT overhead for increased performance which will allow higher sample rates used in SDRs
3. SOAPYSDR support for reading directly from SDRs  
4. Notch filters to reduce local signals  
5. Overlapping over time to improve graphics for VLF experiments/weak signals  
6. Piggyback off FFT to show multiple frequency ranges  
7. Scrolling frequency to change center frequency
8. Full page visual gain adjustment to allow easier setup
9. Support for Android/iOS.

Requirements:  
1. Python3.9 or later  
2. Numpy  
3. PyAudio
4. PySide2
