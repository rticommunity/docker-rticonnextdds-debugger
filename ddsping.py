#!/usr/bin/python
##############################################################################
# Copyright (c) 2005-2017 Real-Time Innovations, Inc.
# All rights reserved. RTI grants Licensee a license to use, modify, compile,
# and create derivative works of the software for their internal use. The software
# is provided "as is", with no warranty of any type, including any warranty for
# fitness for any purpose. RTI is under no obligation to maintain or
# support the software.  RTI shall not be liable for any incidental
# or consequential damages arising out of the use or inability to
# use the software.
##############################################################################
"""Application to check if there are issues with the DDS traffic."""

from __future__ import print_function
from time import sleep
from argparse import ArgumentParser
from signal import signal, SIGINT
from sys import exit as sysExit
from os import environ
import rticonnextdds_connector as rti

options = {}


def read_arguments():
    """Parse the command-line arguments."""
    parser = ArgumentParser(description="Check if DDS traffic works")

    parser.add_argument("-w", "--writer", action='store_true',
                        help="send ping messages")
    parser.add_argument("-r", "--reader", action='store_true',
                        help="read ping messages")
    parser.add_argument("-p", "--peer", action='append',
                        help="add a discovery peer. " +
                        "Default list: \"239.255.0.1, 127.0.0.1\"")
    return parser


def writer():
    """A writer is going to start sending samples."""
    print("Running writer...")

    connector = rti.Connector("MyParticipantLibrary::Zero",
                              "/usr/local/bin/PingConfiguration.xml")

    outputDDS = connector.getOutput("MyPublisher::PingWriter")

    i = 0

    while True:
        print("Sending ping message number " + str(i))
        outputDDS.instance.setNumber("number", i)
        i += 1
        outputDDS.write()
        sleep(1)


def reader():
    """A reader is going to start receiving samples."""
    print("Running reader...")

    connector = rti.Connector("MyParticipantLibrary::Zero",
                              "/bin/PingConfiguration.xml")
    inputDDS = connector.getInput("MySubscriber::PingReader")

    timeout = 2000  # 2 seconds
    while True:
        ret = connector.wait(timeout)
        if ret == 0:
            inputDDS.take()
            numOfSamples = inputDDS.samples.getLength()
            for j in range(1, numOfSamples+1):
                if inputDDS.infos.isValid(j):
                    pingID = int(inputDDS.samples.getNumber(j, "number"))
                    # Print the sample
                    print("Received ping message number " + str(pingID))
        else:
            print("No ping was received")


def stop(s, frame):
    """Handler for the Ctrl + C signal."""
    print("Stopping...")
    sysExit(0)


def main():
    """Main application entry."""
    args = read_arguments()
    parsedArgs = args.parse_args()
    signal(SIGINT, stop)

    if parsedArgs.peer:
        options["peers"] = ",".join(parsedArgs.peer)
        environ["NDDS_DISCOVERY_PEERS"] = options["peers"]
    else:
        options["peers"] = "239.255.0.1,127.0.0.1"

    if parsedArgs.writer:
        writer()
    elif parsedArgs.reader:
        reader()
    else:
        args.print_help()


if __name__ == "__main__":
    main()
