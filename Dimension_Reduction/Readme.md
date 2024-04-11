# Reademe

## My method

In this task, my algorithms are stored in **algorithm file **, tools (including data preparation and plot) in **tool file** , original data in **data file** and interaction&visualization in **interaction&visualization file**, besides all the results are in **result file**(including png and csv).

  To reproduct the result you can just run `python reduction.py` or run all `method.ipynb`, to get classification you should run `python classification.py` , to interact and get data visualization you should `cd interaction&datavisualization` and then run `http-server`.



## DataSet

You can click [dataset](https://www.kaggle.com/datasets/fatihfurkankurt/essay-examination-data-set) to get the original dataset or just `cd data` to get **EssayAnalysis.csv**. This data has 7 dimensions and Essay Analysis table includes the outputs of the essays solved from different brands, the other tables examine the number of course-based errors. 

## Algorithm

In this task I used all **PCA, MDS, t-SNE and UMAP**, all of them perform well and get the cluster correctly, however, as you could see in **PCA** and **MDS**, there are some point really far away from the means central, I think it is because **PCA** excels in preserving variance and interpretability, but it struggles to retain local and global structures and **MDS** best preserves local structure, but it performs poorly in terms of variance retention and interpretability, however, **t-SNE** demonstrates better performance in maintaining both local and global structures, however, it falls short in interpretability and runtime efficiency and **UMAP** achieves a good balance, effectively preserving variance, local and global structures, while also boasting faster runtime speed.

## Interaction

In my interaction, when you click one point, the other 3 chart and this chart will highlight the clicked points and the same **index** point(through lower other points' light) and amplify them, **so that you could easily find the same point in different charts to evaluate the differnce of different algorithm**.





