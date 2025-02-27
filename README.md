
# CPU Stress Test with Python Multiprocessing

## Overview
This Python script utilizes **multiprocessing** to simulate high CPU load on a system by spawning multiple processes, each performing intensive mathematical computations. It is particularly useful for testing **autoscaling** in cloud environments like **Google Cloud Platform (GCP)**.

## Features
- Utilizes **all available CPU cores** for stress testing.
- Continuously runs computationally heavy tasks.
- Helps test **autoscaling configurations** (e.g., in GCP Instance Groups).
- Gracefully terminates processes upon receiving a **keyboard interrupt (Ctrl + C)**.

## How It Works
1. The script detects the **number of CPU cores** available.
2. It spawns **one process per core**, each running an infinite loop of **intensive calculations**.
3. The script keeps running, continuously consuming CPU resources.
4. When manually stopped (Ctrl + C), all spawned processes are **terminated**.

## System Requirements
- **Python 3.6+**
- **Linux/macOS/Windows**
- **Multiprocessing support** (most modern CPUs)

## Deployment Guide

### 1. Clone the Repository
```bash
git clone https://github.com/arsalanrex/Autoscaling_GCP.git
cd Autoscaling_GCP
```

### 2. Install Python (if not installed)
Ensure **Python 3.6 or later** is installed:
```bash
python3 --version
```

### 3. Run the Stress Test
Execute the script using:
```bash
python3 cpu_test.py
```

### 4. Monitor CPU Usage
While the script is running, check CPU utilization using:
- **Linux/macOS:**
  ```bash
  top
  htop  # (if installed)
  ```
- **Windows (PowerShell):**
  ```powershell
  Get-Counter '\Processor(_Total)\% Processor Time'
  ```

### 5. Stopping the Stress Test
To **stop the test**, press:
```bash
Ctrl + C
Ctrl + Z
```
The script will terminate all running processes cleanly.

## Expected Outcome
| Scenario | Expected Result |
|----------|----------------|
| Script starts | All CPU cores reach high utilization (80-100%) |
| Autoscaling (Cloud) | If using GCP Instance Groups, new VMs should be created as CPU crosses threshold |
| Script stopped | CPU usage returns to normal |
| Manual VM scaling | Reducing instances should lower CPU load |

## Troubleshooting

### 1. **High CPU Usage Persists After Stopping**
- Check if zombie processes remain:
  ```bash
  ps aux | grep python
  ```
- Manually kill processes:
  ```bash
  pkill -f stress_test.py
  ```

### 2. **Script Doesn't Utilize All Cores**
- Check CPU core count:
  ```bash
  python3 -c "import multiprocessing; print(multiprocessing.cpu_count())"
  ```
- Run with explicit core count:
  ```bash
  python3 stress_test.py --cores=4
  ```

### 3. **Autoscaling Not Triggering in GCP**
- Verify Autoscaler policy:
  ```bash
  gcloud compute instance-groups managed describe my-mig
  ```
- Ensure CPU metric is enabled in **Cloud Monitoring**.
