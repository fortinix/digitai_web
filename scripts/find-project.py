#!/usr/bin/env python3
import os
import subprocess

# Search for webapp directory
result = subprocess.run(["find", "/", "-type", "d", "-name", "webapp", "-o", "-type", "d", "-name", "new-frontend"], 
                       capture_output=True, text=True, timeout=10)
print("Found directories:")
print(result.stdout)

# Also try locating from relative paths
print("\nTrying relative path traversal...")
for root, dirs, files in os.walk(".."):
    if "webapp" in dirs or "new-frontend" in dirs:
        print(f"Found in: {os.path.abspath(root)}")
        break
