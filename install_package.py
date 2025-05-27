#!/usr/bin/env python3
"""
BoE ETL Package Installation Script
==================================

This script installs the BoE ETL package and its dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python version {version.major}.{version.minor} is compatible")
    return True

def install_package():
    """Install the BoE ETL package."""
    print("🚀 BoE ETL Package Installation")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Check if we're in the right directory
    if not Path("setup.py").exists():
        print("❌ setup.py not found. Please run this script from the boe-etl directory.")
        return False
    
    # Upgrade pip
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install the package in development mode
    if not run_command(f"{sys.executable} -m pip install -e .", "Installing BoE ETL package"):
        return False
    
    # Install optional dependencies
    print("\n📦 Installing optional dependencies...")
    optional_deps = {
        "frontend": "streamlit plotly",
        "dev": "pytest pytest-cov black flake8",
        "docs": "sphinx sphinx-rtd-theme"
    }
    
    for category, deps in optional_deps.items():
        choice = input(f"Install {category} dependencies? ({deps}) [y/N]: ").lower()
        if choice in ['y', 'yes']:
            run_command(f"{sys.executable} -m pip install {deps}", f"Installing {category} dependencies")
    
    # Test installation
    print("\n🧪 Testing installation...")
    test_code = """
import boe_etl
print(f"✅ BoE ETL version {boe_etl.__version__} installed successfully")
print(f"📦 Available modules: {', '.join(boe_etl.__all__)}")
"""
    
    if run_command(f"{sys.executable} -c \"{test_code}\"", "Testing package import"):
        print("\n🎉 Installation completed successfully!")
        print("\n📚 Quick start:")
        print("   from boe_etl import ETLPipeline")
        print("   pipeline = ETLPipeline()")
        print("   results = pipeline.process_document('file.pdf', 'Institution', 'Q1_2025')")
        print("\n🌐 Launch web frontend:")
        print("   boe-etl frontend")
        print("   # or")
        print("   from boe_etl.frontend import launch_frontend")
        print("   launch_frontend()")
        return True
    else:
        print("❌ Installation test failed")
        return False

if __name__ == "__main__":
    success = install_package()
    sys.exit(0 if success else 1)