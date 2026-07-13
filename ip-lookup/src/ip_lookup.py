import ipaddress
import requests


def fetch_ip_data(ip):

    API_KEY = "YOUR_API_KEY"
    response = requests.get('https://api.abuseipdb.com/api/v2/check',
                            headers={
                                'Accept': 'application/json',
                                'Key': API_KEY
                            },
                            params={
                                'ipAddress': ip
                            },
                            timeout=5
                            )
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return 0


def ip_check(counter):
    if counter == 1:
        ip = input("Enter an IP address: ")
    else:
        ip = input("Re-enter a valid IP address: ")
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        return 0


def display_data(data):
    report = data["data"]

    print("== == == == == == == == == == == == == == == == == ==")
    print("\t\tIP Reputation Report")
    print("== == == == == == == == == == == == == == == == == ==")

    print("Ip Address:", report["ipAddress"])
    print("Country:", report["countryCode"])
    print("ISP:", report["isp"])
    print("Usage Type:", report["usageType"])
    print("Abuse Score:", report["abuseConfidenceScore"])
    print("Total Reports:", report["totalReports"])
    print("TOR Exit Node:", report["isTor"])
    print("Whitelisted:", report["isWhitelisted"])
    print("Last Reported:", report["lastReportedAt"])


def main():
    ip = 0
    counter = 1
    while ip == 0:
        ip = ip_check(counter)
        counter = 0
    data = fetch_ip_data(ip)
    if data != 0:
        display_data(data)


if __name__ == "__main__":
    main()
