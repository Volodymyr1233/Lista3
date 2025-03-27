import sys
import io
from datetime import datetime
def readInput():
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    return sys.stdin.read()
def writeOutput(output:str):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stdout.write(output)

def getIpAtributes()->[str]:
    attributes_ip = [
        "ts",
        "uid",
        "id.orig_h",
        "id.orig_p",
        "id.resp_h",
        "id.resp_p",
        "trans_depth",
        "method",
        "host",
        "uri",
        "referrer",
        "user_agent",
        "request_body_len",
        "response_body_len",
        "status_code",
        "status_msg",
        "info_code",
        "info_msg",
        "filename",
        "tags",
        "username",
        "password",
        "proxied",
        "orig_fuids",
        "orig_mime_types",
        "resp_fuids",
        "resp_mime_types"
    ]
    return attributes_ip

if __name__ == "__main__":
    for i,attribute in enumerate(getIpAtributes()):
        print(f'{i}: {attribute}')