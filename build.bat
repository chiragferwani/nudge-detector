@echo off
echo 🚀 Starting Nudge Fake News Build Process...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

REM Check if npm is installed
npm --version >nul 2>&1
if errorlevel 1 (
    echo ❌ npm is not installed or not in PATH
    echo Please install npm (usually comes with Node.js)
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed
echo.

REM Run the build script
python build_exe.py

if errorlevel 1 (
    echo.
    echo ❌ Build failed! Check the error messages above.
    pause
    exit /b 1
) else (
    echo.
    echo 🎉 Build completed successfully!
    echo.
    echo The executable 'nudge-fakenews.exe' has been created in the current directory.
    echo You can now run it by double-clicking the executable.
    echo.
    pause
) 