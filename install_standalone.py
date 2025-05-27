#!/usr/bin/env python3
"""
BoE ETL Standalone Installation Script
=====================================

This script sets up the BoE ETL system to work with your existing codebase.
"""

import subprocess
import sys
import os
import shutil
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

def find_etl_directory():
    """Find the existing ETL directory."""
    current_dir = Path.cwd()
    
    # Check common locations
    possible_paths = [
        current_dir / "src" / "etl",
        current_dir / "etl",
        current_dir.parent / "src" / "etl",
        current_dir.parent / "etl"
    ]
    
    for path in possible_paths:
        if path.exists() and (path / "etl_pipeline.py").exists():
            return path
    
    return None

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    
    # Core dependencies
    core_deps = [
        "pandas>=1.3.0",
        "PyMuPDF>=1.20.0",
        "openpyxl>=3.0.0",
        "pyyaml>=6.0",
        "python-dateutil>=2.8.0"
    ]
    
    # Optional dependencies
    optional_deps = {
        "frontend": ["streamlit>=1.20.0", "plotly>=5.0.0"],
        "dev": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
        "jupyter": ["jupyter>=1.0.0", "ipykernel>=6.0.0"]
    }
    
    # Install core dependencies
    for dep in core_deps:
        if not run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}"):
            return False
    
    # Ask about optional dependencies
    for category, deps in optional_deps.items():
        choice = input(f"Install {category} dependencies? ({', '.join(deps)}) [y/N]: ").lower()
        if choice in ['y', 'yes']:
            for dep in deps:
                run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")
    
    return True

def setup_standalone():
    """Set up the standalone ETL system."""
    print("🚀 BoE ETL Standalone Installation")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Find existing ETL directory
    etl_dir = find_etl_directory()
    if etl_dir:
        print(f"✅ Found existing ETL directory: {etl_dir}")
    else:
        print("⚠️  No existing ETL directory found.")
        create_new = input("Create new ETL setup? [y/N]: ").lower()
        if create_new in ['y', 'yes']:
            etl_dir = Path.cwd() / "src" / "etl"
            etl_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created ETL directory: {etl_dir}")
        else:
            print("❌ Cannot proceed without ETL directory")
            return False
    
    # Copy standalone files if they don't exist
    current_dir = Path(__file__).parent
    standalone_files = [
        "standalone_frontend.py",
        "schema_transformer.py",
        "TAXONOMY_GUIDE.md"
    ]
    
    for filename in standalone_files:
        source = current_dir / filename
        target = Path.cwd() / filename
        
        if source.exists() and not target.exists():
            try:
                shutil.copy2(source, target)
                print(f"📋 Copied {filename}")
            except Exception as e:
                print(f"⚠️  Could not copy {filename}: {e}")
    
    # Test the installation
    print("\n🧪 Testing installation...")
    test_code = """
import sys
sys.path.insert(0, '.')

try:
    import standalone_frontend
    etl = standalone_frontend.StandaloneETL()
    print("✅ Standalone ETL imported successfully")
    
    # Test basic functionality
    import pandas as pd
    test_data = {'text': ['Test'], 'speaker_norm': ['CEO'], 'source_file': ['test.txt'], 'institution': ['Test'], 'quarter': ['Q1_2025']}
    df = pd.DataFrame(test_data)
    enhanced = etl.add_nlp_features(df)
    print(f"✅ NLP features working: {len(enhanced.columns)} columns generated")
    
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Test failed: {e}")
    sys.exit(1)
"""
    
    if run_command(f"{sys.executable} -c \"{test_code}\"", "Testing standalone setup"):
        print("\n🎉 Standalone installation completed successfully!")
        print("\n📚 Quick start:")
        print("   import standalone_frontend")
        print("   etl = standalone_frontend.StandaloneETL()")
        print("   results = etl.process_file('file.pdf', 'Institution', 'Q1_2025')")
        print("\n🌐 Launch web frontend:")
        print("   streamlit run pure_etl_frontend.py")
        print("   # or")
        print("   python standalone_frontend.py --frontend")
        
        # Show next steps
        print("\n📋 Next steps:")
        print("1. Place your documents in a 'data_sources' directory")
        print("2. Update institution and quarter information")
        print("3. Run the processing scripts")
        print("4. Check the output files")
        
        return True
    else:
        print("❌ Installation test failed")
        return False

def show_usage_examples():
    """Show usage examples."""
    print("\n📖 Usage Examples:")
    print("-" * 20)
    
    print("\n1. Process a single file:")
    print("```python")
    print("import standalone_frontend")
    print("etl = standalone_frontend.StandaloneETL()")
    print("results = etl.process_file('earnings_call.pdf', 'JPMorgan', 'Q1_2025')")
    print("etl.save_to_csv(results, 'output.csv')")
    print("```")
    
    print("\n2. Add NLP features:")
    print("```python")
    print("import pandas as pd")
    print("df = pd.DataFrame(results)")
    print("enhanced_df = etl.add_nlp_features(df)")
    print("```")
    
    print("\n3. Launch web interface:")
    print("```bash")
    print("streamlit run pure_etl_frontend.py")
    print("```")

if __name__ == "__main__":
    success = setup_standalone()
    if success:
        show_usage_examples()
    sys.exit(0 if success else 1)