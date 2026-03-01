#!/bin/bash

echo "=================================================="
echo "🚀 Installing DigiAI Web Project Dependencies"
echo "=================================================="

# Install root dependencies
echo ""
echo "📦 Installing root dependencies..."
npm install

# Install webapp dependencies
echo ""
echo "📦 Installing webapp dependencies..."
cd webapp
npm install
cd ..

# Install new-frontend dependencies
echo ""
echo "📦 Installing new-frontend dependencies..."
cd new-frontend
npm install
cd ..

echo ""
echo "=================================================="
echo "✅ All dependencies installed successfully!"
echo "=================================================="
echo ""
echo "🎉 Ready to run your project:"
echo "   Option 1 - Run separately:"
echo "     - Backend:  cd webapp && npm start"
echo "     - Frontend: cd new-frontend && npm run dev"
echo ""
echo "   Option 2 - Run with root npm scripts:"
echo "     - npm run dev:backend  (terminal 1)"
echo "     - npm run dev:frontend (terminal 2)"
echo ""
echo "The frontend will be available at http://localhost:3000"
echo "The backend will be available at http://localhost:5000"
echo "=================================================="
