#!/bin/bash

if [ -z "$1" ]; then
    echo "1 arg: a directory"
    exit 1
fi

DIR="$1"

if [ ! -d "$DIR" ]; then
    echo "$DIR is not a valid directory"
    exit 1
fi

echo "Top sized items in $DIR:"
du -ah "$DIR" --max-depth=1 2>/dev/null | sort -hr | head -n 10
