#!/usr/bin/env python3
import os
import subprocess
import sys

def run_command(cmd, cwd=None):
    """Run a shell command and return the result"""
    try:
        print(f"📦 Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            return False
        print(f"✅ Success: {result.stdout[-100:]}")  # Print last 100 chars
        return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

# Project root
project_root = "/vercel/share/v0-project"

print("=" * 60)
print("🚀 Installing DigiAI Web Project Dependencies")
print("=" * 60)

# Install webapp dependencies
webapp_dir = os.path.join(project_root, "webapp")
if os.path.exists(webapp_dir):
    print(f"\n📁 Installing webapp dependencies...")
    if run_command(["npm", "install"], cwd=webapp_dir):
        print("✅ webapp dependencies installed!")
    else:
        print("⚠️  Failed to install webapp dependencies")
else:
    print(f"⚠️  webapp directory not found at {webapp_dir}")

# Install new-frontend dependencies
frontend_dir = os.path.join(project_root, "new-frontend")
if os.path.exists(frontend_dir):
    print(f"\n📁 Installing new-frontend dependencies...")
    if run_command(["npm", "install"], cwd=frontend_dir):
        print("✅ new-frontend dependencies installed!")
    else:
        print("⚠️  Failed to install new-frontend dependencies")
else:
    print(f"⚠️  new-frontend directory not found at {frontend_dir}")

print("\n" + "=" * 60)
print("✅ Installation Complete!")
print("=" * 60)
print("\nTo run the project:")
print(f"  1. Backend (webapp): cd {webapp_dir} && npm start")
print(f"  2. Frontend (new-frontend): cd {frontend_dir} && npm run dev")
print("\nThe frontend will run on http://localhost:3000")
print("The backend will run on http://localhost:5000")
print("=" * 60)
