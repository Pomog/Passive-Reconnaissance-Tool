#!/usr/bin/env python3
import re
import argparse
import requests

API_KEY = "YOUR_HUNTER_API_KEY"

def main():
    parser = argparse.ArgumentParser(description="Passive Reconnaissance Tool")
    parser.add_argument("-fn", metavar='"Full Name"', help="Search with full-name")
    parser.add_argument("-ip", metavar='"IP Address"', help="Search with IP address")
    parser.add_argument("-u", metavar='"Username"', help="Search with username")
    args = parser.parse_args()

    if args.fn:
        search_full_name(args.fn)
    elif args.ip:
        search_ip(args.ip)
    elif args.u:
        search_username(args.u)
    else:
        parser.print_help()

import re
import requests

def _extract(pattern: str, text: str, default: str = "N/A") -> str:
    """Helper that mimics the Go `extract` function."""
    m = re.search(pattern, text, re.S | re.I)
    return m.group(1).strip() if m else default


def search_full_name(full_name: str) -> None:
    """
    Look up a person by full name on whitepages.be and save the result.

    It mirrors the behaviour of the Go `findByName` example:
      • splits the name into first / last
      • issues a GET request with a desktop User‑Agent
      • scrapes address and phone with regexes
      • writes everything to `result.txt`
    """
    # ---- 1. Basic sanity check ------------------------------------------------
    names = full_name.strip().split()
    if len(names) < 2:
        print("Error: you must supply both first and last name.")
        return

    first_name, last_name = names[0], names[1]

    # ---- 2. Build the URL exactly like the Go code ----------------------------
    url = (
        "https://www.whitepages.be/Search/Person/"
        f"?what={first_name}+{last_name}&where="
    )

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"[!] Error fetching data: {e}")
        return

    content = resp.text

    # ---- 3. Scrape the interesting bits --------------------------------------
    address = _extract(r'<span class="wg-address">\s*([^<]+)</span>', content)
    phone   = _extract(r'"phone"\s*:\s*"(\+\d+)"', content)

    result = {
        "First name": first_name,
        "Last name": last_name,
        "Address": address,
        "Phone": phone,
    }

    # ---- 4. Persist & report --------------------------------------------------
    save_result(result, "result.txt")
    print("→ Saved in result.txt")



def search_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['status'] == 'success':
            result = {
                "ISP": data.get("isp", "Unknown"),
                "City": data.get("city", "Unknown"),
                "Latitude": str(data.get("lat", "N/A")),
                "Longitude": str(data.get("lon", "N/A")),
                "Country": data.get("country", "Unknown")
            }
            save_result(result, "result2.txt")
            print("Saved in result2.txt")
        else:
            print("Invalid IP or not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def search_username(username):
    # Remove leading "@" if present
    username = username.lstrip("@")

    platforms = {
        "Facebook": f"https://www.facebook.com/{username}",
        "Twitter": f"https://www.twitter.com/{username}",
        "GitHub": f"https://www.github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Instagram": f"https://www.instagram.com/{username}",
    }

    result = {}
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for name, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            result[name] = "yes" if response.status_code == 200 else "no"
        except Exception as e:
            result[name] = "error"

    save_result(result, "result3.txt")
    print("Saved in result3.txt")


def save_result(result, filename):
    with open(filename, "w") as file:
        for key, value in result.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()
