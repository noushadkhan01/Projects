# -*- coding: utf-8 -*-
"""visualise_2d_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RKPrQGliCxycONMMrhVJefFIIeplccHh
"""

def visualise_2d_dataset(model = None, x = None, y_label = y):
  import matplotlib.pyplot as plt
  import numpy as np
  %matplotlib inline
  if not model:
      raise ValueError('Please Provide model first')
  if model:
      y_label = model.fit_predict(x)
      plt.figure(figsize = (10, 7))
      plt.scatter(X[:, 0], X[:, 1], c = y_label, cmap = 'coolwarm', edgecolors = 'black', linewidths = 1, alpha = 1, s = 150)
      plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s = 300, c = 'red', label = 'Centroids', edgecolors = 'black', alpha = .7)
      plt.title(f'Visualisation of {optimal_clusters} clusters')
      plt.xlabel('Annual Income (k$)',fontsize =  'large')
      plt.ylabel('Spending Score (1 - 100)',fontsize =  'large')
      plt.legend(bbox_to_anchor = (1.2, 1))
      plt.show()
