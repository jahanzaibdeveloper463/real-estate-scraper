# 🏢Real-estate-scraper

> An automated data extraction engine architected to parse real estate listings, normalize property attributes, and serialize structured records directly into clean Excel workbooks (`.xlsx`). Built for lead-generation agencies and automated real-estate market research.

---

## 🏗️ Pipeline Architecture
## 🧰 Technical Stack

- **Core Runtime:** Python 3.10+
- **HTTP Transport:** `requests` (with exception handling & timeouts)
- **DOM Parsing:** `BeautifulSoup4` (HTML tree mapping)
- **Data Manipulation:** `pandas` (DataFrame memory mapping)
- **Spreadsheet Engine:** `openpyxl` (Office Open XML writer)

---

## ⚡ Engineering Highlights

1. **🛡️ Defensive Pipeline Execution:** Implements strict network timeout handlers and HTTP status verification to ensure fault tolerance.
2. **🧹 Data Normalization Layer:** Cleans raw DOM text strings, maps numerical values into typed primitives (`int`/`float`), and flattens nested tag lists into comma-separated strings.
3. **⚡ Stateless Memory Buffering:** Compiles dictionaries directly into in-memory dataframes, optimizing disk I/O performance before final serialization.

---

## ⚙️ Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/real-estate-scraper.git](https://github.com/your-username/real-estate-scraper.git)
   cd real-estate-scraper
Initialize virtual environment:
