#!/usr/bin/env python3
import subprocess
import os
import sys
import time

def run_command(cmd, cwd=None, description=""):
    """Run a shell command and return success status"""
    try:
        if description:
            print(f"\n{'='*50}")
            print(f"📦 {description}")
            print(f"{'='*50}")
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return False

def main():
    print("\n" + "="*50)
    print("🚀 Installing DigiAI Web Project Dependencies")
    print("="*50)
    
    base_dir = "/vercel/share/v0-project"
    
    # Install webapp dependencies
    webapp_dir = os.path.join(base_dir, "webapp")
    if os.path.isdir(webapp_dir):
        success = run_command(
            ["npm", "install"],
            cwd=webapp_dir,
            description="[1/2] Installing webapp dependencies..."
        )
        if not success:
            print(f"⚠️  Warning: webapp installation may have issues")
    else:
        print(f"⚠️  webapp directory not found at {webapp_dir}")
    
    # Install new-frontend dependencies
    frontend_dir = os.path.join(base_dir, "new-frontend")
    if os.path.isdir(frontend_dir):
        success = run_command(
            ["npm", "install"],
            cwd=frontend_dir,
            description="[2/2] Installing new-frontend dependencies..."
        )
        if not success:
            print(f"⚠️  Warning: new-frontend installation may have issues")
    else:
        print(f"⚠️  new-frontend directory not found at {frontend_dir}")
    
    print("\n" + "="*50)
    print("✅ Installation Complete!")
    print("="*50)
    print("\nTo run the project:")
    print("  1. Backend (webapp): cd webapp && npm start")
    print("  2. Frontend (new-frontend): cd new-frontend && npm run dev")
    print("\nThe frontend will run on http://localhost:3000")
    print("The backend will run on http://localhost:5000 (or as configured)")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
