#!/bin/bash

echo "=========================================="
echo "Installing DigiAI Web Project Dependencies"
echo "=========================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to handle errors
handle_error() {
    echo -e "${YELLOW}Error: $1${NC}"
    exit 1
}

# Navigate to project root
cd "$(dirname "$0")/.." || handle_error "Failed to navigate to project root"

echo -e "${GREEN}[1/3] Installing webapp dependencies...${NC}"
cd webapp || handle_error "Failed to navigate to webapp"
npm install || handle_error "Failed to install webapp dependencies"
cd .. || handle_error "Failed to navigate back"

echo -e "${GREEN}[2/3] Installing new-frontend dependencies...${NC}"
cd new-frontend || handle_error "Failed to navigate to new-frontend"
npm install || handle_error "Failed to install new-frontend dependencies"
cd .. || handle_error "Failed to navigate back"

echo -e "${GREEN}[3/3] Starting development servers...${NC}"
echo ""
echo "=========================================="
echo "Starting Development Servers"
echo "=========================================="
echo "Frontend: http://localhost:3000"
echo "Backend: http://localhost:5000"
echo "=========================================="
echo ""

# Start servers in background
(cd webapp && npm run dev) &
WEBAPP_PID=$!

(cd new-frontend && npm run dev) &
FRONTEND_PID=$!

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Shutting down servers..."
    kill $WEBAPP_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    wait $WEBAPP_PID 2>/dev/null
    wait $FRONTEND_PID 2>/dev/null
    echo "Servers stopped."
}

# Set up trap to cleanup on exit
trap cleanup EXIT INT TERM

# Wait for both processes
wait
