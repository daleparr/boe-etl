# Google Colab Setup Guide for BoE ETL (WORKING VERSION)

Complete guide to using the BoE ETL package in Google Colab notebooks with working solutions.

## 🚨 **Quick Fix for Import Issues**

If you encounter import errors, use this working approach:

### **Method 1: Direct Module Import (Recommended)**

```python
# Install the package
!pip install boe-etl

# Import specific modules directly (avoids complex dependencies)
import boe_etl.etl_pipeline as etl
import boe_etl.schema_transformer as transformer
import pandas as pd
from pathlib import Path

print("✅ BoE ETL modules imported successfully!")
```

### **Method 2: Alternative Import Pattern**

```python
# If Method 1 fails, try this approach
!pip install boe-etl

# Import the package and access components
import boe_etl
from boe_etl.parsers.pdf_parser import parse_pdf
from boe_etl.parsers.text_parser import parse_text
from boe_etl.parsers.excel_parser import parse_excel

print("✅ BoE ETL parsers imported successfully!")
```

## 🔧 **Working Document Processing**

### **Step 1: Upload Files**
```python
from google.colab import files
import tempfile
import os

# Upload files
print("📁 Upload your financial documents:")
uploaded = files.upload()

# Get uploaded file info
for filename, content in uploaded.items():
    print(f"📄 Uploaded: {filename} ({len(content)} bytes)")
```

### **Step 2: Process Documents (Direct Parser Approach)**

```python
# Process PDF files
def process_pdf_document(filename, institution='TestBank', quarter='Q1_2025'):
    try:
        from boe_etl.parsers.pdf_parser import parse_pdf
        from pathlib import Path
        
        file_path = Path(filename)
        results = parse_pdf(institution, quarter, file_path)
        return results
    except Exception as e:
        print(f"❌ Error processing PDF: {e}")
        return None

# Process text files
def process_text_document(filename, institution='TestBank', quarter='Q1_2025'):
    try:
        from boe_etl.parsers.text_parser import parse_text
        from pathlib import Path
        
        file_path = Path(filename)
        results = parse_text(institution, quarter, file_path)
        return results
    except Exception as e:
        print(f"❌ Error processing text: {e}")
        return None

# Process Excel files
def process_excel_document(filename, institution='TestBank', quarter='Q1_2025'):
    try:
        from boe_etl.parsers.excel_parser import parse_excel
        from pathlib import Path
        
        file_path = Path(filename)
        results = parse_excel(institution, quarter, file_path)
        return results
    except Exception as e:
        print(f"❌ Error processing Excel: {e}")
        return None

# Auto-detect and process
def process_document(filename, institution='TestBank', quarter='Q1_2025'):
    """Auto-detect file type and process accordingly."""
    file_ext = filename.lower().split('.')[-1]
    
    if file_ext == 'pdf':
        return process_pdf_document(filename, institution, quarter)
    elif file_ext == 'txt':
        return process_text_document(filename, institution, quarter)
    elif file_ext in ['xlsx', 'xls']:
        return process_excel_document(filename, institution, quarter)
    else:
        print(f"❌ Unsupported file type: {file_ext}")
        return None
```

### **Step 3: Process All Uploaded Files**

```python
# Process all uploaded files
all_results = []

for filename in uploaded.keys():
    print(f"🔄 Processing {filename}...")
    
    # Change these values as needed
    institution = 'JPMorgan'  # Change to your institution
    quarter = 'Q1_2025'      # Change to your quarter
    
    results = process_document(filename, institution, quarter)
    
    if results:
        all_results.extend(results)
        print(f"✅ Processed {filename}: {len(results)} records")
    else:
        print(f"❌ Failed to process {filename}")

print(f"\n📊 Total records processed: {len(all_results)}")
```

### **Step 4: Convert to DataFrame and Analyze**

```python
# Convert to DataFrame
if all_results:
    df = pd.DataFrame(all_results)
    print(f"✅ Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
    
    # Display basic info
    print("\n📋 Column names:")
    print(list(df.columns))
    
    # Show first few rows
    print("\n📊 First 5 rows:")
    display(df.head())
    
    # Basic statistics
    print(f"\n📈 Data Summary:")
    print(f"- Total records: {len(df)}")
    if 'speaker_norm' in df.columns:
        print(f"- Unique speakers: {df['speaker_norm'].nunique()}")
    if 'has_financial_terms' in df.columns:
        print(f"- Records with financial terms: {df['has_financial_terms'].sum()}")
else:
    print("❌ No data to process")
```

### **Step 5: Export Results**

```python
# Save to CSV
if all_results:
    output_filename = f'{institution}_{quarter}_processed_data.csv'
    df.to_csv(output_filename, index=False)
    
    # Download the file
    files.download(output_filename)
    print(f"📥 Downloaded: {output_filename}")
```

## 🌐 **Web Interface in Colab (Alternative Method)**

If the main ETL import fails, try this simplified approach:

```python
# Install required packages
!pip install streamlit pyngrok

# Create a simple processing script
processing_script = '''
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("BoE ETL - Simple Document Processor")

uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'xlsx'])

if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    
    # Save uploaded file
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process based on file type
    if st.button("Process Document"):
        try:
            file_ext = uploaded_file.name.lower().split('.')[-1]
            
            if file_ext == 'pdf':
                from boe_etl.parsers.pdf_parser import parse_pdf
                results = parse_pdf('TestBank', 'Q1_2025', Path(uploaded_file.name))
            elif file_ext == 'txt':
                from boe_etl.parsers.text_parser import parse_text
                results = parse_text('TestBank', 'Q1_2025', Path(uploaded_file.name))
            elif file_ext in ['xlsx', 'xls']:
                from boe_etl.parsers.excel_parser import parse_excel
                results = parse_excel('TestBank', 'Q1_2025', Path(uploaded_file.name))
            
            if results:
                df = pd.DataFrame(results)
                st.success(f"Processed {len(df)} records!")
                st.dataframe(df.head())
                
                # Download button
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"processed_{uploaded_file.name}.csv",
                    mime="text/csv"
                )
            else:
                st.error("Failed to process document")
                
        except Exception as e:
            st.error(f"Error: {e}")
'''

# Save the script
with open('simple_etl_app.py', 'w') as f:
    f.write(processing_script)

print("✅ Created simple ETL app")
```

```python
# Run the Streamlit app with ngrok
import subprocess
import threading
import time
from pyngrok import ngrok

def run_streamlit():
    subprocess.run(["streamlit", "run", "simple_etl_app.py", "--server.port", "8501"])

# Start Streamlit in background
streamlit_thread = threading.Thread(target=run_streamlit, daemon=True)
streamlit_thread.start()

# Wait for server to start
time.sleep(10)

# Create public tunnel
public_url = ngrok.connect(8501)
print(f"🌐 Simple ETL Interface: {public_url}")
```

## 🛠️ **Troubleshooting Common Issues**

### **Issue 1: Import Errors**
```python
# Test individual components
try:
    import boe_etl
    print("✅ boe_etl package imported")
except ImportError as e:
    print(f"❌ boe_etl import failed: {e}")

try:
    from boe_etl.parsers.pdf_parser import parse_pdf
    print("✅ PDF parser imported")
except ImportError as e:
    print(f"❌ PDF parser import failed: {e}")
```

### **Issue 2: Missing Dependencies**
```python
# Install missing dependencies
!pip install PyPDF2 openpyxl pandas streamlit

# Verify installation
import PyPDF2
import openpyxl
import pandas
print("✅ All dependencies available")
```

### **Issue 3: File Processing Errors**
```python
# Debug file processing
def debug_file_processing(filename):
    from pathlib import Path
    
    file_path = Path(filename)
    print(f"File exists: {file_path.exists()}")
    print(f"File size: {file_path.stat().st_size if file_path.exists() else 'N/A'}")
    print(f"File extension: {file_path.suffix}")
    
    # Try to read file content
    try:
        if file_path.suffix.lower() == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()[:200]  # First 200 chars
                print(f"Content preview: {content}")
    except Exception as e:
        print(f"Error reading file: {e}")

# Use this function to debug any problematic files
# debug_file_processing('your_file.txt')
```

## 📋 **Complete Working Template**

```python
# BoE ETL - Complete Working Colab Template
# ==========================================

# 1. Install package
!pip install boe-etl

# 2. Import working modules
from boe_etl.parsers.pdf_parser import parse_pdf
from boe_etl.parsers.text_parser import parse_text
from boe_etl.parsers.excel_parser import parse_excel
from google.colab import files
import pandas as pd
from pathlib import Path

print("✅ All modules imported successfully!")

# 3. Upload files
uploaded = files.upload()

# 4. Process files
results = []
for filename in uploaded.keys():
    file_ext = filename.lower().split('.')[-1]
    
    try:
        if file_ext == 'pdf':
            file_results = parse_pdf('TestBank', 'Q1_2025', Path(filename))
        elif file_ext == 'txt':
            file_results = parse_text('TestBank', 'Q1_2025', Path(filename))
        elif file_ext in ['xlsx', 'xls']:
            file_results = parse_excel('TestBank', 'Q1_2025', Path(filename))
        else:
            print(f"❌ Unsupported file: {filename}")
            continue
            
        results.extend(file_results)
        print(f"✅ Processed {filename}: {len(file_results)} records")
        
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

# 5. Create DataFrame and export
if results:
    df = pd.DataFrame(results)
    print(f"📊 Total: {len(df)} records")
    
    # Save and download
    df.to_csv('processed_data.csv', index=False)
    files.download('processed_data.csv')
    print("📥 Download complete!")
else:
    print("❌ No data processed")
```

This guide provides multiple working approaches to handle the import issues you encountered in Google Colab! 🚀