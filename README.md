# Kali-Linux-Wifi-and-bluetooth-problem-Solved-
Solved problems - . Kali linux wifi and bluetooth drivers are not installed and not working properly.]

Make Sure to add this folder in '/' root folder otherwise the internal path for icons have to be changed to use it outside the root folder.

Extract the .tar file and after entering the directory do the following commands.

1. nano /etc/apt/sources.list

Add these repositories
3. deb http://http.kali.org/kali kali-rolling main non-free contrib
4. deb-src http://http.kali.org/kali kali-rolling main non-free contrib

5. sudo apt update && apt dist-upgrade
6. sudo apt install firmware-linux

cd into the extracted directory and do these
6. make unload
7. make load
8. apt-get update
9. apt-get install linux-image-$(uname -r|sed 's,[^-]*-[^-]*-,,') linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,') broadcom-sta-dkms
10. modprobe -r b44 b43 b43legacy ssb brcmsmac bcma
11. modprobe wl
