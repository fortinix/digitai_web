#!/usr/bin/env python3
import os
import subprocess
import sys

# Change to project root
os.chdir('/vercel/share/v0-project')

def run_npm_install(directory):
    """Run npm install in a given directory"""
    if not os.path.exists(directory):
        print(f"❌ Directory not found: {directory}")
        return False
    
    print(f"\n📁 Installing dependencies in {directory}...")
    try:
        result = subprocess.run(
            ["npm", "install"],
            cwd=directory,
            capture_output=False,  # Show output in real-time
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Successfully installed {directory} dependencies!")
            return True
        else:
            print(f"❌ Failed to install {directory} dependencies")
            return False
    except Exception as e:
        print(f"❌ Exception while installing {directory}: {e}")
        return False

print("=" * 70)
print("🚀 DigiAI Web Project - Installing Dependencies")
print("=" * 70)
print(f"📍 Project root: {os.getcwd()}\n")

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
    print("⚠️  Some installations may have failed")
    print("=" * 70)
