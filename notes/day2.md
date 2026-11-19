# Day2: 19 Nov 2026

#Linux directories

1. /etc - This is for configuration files . Try this - cat /etc/os-release , cat /etc/hostname
2. /var - This is my data that changes ; logs,caches . Try this - ls /var/log
3. /tmp - This is my temporary folder , files are cleared on reboot . Try this - ls /tmp
4. /sys - These have the hardware and kernel settings. Try this - ls /sys/class/net( shows the network cards).
5. /home - User's personal folders . Try this - ls /home , echo $HOME
6. /proc - These are live kernel data , not real files on disk . Try this - head -5 /proc/cpuinfo , cat /proc/loadavg
7. /usr/bin - These shows most installed programs .. Try this - which ls, 'ls/usr/bin'
8. /dev - Devices shown as files. Try this - ls /dev
9. /boot - These shows kernels anbd boot files . Try this - ls /boot 
