import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Data for the tokenomics chart
labels = ['Presale', 'LP Pool', 'Top 50 $NADO Holders Airdrop', 'Early Users Rewards', 'Treasury Vesting (3 months)', 'Liquid Staking Rewards (6 months)']
sizes = [50, 20, 10, 2.5, 10, 7.5]
colors = ['#7C3AED', '#8B5CF6', '#A78BFA', '#C4B5FD', '#DDD6FE', '#F59E0B']

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the pie chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                  startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})

# Customize the appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(12)

# Add a title
plt.title('POST Token Distribution\nTotal Supply: 1 Billion Tokens', 
          fontsize=16, fontweight='bold', pad=20, color='#374151')

# Add a subtitle with vesting details
fig.text(0.5, 0.02, 'Vesting Schedule: Early Users (1 month) • Treasury (3 months) • Liquid Staking (6 months)', 
         ha='center', fontsize=10, style='italic', color='#6B7280')

# Make the chart circular
ax.axis('equal')

# Add a white circle in the center for a donut chart effect
centre_circle = Circle((0,0), 0.40, fc='white', linewidth=2, edgecolor='#E5E7EB')
fig.gca().add_artist(centre_circle)

# Add center text
ax.text(0, 0.1, 'POST', fontsize=24, fontweight='bold', ha='center', va='center', color='#8B5CF6')
ax.text(0, -0.1, 'TOKENOMICS', fontsize=12, fontweight='bold', ha='center', va='center', color='#6B7280')

# Adjust layout and save
plt.tight_layout()
plt.savefig('docs/images/post-tokenomics-distribution.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('docs/images/post-tokenomics-distribution.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Tokenomics chart generated successfully!")
print("Files created:")
print("- docs/images/post-tokenomics-distribution.png")
print("- docs/images/post-tokenomics-distribution.jpg")
