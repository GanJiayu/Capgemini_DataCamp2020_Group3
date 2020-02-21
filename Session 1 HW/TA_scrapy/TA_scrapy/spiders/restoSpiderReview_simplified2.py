# Logging packages
import logging
import logzero
from logzero import logger

# Scrapy packages
import scrapy
#from TA_scrapy.items import ReviewRestoItem     # you can use it if you want but it is not mandatory
from TA_scrapy.spiders import get_info          # package where you can write your own functions


class RestoReviewSpider(scrapy.Spider):
    """
    usage:  cd %SPIDER_DIRECTORY%
            scrapy crawl ZQR -o %OUT_FILENAME% -a max_page=416 -a max_review=200 -a min_review=500

    commandline arguments:
    max_page: [stopping criterion] scrapper stops when it reaches given number of resto pages (30 resto per page) 
    max_review: [stopping criterion] scrapper collects given number of reviews per resto at maximum
    min_review: [filter criterion] scrapper skips a resto if this criterion is not satisfied
    max_resto: [deprecated]
    """
    name = "ZQR"

    def __init__(self, *args, **kwargs): 
        super(RestoReviewSpider, self).__init__(*args, **kwargs)

        # Set logging level
        logzero.loglevel(logging.WARNING)

        # Parse max_page - This is the overview page of all resto avaliable
        # Typically 30 resto in a single page
        self.max_page = kwargs.get('max_page')
        if self.max_page:
            self.max_page = int(self.max_page)
        else:
            self.max_page = None

        # Max_number_of_reviews_of_resto
        self.max_review = kwargs.get('max_review')
        if self.max_review:
            self.max_review = int(self.max_review)
        else:
            self.max_review = None

        self.min_review = kwargs.get('min_review')
        if self.min_review:
            self.min_review = int(self.min_review)
        else:
            self.min_review = None

        self.max_resto = kwargs.get('max_resto')
        if self.max_resto:
            self.max_resto = int(self.max_resto)
        else:
            self.max_resto = None

        print("Max_Page: ", self.max_page)
        print("Max_resto: ", self.max_resto)
        print("Max_Review: ", self.max_review)
        print("Min_Review: ", self.min_review)
        # To track the evolution of scrapping
        self.main_nb = 0
        self.resto_nb = 0
        self.review_nb = 0
        

    def start_requests(self):
        """ Give the urls to follow to scrapy
        - function automatically called when using "scrapy crawl my_spider"
        """

        # Basic restaurant page on TripAdvisor GreaterLondon
        url = 'https://www.tripadvisor.co.uk/Restaurants-g191259-Greater_London_England.html'
        yield scrapy.Request(url=url, callback=self.parse)

   
    def parse(self, response):
        """MAIN PARSING : Start from a classical reastaurant page
            - Usually there are 30 restaurants per page
            - 
        """

        # Display a message in the console
        logger.warn(' > PARSING NEW MAIN PAGE OF RESTO ({})'.format(self.main_nb))
        self.main_nb += 1

        # Get the list of the 30 restaurants of the page
        restaurant_urls = get_info.get_urls_resto_in_main_search_page(response)

        # For each url : follow restaurant url to get the reviews
        for restaurant_url in restaurant_urls:
            logger.warn('> New restaurant detected : {}'.format(restaurant_url))
            yield response.follow(url=restaurant_url, callback=self.parse_resto)
        

        
        # Get next page information
        next_page, next_page_number = get_info.get_urls_next_list_of_restos(response)
        
        # Follow the page if we decide to
        if get_info.go_to_next_resto_page(next_page, next_page_number, max_page=self.max_page, printing=True):
            logger.warn(' > GOING TO THE NEXT RESTO PAGE ({})'.format(next_page))
            yield response.follow(next_page, callback=self.parse)
                


    def parse_resto(self, response):
        """SECOND PARSING : Given a restaurant, get each review url and get to parse it
            - Usually there are 10 comments per page
        """

        # Display a message in the console
        logger.warn(' > PARSING NEW RESTO PAGE ({})'.format(self.resto_nb))
        

        # Get Number of reviews
        nr_reviews = get_info.get_number_of_reviews(response)
        if self.min_review is not None:
            if nr_reviews < self.min_review:
                logger.warn('{} reviews, smaller than threshold {}, skip.'.format(nr_reviews, self.min_review))
                return 
            else:
                logger.warn('{} reviews'.format(nr_reviews))


        self.resto_nb += 1

        # Get the list of the 10 reviews on the restaurant page
        review_urls = get_info.get_urls_review_in_main_search_page(response)

        # For each url : follow review url to get the elements
        for review_url in review_urls:
            #logger.warn('> New review detected : {}'.format(url))
            yield response.follow(url=review_url, callback=self.parse_review)


        # Get next page information
        next_page, next_page_number = get_info.get_urls_next_list_of_reviews(response)

        
        # Follow the page if we decide to
        if get_info.go_to_next_review_page(next_page, next_page_number, max_page=self.max_review, printing=0):
            logger.warn(' > GOING TO THE NEXT REVIEW PAGE ({})'.format(next_page))
            yield response.follow(next_page, callback=self.parse_resto)


    def parse_review(self, response):
        """FINAL PARSING : Open a specific page with review and client opinion
            - Read these data and store them
            - Get all the data you can find and that you believe interesting
        """

        # Count the number of review scrapped
        self.review_nb += 1

        

        # You can store the scrapped data into a dictionnary or create an Item in items.py (cf XActuItem and scrapy documentation)
        review_item = {}
        
        # Exception handling added - GJY 06/02/2020
        # Exception: Reference to a null pointer
        # resto_name, reviewID, date, review_body, rating
        review_item['Restaurant Name'] = get_info.get_resto_name(response)
        review_item['Review ID'] = get_info.get_reviewID(response)
        review_item['Date'] = get_info.get_date(response)
        review_item['Content'] = get_info.get_review_body(response)
        review_item['Rating'] = get_info.get_rating(response)
        
        yield review_item 



