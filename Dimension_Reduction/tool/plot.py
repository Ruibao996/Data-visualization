import matplotlib.pyplot as plt

def plot_clusters(data, labels, title):
    plt.scatter(data.iloc[:, 1], data.iloc[:, 2], c=labels, cmap='viridis')
    plt.title(title)
    plt.savefig('/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/tool/result/' + title + '.png')  # Save the plot
    plt.show()