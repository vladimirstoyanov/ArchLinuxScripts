#!/bin/bash
CACHE_BASE="$HOME/.cache/mozilla/firefox"

for profile in "$CACHE_BASE"/*/; do
    if [ -d "$profile/cache2" ]; then
        rm -rf "$profile/cache2/*"
        echo "Cleared cache for $(basename "$profile")"
    fi
done
