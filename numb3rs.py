import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pat = (r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b")
    ipLen = len(ip)
    difference = len(ip.replace(".",""))-ipLen
    if re.compile(pat,re.IGNORECASE).search(ip) and difference == -3:
        print(difference)
        return True
    else:
        print(difference)
        return False


if __name__ == "__main__":
    main()
