# Google Colab Setup Guide for BoE ETL

Complete guide to using the BoE ETL package in Google Colab notebooks.

## 🚀 **Quick Start in Google Colab**

### **Step 1: Install the Package**
```python
# Install BoE ETL package
!pip install boe-etl

# Install additional dependencies for Colab
!pip install streamlit pyngrok
```

### **Step 2: Import and Initialize**
```python
from boe_etl import ETLPipeline
import pandas as pd

# Initialize the ETL pipeline
pipeline = ETLPipeline()
print("✅ BoE ETL Pipeline initialized successfully!")
```

### **Step 3: Upload Files to Colab**
```python
from google.colab import files
import io

# Upload files using Colab's file upload widget
print("📁 Upload your financial documents (PDF, Excel, Text):")
uploaded = files.upload()

# Get the uploaded filename
filename = list(uploaded.keys())[0]
print(f"📄 Uploaded: {filename}")
```

### **Step 4: Process Documents**
```python
# Process the uploaded document
results = pipeline.process_document(
    filename, 
    institution='JPMorgan',  # Change to your institution
    quarter='Q1_2025'        # Change to your quarter
)

# Convert to DataFrame
df = pipeline.to_dataframe(results)
print(f"✅ Processed {len(df)} records")

# Display first few rows
df.head()
```

## 🌐 **Launch Web Interface in Colab**

### **Method 1: Using ngrok (Recommended)**

```python
# Install ngrok for public URL
!pip install pyngrok

# Set up ngrok (you'll need a free ngrok account)
from pyngrok import ngrok
import threading
import time

# Start the ETL frontend in a separate thread
def start_frontend():
    from boe_etl.frontend import launch_frontend
    launch_frontend(port=8501, host='0.0.0.0')

# Start frontend in background
frontend_thread = threading.Thread(target=start_frontend, daemon=True)
frontend_thread.start()

# Wait for server to start
time.sleep(10)

# Create public tunnel
public_url = ngrok.connect(8501)
print(f"🌐 BoE ETL Web Interface: {public_url}")
print("Click the link above to access your ETL interface!")
```

### **Method 2: Using Colab's Built-in Tunneling**

```python
# For newer Colab versions with built-in tunneling
import subprocess
import threading
import time

def run_streamlit():
    subprocess.run([
        "streamlit", "run", 
        "--server.port", "8501",
        "--server.address", "0.0.0.0",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ])

# Start Streamlit in background
streamlit_thread = threading.Thread(target=run_streamlit, daemon=True)
streamlit_thread.start()

# Wait and then use Colab's tunnel
time.sleep(10)
print("🌐 Use Colab's 'Open in new tab' feature on port 8501")
```

## 📊 **Direct Data Processing (No Web Interface)**

### **Basic ETL Processing**
```python
from boe_etl import ETLPipeline
import pandas as pd

# Initialize pipeline
pipeline = ETLPipeline()

# Upload and process file
from google.colab import files
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Process document
results = pipeline.process_document(filename, 'YourBank', 'Q1_2025')
df = pipeline.to_dataframe(results)

# Display results
print(f"📊 Extracted {len(df)} records")
print(f"📋 Columns: {list(df.columns)}")
df.head(10)
```

### **Batch Processing Multiple Files**
```python
# Upload multiple files
print("📁 Upload multiple documents:")
uploaded = files.upload()

all_results = []

for filename in uploaded.keys():
    print(f"🔄 Processing {filename}...")
    results = pipeline.process_document(filename, 'YourBank', 'Q1_2025')
    all_results.extend(results)

# Combine all results
combined_df = pipeline.to_dataframe(all_results)
print(f"✅ Total records processed: {len(combined_df)}")
combined_df.head()
```

### **Export Results**
```python
# Save to CSV
output_filename = 'processed_financial_data.csv'
combined_df.to_csv(output_filename, index=False)

# Download the processed file
files.download(output_filename)
print(f"📥 Downloaded: {output_filename}")
```

## 🔧 **Advanced Colab Usage**

### **Custom Configuration**
```python
# Create custom configuration
config = {
    'processing': {
        'batch_size': 50,
        'timeout': 300
    },
    'output': {
        'include_metadata': True,
        'timestamp_format': '%Y%m%d_%H%M%S'
    }
}

# Initialize with custom config
pipeline = ETLPipeline(config=config)
```

### **Data Analysis in Colab**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Analyze processed data
print("📈 Data Analysis:")
print(f"Total records: {len(df)}")
print(f"Unique speakers: {df['speaker_norm'].nunique()}")
print(f"Financial content: {df['has_financial_terms'].sum()} records")

# Visualize data
plt.figure(figsize=(10, 6))
df['has_financial_terms'].value_counts().plot(kind='bar')
plt.title('Financial Content Distribution')
plt.show()
```

### **Integration with Google Drive**
```python
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Save results to Drive
drive_path = '/content/drive/MyDrive/BoE_ETL_Results/'
df.to_csv(f'{drive_path}processed_data.csv', index=False)
print("💾 Saved to Google Drive")
```

## 🛠️ **Troubleshooting in Colab**

### **Common Issues & Solutions**

1. **Package Installation Issues**
```python
# Force reinstall if needed
!pip uninstall boe-etl -y
!pip install boe-etl --no-cache-dir
```

2. **Memory Issues with Large Files**
```python
# Process in smaller batches
def process_large_file(filename, chunk_size=100):
    # Implementation for chunked processing
    pass
```

3. **Streamlit Port Issues**
```python
# Try different ports
import socket

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port = find_free_port()
print(f"Using port: {port}")
```

## 📋 **Complete Colab Notebook Template**

```python
# BoE ETL - Complete Colab Setup
# ===============================

# 1. Install packages
!pip install boe-etl pyngrok

# 2. Import libraries
from boe_etl import ETLPipeline
from google.colab import files
import pandas as pd

# 3. Initialize pipeline
pipeline = ETLPipeline()
print("✅ BoE ETL ready!")

# 4. Upload files
print("📁 Upload your financial documents:")
uploaded = files.upload()

# 5. Process documents
results = []
for filename in uploaded.keys():
    print(f"🔄 Processing {filename}...")
    file_results = pipeline.process_document(filename, 'YourBank', 'Q1_2025')
    results.extend(file_results)

# 6. Create DataFrame
df = pipeline.to_dataframe(results)
print(f"✅ Processed {len(df)} records")

# 7. Display results
df.head()

# 8. Export results
df.to_csv('processed_data.csv', index=False)
files.download('processed_data.csv')
print("📥 Download complete!")
```

## 🌐 **Web Interface Access Options**

### **Option 1: ngrok (Most Reliable)**
- Requires free ngrok account
- Provides stable public URL
- Works with any Colab version

### **Option 2: Colab Tunneling**
- Built into newer Colab versions
- No external dependencies
- May have limitations

### **Option 3: Direct Processing**
- No web interface needed
- Programmatic access only
- Best for automated workflows

## 🎯 **Best Practices for Colab**

1. **Always install packages first**
2. **Use file upload widget for documents**
3. **Process data in manageable chunks**
4. **Save results to Google Drive for persistence**
5. **Use ngrok for reliable web interface access**

Your BoE ETL package is now fully compatible with Google Colab! 🚀