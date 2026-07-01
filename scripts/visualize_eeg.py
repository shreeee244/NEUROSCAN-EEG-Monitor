"""
Visualize EEG data and detected events
Run: python scripts/visualize_eeg.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import json
import os

def visualize_eeg():
    # Load data
    df = pd.read_csv('data/sample_eeg_data.csv')
    
    # Load events
    with open('output/eeg_analysis.json', 'r') as f:
        analysis = json.load(f)
    
    # Plot channels
    fig, axes = plt.subplots(4, 1, figsize=(14, 8), sharex=True)
    channels = ['Fp1', 'Fp2', 'C3', 'C4']
    colors = ['#f472b6', '#fbbf24', '#39ff88', '#22d3ee']
    
    for i, (channel, color) in enumerate(zip(channels, colors)):
        axes[i].plot(df['time'], df[channel], color=color, linewidth=0.8, alpha=0.8)
        axes[i].set_ylabel(channel, fontsize=10)
        axes[i].grid(True, alpha=0.3)
        axes[i].set_xlim(0, 60)
        
        # Mark events
        for event in analysis['events']:
            if event.get('channel') == channel:
                axes[i].axvline(x=event['time'], color='red', alpha=0.5, linestyle='--', linewidth=1)
    
    axes[-1].set_xlabel('Time (seconds)', fontsize=12)
    plt.suptitle('EEG Data with Detected Events (Red Lines)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('output/eeg_visualization.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("📊 Visualization saved to: output/eeg_visualization.png")

if __name__ == "__main__":
    visualize_eeg()