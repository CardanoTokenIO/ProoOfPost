#!/usr/bin/env python3
"""
Generate presale visualization graphs for $POST token documentation
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Set style for professional looking graphs
plt.style.use('default')
sns.set_palette("husl")

# Presale data from the HTML page
TIER_DATA = [
    {"name": "Tier 0\n(Allowlist)", "rate": 3600, "ada_cap": 3000, "color": "#10B981"},
    {"name": "Tier 1", "rate": 3200, "ada_cap": 7000, "color": "#3B82F6"},
    {"name": "Tier 2", "rate": 3000, "ada_cap": 10000, "color": "#8B5CF6"},
    {"name": "Tier 3", "rate": 2800, "ada_cap": 42000, "color": "#F59E0B"},
    {"name": "Tier 4\n(Final)", "rate": 2400, "ada_cap": 133000, "color": "#EF4444"}
]

LAUNCH_RATE = 2300
TOTAL_SUPPLY = 1_000_000_000
PRESALE_ALLOCATION = 500_000_000

def create_tier_structure_graph():
    """Create tier structure visualization"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Left plot: Token rates per tier
    tiers = [t["name"] for t in TIER_DATA]
    rates = [t["rate"] for t in TIER_DATA]
    colors = [t["color"] for t in TIER_DATA]
    
    bars1 = ax1.bar(tiers, rates, color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    ax1.axhline(y=LAUNCH_RATE, color='red', linestyle='--', linewidth=2, label=f'Launch Rate ({LAUNCH_RATE} tokens/ADA)')
    ax1.set_title('Token Allocation Rates by Tier', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Tokens per ADA', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Presale Tiers', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, rate in zip(bars1, rates):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 50,
                f'{rate:,}', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # Right plot: ADA capacity per tier
    ada_caps = [t["ada_cap"] for t in TIER_DATA]
    bars2 = ax2.bar(tiers, ada_caps, color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    ax2.set_title('ADA Capacity by Tier', fontsize=16, fontweight='bold', pad=20)
    ax2.set_ylabel('ADA Capacity', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Presale Tiers', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, cap in zip(bars2, ada_caps):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 2000,
                f'{cap:,}', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('images/presale-tier-structure.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_profit_potential_graph():
    """Create profit potential visualization"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    tiers = [t["name"] for t in TIER_DATA]
    rates = [t["rate"] for t in TIER_DATA]
    colors = [t["color"] for t in TIER_DATA]
    
    # Calculate profit percentages
    profit_percentages = [((rate - LAUNCH_RATE) / LAUNCH_RATE) * 100 for rate in rates]
    
    bars = ax.bar(tiers, profit_percentages, color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.set_title('Profit Potential at Launch vs Presale Tiers', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Profit Percentage (%)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Presale Tiers', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, profit in zip(bars, profit_percentages):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'+{profit:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Add launch rate reference
    ax.text(0.02, 0.98, f'Launch Rate: {LAUNCH_RATE:,} tokens/ADA', 
            transform=ax.transAxes, fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('images/presale-profit-potential.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_token_distribution_graph():
    """Create token distribution pie chart"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Token distribution data
    distribution = {
        'Presale (50%)': 500_000_000,
        'Liquidity Pool (20%)': 200_000_000,
        'Team & Development (25%)': 250_000_000,
        'CEX Listings (5%)': 50_000_000
    }
    
    colors = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444']
    
    wedges, texts, autotexts = ax.pie(distribution.values(), labels=distribution.keys(), 
                                     colors=colors, autopct='%1.1f%%', startangle=90,
                                     textprops={'fontsize': 12, 'fontweight': 'bold'},
                                     wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    
    # Enhance the percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    
    ax.set_title('$POST Token Distribution', fontsize=18, fontweight='bold', pad=30)
    
    # Add total supply info
    ax.text(0.5, -1.3, f'Total Supply: {TOTAL_SUPPLY:,} $POST tokens', 
            transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('images/presale-token-distribution.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_cumulative_progress_graph():
    """Create cumulative funding progress visualization"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Calculate cumulative ADA caps
    cumulative_ada = []
    cumulative_tokens = []
    tier_names = []
    current_ada = 0
    current_tokens = 0
    
    for tier in TIER_DATA:
        current_ada += tier["ada_cap"]
        current_tokens += tier["ada_cap"] * tier["rate"]
        cumulative_ada.append(current_ada)
        cumulative_tokens.append(current_tokens / 1_000_000)  # Convert to millions
        tier_names.append(tier["name"])
    
    # Create the step plot
    x_positions = range(len(TIER_DATA))
    colors = [t["color"] for t in TIER_DATA]
    
    # Bar chart for cumulative ADA
    bars = ax.bar(x_positions, cumulative_ada, color=colors, alpha=0.7, 
                  edgecolor='white', linewidth=2, label='Cumulative ADA Raised')
    
    # Add soft cap and hard cap lines
    soft_cap = 20000
    hard_cap = 195000
    ax.axhline(y=soft_cap, color='orange', linestyle='--', linewidth=2, 
               label=f'Soft Cap ({soft_cap:,} ADA)')
    ax.axhline(y=hard_cap, color='red', linestyle='--', linewidth=2, 
               label=f'Hard Cap ({hard_cap:,} ADA)')
    
    ax.set_title('Cumulative Funding Progress by Tier', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Cumulative ADA Raised', fontsize=12, fontweight='bold')
    ax.set_xlabel('Tier Completion', fontsize=12, fontweight='bold')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(tier_names)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for i, (bar, ada, tokens) in enumerate(zip(bars, cumulative_ada, cumulative_tokens)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 3000,
                f'{ada:,} ADA\n{tokens:.0f}M tokens', ha='center', va='bottom', 
                fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('images/presale-cumulative-progress.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_timeline_graph():
    """Create presale timeline visualization"""
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Timeline data
    timeline_events = [
        {"date": "Sep 27, 2025", "event": "Presale Starts", "color": "#10B981"},
        {"date": "Oct 3, 2025", "event": "Presale Ends", "color": "#EF4444"},
        {"date": "TGE", "event": "Token Launch\n(2,300 tokens/ADA)", "color": "#8B5CF6"}
    ]
    
    # Create timeline
    y_pos = 0.5
    for i, event in enumerate(timeline_events):
        x_pos = i * 2
        
        # Draw event circle
        circle = plt.Circle((x_pos, y_pos), 0.15, color=event["color"], alpha=0.8)
        ax.add_patch(circle)
        
        # Add event text
        ax.text(x_pos, y_pos + 0.4, event["date"], ha='center', va='bottom', 
                fontsize=12, fontweight='bold')
        ax.text(x_pos, y_pos - 0.4, event["event"], ha='center', va='top', 
                fontsize=10, fontweight='bold')
        
        # Draw connecting line (except for last event)
        if i < len(timeline_events) - 1:
            ax.plot([x_pos + 0.15, (i+1) * 2 - 0.15], [y_pos, y_pos], 
                   color='gray', linewidth=3, alpha=0.6)
    
    ax.set_xlim(-0.5, (len(timeline_events) - 1) * 2 + 0.5)
    ax.set_ylim(0, 1)
    ax.set_title('$POST Presale Timeline', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Add duration info
    ax.text(2, 0.1, 'Duration: 7 Days', ha='center', va='center', 
            fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('images/presale-timeline.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def main():
    """Generate all presale graphs"""
    print("Generating presale visualization graphs...")
    
    # Create images directory if it doesn't exist
    import os
    os.makedirs('images', exist_ok=True)
    
    # Generate all graphs
    create_tier_structure_graph()
    print("✓ Generated tier structure graph")
    
    create_profit_potential_graph()
    print("✓ Generated profit potential graph")
    
    create_token_distribution_graph()
    print("✓ Generated token distribution graph")
    
    create_cumulative_progress_graph()
    print("✓ Generated cumulative progress graph")
    
    create_timeline_graph()
    print("✓ Generated timeline graph")
    
    print("\nAll presale graphs generated successfully!")
    print("Files saved in images/ directory:")
    print("- presale-tier-structure.png")
    print("- presale-profit-potential.png")
    print("- presale-token-distribution.png")
    print("- presale-cumulative-progress.png")
    print("- presale-timeline.png")

if __name__ == "__main__":
    main()
