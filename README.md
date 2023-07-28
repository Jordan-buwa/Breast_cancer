---
date: "2023-07-21T12:00:00-05:00"
title: "Deep Transfer Learning for Classification of Breast Cancer"
---



# Deep Transfer Learning for Classification of Breast Cancer

## By Jordan Kevin Buwa Mbouobda
## Supervision: Dr. Prudence Djagba

## Introduction

Deep transfer learning is a machine learning technique that leverages knowledge from one task to improve the performance on a different but related task. In the context of breast cancer classification, algorithms are used to distinguish between cancerous and non-cancerous tumors in medical images such as mammograms.

According to a study conducted by Hyuna Sung, Jacques Ferlay, and other scholars in 2020, there were 19.3 million new cases of cancer, with a projected increase to 28.4 million by 2040. Among these cases, 2.3 million were related to breast cancer. Early detection and treatment planning through breast cancer classification are crucial for better patient outcomes.

## Previous research

Qasem Al-Haija and other scholars proposed the use of a pretrained ResNet-50 model for breast cancer classification, achieving an accuracy of 99.10%. They utilized the BreakHis cancer dataset for their experiments.

The objective of this study is to review various deep learning algorithms commonly used in breast cancer classification. We will employ these algorithms to classify images of breast cancer using the invasive ductal carcinoma dataset. Subsequently, we will compare the performance of different models.

## Dataset

For this study, we utilized a dataset consisting of 162 whole-mount microscope slide images from patients at the Hospital of the University of Pennsylvania and The Cancer Institute of New Jersey. These images were magnified at 40x, and they were divided into 277,524 patches, each measuring 50 pixels by 50 pixels. Out of these patches, 78,786 were classified as IDC-positive (indicative of cancer presence), and 198,738 were IDC-negative (indicative of no cancer presence). ([Data source](https://bit.ly/3XBOdum))

![Some images from the data  ](/images/cancer_img.png)

## Models Explored

### VGG (Visual Geometry Group)

VGG was developed in 2015 by Karen Simonyan and Andrew Zisserman. It is known for its simplicity and uniformity in design, consisting of a series of convolutional layers with small filters followed by max-pooling layers. The commonly used architecture in the literature is VGG16, which is well-suited for computer vision tasks.

![VGG16 diagram](/images/vgg-16.jpg)

### ResNet (Residual Neural Network)

ResNet was developed in 2015 by Kaiming He and other scholars to address the vanishing gradient problem associated with increasing network depth. The architecture of ResNet includes residual connections, enabling the network to skip certain layers and directly propagate information. This structure leads to effective learning and better accuracy with increasing depth. In this project, we used ResNet34 instead of the commonly used ResNet50.

![Resnet34 diagram](/images/Architecture-of-ResNet34-29.png)

### Vision Transformers (ViT)

Vision Transformers were introduced in 2020 by Alexey Dosovitskiy and other scholars. These models adapt the Transformer architecture from natural language processing to process images by dividing the image into patches and using self-attention mechanisms to capture relationships between them. Vision Transformers have demonstrated similar or better accuracy on image recognition tasks compared to state-of-the-art CNN-based models. However, they require more computational resources.

![Vision Transformers diagram](/images/vit_figure.png)

## Model Performance

We evaluated the performance of the different models using standard metrics for classification tasks:

| Model      | Accuracy | Precision | Recall  | F1-score |
|------------|----------|-----------|---------|---------|
| ResNet-34  | 90.40%   | 82.55%    | 85.90%  | 83.78%  |
| VGG-16     | 86.81%   | 84.00%    | 83.50%  | 82.50%  |
| ViT        | 83.33%   | 78.04%    | 83.28%  | 79.75%  |
| CNN Baseline| 71.64%  |   -      |    -    |    -    |

## Future Work

In the future, we plan to:
- Employ the algorithms for the detection of invasive ductal carcinoma (IDC).
- Perform classification on other datasets with more than two classes.
- Develop a new loss function to improve accuracy.

