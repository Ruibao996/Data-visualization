from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, MDS
from sklearn.cluster import KMeans
import umap

def pca(data, n_components=2):
    """
    Perform PCA
    :param data: The input data
    :param n_components: The number of components
    :return: The transformed data
    """
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data)
    return pca_data

def tsne(data, n_components=2, perplexity=5, learning_rate=200):
    """
    Perform t-SNE
    :param data: The input data
    :param n_components: The number of components
    :param perplexity: The perplexity
    :param learning_rate: The learning rate
    :return: The transformed data
    """
    tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=learning_rate)
    tsne_data = tsne.fit_transform(data)
    return tsne_data

def mds(data, n_components=2, metric=True):
    """
    Perform MDS
    :param data: The input data
    :param n_components: The number of components
    :param metric: If True, use metric MDS
    :return: The transformed data
    """
    mds = MDS(n_components=n_components, metric=metric)
    mds_data = mds.fit_transform(data)
    return mds_data

def umap_func(data, n_components=2, n_neighbors=15, min_dist=0.1):
    """
    Perform UMAP
    :param data: The input data
    :param n_components: The number of components
    :param n_neighbors: The number of neighbors
    :param min_dist: The minimum distance
    :return: The transformed data
    """
    umap_data = umap.UMAP(n_components=n_components, n_neighbors=n_neighbors, min_dist=min_dist).fit_transform(data)
    return umap_data

def kmeans(data, n_clusters=2):
    """
    Perform k-means clustering
    :param data: The input data
    :param n_clusters: The number of clusters
    :return: The cluster labels
    """
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    return kmeans.labels_

# Path: Dimension_Reduction/algorithm/algorithm.py