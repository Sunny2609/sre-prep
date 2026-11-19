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


-> Also done the bandit challenges (Levels 0 -5)
- Level 0->1: ssh user@host -p PORT to log in , 'cd' alone takes me to my home folder.
- Level 1->2: a file named '-' confuses cat ( it means stdin). For that we hve fixed it by using: cat ./-
- Level 2->3: filenames with spaces need "quotes" or Tab-complete
- Level 3->4: files starting with . are hidden. 'ls -a' shows them.
- Level 4->5: 'file ./*' shows each file's type. Check the type before using cat 





Learned the concepts of relative paths and absolute paths.
Absolute path starts with / (from root). Relative path starts from where I am.
. = current folder , .. = parent folder , ~ = home folder
-rw-r----- bandit4 bandit3: owner can read/write, group can read , others can do nothing .
If cat on a binary file breaks the terminal, then just type 'reset'. 
