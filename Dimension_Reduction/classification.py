import pandas as pd
from sklearn.cluster import KMeans
from tool import plot_clusters
from algorithm import kmeans
import matplotlib.pyplot as plt


# Load the data
data_path_pca = "/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/pca_data.csv"
data_path_tsne = "/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/tsne_data.csv"
data_path_mds = "/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/mds_data.csv"
data_path_umap = "/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/umap_data.csv"

# Read the data
data_pca = pd.read_csv(data_path_pca)
data_tsne = pd.read_csv(data_path_tsne)
data_mds = pd.read_csv(data_path_mds)
data_umap = pd.read_csv(data_path_umap)

# Perform k-means clustering
n_clusters = 2
labels_pca = kmeans(data_pca, n_clusters=n_clusters)
labels_tsne = kmeans(data_tsne, n_clusters=n_clusters)
labels_mds = kmeans(data_mds, n_clusters=n_clusters)
labels_umap = kmeans(data_umap, n_clusters=n_clusters)

# Save the cluster labels
data_pca['Cluster'] = labels_pca
data_tsne['Cluster'] = labels_tsne
data_mds['Cluster'] = labels_mds
data_umap['Cluster'] = labels_umap

# Plot the clusters
plot_clusters(data_pca, labels_pca, 'PCA Clusters')
plot_clusters(data_tsne, labels_tsne, 't-SNE Clusters')
plot_clusters(data_mds, labels_mds, 'MDS Clusters')
plot_clusters(data_umap, labels_umap, 'UMAP Clusters')


# Save the data
data_pca.to_csv('result/pca_data_cluster.csv', index=False)
data_tsne.to_csv('result/tsne_data_cluster.csv', index=False)
data_mds.to_csv('result/mds_data_cluster.csv', index=False)
data_umap.to_csv('result/umap_data_cluster.csv', index=False)
