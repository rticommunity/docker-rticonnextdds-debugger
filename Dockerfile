##############################################################################
# Copyright (c) 2005-2014 Real-Time Innovations, Inc.
# All rights reserved. RTI grants Licensee a license to use, modify,
# compile, and create derivative works of the Software.  Licensee has the right
# to distribute object form only for use with RTI products. The Software
# is provided "as is", with no warranty of any type, including any warranty for
# fitness for any purpose. RTI is under no obligation to maintain or
# support the Software.  RTI shall not be liable for any incidental
# or consequential damages arising out of the use or inability to
# use the software.
##############################################################################
FROM debian:buster-slim as builder
LABEL "com.example.vendor"="Real-Time Innovations" \
    version="1.1" \
    maintainer="israel@rti.com" \
    description="This image helps you to debug your network issues with \
    RTI Connext DDS and RTI Micro."

# Install some packages:
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    zip

# Install RTI Logparser
RUN git clone https://github.com/rticommunity/rticonnextdds-logparser.git
WORKDIR /rticonnextdds-logparser
RUN ./create_redist.sh


FROM debian:buster-slim
COPY --from=builder /rticonnextdds-logparser/rtilogparser /bin

# Install some packages:
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    iperf \
    iproute2 \
    iputils-* \
    nmap \
    net-tools \
    netcat \
    python \
    python-pip \
    tcpdump \
    tcpflow \
    traceroute \
    vim \
    wget \
    python-setuptools && \
    pip install rticonnextdds_connector && rm -rf \
    /usr/local/lib/python2.7/dist-packages/lib/armv6vfphLinux3.xgcc4.7.2 \
    /usr/local/lib/python2.7/dist-packages/lib/armv7aAndroid2.3gcc4.8 \
    /usr/local/lib/python2.7/dist-packages/lib/armv7aQNX6.5.0SP1qcc_cpp4.4.2 \
    /usr/local/lib/python2.7/dist-packages/lib/i86Linux3.xgcc4.6.3 \
    /usr/local/lib/python2.7/dist-packages/lib/i86Win32VS2010 \
    /usr/local/lib/python2.7/dist-packages/lib/x64Darwin16clang8.0 \
    /usr/local/lib/python2.7/dist-packages/lib/x64Win64VS2013 && \
    apt-get remove python-setuptools -y && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Add the ddsping application to the container
COPY ddsping.py /bin/ddsping
COPY PingConfiguration.xml /bin
