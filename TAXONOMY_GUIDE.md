# 📋 Standard Taxonomy & File Naming Guide

## 🎯 **Purpose**
This guide ensures consistent data organization and makes it easy to track who uploaded what, when, and for which institution/quarter.

## 📁 **Recommended File Naming Convention**

### **Format:**
```
[Institution]_[Quarter]_[Year]_[DocumentType]_[UploadedBy]_[Date].[extension]
```

### **Examples:**
```
JPMorgan_Q1_2025_EarningsCall_JohnSmith_20250526.pdf
Citigroup_Q2_2024_Presentation_SarahJones_20250526.pdf
BankOfAmerica_Q3_2025_FinancialSupplement_MikeWilson_20250526.xlsx
WellsFargo_Q4_2024_PressRelease_EmilyBrown_20250526.txt
```

## 🏛️ **Institution Names (Standardized)**

### **Major US Banks:**
- `JPMorgan` (JPMorgan Chase & Co.)
- `BankOfAmerica` (Bank of America Corporation)
- `Citigroup` (Citigroup Inc.)
- `WellsFargo` (Wells Fargo & Company)
- `GoldmanSachs` (The Goldman Sachs Group, Inc.)
- `MorganStanley` (Morgan Stanley)
- `USBancorp` (U.S. Bancorp)
- `TrustFinancial` (Truist Financial Corporation)
- `PNCFinancial` (PNC Financial Services Group)
- `CapitalOne` (Capital One Financial Corporation)

### **Major European Banks:**
- `HSBC` (HSBC Holdings plc)
- `Barclays` (Barclays PLC)
- `Lloyds` (Lloyds Banking Group plc)
- `RoyalBankScotland` (NatWest Group plc)
- `StandardChartered` (Standard Chartered PLC)
- `Deutsche` (Deutsche Bank AG)
- `UBS` (UBS Group AG)
- `CreditSuisse` (Credit Suisse Group AG)
- `BNPParibas` (BNP Paribas)
- `SocGen` (Société Générale)

### **Other Institutions:**
- Use CamelCase format: `FirstSecond` (no spaces, no special characters)

## 📅 **Quarter & Year Format**

### **Quarters:**
- `Q1` (January - March)
- `Q2` (April - June)  
- `Q3` (July - September)
- `Q4` (October - December)

### **Years:**
- `2024`, `2025`, `2026`, etc.

## 📄 **Document Types (Standardized)**

### **Primary Document Types:**
- `EarningsCall` - Earnings call transcripts
- `Presentation` - Earnings presentations/slide decks
- `FinancialSupplement` - Financial data supplements
- `PressRelease` - Press releases and announcements
- `QuarterlyReport` - 10-Q quarterly reports
- `AnnualReport` - 10-K annual reports
- `ProxyStatement` - DEF 14A proxy statements

### **Secondary Document Types:**
- `Transcript` - General transcripts
- `FactSheet` - Fact sheets and summaries
- `Guidance` - Forward guidance documents
- `RiskDisclosure` - Risk management disclosures
- `RegulatoryFiling` - Other regulatory filings

## 👤 **User Identification**

### **Format:**
- `FirstnameLastname` (CamelCase, no spaces)
- Examples: `JohnSmith`, `SarahJones`, `MikeWilson`

### **Team Codes (Alternative):**
- `Analyst1`, `Analyst2`, `Researcher1`, etc.
- `TeamLead`, `SeniorAnalyst`, `JuniorAnalyst`

## 📊 **ETL Interface Fields**

### **Required Fields in Tool:**
1. **Institution Name** - Select from dropdown or enter standardized name
2. **Quarter** - Select: Q1, Q2, Q3, Q4
3. **Year** - Select: 2024, 2025, 2026
4. **Uploaded By** - Enter your name/ID
5. **Document Type** - Auto-detected or manual override

### **Example Interface:**
```
Institution: [JPMorgan ▼]
Quarter: [Q1 ▼] Year: [2025 ▼]
Uploaded By: [JohnSmith]
Files: [Drag & Drop Area]
```

## 🗂️ **Output File Organization**

### **Generated CSV Files:**
```
JPMorgan_Q1_2025_PureETL_JohnSmith_20250526.csv
Citigroup_Q2_2024_PureETL_SarahJones_20250526.csv
```

### **Processing History:**
```json
{
  "timestamp": "2025-05-26T16:30:00",
  "institution": "JPMorgan",
  "quarter": "Q1",
  "year": "2025",
  "uploaded_by": "JohnSmith",
  "document_types": ["EarningsCall", "Presentation"],
  "files_processed": 2,
  "records_generated": 1247
}
```

## 📋 **Quality Control Checklist**

### **Before Upload:**
- [ ] File named according to convention
- [ ] Institution name standardized
- [ ] Quarter/year correct
- [ ] Document type identified
- [ ] Your name/ID included

### **After Processing:**
- [ ] Check document type detection accuracy
- [ ] Verify institution/quarter in output
- [ ] Confirm record count reasonable
- [ ] Download and spot-check CSV data

## 🔍 **Search & Filter Examples**

### **Find All JPMorgan Q1 2025 Data:**
- Filter: `institution = "JPMorgan" AND quarter = "Q1" AND year = "2025"`

### **Find All Earnings Calls:**
- Filter: `source_type = "earnings_call"`

### **Find All John Smith Uploads:**
- Filter: `uploaded_by = "JohnSmith"`

### **Find Recent Uploads:**
- Filter: `processing_date >= "2025-05-26"`

## 📈 **Benefits of This Taxonomy**

### **✅ Data Organization:**
- Consistent naming across team
- Easy to find specific documents
- Clear audit trail of who uploaded what

### **✅ Analysis Efficiency:**
- Filter by institution, quarter, year
- Compare across time periods
- Track document type patterns

### **✅ Team Collaboration:**
- Know who processed which data
- Avoid duplicate work
- Share processing responsibilities

### **✅ Quality Assurance:**
- Standardized metadata
- Consistent data structure
- Easy error tracking

## 🚀 **Implementation**

### **Step 1: Team Training**
- Share this guide with all team members
- Practice with sample files
- Establish naming conventions

### **Step 2: Tool Enhancement**
- Add dropdown menus for institutions
- Include user identification field
- Auto-generate standardized output names

### **Step 3: Quality Monitoring**
- Regular review of uploaded files
- Check naming convention compliance
- Monitor data quality metrics

---

**📋 Consistent taxonomy = Better data = Faster analysis!** 🎯