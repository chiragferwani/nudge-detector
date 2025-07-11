#!/usr/bin/env python3
"""
Build script to create an executable from the React frontend and FastAPI backend.
This script will:
1. Install frontend dependencies
2. Build the React frontend
3. Copy the built frontend to the backend directory
4. Create an executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

def run_command(command, cwd=None, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {command}")
    if cwd:
        print(f"Working directory: {cwd}")
    
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    
    if result.stdout:
        print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, command)
    
    return result

def main():
    print("🚀 Starting build process...")
    
    # Get the project root directory
    project_root = Path(__file__).parent
    frontend_dir = project_root
    backend_dir = project_root / "backend"
    
    print(f"Project root: {project_root}")
    print(f"Frontend directory: {frontend_dir}")
    print(f"Backend directory: {backend_dir}")
    
    # Step 1: Install frontend dependencies
    print("\n📦 Installing frontend dependencies...")
    try:
        run_command("npm install", cwd=frontend_dir)
    except subprocess.CalledProcessError:
        print("❌ Failed to install frontend dependencies")
        return 1
    
    # Step 2: Build the React frontend
    print("\n🔨 Building React frontend...")
    try:
        run_command("npm run build", cwd=frontend_dir)
    except subprocess.CalledProcessError:
        print("❌ Failed to build frontend")
        return 1
    
    # Step 3: Copy built frontend to backend directory
    print("\n📁 Copying built frontend to backend...")
    dist_source = frontend_dir / "dist"
    dist_dest = backend_dir / "dist"
    
    if dist_dest.exists():
        shutil.rmtree(dist_dest)
    
    shutil.copytree(dist_source, dist_dest)
    print(f"✅ Copied {dist_source} to {dist_dest}")
    
    # Step 4: Install backend dependencies
    print("\n📦 Installing backend dependencies...")
    try:
        run_command("pip install -r requirements.txt", cwd=backend_dir)
    except subprocess.CalledProcessError:
        print("❌ Failed to install backend dependencies")
        return 1
    
    # Step 5: Install PyInstaller
    print("\n📦 Installing PyInstaller...")
    try:
        run_command("pip install pyinstaller")
    except subprocess.CalledProcessError:
        print("❌ Failed to install PyInstaller")
        return 1
    
    # Step 6: Create executable
    print("\n🔨 Creating executable...")
    
    # Create PyInstaller spec file
    main_py_path = backend_dir / "main.py"
    dist_path = backend_dir / "dist"
    
    spec_content = f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    [r'{main_py_path}'],
    pathex=[],
    binaries=[],
    datas=[(r'{dist_path}', 'dist')],
    hiddenimports=[
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'fastapi',
        'fastapi.staticfiles',
        'fastapi.responses',
        'fastapi.middleware.cors',
        'pydantic',
        'requests',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='nudge-fakenews',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    
    spec_file = backend_dir / "nudge-fakenews.spec"
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    
    # Run PyInstaller
    try:
        run_command(f"pyinstaller --clean nudge-fakenews.spec", cwd=backend_dir)
    except subprocess.CalledProcessError:
        print("❌ Failed to create executable")
        return 1
    
    # Step 7: Copy executable to project root
    print("\n📁 Copying executable to project root...")
    exe_name = "nudge-fakenews.exe" if platform.system() == "Windows" else "nudge-fakenews"
    exe_source = backend_dir / "dist" / exe_name
    exe_dest = project_root / exe_name
    
    if exe_dest.exists():
        exe_dest.unlink()
    
    shutil.copy2(exe_source, exe_dest)
    print(f"✅ Executable created: {exe_dest}")
    
    print(f"\n🎉 Build completed successfully!")
    print(f"Executable location: {exe_dest}")
    print(f"To run the application, double-click: {exe_name}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 