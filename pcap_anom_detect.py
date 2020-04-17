#!/usr/bin/env python3

import argparse

from scapy.all import rdpcap


def main():
    parser = argparse.ArgumentParser("Detect anomalies in packet captures, potentially rooting out covert channels")
    parser.add_argument(
        "pcap",
        type=argparse.FileType('rb'),
        help="The packet capture file to be analyzed in pcap or pcapng format"
    )
    parser.add_argument(
        "-a",
        "--analyzers",
        help="Specifies one or more comma-separated identifiers to search for"
    )
    args = parser.parse_args()

    pcap = rdpcap(args.pcap)
    print(f"{len(pcap)} frames")  # Placeholder


if __name__ == "__main__":
    main()
