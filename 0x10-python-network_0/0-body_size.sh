#!/bin/bash
# This script displays the size of the body of the HTTP response.
curl -s "$1" | wc -c
