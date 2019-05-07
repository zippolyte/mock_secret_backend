#!/usr/bin/python

import sys
import json

data = json.loads(sys.stdin.read())

res = {}
for secret_handle in data["secrets"]:
    res[secret_handle] = {
        "value": "decrypted_{}".format(secret_handle),
        "error": None,
    }

sys.stdout.write(json.dumps(res))
