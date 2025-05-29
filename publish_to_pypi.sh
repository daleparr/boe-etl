#!/bin/bash
# publish_to_pypi.sh - Automated PyPI publishing script for BoE ETL

set -e  # Exit on any error

echo "🚀 BoE ETL PyPI Publishing Script"
echo "================================="

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Please run from boe-etl directory."
    exit 1
fi

# Check Python version
python_version=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "🐍 Python version: $python_version"

# Install/upgrade build tools
echo "🔧 Installing build tools..."
pip install --upgrade pip build twine

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Verify package can be imported
echo "🧪 Testing package import..."
python -c "import boe_etl; print(f'✅ Package v{boe_etl.__version__} ready for publishing')"

# Build package
echo "🏗️ Building package..."
python -m build

# Validate package
echo "🔍 Validating package..."
twine check dist/*

# Show what was built
echo "📦 Built packages:"
ls -la dist/

# Ask for confirmation
echo ""
echo "📋 Ready to publish:"
echo "   - Source: $(ls dist/*.tar.gz)"
echo "   - Wheel: $(ls dist/*.whl)"
echo ""

read -p "🤔 Upload to Test PyPI first? (y/N): " test_upload
if [[ $test_upload =~ ^[Yy]$ ]]; then
    echo "📤 Uploading to Test PyPI..."
    twine upload --repository testpypi dist/*
    echo ""
    echo "✅ Uploaded to Test PyPI!"
    echo "🔗 Check: https://test.pypi.org/project/boe-etl/"
    echo ""
    echo "🧪 Test installation with:"
    echo "pip install --index-url https://test.pypi.org/simple/ boe-etl"
    echo ""
    
    read -p "🚀 Continue to production PyPI? (y/N): " prod_upload
    if [[ $prod_upload =~ ^[Yy]$ ]]; then
        echo "📤 Uploading to production PyPI..."
        twine upload dist/*
        echo ""
        echo "🎉 Successfully published to PyPI!"
        echo "🔗 Package: https://pypi.org/project/boe-etl/"
        echo "📦 Install: pip install boe-etl"
    else
        echo "⏸️ Stopped at Test PyPI. Run 'twine upload dist/*' when ready for production."
    fi
else
    read -p "🚀 Upload directly to production PyPI? (y/N): " direct_upload
    if [[ $direct_upload =~ ^[Yy]$ ]]; then
        echo "📤 Uploading to production PyPI..."
        twine upload dist/*
        echo ""
        echo "🎉 Successfully published to PyPI!"
        echo "🔗 Package: https://pypi.org/project/boe-etl/"
        echo "📦 Install: pip install boe-etl"
    else
        echo "⏸️ Build completed. Run 'twine upload dist/*' when ready to publish."
    fi
fi

echo ""
echo "✅ Publishing workflow completed!"