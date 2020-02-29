1. Preprocessed scrapped reviews by pipeline established in Week2
2. Extracted 300 topic features using LSI, WORD2VEC, FastText techniques
3. Trained toy XGBoost models using the features extracted by all 3 methods to estimate the predictive capability of the features extracted.
  3.1. LSI/FastText -> Yielded RMSE equivalent to dummy model -> no predictive power
  3.2. WORD2VEC -> Yielded RMSE 0.7 -> Useful in prediction of ratings
