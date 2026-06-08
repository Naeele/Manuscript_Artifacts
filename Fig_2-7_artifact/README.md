# Reproducing Figure 2.7

This repository contains the scripts, binaries, and data required to reproduce **Figure 2.7** of the manuscript.

The figure illustrates a FLUSH+RELOAD attack performed against the modular exponentiation implementation used for RSA decryption in **GnuPG 1.4.13**, using the **Mastik** side-channel analysis framework.

## Experimental Setup

The experiment was conducted on:

* **Laptop:** DELL Latitude 5320
* **Processor:** Intel Core i7-1185G7

### Software

* [Mastik](https://cs.adelaide.edu.au/~yval/Mastik/)
* GnuPG 1.4.13
* FLUSH+RELOAD trace collection tool (`FR-trace`)
* Python visualization script (`visualization.py`)

## Repository Structure

```text
.
├── APO.txt                # Test plaintext
├── APO.txt.gpg            # Encrypted file used as victim input
├── FR-trace               # FLUSH+RELOAD tracing tool
├── gpg-1.4.13             # GnuPG 1.4.13 binary
├── Mastik-main/           # Mastik framework
├── result.csv             # Generated trace
└── visualization.py       # Trace visualization script
```

## Trace Collection

The trace, stored in `result.csv`, was collected by monitoring the square-and-multiply implementation used during RSA decryption.

The monitored locations correspond to arithmetic routines involved in the modular exponentiation process. Their execution pattern reveals the sequence of squaring and multiplication operations, which can be used to infer information about the secret exponent.

First, start the FLUSH+RELOAD attack using the following parameters, which were determined empirically:

```bash
./FR-trace \
    -a 0 \
    -s 1500 \
    -c 200000 \
    -i 100000 \
    -p 1 \
    -f gpg-1.4.13 \
    -m mpih-mul.c:101 \
    -m mpih-mul.c:253 \
    -t mpih-mul3.c:52 \
    -t mpih-div.c:330 \
    > result.csv
```

Then, in a second terminal, trigger the victim execution:

```bash
sleep 2 && taskset --cpu-list 4 ./gpg-1.4.13 -r 116EC79E -d APO.txt.gpg
```

Once the decryption completes, the collected trace will be available in `result.csv`.

## Figure Generation

After collecting the trace, the figure can be generated using:

```bash
python3 visualization.py result.csv
```

## Notes

The **Figure 2.7** presents a zoomed view of the FLUSH+RELOAD trace in the interval `[2000, 14000]`. The corresponding exponent bits are highlighted in green.

The attack was performed using Mastik on a DELL Latitude 5320 equipped with an Intel Core i7-1185G7 processor. Due to the hardware-dependent nature of cache attacks, reproducing identical results on a different platform may be difficult. Similarly, a heavily loaded system may introduce noise that affects the quality of the collected traces.

Consequently, the exact appearance of the trace may vary across systems, although the overall leakage pattern should remain observable on compatible hardware.
