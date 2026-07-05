import ipaddress


def read_file():
    l = []
    with open("src/sample.log") as file:
        for line in file:
            l.append(line)
    return l


def SuccessfulLogins(f: list):
    accept = sum(1 for i in f if "Accepted" in i)
    return accept


def FailedLogins(f: list):
    reject = sum(1 for i in f if "Failed" in i)
    return reject


def unique_ip(f: list):

    IP_list = []
    ip = []
    for line in f:
        s = str(line).split(" ")
        ip.append(s[len(s)-4])
    unique_list = list(set(ip))
    for line in unique_list:
        try:
            ipaddress.ip_address(line)
            IP_list.append(line)
        except ValueError:
            False
    return IP_list


def TopFailedIPs(f: list, ip: list):
    print("Top Failed IPs:")
    s = ""
    bf = []
    for line in f:
        if "Failed" in line:
            s += str(line)
    for i in ip:
        if i in s:
            print(i, ":", s.count(i))
            if s.count(i) > 3:
                bf.append(i)
    BruteForce(bf)


def BruteForce(s: list):
    print("")
    print("Possible Brute Force Attempts ( > 3 failures)")
    print("------------------------------------------")
    for i in s:
        print(i)


def UsersLoggedIn(f: list):
    print("Users Logged in:")
    print("-------------------")
    for i in f:
        if "Accepted" in i:
            s = i.split(" ")
            x = s.index("for")
            print(s[x+1])


def main():
    print("============ Log Summary ============")

    print("")
    files = read_file()
    print("Total log entries:", len(files))

    print("")
    success = SuccessfulLogins(files)
    failed = FailedLogins(files)
    print("Successful logins:", success)

    print("")
    print("Failed logins:", failed)

    print("")
    iplist = unique_ip(files)
    print("Unique IPs:", len(iplist))

    print("")
    TopFailedIPs(files, iplist)

    print("")
    UsersLoggedIn(files)


if __name__ == "__main__":
    main()
