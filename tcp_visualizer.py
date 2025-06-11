import pandas as pd
import matplotlib.pyplot as plt
import re

# Function to extract throughput (in Mbps) and retransmits
def parse_iperf_log(filename):
    with open(filename, 'r') as file:
        data = file.read()

    # Defaults
    throughput_mbps = 0.0
    retransmits = 0

    # Regex: look for the FINAL summary line with either Mbits/sec or Gbits/sec
    # e.g. "... 11.8 Gbits/sec    0 sender"  OR "... 1.50 Mbits/sec   61 sender"
    summary_re = re.compile(
        r'\[\s*\d+\]\s+'               # [ ID]
        r'\d+\.\d+-\d+\.\d+\s+sec\s+'  # 0.00-20.00 sec
        r'[\d\.]+\s+\w+Bytes\s+'       # 11.8 GBytes
        r'([\d\.]+)\s+([MG])bits/sec\s+'  # capture value & unit
        r'(\d+)\s+sender'              # retransmits
    )

    m = summary_re.search(data)
    if m:
        val, unit, rtx = m.groups()
        val = float(val)
        # convert G → Mbps
        if unit == 'G':
            val *= 1000
        throughput_mbps = val
        retransmits = int(rtx)
    else:
        print(f"[WARN] Could not extract throughput/retransmits from {filename}")

    return throughput_mbps, retransmits

# Collect data
algorithms = ['reno', 'cubic', 'bbr']
results = []

for algo in algorithms:
    thr, rtx = parse_iperf_log(f'test_{algo}.txt')
    results.append({
        'Algorithm': algo.upper(),
        'Throughput (Mbps)': thr,
        'Retransmits': rtx
    })

df = pd.DataFrame(results)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Throughput
df.plot.bar(
    x='Algorithm',
    y='Throughput (Mbps)',
    ax=axes[0]
)
axes[0].set_title('Throughput Comparison (Mbps)')

# Retransmits
df.plot.bar(
    x='Algorithm',
    y='Retransmits',
    ax=axes[1]
)
axes[1].set_title('Retransmissions Comparison')

plt.tight_layout()
plt.show()
