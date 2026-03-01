#!/usr/bin/env python3
import os
import subprocess
import sys

def find_project_root():
    """Find the project root by looking for webapp and new-frontend directories"""
    # Try current directory first
    if os.path.exists("webapp") and os.path.exists("new-frontend"):
        return os.getcwd()
    
    # Try parent directories
    for i in range(5):
        parent = os.path.join("..", "*" * i)
        test_path = os.path.abspath(parent)
        if os.path.exists(os.path.join(test_path, "webapp")):
            return test_path
    
    # Last resort: search from home
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        if "webapp" in dirs and "new-frontend" in dirs:
            return root
    
    return None

def run_npm_install(directory):
    """Run npm install in a given directory"""
    if not os.path.exists(directory):
        print(f"❌ Directory not found: {directory}")
        return False
    
    print(f"\n{'=' * 70}")
    print(f"📦 Installing dependencies in {os.path.abspath(directory)}...")
    print(f"{'=' * 70}")
    try:
        # Run npm install with visible output
        result = subprocess.run(
            ["npm", "install"],
            cwd=directory
        )
        if result.returncode == 0:
            print(f"✅ Successfully installed {directory} dependencies!\n")
            return True
        else:
            print(f"❌ Failed to install {directory} dependencies\n")
            return False
    except Exception as e:
        print(f"❌ Exception while installing {directory}: {e}\n")
        return False

print("🔍 Locating project root...")
project_root = find_project_root()

if not project_root:
    print("❌ Could not find project root with webapp and new-frontend directories")
    sys.exit(1)

print(f"✅ Found project root: {project_root}\n")
os.chdir(project_root)

print("=" * 70)
print("🚀 DigiAI Web Project - Installing Dependencies")
print("=" * 70)

# Install webapp
success_webapp = run_npm_install("webapp")

# Install new-frontend  
success_frontend = run_npm_install("new-frontend")

print("\n" + "=" * 70)
if success_webapp and success_frontend:
    print("✅ All dependencies installed successfully!")
    print("=" * 70)
    print("\n🎉 Ready to run your project:")
    print("   Backend:  cd webapp && npm start")
    print("   Frontend: cd new-frontend && npm run dev")
else:
    print("⚠️  Some installations may have failed - check output above")
    print("=" * 70)
