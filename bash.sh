#!/usr/bin/env bash

set -euf -o pipefile

# try to use Python first
# always quote variables "$var"
# only use "$@" to pass args through
# pass user supplied args after -- to avoid user passing -x flags
