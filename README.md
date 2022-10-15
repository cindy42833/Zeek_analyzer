# Zeek Analyzer
## Background
This program is homework for the course Techniques of Network Attacks and Defenses held by Po-Ching Lin in CCU.

## What is Zeek? 
Please look introduction up in the official website https://zeek.org

## How to Install and Run 
This is a Zeek analyzer written by Python that can parse your pcap file.
Environment:
- Python: 3.8.9
- Docker: 20.10.17
- Zeek: runs on Docker container
- Host OS: macOS Monerey 12.6 (M1 chip)

### 1. Install Docker 
Please check out the official document to install compatible version: https://docs.docker.com/desktop/install/mac-install/

### 2. Install Zeek running on Docker container
#### Before cloning **zeek-docker** project from Git, you have to install the following package
* Homebrew or other package management tools
  * Install [Homebrew](https://brew.sh/index_zh-tw)
  
    ```
    % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
* Git
  * After setting up Homebrew, we can use it to install Git
  
    ```
    % brew install git
    ```
  
#### Clone [**zeek-docker**](https://github.com/zeek/zeek-docker) from Git
```
% git clone https://github.com/zeek/zeek-docker.git
```

#### Enter the project directory
```
% cd zeek-docker 
```

#### Build a image
```
% make 
or 
% make build-stamp_<version>
```
* If you just type `make`, the latest released version will build. 

* Or you can designate a specific version by typing `make build-stamp_<version>`.
<br>e.g. `make build-stamp_3.0.0` builds a image from [3.0.0.Dockerfile](https://github.com/zeek/zeek-docker/blob/master/3.0.0.Dockerfile)

#### Create a container
After the process of build completed, you can see your image here.
```
% sudo docker image ls 
REPOSITORY           TAG          IMAGE ID       CREATED       SIZE
broplatform/bro      4.2.0        e0a00cb9d05e   2 days ago    199MB
```
To connect the local folder to the folder in the container, we have to make a new directory whenever you'd like.
```
% mkdir ../volumes
```
This is my file tree so far.
```
.
├── volumes
└── zeek-docker
```
Create a container connecting the current working directory to /pcap in it.
```
% cd ../volumes
volumes % docker run -it -v `pwd`:/pcap broplatform/bro:4.2.0
```

* `-v <directory of the local folder>:<directory of designated folder in the container>`
* \`pwd\` means the current working directory
* If the directory of the designated folder in the container doesn't exist, it will be created automatically.

You can see the container running now.
```
volumes % sudo docker ps -a
CONTAINER ID   IMAGE                   COMMAND                  CREATED       STATUS                     PORTS     NAMES
ccaf8d74f88c   broplatform/bro:4.2.0   "/bin/bash"              2 days ago    Up 6 minutes                         trusting_hofstadter
```

Enter the container and find Seek.
```
volumes % sudo docker exec -it ccaf8d74f88c bash
Password: <Type your password>

# List all files
# Notice that pcap was built by `docker run -it -v `pwd`:/pcap broplatform/bro:4.2.0`
root@ccaf8d74f88c:/# ls
bin  boot  bro	dev  etc  home	lib  media  mnt  opt  pcap  proc  root	run  sbin  srv	sys  tmp  usr  var  zeek

# Use command to find Zeek
root@ccaf8d74f88c:/# which zeek
/zeek/bin//zeek

# Exit the container if you need
root@ccaf8d74f88c:/# exit
exit
volumes % 
```

### 3. Analyze pcap file by Zeek
Download any pcap files you like and put it into **volumes** folder. In this example, we use [2009-M57-day11-18.pcap](https://drive.google.com/file/d/1iX_fS1EoJOnFKEajdOsNXf9yymoHKp4b/view?usp=sharing).
```
volumes % ls
2009-M57-day11-18.pcap
```
Enter the pcap folder in the container, you will see 2009-M57-day11-18.pcap as well and analyze it by Zeek.
```
root@ccaf8d74f88c:/# cd pcap
root@ccaf8d74f88c:/pcap# ls
2009-M57-day11-18.pcap
root@ccaf8d74f88c:/pcap# zeek -r 2009-M57-day11-18.pcap
root@ccaf8d74f88c:/pcap# ls
2009-M57-day11-18.pcap	dhcp.log  files.log  http.log  ntp.log	 packet_filter.log  smtp.log  weird.log
conn.log		dns.log   ftp.log    ntlm.log  ocsp.log  pe.log		    ssl.log   x509.log
```

### 4. Analyze log files by my Python script
#### Clone my project
```
% git clone https://github.com/cindy42833/Zeek_analyzer.git
```
#### Put log files into the same working directory as the **parseZeek.py**
```
% cd Zeek_analyzer

# File tree
.
├── conn.log
├── dhcp.log
├── dns.log
├── http.log
└── parseZeek.py
```

#### Run parseZeek.py
```
Zeek_analyzer % python3 ./parseZeek.py 
```
My program can give ansers for the following questions.

* What is the top 10 most active originator host?
* What is the top 10 most visited host in HTTP?
* What is the top 10 most queried name in DNS?
* What is the top 10 most pair of hosts in conn.log?
* What is the top 10 most popular user agent in HTTP?
