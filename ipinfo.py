import requests
import argparse

def get_ip_info(ip=""):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        return {
            "IP": data.get("ip", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location": data.get("loc", "N/A"),
            "ISP": data.get("org", "N/A"),
            "Timezone": data.get("timezone", "N/A")
        }
    except requests.RequestException as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get information about an IP address.")
    parser.add_argument("ip", nargs="?", default="", help="IP address to look up (leave blank for your own IP)")
    args = parser.parse_args()
    
    info = get_ip_info(args.ip)
    for key, value in info.items():
        print(f"{key}: {value}")
