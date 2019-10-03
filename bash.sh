#!/bin/bash
#
# Generic base script to use as a template
#
# Author: Roger Collins
#
# Some caveats:
# - Try to use Python first
# - Always quote variables "$var"
# - Only use "$@" to pass args through
# - Pass user supplied args after -- to avoid user passing -x flags (ie. curl -v -- "$@")

# set flags here so that "bash <script>" doesn't break
set -euf -o pipefail

#---------------------------------#
# Function to print error messages
#
# Arguments:
#   Message to print to STDERR
# Returns:
#   None
#---------------------------------#
err() {
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}
