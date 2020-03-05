# Session 3 Homework

To practice what we learnt today, for next session, you’ll have to :

- [X] Apply LSI on your scraped data
- [X] Build a simple classification model using the embedding matrix and the rating of the review as target variable with a modern ML technique
- [X] Carry out the same analysis using FastText with the gensim package (optional)
- [X] Compare the performances of your models with the two or three type of embeddings </br>
    -- XGBoost + LSI/W2V/FT features </br>
    -- MSE: Dummy(constant predictor) 1.33, LSI 0.81, W2V 0.70, FT 1.39

# Remarks:
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) We cached dataset/model/features on HDD </br>
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) The notebooks were extremely time-consuming
## Word_embedding.ipynb
- Extract latent topic features for modeling
    - LSI: 300 topics
    - W2V: 300 topics 
        - With word embedding t-SNE clustering
    - Fast: 300 topics
- Extract latent topic features for visualization
    - LDA: 6 topics

## LSTM.ipynb
- 2-layer Bidirection LSTM model with implicit word embedding
- Target: 5 classes Onehot-Encoding 
- Performance(Accuracy): 62% versus 52% (Constant Predictor)

## XGB.ipynb
- (As the dataset we have scrapped is too big to be trained, We used a subset of dataset for visualization/modeling)
- RMSE of constant predictor: 1.33 (Ratings from 1.0 to 5.0)
- XGB + LSI:
    - RandomSearch on 5K samples
    - Model trained on 50K samples
    - Target: Ratings as scalar
    - Metric(RMSE): 0.816 +/- 0.009
- XGB + Word2Vec
    - RandomSearch on 5K samples
    - Model trained on 50K samples
    - t-SNE visualization of Doc2Vec embedding
    - Target: Ratings as scalar
    - Metric(RMSE): 0.701 +/- 0.006
- FastText + Word2Vec
    - RandomSearch on 5K samples
    - Model trained on 50K samples
    - Target: Ratings as scalar
    - Metric(RMSE): 1.39 +/- 0.02
    - ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Something went wrong with FastText model
