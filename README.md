# RTI Docker Debugger

[![Build Status](https://travis-ci.org/rticommunity/rticonnextdds-docker-debugger.svg?branch=master)](https://travis-ci.org/rticommunity/rticonnextdds-docker-debugger)

This Docker image helps you to create a Docker container with some interesting
tools to debug your system.

### License
All programs and components within this image are the property of their
respective owners under the license associated with such component in the
installation. Please refer to the documentation associated with each program
or component and/or the [Licenses.md](Licenses.md) file.

## Included tools

### ddsping

This small tool was inspired by RTI DDS Ping (shipped with RTI Connext DDS).
It has been developed using [RTI Connector for Connext DDS](https://github.com/rticommunity/rticonnextdds-connector). ``ddsping``
allows you to know if the DDS traffic works properly on your
system. You can execute it directly typing ``ddsping``.

```shell
optional arguments:
  -h, --help            show this help message and exit
  -w, --writer          send ping messages
  -r, --reader          read ping messages
  -p PEER, --peer PEER  add a discovery peer.
                        Default list: "239.255.0.1,127.0.0.1"
```

### RTI Log Parser

[RTI Log Parser](https://github.com/rticommunity/rticonnextdds-logparser)
is also incorporated to make easier to debug your RTI Connext DDS and RTI
Micro applications. You can call this tool directly from any directory
running ``rtilogparser [options]``. All the documentation about this tool is
available in the
[oficial repository of RTI Log Parser](https://github.com/rticommunity/rticonnextdds-logparser).

### Other applications included in this Docker image

Also, this Docker image includes some useful Linux packages.
These packages are not in the base image of Ubuntu. Now, they are included on
this Docker image to help you to debug issues in your system.

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

The idea of this Docker image is to provide you with a mechanism to debug
issues that can made your system miscommunicate (mainly network issues).

### Build the image
First, you need to clone this repository and build the image.
When you finish to download the repository, you can go to it and run:

```bash
$ docker build -t rtidebugger .
```

### Run the image

You can run a ``bash`` process on your Docker container and interact with it.
You can do it with the following command:

```bash
$ docker run --network=host --name debugger -ti rtidebugger:latest /bin/bash
```

Also, you can run the different installed packages directly from the run command:

```bash
$ docker run --network=bridge --name debugger -ti rtidebugger:latest ping rti.com
```