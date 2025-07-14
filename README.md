# `Sound to Image`

## sudo apt-get install qsstv

<img width="768" height="602" alt="image" src="https://github.com/user-attachments/assets/eed9aed0-8437-46e2-9c57-2e921acf8d48" />

```bash
vicky@vicky-HP-ProBook-430-G3:~/Documents/Projects/SSTV-main$ sudo apt-get install qsstv
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libfftw3-double3 libhamlib4 libqt5xml5
Suggested packages:
  libfftw3-bin libfftw3-dev
The following NEW packages will be installed:
  libfftw3-double3 libhamlib4 libqt5xml5 qsstv
0 upgraded, 4 newly installed, 0 to remove and 48 not upgraded.
Need to get 2,590 kB of archives.
After this operation, 15.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libfftw3-double3 amd64 3.3.8-2ubuntu8 [770 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libhamlib4 amd64 4.3.1-1build2 [924 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5xml5 amd64 5.15.3+dfsg-2ubuntu0.2 [124 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 qsstv amd64 9.5.8-2 [771 kB]
Fetched 2,590 kB in 4s (729 kB/s)
Selecting previously unselected package libfftw3-double3:amd64.
(Reading database ... 290882 files and directories currently installed.)
Preparing to unpack .../libfftw3-double3_3.3.8-2ubuntu8_amd64.deb ...
Unpacking libfftw3-double3:amd64 (3.3.8-2ubuntu8) ...
Selecting previously unselected package libhamlib4:amd64.
Preparing to unpack .../libhamlib4_4.3.1-1build2_amd64.deb ...
Unpacking libhamlib4:amd64 (4.3.1-1build2) ...
Selecting previously unselected package libqt5xml5:amd64.
Preparing to unpack .../libqt5xml5_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5xml5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package qsstv.
Preparing to unpack .../qsstv_9.5.8-2_amd64.deb ...
Unpacking qsstv (9.5.8-2) ...
Setting up libqt5xml5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up libfftw3-double3:amd64 (3.3.8-2ubuntu8) ...
Setting up libhamlib4:amd64 (4.3.1-1build2) ...
Setting up qsstv (9.5.8-2) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.10) ...

vicky@vicky-HP-ProBook-430-G3:~/Documents/Projects/SSTV-main$ python3 sound2image.py 
✅ Image decoded and saved to: decoded_image.png
```
