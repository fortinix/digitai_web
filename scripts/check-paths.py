#!/usr/bin/env python3
import os
import subprocess

print("Current working directory:", os.getcwd())
print("\nContents of current directory:")
for item in os.listdir('.'):
    full_path = os.path.join('.', item)
    if os.path.isdir(full_path):
        print(f"  📁 {item}/")
    else:
        print(f"  📄 {item}")

print("\nChecking common paths:")
paths_to_check = [
    "/vercel/share/v0-project",
    "/vercel/share/v0-project/webapp",
    "/vercel/share/v0-project/new-frontend",
    "./webapp",
    "./new-frontend",
]

for path in paths_to_check:
    exists = os.path.exists(path)
    is_dir = os.path.isdir(path) if exists else False
    print(f"  {path}: {'✅ EXISTS' if exists else '❌ NOT FOUND'} {'(dir)' if is_dir else ''}")

print("\nRunning npm install in webapp...")
result = subprocess.run(["npm", "install"], cwd="./webapp", capture_output=True, text=True)
print(f"Return code: {result.returncode}")
if result.stdout:
    print(f"stdout: {result.stdout[:200]}")
if result.stderr:
    print(f"stderr: {result.stderr[:200]}")

print("\nRunning npm install in new-frontend...")
result = subprocess.run(["npm", "install"], cwd="./new-frontend", capture_output=True, text=True)
print(f"Return code: {result.returncode}")
if result.stdout:
    print(f"stdout: {result.stdout[:200]}")
if result.stderr:
    print(f"stderr: {result.stderr[:200]}")
