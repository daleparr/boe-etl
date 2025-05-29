# PyPI Publishing Guide for BoE ETL

Complete workflow to publish the boe-etl package to PyPI.

## 🔄 **Step 1: Update GitHub Repository**

### Commit Current Changes
```bash
cd boe-etl
git add .
git commit -m "feat: update to pure ETL pipeline v1.0.0

- Remove NLP analysis features to maintain pure ETL philosophy
- Focus on raw data extraction without analytical assumptions
- Update README to reflect pure ETL approach
- Prepare for PyPI publishing"

git push origin main
```

## 📦 **Step 2: Prepare Package for PyPI**

### Install Build Tools
```bash
pip install --upgrade pip
pip install build twine
```

### Verify Package Structure
```bash
# Check setup.py is correct
python setup.py check

# Verify package can be imported
python -c "import boe_etl; print(f'✅ Package v{boe_etl.__version__} ready')"
```

### Clean Previous Builds
```bash
rm -rf dist/ build/ *.egg-info/
```

## 🏗️ **Step 3: Build Package**

### Build Source and Wheel Distributions
```bash
python -m build
```

This creates:
- `dist/boe-etl-1.0.0.tar.gz` (source distribution)
- `dist/boe_etl-1.0.0-py3-none-any.whl` (wheel distribution)

### Verify Build
```bash
ls -la dist/
# Should show both .tar.gz and .whl files
```

## 🧪 **Step 4: Test Package Locally**

### Test Installation from Wheel
```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# or
test_env\Scripts\activate     # Windows

# Install from wheel
pip install dist/boe_etl-1.0.0-py3-none-any.whl

# Test import
python -c "from boe_etl import ETLPipeline; print('✅ Local install works')"

# Deactivate test environment
deactivate
rm -rf test_env
```

## 🔍 **Step 5: Validate Package**

### Check Package with Twine
```bash
twine check dist/*
```

This validates:
- Package metadata
- README rendering
- Distribution format

## 🚀 **Step 6: Publish to PyPI**

### Option A: Test PyPI First (Recommended)
```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# You'll be prompted for credentials:
# Username: daleparr
# Password: [your PyPI token]
```

### Test Installation from Test PyPI
```bash
pip install --index-url https://test.pypi.org/simple/ boe-etl
```

### Option B: Publish to Production PyPI
```bash
# Upload to production PyPI
twine upload dist/*

# You'll be prompted for credentials:
# Username: daleparr
# Password: [your PyPI token]
```

## 🔐 **Step 7: PyPI Authentication**

### Using API Tokens (Recommended)
1. Go to https://pypi.org/manage/account/token/
2. Create new token for "boe-etl" project
3. Use token as password when prompted

### Configure .pypirc (Optional)
```bash
# Create ~/.pypirc
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-token-here
```

## ✅ **Step 8: Verify Publication**

### Check PyPI Page
- Visit: https://pypi.org/project/boe-etl/
- Verify package information
- Check README rendering

### Test Installation
```bash
pip install boe-etl
python -c "from boe_etl import ETLPipeline; print('✅ PyPI install works')"
```

## 🔄 **Step 9: Update Version for Future Releases**

### Version Bump Process
```bash
# Update version in setup.py
# Update version in boe_etl/__init__.py
# Update CHANGELOG.md

# Build and publish new version
python -m build
twine upload dist/*
```

## 📋 **Complete Workflow Script**

```bash
#!/bin/bash
# publish_to_pypi.sh

echo "🚀 Publishing BoE ETL to PyPI"

# Step 1: Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Step 2: Build package
echo "🏗️ Building package..."
python -m build

# Step 3: Check package
echo "🔍 Validating package..."
twine check dist/*

# Step 4: Upload to Test PyPI
echo "📤 Uploading to Test PyPI..."
twine upload --repository testpypi dist/*

echo "✅ Package uploaded to Test PyPI"
echo "🔗 Check: https://test.pypi.org/project/boe-etl/"
echo ""
echo "To publish to production PyPI, run:"
echo "twine upload dist/*"
```

## 🛠️ **Troubleshooting**

### Common Issues

1. **Authentication Errors**
   - Use API tokens instead of username/password
   - Check token permissions

2. **Package Already Exists**
   - Increment version number
   - Cannot overwrite existing versions

3. **README Not Rendering**
   - Check Markdown syntax
   - Verify long_description_content_type="text/markdown"

4. **Import Errors**
   - Check __init__.py imports
   - Verify package structure

### Useful Commands
```bash
# Check what's in your package
tar -tzf dist/boe-etl-1.0.0.tar.gz

# Install in development mode
pip install -e .

# Uninstall package
pip uninstall boe-etl

# Check installed version
pip show boe-etl
```

## 🎯 **Final Checklist**

- [ ] README.md reflects pure ETL philosophy
- [ ] Version number updated in setup.py and __init__.py
- [ ] Package builds without errors
- [ ] Twine check passes
- [ ] Test installation works
- [ ] GitHub repository updated
- [ ] PyPI credentials ready
- [ ] Package uploaded to Test PyPI
- [ ] Production PyPI upload completed

**Your package will be available at: https://pypi.org/project/boe-etl/**

Users can then install with: `pip install boe-etl`