#!/usr/bin/env python
"""
Converts an .env file to a Kubernetes Secret .yml format

Usage: env-to-secret.py <secret name> [namespace]

"""
import sys
from base64 import b64encode
from yaml import dump


def get_args():
    if not len(sys.argv) == 2 and not len(sys.argv) == 3:
        return None
    return sys.argv[1:]

def sanitize_value(val):
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1]
    if val.startswith("'") and val.endswith("'"):
        return val[1:-1]
    return val

def encode_value(val):
    return b64encode(sanitize_value(val).encode('utf-8')).decode('utf-8')

def get_secrets_data(fh):
    data = {}
    for line in fh:
        parts = line.rstrip().split('=', 2)
        if len(parts) == 2 and not line.strip().startswith("#"):
            key, value = parts
            data[key] = encode_value(value)
    return {'data':data}

def get_yaml(secret_name, namespace=''):
    if namespace:
        namespace = "\n  namespace: {}".format(namespace)
    return """apiVersion: v1\nkind: Secret\nmetadata:\n  name: {}{}\ntype: Opaque\n{}\n""".format(
        secret_name,
        namespace,
        dump(get_secrets_data(sys.stdin))
    )

def main(*args):
    sys.stdout.write(get_yaml(*args))

if __name__ == "__main__":
    args = get_args()
    if not args:
        sys.stderr.write(__doc__)
        exit(-1)
    main(*args)
