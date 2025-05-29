"""
BoE ETL Package
===============

A comprehensive ETL pipeline for financial document processing and NLP analysis.

This package provides tools for:
- Extracting data from PDFs, Excel files, and text documents
- Processing financial documents (earnings calls, reports, presentations)
- Converting unstructured data to structured NLP-ready formats
- Standardized taxonomy and naming conventions
- Web-based frontend for easy document processing

Main Components:
- parsers: Document parsing modules (PDF, Excel, Text, JSON)
- schema: Data transformation and standardization
- nlp: Natural language processing and feature extraction
- frontend: Streamlit-based web interface
- utils: Utility functions and helpers

Example Usage:
    >>> from boe_etl import ETLPipeline
    >>> pipeline = ETLPipeline()
    >>> results = pipeline.process_document('earnings_call.pdf', 'JPMorgan', 'Q1_2025')
    
    >>> from boe_etl.frontend import launch_frontend
    >>> launch_frontend()  # Starts web interface
"""

__version__ = "1.0.0"
__author__ = "Bank of England ETL Team"
__email__ = "etl-team@bankofengland.co.uk"

# Import main classes for easy access
__all__ = ['__version__', '__author__', '__email__']

try:
    from .etl_pipeline import ETLPipeline
    __all__.append('ETLPipeline')
except ImportError:
    pass

try:
    from .schema_transformer import SchemaTransformer
    __all__.append('SchemaTransformer')
except ImportError:
    pass

try:
    from .parsers.pdf_parser import PDFParser
    __all__.append('PDFParser')
except ImportError:
    pass

try:
    from .parsers.excel_parser import ExcelParser
    __all__.append('ExcelParser')
except ImportError:
    pass

try:
    from .parsers.text_parser import TextParser
    __all__.append('TextParser')
except ImportError:
    pass

try:
    from .parsers.json_parser import JSONParser
    __all__.append('JSONParser')
except ImportError:
    pass

try:
    from .nlp import NLPProcessor
    __all__.append('NLPProcessor')
except ImportError:
    pass

# Alternative import for core ETLPipeline if direct import fails
if 'ETLPipeline' not in __all__:
    try:
        from .core import ETLPipeline
        __all__.append('ETLPipeline')
    except ImportError:
        import warnings
        warnings.warn("ETLPipeline could not be imported. Use direct module imports instead.")

# Package metadata
PACKAGE_INFO = {
    'name': 'boe-etl',
    'version': __version__,
    'description': 'A comprehensive ETL pipeline for financial document processing and NLP analysis',
    'author': __author__,
    'email': __email__,
    'url': 'https://github.com/daleparr/boe-etl',
    'license': 'MIT',
    'keywords': ['etl', 'nlp', 'financial', 'banking', 'document-processing'],
}

def get_version():
    """Return the package version."""
    return __version__

def get_info():
    """Return package information."""
    return PACKAGE_INFO.copy()
