# pcap-anom-detect

Detect anomalies in packet captures, potentially rooting out covert channels

## Usage

### Arguments

#### Arguments Overview

`[-a|--analyzers <identifier,...>] <pcap>`

#### Argument Specifics

- `<pcap>`
  - Mandatory
  - The packet capture file to be analyzed in pcap or pcapng format
- `[-a|--analyzers <identifier,...>]`
  - Optional
  - Specifies one or more comma-separated identifiers to search for
  - Reference [Attempts to Detect](#attempts-to-detect) for identifiers that may be used
  - If this option is not provided, all available identifiers are used

### Usage with Docker

(Preferred)

**Pre-requisite:** [Docker](https://docs.docker.com/get-docker/) must be installed

``` sh
git clone https://github.com/cetaSYN/pcap-anom-detect.git
docker build -t pcap-anom-detect .
docker run --rm pcap-anom-detect <args>
```

Replace `<args>` with the desired arguments and options from [Arguments](#arguments)

### Standalone Usage

``` sh
git clone https://github.com/cetaSYN/pcap-anom-detect.git
pip install -r requirements.txt
./pcap_anom_detect.py <args>
```

Replace `<args>` with the desired arguments and options from [Arguments](#arguments)

## What It Does

pcap-anom-detect detects anomalies in packet captures with the intent of rooting out covert channels.
This is not a utility for detecting low-and-slow malware callbacks or malware C2, but rather, active communication leveraging novel mechanisms

### Attempts to Detect

The categories provide the most common vectors by which covert channel communication may take place.
If a category has been assigned an analyzer identifier (e.g. `frame-timing-entropy`), that category has an applicable analyzer built into pcap-anom-detect.
If no identifier is present, the category is not checked in the current implementation.

Categorization based upon [Wendzel, Steffen, et al.](#references).
![Categorization Heriarchy](https://github.com/cetaSYN/pcap-anom-detect/blob/master/docs/images/heirarchy.png)

#### Size Modulation Pattern

No analyzers presently

#### Sequence Pattern

No analyzers presently

##### Position Pattern

No analyzers presently

##### Number of Elements Pattern

No analyzers presently

#### Add Redundancy Pattern

No analyzers presently

#### PDU Corruption/Loss Pattern

No analyzers presently

#### Random Value Pattern

No analyzers presently

#### Value Modulation Pattern

No analyzers presently

##### Case Pattern

No analyzers presently

##### Least Significant Bit Pattern

No analyzers presently

#### Reserved/Unused Pattern

No analyzers presently

#### Inter-arrival Time Pattern

Analyzers:

- `frame-timing-entropy` (WIP)
  - Analyzes the timing entropy between LAN frames, classifying ~0.35-0.5 as potential English text

#### Rate Pattern

No analyzers presently

#### PDU Order Pattern

No analyzers presently

#### Re-transmission Pattern

No analyzers presently

## References

1. Wendzel, Steffen, et al. “A Pattern-based Survey and Categorization of Network Covert Channel Techniques.” ACM Computing Surveys, no. 1, 2014.
    - <https://arxiv.org/pdf/1406.2901.pdf>
    - This project made heavy reference to the 11 techniques outlines by this publication
