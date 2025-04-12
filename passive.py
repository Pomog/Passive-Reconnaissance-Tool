#!/usr/bin/env python3
import argparse

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
    # Mock data for demonstration
    mock_data = {
        "Jean Dupont": {
            "First name": "Jean",
            "Last name": "Dupont",
            "Address": "7 rue du Progrès\n75016 Paris",
            "Number": "+33601010101"
        }
    }

    if full_name in mock_data:
        result = mock_data[full_name]
        save_result(result, "result.txt")
        print(f"Saved in result.txt")
    else:
        print(f"No information found for {full_name}")

def search_ip(ip_address):
    # Mock data for demonstration
    mock_data = {
        "127.0.0.1": {
            "ISP": "FSociety, S.A.",
            "City Lat/Lon": "(13.731) / (-1.1373)"
        }
    }

    if ip_address in mock_data:
        result = mock_data[ip_address]
        save_result(result, "result2.txt")
        print(f"Saved in result2.txt")
    else:
        print(f"No information found for {ip_address}")

def search_username(username):
    # Mock data for demonstration
    mock_data = {
        "@user01": {
            "Facebook": "yes",
            "Twitter": "yes",
            "Linkedin": "yes",
            "Instagram": "no",
            "Skype": "yes"
        }
    }

    if username in mock_data:
        result = mock_data[username]
        save_result(result, "result3.txt")
        print(f"Saved in result3.txt")
    else:
        print(f"No information found for {username}")

def save_result(result, filename):
    with open(filename, "w") as file:
        for key, value in result.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()