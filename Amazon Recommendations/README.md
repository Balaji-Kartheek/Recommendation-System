# Amazon-Product Recommender System


#### The overall Objective of the project is to build an app with a simple UI. The app will allow the user to 
choose between 5 categories of products , for instance cell phones, clothing, shoes, software etc. On 
choosing the category of product, recommendations are displayed based on User Based Similarity.

## Dataset: 

Dataset – Amazon reviews : http://snap.stanford.edu/data/web-Amazon-links.html

snippets of the recommender website

first snippet:

![image](https://user-images.githubusercontent.com/77656115/189540146-9eac1b06-bc2c-47f9-8ff9-1c7f4c70bfcc.png)

second snippet: 
![image](https://user-images.githubusercontent.com/77656115/189540160-13144fac-eeb2-4833-a65e-43b806188e69.png)

#### A content based Amazon Products recommender system using cosine similarity based on the selected category

## Similarity Score:
How does it decide which item is most similar to the item user likes(or selects in our case)? Here comes the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity Works
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/77656115/206839091-da313c5a-5c40-4716-b55a-94a9c656b44a.png)

### Workflow Steps:
1. Data Pre-processing and Exploratory Data Analysis
2. Building a Recommendation Function based on User-Similarity.
3. Importing pickle files in PyCharm making a UI using Streamlit interface.




