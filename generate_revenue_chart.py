import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Data for the revenue distribution chart
labels = ['$POST Token Holders', 'Team Maintenance']
sizes = [90, 10]
colors = ['#7C3AED', '#F59E0B']  # Purple for holders, orange for team

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create the pie chart with no labels initially
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='',
                                  startangle=90, wedgeprops=dict(width=0.3))

# Add a title
plt.title('PoP Network Revenue Distribution', 
          fontsize=18, fontweight='bold', pad=30, color='#374151')

# Make the chart circular
ax.axis('equal')

# Add a larger white circle in the center for a thin donut chart effect
centre_circle = Circle((0,0), 0.70, fc='white', linewidth=1, edgecolor='#E5E7EB')
fig.gca().add_artist(centre_circle)

# Add center text
ax.text(0, 0.15, 'REVENUE', fontsize=24, fontweight='bold', ha='center', va='center', color='#7C3AED')
ax.text(0, 0, 'SHARING', fontsize=16, fontweight='bold', ha='center', va='center', color='#6B7280')
ax.text(0, -0.15, '90% / 10%', fontsize=14, fontweight='bold', ha='center', va='center', color='#374151')

# Add clean external labels
ax.text(0.6, 0.3, '$POST Token Holders\n90%', fontsize=14, fontweight='bold', 
        ha='center', va='center', color='#7C3AED', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#7C3AED', linewidth=2))

ax.text(-0.6, -0.3, 'Team Maintenance\n10%', fontsize=14, fontweight='bold', 
        ha='center', va='center', color='#F59E0B',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#F59E0B', linewidth=2))

# Add connecting lines
ax.annotate('', xy=(0.35, 0.15), xytext=(0.5, 0.25),
            arrowprops=dict(arrowstyle='-', color='#7C3AED', lw=2))
ax.annotate('', xy=(-0.35, -0.15), xytext=(-0.5, -0.25),
            arrowprops=dict(arrowstyle='-', color='#F59E0B', lw=2))

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
