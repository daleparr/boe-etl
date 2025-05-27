import unittest
import os
from pathlib import Path
import tempfile
import sqlite3
from datetime import datetime
from unittest.mock import patch, MagicMock

from fetch_and_parse import (
    validate_bank_name,
    validate_quarter,
    register_call,
    fetch_assets,
    parse_pdf,
    parse_html,
    parse_vtt,
    clean_and_split,
    write_parquet,
    process_call
)

class TestETLFunctions(unittest.TestCase):
    def setUp(self):
        # Create temporary directory for tests
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_db = Path(self.temp_dir.name) / "test.db"
        
        # Initialize test database
        conn = sqlite3.connect(self.test_db)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS calls (
                call_id TEXT PRIMARY KEY,
                bank_name TEXT NOT NULL,
                quarter TEXT NOT NULL,
                source_url TEXT,
                source_type TEXT,
                processed_at TIMESTAMP,
                status TEXT,
                error_message TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_validate_bank_name(self):
        """Test bank name validation"""
        self.assertTrue(validate_bank_name("bank1"))
        self.assertTrue(validate_bank_name("Bank Name"))
        
        with self.assertRaises(ValueError):
            validate_bank_name("")
            validate_bank_name(None)
            validate_bank_name(123)

    def test_validate_quarter(self):
        """Test quarter format validation"""
        self.assertTrue(validate_quarter("Q1_2023"))
        self.assertTrue(validate_quarter("Q4_2022"))
        
        with self.assertRaises(ValueError):
            validate_quarter("Q12023")
            validate_quarter("2023_Q1")
            validate_quarter("Q0_2023")

    @patch('fetch_and_parse.requests.get')
    def test_fetch_asset(self, mock_get):
        """Test asset fetching"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"test content"
        mock_get.return_value = mock_response
        
        test_url = "https://example.com/test.pdf"
        test_path = Path(self.temp_dir.name) / "test.pdf"
        
        fetch_asset(test_url, test_path)
        self.assertTrue(test_path.exists())

    def test_parse_pdf(self):
        """Test PDF parsing"""
        # Create test PDF with sample content
        test_pdf = Path(self.temp_dir.name) / "test.pdf"
        with open(test_pdf, 'wb') as f:
            f.write(b"CEO: This is a test PDF\n\nAnalyst: Another test")
        
        records = parse_pdf(test_pdf)
        self.assertGreater(len(records), 0)
        self.assertIn("speaker", records[0])
        self.assertIn("text", records[0])

    def test_parse_html(self):
        """Test HTML parsing"""
        # Create test HTML with sample content
        test_html = Path(self.temp_dir.name) / "test.html"
        with open(test_html, 'w', encoding='utf-8') as f:
            f.write("""
                <div class="speaker-block">
                    <span class="speaker-name">CEO</span>
                    <span class="timestamp">2023-05-23T10:00:00</span>
                    <div class="content">This is a test HTML</div>
                </div>
            """)
        
        records = parse_html(test_html)
        self.assertGreater(len(records), 0)
        self.assertIn("speaker", records[0])
        self.assertIn("text", records[0])

    def test_parse_vtt(self):
        """Test VTT parsing"""
        # Create test VTT with sample content
        test_vtt = Path(self.temp_dir.name) / "test.vtt"
        with open(test_vtt, 'w', encoding='utf-8') as f:
            f.write("""
                00:00:00.000 --> 00:00:10.000
                This is a test VTT
            """)
        
        records = parse_vtt(test_vtt)
        self.assertGreater(len(records), 0)
        self.assertIn("speaker", records[0])
        self.assertIn("text", records[0])

    def test_clean_and_split(self):
        """Test text cleaning and splitting"""
        test_records = [{
            'speaker': 'CEO',
            'timestamp': '2023-05-23T10:00:00',
            'text': 'This is a test. Another sentence.'
        }]
        
        cleaned = clean_and_split(test_records)
        self.assertGreater(len(cleaned), 0)
        self.assertIn('sentence_id', cleaned[0])
        self.assertIn('text', cleaned[0])

    def test_register_call(self):
        """Test call registration in database"""
        call_id = "test_call"
        bank = "test_bank"
        quarter = "Q1_2023"
        source_url = "test_url"
        source_type = "PDF"
        
        register_call(
            call_id,
            bank,
            quarter,
            source_url,
            source_type
        )
        
        # Verify record in database
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calls WHERE call_id = ?", (call_id,))
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        conn.close()

if __name__ == '__main__':
    unittest.main()
