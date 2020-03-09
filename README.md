# Capgemini_DataCamp2020_Group3

### Team members: Delong LI, Doha KADDAF, Honghao YU, Jiayu GAN, Qiwen ZHAO

# Session1 homework:

- [x] Create a spider which gets reviews and ratings from multiple pages of reviews for a given restaurant
      Spider: restoSpiderReview_Brokan.py
      Data: Scraped_Brokan.csv
      Execute: Run Scrapper.ipynb 
      
- [x] It might be interesting to get other information available on the webpages
      Additional entries: ReviewerID, Date, Rating(1~5)

- [x] Bonus (+1 pt on final mark) : create a spider which crawls multiple pages of restaurants to get multiple pages of reviews. At least 500 full reviews per restaurant for 100 restaurants.
      Spider: restoSpiderReview_simplified2.py
      Data: Allresto.csv
      Execute: Run Scrapper.ipynb 


# Session2 homework:

Data pipeline: data collection -> data cleaning -> word embedding -> topic extraction -> sentiment analysis  
- [x] Apply every step of text processing to the collected reviews: EDA, transforming the text into a "corpus", tokenizing, removing punctuation, removing/replacing specific characters, replacing accents, removing stop words, lemmatization, stemming
- [x] Create a TF-IDF Matrix with all the reviews scrapped on the web, and find the best way to represent it (maybe WordCloud)
- [x] Bonus reward (build 2 functions):
     * One that takes a corpus of raw text and creates a new corpus with cleaned and lemmatized text
     * One that takes a corpus (or a dataframe text column) and creates a WordCloud from it
- [x] Create sets of KPI (both evident and shadow) you may collect from available open information (the idea is to anticipate what you'll present on the fourth session for the client meeting simulation)

# Session3 homework:

To practice what we learnt today, for next session, you’ll have to :

- [X] Apply LSI on your scraped data
- [X] Build a simple classification model using the embedding matrix and the rating of the review as target variable with a modern ML technique
- [X] Carry out the same analysis using FastText with the gensim package (optional)
- [X] Compare the performances of your models with the two or three type of embeddings </br>
    -- XGBoost + LSI/W2V/FT features </br>
    -- MSE: Dummy(constant predictor) 1.34, LSI 1.34, W2V 0.70, FT 1.34
    
# Session5 highlights:
- [ ] Storyboarding: 
      * Design the scenario: write the plan
      * Design the arguments within the scenario
      * Produce views: checking the fluidity between the messages
      * Write the introduction and the conclusion
      * Master the content
      * Manage the transitions
- [ ] Advanced word representations:
      * Vectorization: Word2Vec, Word2Vec Skipgram, negative sampling
      * Efficient text classfication: FastText, hierarchical SOFTMAX
      * Misspelling Oblivious Word Embeddings
      * RNN, RNN encoder-decoder, attention mechanism
- [ ] Graph representations:
      * Graphs can help for a various range of NLP tasks: Coreference Resolution, Entity Linking, Knowledge graph applications, Hypernym discovery
      * Node embeddings
      * Graph embeddings
      * Random walk embeddings: expressivity, efficiency; optimization
      * Node2Vec
      
      
