"""
Generate realistic EEG sample data
Run: python scripts/generate_eeg.py
"""

import numpy as np
import pandas as pd
import os

def generate_realistic_eeg(duration_seconds=60, sample_rate=256, channels=4):
    """
    Generate realistic-looking EEG data with different brain states
    """
    print("🧠 Generating realistic EEG sample data...")
    
    # Number of samples
    n_samples = duration_seconds * sample_rate
    
    # Create time array
    time = np.linspace(0, duration_seconds, n_samples)
    
    # Generate different brain waves
    # Alpha waves (8-12 Hz) - relaxed
    alpha = 0.5 * np.sin(2 * np.pi * 10 * time) + 0.1 * np.random.randn(n_samples)
    
    # Beta waves (13-30 Hz) - active
    beta = 0.3 * np.sin(2 * np.pi * 20 * time) + 0.1 * np.random.randn(n_samples)
    
    # Theta waves (4-8 Hz) - drowsy
    theta = 0.6 * np.sin(2 * np.pi * 6 * time) + 0.1 * np.random.randn(n_samples)
    
    # Delta waves (0.5-4 Hz) - deep sleep
    delta = 0.8 * np.sin(2 * np.pi * 2 * time) + 0.1 * np.random.randn(n_samples)
    
    # Create channels
    channel_names = ['Fp1', 'Fp2', 'C3', 'C4']
    channels_data = {'time': time}
    
    for i, name in enumerate(channel_names[:channels]):
        # Each channel has different mix of waves
        mix = np.random.rand(4)
        mix = mix / mix.sum()  # Normalize
        channels_data[name] = (
            mix[0] * alpha + 
            mix[1] * beta + 
            mix[2] * theta + 
            mix[3] * delta + 
            0.1 * np.random.randn(n_samples)
        )
    
    # Add eye blinks (frontal channels)
    if 'Fp1' in channels_data:
        blink_idx = np.random.choice(n_samples, size=3, replace=False)
        for idx in blink_idx:
            channels_data['Fp1'][idx:idx+50] += 3.0
            if 'Fp2' in channels_data:
                channels_data['Fp2'][idx:idx+50] += 3.0
    
    # Add a spike
    spike_idx = np.random.choice(n_samples, size=1)[0]
    if 'C3' in channels_data:
        channels_data['C3'][spike_idx:spike_idx+10] += 5.0
    
    # Create DataFrame
    df = pd.DataFrame(channels_data)
    
    # Add state labels
    states = []
    for t in time:
        if t < 20:
            states.append('awake')
        elif t < 35:
            states.append('drowsy')
        elif t < 45:
            states.append('sleep')
        else:
            states.append('awake')
    df['state'] = states
    
    # Save to CSV
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/sample_eeg_data.csv', index=False)
    
    print(f"✅ Generated {duration_seconds} seconds of EEG data")
    print(f"   - {n_samples} samples")
    print(f"   - {channels} channels")
    print(f"   - Saved to: data/sample_eeg_data.csv")
    
    print("\n📊 Data Preview:")
    print(df.head())
    print("\n📈 Statistics:")
    print(df.describe())
    
    return df

if __name__ == "__main__":
    generate_realistic_eeg()