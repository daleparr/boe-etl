"""
Utilities for extracting and normalizing quarter information from filenames.
"""
import re
import yaml
import logging
from pathlib import Path
from typing import Dict, List, Optional, Pattern

# Configure logger
logger = logging.getLogger(__name__)

# Load quarter patterns from YAML config
QUARTER_PATTERNS: Dict[str, List[Pattern]] = {}

def load_quarter_patterns(config_path: Optional[Path] = None) -> None:
    """
    Load quarter patterns from YAML configuration file.
    
    Args:
        config_path: Path to the YAML configuration file. If None, uses default location.
    """
    global QUARTER_PATTERNS
    
    if config_path is None:
        config_path = Path(__file__).parent.parent / 'config' / 'quarter_patterns.yml'
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)
            
        QUARTER_PATTERNS.clear()
        for item in cfg.get('quarter_patterns', []):
            QUARTER_PATTERNS[item['name']] = [
                re.compile(pattern) for pattern in item['patterns']
            ]
            
    except Exception as e:
        logger.error(f"Failed to load quarter patterns: {e}")
        raise

def normalize_quarter(filename: str) -> Optional[str]:
    """
    Extract and normalize quarter information from a filename.
    
    Args:
        filename: The input filename to extract quarter from
        
    Returns:
        str: The normalized quarter string (e.g., 'Q1_2025') or None if no match found
    """
    if not QUARTER_PATTERNS:
        load_quarter_patterns()
    
    filename = str(filename).lower()
    
    for quarter, patterns in QUARTER_PATTERNS.items():
        for pattern in patterns:
            if pattern.search(filename):
                return quarter
    
    return None

def process_file_path(file_path: Path, base_dir: Path) -> Optional[Path]:
    """
    Process a file path and return the target path with quarter information.
    
    Args:
        file_path: The source file path
        base_dir: The base directory for output files
        
    Returns:
        Path: The target file path with quarter information, or None if quarter cannot be determined
    """
    quarter = normalize_quarter(file_path.name)
    if not quarter:
        logger.warning(f"Could not determine quarter for file: {file_path.name}")
        return None
    
    # Create target directory structure: base_dir/quarter=Q1_2025/filename
    target_dir = base_dir / f"quarter={quarter}"
    target_dir.mkdir(parents=True, exist_ok=True)
    
    return target_dir / file_path.name

# Load patterns when module is imported
load_quarter_patterns()
