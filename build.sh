#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting build process..."

# Update pip and install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Build completed successfully!"
