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

