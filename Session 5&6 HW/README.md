# Session 5&6 Homework

## Objectives:

- [x] Complete the hands-on notebook 

## Contents:

- Dataset: first 10000 reviews in capgemini data
  - 18557 words in vocabulary after tokenization
- A skipgram model was trained for 2 epochs (30 mins/epoch) with 90% accuracy
  - Given more training time, the model should achieve better performance
- The first layer of skipgram model acts as word embedding layer, which is able to convert each in-vocab-word into 300 latent features.
  - http://projector.tensorflow.org/ failed to give feed back after 5 hrs waiting, so we decided to take an alternative way.
  - We visualized word embedding space with the help of TSNE, there were some small clusters of words with similar semantics.
- Text Classification
  - X: 10000 reviews embedded by the pretrained skipgram model.
  - Y: Associated ratings of the reviews, ranged from 3.0 to 5.0, converted into one-hot-encoding with 5 classes.
  - ModelA: Pretrained Embedding + 3 Dense layers + 1 GlobalAveragePooling
  - ModelB: Pretrained Embedding + 2 LSTM + 1 Softmax Dense
  - Remarks: both model suffered from overfitting
- Coupling models
  - The model takes both tokenized reviews and embedded reviewers as input
  - Reviewer embedding
    - A pretrained node2vector model provided by instructor
      - Remarks: there were OOV 29% reviewers
  - We continued training coupling model with 29% missing values from reviewer embedding, the performance is not satisfying.
