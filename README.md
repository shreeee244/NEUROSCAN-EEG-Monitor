# 🧠 NEUROSCAN · EEG Data Pipeline

> **End-to-end data pipeline for brain signal processing with anomaly detection and real-time visualization.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

---

## 📊 Results

| Metric | Value |
|--------|-------|
| Channels | 4 (Fp1, Fp2, C3, C4) |
| Samples | 15,360 |
| Anomalies Detected | 317 |
| Processing Time | < 2 sec |

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/shreeee244/NEUROSCAN-EEG-Monitor.git
cd NEUROSCAN-EEG-Monitor

# Install
pip install pandas numpy matplotlib openpyxl

# Run pipeline
python scripts/generate_eeg.py      # Generate data
python scripts/eeg_processor.py     # Process & detect anomalies

# Open dashboard
# Double-click web/neuroscan.html
```

---

## 📁 Project Structure

```
NEUROSCAN-EEG-Monitor/
├── data/
│   └── sample_eeg_data.csv          # Generated EEG data
├── scripts/
│   ├── generate_eeg.py              # Data generator
│   └── eeg_processor.py             # ETL & anomaly detection
├── web/
│   └── neuroscan.html               # Real-time dashboard
├── output/
│   ├── eeg_analysis.json            # Full results
│   └── eeg_analysis.csv             # Summary stats
└── README.md
```

---

## 🔍 Features

### Data Processing
- **Generates** realistic 4-channel EEG data
- **Detects** spikes, eye blinks, and artifacts
- **Extracts** band power (δ, θ, α, β)
- **Classifies** brain states (awake, drowsy, sleep)

### Dashboard
- Live channel display with sweep cursor
- Event logging with timestamps
- FREEZE / SILENCE controls
- CSV/JSON file loading

---

## 🛠️ Technologies

| Category | Technologies |
|----------|--------------|
| Data Processing | Python, Pandas, NumPy |
| Visualization | Matplotlib |
| Dashboard | HTML5, Canvas, Vanilla JS |
| Formats | CSV, JSON |

---

## 📬 Connect

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/shreeee244)

---

**⭐ Star this repo if you found it useful!**
