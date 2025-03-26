
__attributes = [
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

def entry_to_dict(tupla:tuple)->dict:
    if tuple is tuple and len(tupla)==27:
        result = dict()
        for i,item in enumerate(tupla):
            result.update({__attributes[i]:item})
        return result
    else:
        raise ValueError(f"{tupla} is not a tuple or length!=27")