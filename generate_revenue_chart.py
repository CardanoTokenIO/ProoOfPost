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

# No title - clean design

# Make the chart circular
ax.axis('equal')

# Add a larger white circle in the center for a thin donut chart effect
centre_circle = Circle((0,0), 0.70, fc='white', linewidth=1, edgecolor='#E5E7EB')
fig.gca().add_artist(centre_circle)

# Add center text
ax.text(0, 0.15, 'REVENUE', fontsize=24, fontweight='bold', ha='center', va='center', color='#7C3AED')
ax.text(0, 0, 'SHARING', fontsize=16, fontweight='bold', ha='center', va='center', color='#6B7280')
ax.text(0, -0.15, '90% / 10%', fontsize=14, fontweight='bold', ha='center', va='center', color='#374151')

# Calculate the center angles for each section
# Purple section (90%) starts at 90 degrees, covers 324 degrees (90% of 360)
purple_center_angle = 90 + (324/2)  # Center of purple section
orange_center_angle = 90 - (36/2)   # Center of orange section (10% = 36 degrees)

# Convert to radians and calculate positions
purple_angle_rad = np.radians(purple_center_angle)
orange_angle_rad = np.radians(orange_center_angle)

# Position labels at 1.3 radius from center, directly above their sections
purple_x = 1.3 * np.cos(purple_angle_rad)
purple_y = 1.3 * np.sin(purple_angle_rad)
orange_x = 1.3 * np.cos(orange_angle_rad)
orange_y = 1.3 * np.sin(orange_angle_rad)

# Add labels positioned correctly over their colors
ax.text(purple_x, purple_y, '$POST Token Holders\n90%', fontsize=14, fontweight='bold', 
        ha='center', va='center', color='#7C3AED', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#7C3AED', linewidth=2))

ax.text(orange_x, orange_y, 'Team Maintenance\n10%', fontsize=14, fontweight='bold', 
        ha='center', va='center', color='#F59E0B',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#F59E0B', linewidth=2))

# Add connecting lines from chart edge to labels
purple_edge_x = 1.0 * np.cos(purple_angle_rad)
purple_edge_y = 1.0 * np.sin(purple_angle_rad)
orange_edge_x = 1.0 * np.cos(orange_angle_rad)
orange_edge_y = 1.0 * np.sin(orange_angle_rad)

ax.annotate('', xy=(purple_edge_x, purple_edge_y), xytext=(purple_x*0.9, purple_y*0.9),
            arrowprops=dict(arrowstyle='-', color='#7C3AED', lw=2))
ax.annotate('', xy=(orange_edge_x, orange_edge_y), xytext=(orange_x*0.9, orange_y*0.9),
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
