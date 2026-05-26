import json
import time
import requests


def load_sites(file_path="sites.json"):
    """Loads the list of websites from Json config file"""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found..")
        return []

def check_site(site):
    """Pings a single website , measure latency, and checks HTTPS status"""
    name = site["name"]
    url = site["url"]

    print(f"Checking {name} ({url})...")
    start_time = time.time()

    try:
        response = requests.get(url,timeout=5)
        latency = round((time.time() - start_time) * 1000)

        if response.status_code == 200:
            print(f"SUCCESS: {name} is UP. Status : {response.status_code} | Latency : {latency} ms")
            return {"name": name, "url": url, "status": "UP", "code": response.status_code, "Latency": latency}
        else:
            print(f" WARNING: {name} returned Status: {response.status_code}")
            return {"name": name, "url": url, "status": "DOWN", "code": response.status_code, "latency": latency}
    except requests.exceptions.RequestException:
        print(f" Alert: {name} is DOWN. ERROR : could not find the host ")
        return {"name": name, "url": url, "status": "down", "code": "ERROR", "latency": None}


def main():
    sites = load_sites()
    if not sites:
        return
    print("--- Starting Uptime Check ---")
    for site in sites:
        check_site(site)
        print("-" * 30)


if __name__=="__main__":
    try :
        main()
    except KeyboardInterrupt:
        print ("\n monitor stopped by user . Exiting ")
