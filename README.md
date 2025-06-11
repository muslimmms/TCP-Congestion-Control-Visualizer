# TCP Congestion Control Visualizer

This project compares and visualizes the behavior of three TCP congestion control algorithms — **Reno**, **Cubic**, and **BBR** — under simulated adverse network conditions. It uses real transfer data from `iperf3` and visualizes throughput and retransmissions using Python.

---

## Features

- Runs TCP performance tests using `iperf3`
- Simulates latency, packet loss, and bandwidth constraints using `tc netem`
- Parses `iperf3` logs and extracts:
  - Total throughput (Mbps)
  - Number of retransmissions
- Visualizes comparisons with bar charts using `matplotlib`

---

## Technologies Used

- **Linux (Ubuntu)**
- **Python**: `pandas`, `matplotlib`
- **iperf3**: For bandwidth testing
- **tc (netem)**: To simulate real-world network impairments
- **VMWare Workstation Pro**: For creating isolated test VMs

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/muslimmms/TCP-Congestion-Control-Visualizer.git
cd TCP-Congestion-Control-Visualizer
