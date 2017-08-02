# RTI Docker Debugger

This Docker image helps you to create a Docker container with some interesting tools to debug your system.

### License
All programs and components within this image are the property of their respective owners under the license associated with such component in the installation.  Please refer to the documentation associated with each program or component and/or the Licenses.md file included in the Docker image.

## Included tools

### ddsping

This Docker image includes a small tool call "ddsping", inspired by RTI DDS Ping (shipped with RTI Connext DDS). It has been developed with [RTI Connector for Connext DDS](https://github.com/rticommunity/rticonnextdds-connector). This small tool allows you to know if the DDS traffic works properly in your system. You can call it directly typing `ddsping`.

```bash
optional arguments:
  -h, --help            show this help message and exit
  -w, --writer          send ping messages
  -r, --reader          read ping messages
  -p PEER, --peer PEER  add a discovery peer.
                        Default list: "239.255.0.1,127.0.0.1"
```

### RTI Log Parser

[RTI Log Parser](https://github.com/rticommunity/rticonnextdds-logparser) is also incorporated to make easier the debugging of your RTI Connext DDS and RTI Micro applications. You can call this tool directly from any directory running `rtilogparser [options]`. All the documentation about this tool is available at the [oficial repository of RTI Log Parser](https://github.com/rticommunity/rticonnextdds-logparser).

### Other applications included in this Docker image

Also, this Docker image includes some useful Linux packages. These packages can are not in the base image of Ubuntu and we think the y can help you to detect issues in your system.

These packages are:

- curl
- dig
- nslookup
- nsupdate
- iperf
- ifconfig
- route
- iptunnel
- nameif
- ipmaddr
- netstat
- arping
- clockdiff
- ping
- tracepath
- nmap
- netstat
- rarp
- nc
- python
- pip
- tcpdump
- tcpflow
- traceroute
- vim
- wget

## How to use this Docker image

The idea of this Docker image is to provide you with a mechanism to debug issues that can made your system miscommunicate (mainly network issues). So, the proper way to use this Docker image is to create a Docker container and open a terminal on it. For example, you can use the following command:

    $ docker run --network=<Your network> -v <Path to your Connext DDS application>:/<Mountpoint>  --name debugger -ti rti-docker-debugger:latest /bin/bash
