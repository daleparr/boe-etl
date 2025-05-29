@echo off
REM publish_to_pypi.bat - Windows batch script for PyPI publishing

echo 🚀 BoE ETL PyPI Publishing Script
echo =================================

REM Check if we're in the right directory
if not exist "setup.py" (
    echo ❌ Error: setup.py not found. Please run from boe-etl directory.
    pause
    exit /b 1
)

REM Install/upgrade build tools
echo 🔧 Installing build tools...
pip install --upgrade pip build twine

REM Clean previous builds
echo 🧹 Cleaning previous builds...
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build
if exist "*.egg-info" rmdir /s /q *.egg-info

REM Verify package can be imported
echo 🧪 Testing package import...
python -c "import boe_etl; print(f'✅ Package v{boe_etl.__version__} ready for publishing')"

REM Build package
echo 🏗️ Building package...
python -m build

REM Validate package
echo 🔍 Validating package...
twine check dist/*

REM Show what was built
echo 📦 Built packages:
dir dist

echo.
echo 📋 Ready to publish to PyPI
echo.
set /p test_upload="🤔 Upload to Test PyPI first? (y/N): "
if /i "%test_upload%"=="y" (
    echo 📤 Uploading to Test PyPI...
    twine upload --repository testpypi dist/*
    echo.
    echo ✅ Uploaded to Test PyPI!
    echo 🔗 Check: https://test.pypi.org/project/boe-etl/
    echo.
    
    set /p prod_upload="🚀 Continue to production PyPI? (y/N): "
    if /i "%prod_upload%"=="y" (
        echo 📤 Uploading to production PyPI...
        twine upload dist/*
        echo.
        echo 🎉 Successfully published to PyPI!
        echo 🔗 Package: https://pypi.org/project/boe-etl/
        echo 📦 Install: pip install boe-etl
    ) else (
        echo ⏸️ Stopped at Test PyPI. Run 'twine upload dist/*' when ready for production.
    )
) else (
    set /p direct_upload="🚀 Upload directly to production PyPI? (y/N): "
    if /i "%direct_upload%"=="y" (
        echo 📤 Uploading to production PyPI...
        twine upload dist/*
        echo.
        echo 🎉 Successfully published to PyPI!
        echo 🔗 Package: https://pypi.org/project/boe-etl/
        echo 📦 Install: pip install boe-etl
    ) else (
        echo ⏸️ Build completed. Run 'twine upload dist/*' when ready to publish.
    )
)

echo.
echo ✅ Publishing workflow completed!
pause