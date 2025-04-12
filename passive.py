#!/usr/bin/env python3
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

def search_full_name(full_name):
    first_name, last_name = full_name.strip().split(" ", 1)

    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")

    query_variants = [
        f'"{full_name}" site:linkedin.com',
        f'"{full_name}" site:thatsthem.com',
        f'"{full_name}" site:peekyou.com',
        f'"{full_name}" site:facebook.com',
        f'"{full_name}" site:findpeoplefast.net'
    ]

    results = {}

    for query in query_variants:
        print(f"Searching: {query}")
        search_results = ddg(query, max_results=2)
        print(search_results)
        for result in search_results:
            title = result.get("title", "No title")
            link = result.get("href", "No link")
            results[title] = link

    if results:
        save_result(results, "result.txt")
        print("Saved in result.txt")
    else:
        print("No data found.")


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