#!/usr/bin/env python3
import os
import subprocess
import sys

def run_command(cmd, cwd=None, show_output=False):
    """Run a shell command and return the result"""
    try:
        print(f"📦 Running: {' '.join(cmd)}")
        if show_output:
            result = subprocess.run(cmd, cwd=cwd)
            return result.returncode == 0
        else:
            result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Error output: {result.stderr}")
                return False
            return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

print("=" * 70)
print("🚀 Installing DigiAI Web Project Dependencies")
print("=" * 70)
print(f"📍 Current directory: {os.getcwd()}\n")

# Install webapp dependencies
webapp_dir = "webapp"
if os.path.exists(webapp_dir):
    print(f"📁 Installing {webapp_dir} dependencies...")
    if run_command(["npm", "install"], cwd=webapp_dir, show_output=True):
        print(f"✅ {webapp_dir} dependencies installed!\n")
    else:
        print(f"⚠️  Failed to install {webapp_dir} dependencies\n")
else:
    print(f"⚠️  {webapp_dir} directory not found\n")

# Install new-frontend dependencies
frontend_dir = "new-frontend"
if os.path.exists(frontend_dir):
    print(f"📁 Installing {frontend_dir} dependencies...")
    if run_command(["npm", "install"], cwd=frontend_dir, show_output=True):
        print(f"✅ {frontend_dir} dependencies installed!\n")
    else:
        print(f"⚠️  Failed to install {frontend_dir} dependencies\n")
else:
    print(f"⚠️  {frontend_dir} directory not found\n")

print("=" * 70)
print("✅ Installation Complete!")
print("=" * 70)
print("\nTo run the project:")
print(f"  1. Backend (webapp): cd {webapp_dir} && npm start")
print(f"  2. Frontend (new-frontend): cd {frontend_dir} && npm run dev")
print("\nThe frontend will run on http://localhost:3000")
print("The backend will run on http://localhost:5000 (or as configured)")
print("=" * 70)
