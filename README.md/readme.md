# EEG Data Pipeline

## Project Overview
A complete data engineering pipeline for processing EEG (brain wave) data with:
- **Data Generation** - Synthetic EEG with realistic brain states
- **Anomaly Detection** - Spikes, eye blinks, artifacts
- **Feature Extraction** - Band power analysis (delta, theta, alpha, beta)
- **Real-time Dashboard** - Interactive EEG monitor

## Results
- Processed 60 seconds of 4-channel EEG data
- Detected **317 events** including spikes and eye blinks
- Classified brain states: awake, drowsy, sleep

## Technologies
- Python (pandas, numpy)
- Real-time web dashboard
- CSV/JSON data processing

## How to Run
1. `python scripts/generate_eeg.py` - Generate data
2. `python scripts/eeg_processor.py` - Process data
3. Open `web/neuroscan.html` - View dashboard