# 🧠 NEUROSCAN · EEG Data Pipeline

> **End-to-end data pipeline for brain signal processing with anomaly detection and real-time visualization.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

## 🧪 Testing

```bash
# Validate data format
python -c "import pandas as pd; df=pd.read_csv('data/sample_eeg_data.csv'); print('✅', df.shape)"

# Check processing
python scripts/eeg_processor.py

# Run full test suite
python -c "import subprocess; subprocess.run(['python', 'scripts/eeg_processor.py'])"
```

**Expected Output:**
```
🔬 Loaded 15360 samples from 4 channels
✅ Processing complete! - 317 events detected
```

---

## 📊 Visualizations

```bash
# Generate all visualizations
python scripts/run_all_visualizations.py
```

| Output | Description |
|--------|-------------|
| `channel_visualization.png` | 4-channel EEG with marked events |
| `state_visualization.png` | Band power & state distribution |
| `anomaly_heatmap.png` | Time-based anomaly heatmap |

---

## 🛠️ Technologies

| Category | Technologies |
|----------|--------------|
| Data Processing | Python, Pandas, NumPy |
| Visualization | Matplotlib |
| Dashboard | HTML5, Canvas, Vanilla JS |
| Formats | CSV, JSON |

---

## 🎓 Key Skills Demonstrated

- ✅ Complete ETL pipeline (generate → process → export)
- ✅ Anomaly detection in time-series data
- ✅ Real-time data visualization
- ✅ Structured Python project with documentation

---

## 🗓️ Next Steps

- [ ] Connect to real EEG hardware (Muse/OpenBCI)
- [ ] Deploy dashboard to GitHub Pages
- [ ] Add ML for sleep stage classification

---

## 📬 Connect

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/shreeee244)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/yourprofile)

---

**⭐ Star this repo if you found it useful!**