# 🔧 Pure Financial Document ETL Pipeline

A **data engineering focused** ETL pipeline that extracts from unstructured financial document data (pdf, spreadsheet, doc) without making analytical assumptions or classifications.

## 🎯 **Pure ETL Philosophy**

This pipeline follows **separation of concerns** principles:

- **ETL Layer**: Extract → Structure → Export (no analysis)

## 🚀 **Quick Start**

### **Installation**
```bash
pip install streamlit pandas PyPDF2 openpyxl
```

### **Launch Web Interface**
```bash
streamlit run pure_etl_frontend.py
```

### **Access Application**
Open your browser to: `http://localhost:8502`

## 📊 **What This ETL Does**

### **✅ Raw Data Extraction**
- **PDF Documents**: Text extraction from earnings reports
- **Excel Files**: Multi-sheet data extraction
- **Text Files**: Direct text processing
- **Sentence Segmentation**: Clean, structured sentences

### **✅ Raw Feature Extraction**
- **`all_financial_terms`**: Financial vocabulary found (no classification)
- **`financial_figures`**: Numbers and amounts extracted (no interpretation)
- **`temporal_indicators`**: Time-related language (no actual/projection labels)
- **`speaker_raw`**: Speaker patterns identified (no role classification)

### **✅ Factual Boolean Flags**
- **`has_financial_terms`**: Terms present or not
- **`has_financial_figures`**: Figures present or not
- **`has_temporal_language`**: Temporal words present or not
- **`has_speaker_identified`**: Speaker pattern found or not

## 🚫 **What This ETL Does NOT Do**

### **❌ No Analytical Assumptions**
- No topic classification (Revenue & Growth, Risk Management, etc.)
- No actual vs projection classification
- No financial content relevance scoring
- No speaker role interpretation (CEO, CFO, Analyst)

### **❌ No Machine Learning**
- No topic modeling
- No sentiment analysis
- No content classification
- No predictive features

## 📈 **Output Schema**

### **Core Fields**
```csv
source_file,institution,quarter,sentence_id,speaker_raw,text,source_type
```

### **Raw Extraction Fields**
```csv
all_financial_terms,financial_figures,financial_figures_text,temporal_indicators
```

### **Factual Flags**
```csv
has_financial_terms,has_financial_figures,has_temporal_language,has_speaker_identified
```

### **Metadata**
```csv
word_count,char_count,processing_date,extraction_timestamp
```

## 🔄 **Example Processing**

### **Input Document**
```
"We reported revenue of $2.5 billion this quarter, up 15% from last year."
```

### **Pure ETL Output**
```csv
all_financial_terms: "revenue"
financial_figures: "$2.5 billion|15%"
temporal_indicators: "reported|this quarter|last year"
has_financial_terms: True
has_financial_figures: True
has_temporal_language: True
```

### **No Analysis Applied**
- ❌ No classification as "actual" vs "projection"
- ❌ No topic assignment like "Revenue & Growth"
- ❌ No sentiment or relevance scoring

## 🏗️ **Architecture**

### **Pure ETL Pipeline**
```
Documents → Extract Text → Segment Sentences → Extract Raw Features → Export CSV
```

### **Downstream Analysis (Separate)**
```
Raw CSV → Topic Modeling → Classification → Feature Engineering → ML Models
```

## 🛠️ **Technical Features**

### **✅ Missing Value Handling**
- No null values in output
- Consistent defaults for all fields
- NLP-ready datasets

### **✅ Multi-Format Support**
- PDF processing with PyPDF2
- Excel processing with openpyxl
- Text file processing
- Graceful error handling

### **✅ Web Interface**
- Drag-and-drop file upload
- Multi-institution processing
- Progress tracking
- Processing history
- CSV download

## 📚 **Use Cases**

### **Financial Institutions**
- Earnings call transcript processing
- Financial report data extraction
- Regulatory document structuring
- Multi-quarter analysis preparation

### **Research & Analytics**
- Academic financial research
- Market analysis preparation
- NLP model training data
- Time series analysis datasets

### **Compliance & Audit**
- Document processing audit trails
- Structured data for compliance
- Historical document analysis
- Regulatory reporting preparation

## 🔧 **Development**

### **Project Structure**
```
boe-etl/
├── pure_etl_frontend.py    # Main Streamlit application
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore patterns
└── LICENSE                # MIT License
```

### **Dependencies**
- **streamlit**: Web interface framework
- **pandas**: Data manipulation
- **PyPDF2**: PDF text extraction
- **openpyxl**: Excel file processing

## 📄 **License**

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 **Contributing**

This is a pure ETL pipeline focused on data engineering principles. Contributions should maintain the separation between extraction and analysis.

### **Guidelines**
- Keep ETL layer free of analytical assumptions
- Maintain raw data extraction focus
- Preserve downstream analysis flexibility
- Follow data engineering best practices

## 🎯 **Philosophy: Extract, Don't Analyze**

This pipeline embodies the principle that **ETL should extract and structure data, not make analytical decisions**. Analysis belongs in separate, specialized pipelines that can evolve independently.

**Pure ETL = Maximum Flexibility for Downstream Analysis** 🔧
