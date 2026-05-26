import shutil
import datetime
import sys

# configuration
DISK_PATH ='c:\\'
DISK_THRESHOLD_PERCENT= 15 # alert if the free space drop below this percentage
LOG_FILE="disk_alerts.log"

# terminal color
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_BOLD = "\033[1m"
COLOR_RESET = "\033[0m"

def check_disk_space():
    # Fetch total, used, and free space in bytes
    total,used,free=shutil.disk_usage(DISK_PATH)

    # Calculate the percentage of free space left
    free_percent = (free/total)*100
    # Convert bytes to Gigabytes (GB) for human-readable logs
    bytes_in_gb = 1024 ** 3
    free_gb = free / bytes_in_gb
    total_gb = total / bytes_in_gb

    timestamp = datetime.datetime.now().strftime("%y-%m%d %S:%M:%S")
    print(f"{COLOR_BOLD}--- System storage check [{timestamp}] ---{COLOR_RESET}")
    print(f" Total Capacity : {total_gb:.2f} GB")
    print(f"Available Space : {free_gb:.2f} GB ({free_percent:.2f}% free )")

