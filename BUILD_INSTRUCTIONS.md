# Building Nudge Fake News Executable

This guide will help you convert your React frontend and FastAPI backend into a single executable file.

## Prerequisites

Before building the executable, make sure you have the following installed:

### Required Software
1. **Python 3.8+** - [Download from python.org](https://python.org)
2. **Node.js 16+** - [Download from nodejs.org](https://nodejs.org)
3. **npm** - Usually comes with Node.js

### Verify Installation
Open a terminal/command prompt and run:
```bash
python --version
node --version
npm --version
```

## Building the Executable

### Option 1: Using the Build Scripts (Recommended)

#### Windows
1. Open Command Prompt or PowerShell in the project directory
2. Run:
   ```cmd
   build.bat
   ```

#### Linux/macOS
1. Open Terminal in the project directory
2. Run:
   ```bash
   ./build.sh
   ```

### Option 2: Manual Build

If the build scripts don't work, you can run the build process manually:

1. **Install frontend dependencies:**
   ```bash
   npm install
   ```

2. **Build the React frontend:**
   ```bash
   npm run build
   ```

3. **Install backend dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

4. **Run the build script:**
   ```bash
   python build_exe.py
   ```

## What the Build Process Does

1. **Frontend Build**: Compiles your React application into static files
2. **Dependency Installation**: Installs all required Python packages
3. **File Copying**: Copies the built frontend to the backend directory
4. **Executable Creation**: Uses PyInstaller to create a single executable
5. **Final Copy**: Moves the executable to the project root

## Output

After successful build, you'll find:
- **Windows**: `nudge-fakenews.exe` in the project root
- **Linux/macOS**: `nudge-fakenews` in the project root

## Running the Application

### From Executable
Simply double-click the executable file or run it from the command line:
```bash
# Windows
nudge-fakenews.exe

# Linux/macOS
./nudge-fakenews
```

The application will:
1. Start a local web server (usually on port 8000)
2. Open your default web browser to the application
3. Serve both the frontend and API from the same executable

### Development Mode
For development, you can still run the frontend and backend separately:

**Frontend (Terminal 1):**
```bash
npm run dev
```

**Backend (Terminal 2):**
```bash
cd backend
python main.py
```

## Troubleshooting

### Common Issues

1. **"Python not found"**
   - Make sure Python is installed and in your PATH
   - Try using `python3` instead of `python`

2. **"Node.js not found"**
   - Install Node.js from the official website
   - Restart your terminal after installation

3. **"npm not found"**
   - npm usually comes with Node.js
   - Try reinstalling Node.js

4. **Build fails with PyInstaller errors**
   - Make sure all dependencies are installed
   - Try running `pip install --upgrade pyinstaller`

5. **Frontend build fails**
   - Check that all npm dependencies are installed
   - Try deleting `node_modules` and running `npm install` again

6. **Executable doesn't start**
   - Check if antivirus software is blocking it
   - Try running from command line to see error messages

### Getting Help

If you encounter issues:
1. Check the error messages in the terminal
2. Make sure all prerequisites are installed
3. Try running the manual build steps one by one
4. Check that you have sufficient disk space for the build

## File Structure After Build

```
nudge-fakenews/
├── nudge-fakenews.exe (or nudge-fakenews on Linux/macOS)
├── backend/
│   ├── dist/ (built frontend files)
│   ├── main.py
│   └── requirements.txt
├── src/ (frontend source)
├── build_exe.py
├── build.bat (Windows)
└── build.sh (Linux/macOS)
```

## Notes

- The executable includes both the frontend and backend
- The application runs on `http://localhost:8000` by default
- All API endpoints are available at `http://localhost:8000/analyze/text`
- The executable is self-contained and doesn't require Python or Node.js to run 