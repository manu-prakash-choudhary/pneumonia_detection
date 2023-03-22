import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
category1 = ['Covid-19']*3700 + ['Normal']*1200
# print(category1)

# Create countplot
sns.countplot(x=category1)

# Add labels and title
plt.xlabel("X-Rays of Two Categories")
plt.ylabel("Count")
plt.title("Countplot of Pneumonia and Normal X-Rays")

# Show plot
plt.show()