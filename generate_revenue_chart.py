import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Data for the revenue distribution chart
labels = ['$POST Token Holders', 'Team Maintenance']
sizes = [90, 10]
colors = ['#7C3AED', '#F59E0B']  # Purple for holders, orange for team

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create the pie chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                  startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})

# Customize the appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(14)

# Add a title
plt.title('PoP Network Revenue Distribution\nHow Platform Revenue is Allocated', 
          fontsize=16, fontweight='bold', pad=20, color='#374151')

# Add a subtitle with revenue sources
fig.text(0.5, 0.02, 'Revenue Sources: Trading Fees • Advertisements • Verification Badges • Paid Content • Promoted Posts', 
         ha='center', fontsize=10, style='italic', color='#6B7280')

# Make the chart circular
ax.axis('equal')

# Add a white circle in the center for a donut chart effect
centre_circle = Circle((0,0), 0.50, fc='white', linewidth=2, edgecolor='#E5E7EB')
fig.gca().add_artist(centre_circle)

# Add center text
ax.text(0, 0.1, 'REVENUE', fontsize=20, fontweight='bold', ha='center', va='center', color='#7C3AED')
ax.text(0, -0.1, 'SHARING', fontsize=16, fontweight='bold', ha='center', va='center', color='#6B7280')

# Adjust layout and save
plt.tight_layout()

# Save regular version with white background
plt.savefig('docs/images/post-revenue-distribution.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('docs/images/post-revenue-distribution.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# Save transparent version
plt.savefig('docs/images/post-revenue-distribution-transparent.png', dpi=300, bbox_inches='tight', 
            facecolor='none', edgecolor='none', transparent=True)

print("Revenue distribution charts generated successfully!")
print("Files created:")
print("- docs/images/post-revenue-distribution.png (white background)")
print("- docs/images/post-revenue-distribution.jpg (white background)")
print("- docs/images/post-revenue-distribution-transparent.png (transparent)")
