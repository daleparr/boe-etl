# BoE ETL Package

A comprehensive ETL pipeline for financial document processing and NLP analysis.

## 🚀 Features

- **Multi-format Document Processing**: PDF, Excel, CSV, Text, and JSON files
- **Financial NLP Analysis**: Automatic extraction of financial terms, figures, and metrics
- **Speaker Identification**: Automatic role detection (CEO, CFO, Analyst, etc.)
- **Topic Classification**: 8+ financial topic categories with confidence scores
- **Data Quality Assurance**: Missing value handling and validation
- **Standardized Schema**: Consistent output format for NLP workflows
- **Web Interface**: User-friendly Streamlit frontend
- **Command Line Tools**: Full CLI support for automation
- **Professional Taxonomy**: Standardized naming conventions

## 📦 Installation

### From PyPI (when published)
```bash
pip install boe-etl
```

### From Source
```bash
git clone https://github.com/daleparr/boe-etl.git
cd boe-etl
pip install -e .
```

### With Optional Dependencies
```bash
# For web frontend
pip install boe-etl[frontend]

# For development
pip install boe-etl[dev]

# All dependencies
pip install boe-etl[all]
```

## 🏃 Quick Start

### Python API

```python
from boe_etl import ETLPipeline

# Initialize pipeline
pipeline = ETLPipeline()

# Process a single document
results = pipeline.process_document(
    'earnings_call.pdf', 
    institution='JPMorgan', 
    quarter='Q1_2025'
)

# Convert to DataFrame
df = pipeline.to_dataframe(results)
print(f"Processed {len(df)} records")

# Save results
pipeline.save_results(results, 'output.csv', format='csv')
```

### Command Line Interface

```bash
# Process a single file
boe-etl process --file earnings_call.pdf --institution JPMorgan --quarter Q1_2025

# Process a directory
boe-etl process --directory ./documents --institution Citigroup --quarter Q2_2025

# Launch web frontend
boe-etl frontend --port 8501

# Validate processed data
boe-etl validate --file processed_data.csv
```

### Web Frontend

```python
from boe_etl.frontend import launch_frontend

# Launch on default port (8501)
launch_frontend()

# Launch on custom port
launch_frontend(port=8080, host='0.0.0.0')
```

## 📊 Output Schema

The ETL pipeline produces standardized records with 25+ fields:

### Core Fields
- `text`: Processed text content
- `speaker_norm`: Normalized speaker role (CEO, CFO, etc.)
- `institution`: Financial institution name
- `quarter`: Reporting quarter (Q1_2025, etc.)
- `source_file`: Original filename

### NLP Features
- `all_financial_terms`: Extracted financial vocabulary
- `financial_figures`: Numerical values and metrics
- `primary_topic`: Main topic classification
- `data_type`: Actual vs Projection classification
- `sentiment_score`: Financial sentiment analysis

### Quality Indicators
- `is_actual_data`: Boolean flag for historical data
- `is_projection_data`: Boolean flag for forward-looking data
- `has_financial_content`: Boolean flag for financial relevance
- `confidence_score`: Processing confidence level

## 🏛️ Supported Institutions

Pre-configured support for major financial institutions:

**US Banks**: JPMorgan Chase, Bank of America, Citigroup, Wells Fargo, Goldman Sachs, Morgan Stanley, U.S. Bancorp, PNC Financial, Truist Financial, Charles Schwab

**European Banks**: HSBC, Barclays, Lloyds Banking Group, NatWest Group, Standard Chartered, Deutsche Bank, BNP Paribas, Credit Suisse, UBS, ING Group, Santander, BBVA, UniCredit, Intesa Sanpaolo, Nordea

## 📁 File Format Support

| Format | Extensions | Description |
|--------|------------|-------------|
| PDF | `.pdf` | Earnings calls, financial reports |
| Excel | `.xlsx`, `.xls` | Spreadsheet data, financial metrics |
| CSV | `.csv` | Tabular data, time series |
| Text | `.txt` | Plain text transcripts |
| JSON | `.json` | Structured data files |

## 🔧 Configuration

### Environment Variables
```bash
export BOE_ETL_CONFIG_PATH=/path/to/config.yaml
export BOE_ETL_LOG_LEVEL=INFO
export BOE_ETL_OUTPUT_DIR=/path/to/outputs
```

### Configuration File
```yaml
# config.yaml
processing:
  batch_size: 100
  max_workers: 4
  timeout: 300

nlp:
  include_sentiment: true
  include_entities: true
  confidence_threshold: 0.7

output:
  format: csv
  include_metadata: true
  timestamp_format: "%Y%m%d_%H%M%S"
```

## 🏷️ Naming Convention

Output files follow the standardized format:
```
{Institution}_{Quarter}_{Year}_PureETL_{User}_{Timestamp}
```

Example: `JPMorgan_Q1_2025_PureETL_JohnSmith_20250526_143022.csv`

## 🧪 Testing

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=boe_etl

# Run specific test
python -m pytest tests/test_pipeline.py
```

## 📚 Documentation

- [API Reference](docs/api.md)
- [Configuration Guide](docs/configuration.md)
- [Development Setup](docs/development.md)
- [Taxonomy Guide](TAXONOMY_GUIDE.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/daleparr/boe-etl/issues)
- **Documentation**: [GitHub Wiki](https://github.com/daleparr/boe-etl/wiki)
- **Email**: etl-team@bankofengland.co.uk

## 🏆 Acknowledgments

- Built for the Bank of England ETL team
- Powered by pandas, PyMuPDF, and Streamlit
- Designed for financial document processing workflows

---

**Version**: 1.0.0  
**Author**: Bank of England ETL Team  
**Repository**: https://github.com/daleparr/boe-etl
