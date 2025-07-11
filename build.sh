#!/bin/bash

echo "🚀 Starting Nudge Fake News Build Process..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed or not in PATH"
    echo "Please install Node.js from https://nodejs.org"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed or not in PATH"
    echo "Please install npm (usually comes with Node.js)"
    exit 1
fi

echo "✅ Prerequisites check passed"
echo

# Run the build script
python3 build_exe.py

if [ $? -eq 0 ]; then
    echo
    echo "🎉 Build completed successfully!"
    echo
    echo "The executable 'nudge-fakenews' has been created in the current directory."
    echo "You can now run it by executing: ./nudge-fakenews"
    echo
else
    echo
    echo "❌ Build failed! Check the error messages above."
    exit 1
fi 