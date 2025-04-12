# 🔥 Project Overview: “Passive Reconnaissance Tool”
This beginner-level command-line tool for passive reconnaissance allows users to input information such as full names, IP addresses, and usernames.

## 🧭 STEP 0 — Set up VMware Bridged Network
### 🎯 Goal: Make sure your VM can access the internet
✅ Concept: Bridged Mode in VMware
It connects your VM directly to your physical network like a real PC. You get an IP from the router (not NATed).
- we will use
```bash
cat /etc/os-release
PRETTY_NAME="Parrot Security 6.2 (lorikeet)"
NAME="Parrot Security"
VERSION_ID="6.2"
VERSION="6.2 (lorikeet)"
VERSION_CODENAME=lory
ID=debian
HOME_URL="https://www.parrotsec.org/"
SUPPORT_URL="https://www.parrotsec.org/community/"
BUG_REPORT_URL="https://gitlab.com/parrotsec/"
```
- test internet:
```bash
ip a | grep inet
ping -c 3 google.com
```
✅ Reply = Success. If not, fix before proceeding.
## 🧪 STEP 1 — Install & test Python 3
### 🎯 Goal: Make sure you can run Python scripts
✅ Concept: Python is a programming language we’ll use to build your tool.
```bash
python3 --version
```
✅ Reply = Python 3.x.x. If not, install before proceeding.
```bash
sudo apt update && sudo apt install python3
sudo apt install python3-pip
```
🧪 Test:
```bash
python3 -c 'print("Hello, Passive Recon/!")'
```

## 🧪 STEP 2 — Install & Configure Git
### 🎯 Goal: Prepare Git to sync with your GitHub repo
✅ Concept: Git tracks your code, GitHub stores it in the cloud
```bash
git -v
```
✅ Reply = git version 2.x.x. If not, install before proceeding.
```bash
sudo apt install git
git config --global user.name "Name Surname"
git config --global user.email "your-email@example.com"
```
🧪 Test:
```bash
git config --list
git config --global --list
```

## 🧪 STEP 3 — Create and clone your GitHub repo
### 🎯 Goal: Work locally on a project folder synced with GitHub
✅ Concept: Your code lives in a local Git repo, which syncs with the GitHub cloud.

## 🛠️ STEP 4 — Create passive.py Script
🎯 Goal: Setup basic script structure for handling CLI arguments
✅ Concept: Python script to process -fn, -ip, -u options, fetch data, and save results.
- Create passive.py
- Make passive.py executable

## 🛠️ STEP 5 — Real IP Info Lookup with API
### 🎯 Goal: Use a public IP geolocation API to fetch real data
✅ Concept: Query a free API (e.g., ip-api.com) to retrieve city and ISP from an IP address.
- Implement functions to search for full_name, ip_address, and username.
- Add logic to fetch data (mock for now).
- Save results in result.txt or result2.txt based on the option chosen.

## 🛠️ STEP 6 — Implement Search Functions in passive.py
### 🎯 Goal: Add functionality to search based on -fn, -ip, or -u options
✅ Concept: Fetch data (mock for now) based on input type and save results.
- Modify passive.py to use the real API in search_ip
🧪 Test:
```bash
./passive.py -ip 8.8.8.8
```
## 🛠️ STEP 6 — Check if a Username Exists on Multiple Social Networks
### 🎯 Goal:
Implement real checks to verify if a given username is in use on at least 5 platforms (Facebook, Twitter, GitHub, Instagram, Reddit, TikTok)
✅ Concept:
HTTP GET requests to known user profile URLs and analyze the response status code:
```
200 OK → user exists ✅

404 Not Found → user doesn’t exist ❌
```
- ⚠️ This is passive OSINT. We’re just visiting public URLs. No login or scraping.
- 📄 Modify passive.py - search_username

## 🛠️ STEP 7 — Full Name Search Using Real OSINT Techniques
### 🎯 Goal: Search public directories or platforms (Google, DuckDuckGo, Pipl, LinkedIn, Whitepages). Report possible addresses, phone numbers, emails, or profiles.
✅ Concept:
Unlike IPs/usernames, full names are less deterministic. So instead of fixed URLs, we perform targeted search queries on public engines like:
🔧 Plan
1. Build a search query: "{first} {last}" site:linkedin.com or site:thatsthem.com
2. Fetch results using the duckduckgo_search Python module.
3. Store the top 3–5 links.
