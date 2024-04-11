from algorithm import pca, tsne, mds, umap_func
from tool import data_prep, change
import pandas as pd

# Load the data
datapath = "/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/data/EssayAnalysis.csv"

# Define the numerical and categorical features
num_features = ['Number of Essays', 'True', 'False', 'Blank', 'Net', 'ExamDuration']
cat_features = ['EssayPublication']
date_feature = 'Date'
data_prepared = data_prep(datapath, num_features, cat_features, date_feature)

# Prepare the data
data = data_prep(datapath, num_features, cat_features, date_feature)

# # Print data
# print(data)

# Perform PCA
pca_data = pca(data, n_components=2)

# Perform t-SNE
tsne_data = tsne(data, n_components=2, perplexity=5, learning_rate=200)

# Perform MDS
mds_data = mds(data, n_components=2, metric=True)

# Perform UMAP
umap_data = umap_func(data, n_components=2, n_neighbors=15, min_dist=0.1)

# Convert the numpy arrays to pandas DataFrames
pca_data_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
tsne_data_df = pd.DataFrame(tsne_data, columns=['TSNE1', 'TSNE2'])
mds_data_df = pd.DataFrame(mds_data, columns=['MDS1', 'MDS2'])
umap_data_df = pd.DataFrame(umap_data, columns=['UMAP1', 'UMAP2'])

# Save the DataFrames to CSV files
pca_data_df.to_csv('result/pca_data.csv', index=True)
tsne_data_df.to_csv('esult/tsne_data.csv', index=True)
mds_data_df.to_csv('esult/mds_data.csv', index=True)
umap_data_df.to_csv('esult/umap_data.csv', index=True)

# Save the data to 01 CSV File
datapath_pca = '/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/pca_data_cluster.csv'
datapath_mds = '/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/mds_data_cluster.csv'
datapath_tsne = '/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/tsne_data_cluster.csv'
datapath_umap = '/Users/liruifeng/Desktop/Data Visualization/homework/hw2/Dimension_Reduction/result/umap_data_cluster.csv'

change(datapath_pca, 'PC1', 'PC2', '../result/pca_data_cluster.csv')
change(datapath_mds, 'MDS1', 'MDS2', '../result/mds_data_cluster.csv')
change(datapath_tsne, 'TSNE1', 'TSNE2', '../result/tsne_data_cluster.csv')
change(datapath_umap, 'UMAP1', 'UMAP2', '../result/umap_data_cluster.csv')