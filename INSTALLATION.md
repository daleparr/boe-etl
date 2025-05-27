# BoE ETL Installation Guide

This document provides two installation methods for the BoE ETL system:

1. **Package Installation** - Clean, pip-installable package
2. **Standalone Installation** - Using existing ETL codebase

## 📦 Method 1: Package Installation (Recommended)

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/daleparr/boe-etl.git
cd boe-etl

# Install the package in development mode
pip install -e .

# Or install with optional dependencies
pip install -e .[all]
```

### Usage
```python
from boe_etl import ETLPipeline

# Initialize and use
pipeline = ETLPipeline()
results = pipeline.process_document('file.pdf', 'JPMorgan', 'Q1_2025')
```

### Launch Web Frontend
```bash
# Command line
boe-etl frontend

# Or in Python
from boe_etl.frontend import launch_frontend
launch_frontend()
```

---

## 🔧 Method 2: Standalone Installation (Existing Codebase)

### Prerequisites
- Python 3.8 or higher
- Existing BoE ETL codebase

### Installation Steps

```bash
# Navigate to your existing ETL directory
cd /path/to/your/etl/project

# Install required dependencies
pip install -r requirements.txt

# Copy the standalone frontend (if not already present)
curl -O https://raw.githubusercontent.com/daleparr/boe-etl/main/standalone_frontend.py
```

### Usage
```python
import standalone_frontend
import pandas as pd

# Initialize the standalone ETL
etl = standalone_frontend.StandaloneETL()

# Process documents
results = etl.process_file('earnings_call.pdf', 'JPMorgan', 'Q1_2025')

# Add NLP features
df = pd.DataFrame(results)
enhanced_df = etl.add_nlp_features(df)
```

### Launch Web Frontend
```bash
# Using the existing frontend
streamlit run pure_etl_frontend.py

# Or using the standalone version
python standalone_frontend.py --frontend
```

---

## 🔄 Migration Between Methods

### From Standalone to Package
```bash
# Install the package
pip install -e /path/to/boe-etl

# Update your imports
# OLD: import standalone_frontend
# NEW: from boe_etl import ETLPipeline
```

### From Package to Standalone
```bash
# Copy your existing ETL modules
cp -r /path/to/existing/src/etl/* ./

# Use the standalone approach
python standalone_frontend.py
```

---

## 📋 Feature Comparison

| Feature | Package Method | Standalone Method |
|---------|----------------|-------------------|
| **Installation** | `pip install` | Manual setup |
| **Dependencies** | Automatic | Manual |
| **Updates** | `pip upgrade` | Manual sync |
| **CLI Tools** | ✅ Built-in | ❌ Manual |
| **Import Style** | `from boe_etl import` | `import standalone_frontend` |
| **Web Frontend** | ✅ Integrated | ✅ Separate file |
| **Existing Code** | Requires migration | ✅ Works as-is |
| **Team Sharing** | ✅ Easy distribution | ❌ Manual sharing |

---

## 🚀 Quick Start Examples

### Package Method
```python
from boe_etl import ETLPipeline

pipeline = ETLPipeline()
df = pipeline.process_file('transcript.pdf', 'Citigroup', 'Q1_2025')
pipeline.save_results(df.to_dict('records'), 'output.csv')
```

### Standalone Method
```python
import standalone_frontend

etl = standalone_frontend.StandaloneETL()
results = etl.process_file('transcript.pdf', 'Citigroup', 'Q1_2025')
etl.save_to_csv(results, 'output.csv')
```

---

## 🔧 Troubleshooting

### Package Installation Issues
```bash
# If installation fails
pip install --upgrade pip setuptools wheel
pip install -e . --verbose

# Check installation
python -c "import boe_etl; print(boe_etl.__version__)"
```

### Standalone Issues
```bash
# Check dependencies
pip install pandas PyMuPDF openpyxl streamlit

# Test basic functionality
python -c "import standalone_frontend; print('✅ Import successful')"
```

### Common Problems

1. **Import Errors**: Ensure all dependencies are installed
2. **Path Issues**: Use absolute paths for file processing
3. **Permission Errors**: Check file/directory permissions
4. **Memory Issues**: Process large files in batches

---

## 📞 Support

- **Package Issues**: [GitHub Issues](https://github.com/daleparr/boe-etl/issues)
- **Standalone Issues**: Check existing ETL documentation
- **General Help**: etl-team@bankofengland.co.uk

Choose the method that best fits your workflow and existing setup!