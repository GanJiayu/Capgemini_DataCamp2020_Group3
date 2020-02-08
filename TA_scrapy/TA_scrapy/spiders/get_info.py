################################################################################################
################################################################################################
#                                       TA NAVIGATION 
################################################################################################
################################################################################################
from string import digits

def get_urls_resto_in_main_search_page(response):
    """
    Get the list of 30 restaurants in a given page
    """
    xpath = '//div[@class="_1llCuDZj"]//a[@class="_15_ydu6b"]'
    return response.xpath(xpath).css('::attr(href)').extract()


# Todo: possible exception emit if Xpath extract returns a null list
def get_urls_next_list_of_restos(response):
    xpath = '//*[@id="EATERY_LIST_CONTENTS"]/div/div/a'
    next_page = response.xpath(xpath).css('::attr(href)').extract()[-1]
    next_page_number = response.xpath(xpath).css('::attr(data-page-number)').extract_first()
    return next_page, next_page_number

def get_number_of_reviews(response):
    """
    response: Resto Page
    """
    xpath = '//*[@id="REVIEWS"]/div[1]/div/div[1]/span[@class="reviews_header_count"]//text()'
    nr_reviews = response.xpath(xpath).extract()

    # Expected returns: (600)  (1,241) (4,890)
    if len(nr_reviews) > 0:
        nr_reviews = int(''.join(char for char in nr_reviews[0] if char in digits))
    else:
        nr_reviews = None
    return nr_reviews



def go_to_next_resto_page(next_page, next_page_number=None, max_page=10, printing=False):
    """ According to next_page, and number of pages to scrap, tells if we should go on or stop.
    returns a boolean value : True (you should follow taht url) / False (you should stop scrapping)

    - next_page (str)           : the url of the next_page
    - next_page_number (int)    : often extracte from next_page, it is the number of the next page on the website
    - max_page (int)            : number of page you want to scrap.
                                If set to None, will scrap until the end of the website (might be very long).
    - printing(bool)            : If set to true will display messages at each new page to explain what is happening (useful for debug purprose)

    """

    if next_page is None:
        pass
        #if printing: print(' - There is no next_page')
    else:
        #if printing: print(' - There is a next_page')
        #if printing: print(' - Page url is : {}'.format(next_page))
        if max_page is None:
            if printing: print(' - There is no number of page restriction. Go on.')
            return True
        else:
            if printing: print(' - Max Resto page number is : {}'.format(max_page))

            if next_page_number is None:
                if printing: print(' -  No next number page : STOP.')
            else:
                if printing: print(' - Next Resto page number is {}'.format(next_page_number))
                if int(next_page_number) <= int(max_page):
                    if printing: print(' - It is smaller than limit. Go on.')
                    return True
                else:
                    if printing: print('LIMIT was reached. STOP.')
    return False

################################################################################################
################################################################################################
#                                       REVIEW INFORMATION 
################################################################################################
################################################################################################
def get_urls_review_in_main_search_page(response):
    """
    Get the list of 10 reviews in a given page
    """
    xpath = '//div[@class="reviewSelector"]//a[@class="title "]'
    return response.xpath(xpath).css('::attr(href)').extract()


def get_urls_next_list_of_reviews(response):
    xpath = '//div[@class="unified ui_pagination "]//a[@class="nav next ui_button primary"]'
    #next_page = response.xpath(xpath).css('::attr(href)').extract()[0]
    #next_page_number = response.xpath(xpath).css('::attr(data-page-number)').extract()[0]
    next_page = response.xpath(xpath).css('::attr(href)').extract()
    next_page_number = response.xpath(xpath).css('::attr(data-page-number)').extract()
    if len(next_page) > 0:
        next_page = next_page[0]
    else:
        next_page = None

    if len(next_page_number) > 0:
        next_page_number = next_page_number[0]
    else:
        next_page_number = None

    return next_page, next_page_number


def go_to_next_review_page(next_page, next_page_number=None, max_page=10, printing=False):
    """ According to next_page, and number of pages to scrap, tells if we should go on or stop.
    returns a boolean value : True (you should follow taht url) / False (you should stop scrapping)

    - next_page (str)           : the url of the next_page
    - next_page_number (int)    : often extracte from next_page, it is the number of the next page on the website
    - max_page (int)            : number of page you want to scrap.
                                If set to None, will scrap until the end of the website (might be very long).
    - printing(bool)            : If set to true will display messages at each new page to explain what is happening (useful for debug purprose)

    """

    if next_page is None:
        pass
        #if printing: print(' - There is no next_page')
    else:
        #if printing: print(' - There is a next_page')
        #if printing: print(' - Page url is : {}'.format(next_page))
        if max_page is None:
            if printing: print(' - There is no number of page restriction. Go on.')
            return True
        else:
            if printing: print(' - Max Review page number is : {}'.format(max_page))

            if next_page_number is None:
                if printing: print(' -  No next number page : STOP.')
            else:
                if printing: print(' - Next Review page number is {}'.format(next_page_number))
                if int(next_page_number) <= int(max_page):
                    if printing: print(' - It is smaller than limit. Go on.')
                    return True
                else:
                    if printing: print('LIMIT was reached. STOP.')
    return False






# Exception handling added - GJY 06/02/2020
# Exception: Reference to a null pointer
def get_resto_name(response):
    """
    response: Review Page
    """
    resto_xpath = '//div[@id="HEADING_GROUP"]//div[@class="rating"]//span[2]/a/text()'
    resto = response.xpath(resto_xpath).extract()
    if len(resto) > 0:
        resto = resto[0]
    else:
        resto = None
    return resto


def get_reviewID(response):
    """
    response: Review Page
    """
    reviewID_xpath = '//div[@class="prw_rup prw_reviews_basic_review_hsx"]//div[@class="reviewSelector"]/@data-reviewid'
    #reviewID = response.xpath(reviewID_xpath).extract()[0].replace('\t', '').replace('\n', '').strip()
    reviewID = response.xpath(reviewID_xpath).extract()
    if len(reviewID) > 0:
        reviewID = reviewID[0].replace('\t', '').replace('\n', '').strip()
    else:
        reviewID = None
    return reviewID
    
def get_date(response):
    """
    response: Review Page
    """
    date_xpath = '//div[@class="prw_rup prw_reviews_stay_date_hsx"]/text()'
    #date = response.xpath(date_xpath).extract()[0].replace('\t', '').replace('\n', '').strip()
    date = response.xpath(date_xpath).extract()
    if len(date) > 0:
        date = date[0].replace('\t', '').replace('\n', '').strip()
    else:
        date = None
    return date

def get_review_body(response):
    """
    response: Review Page
    """
    review_xpath = '//div[@class="entry"]//p[@class="partial_entry"]/text()'
    #review_body = response.xpath(review_xpath).extract()[0].replace('\t', '').replace('\n', '').strip()
    review_body = response.xpath(review_xpath).extract()
    if len(review_body) > 0:
        review_body = review_body[0].replace('\t', '').replace('\n', '').strip()
    else:
        review_body = None
    return review_body

def get_rating(response):
    """
    response: Review Page
    """
    rating_xpath = '//div[@id="HEADING_GROUP"]//div[@class="rating"]//span[1]/@class'
    #rating = int(response.xpath(rating_xpath).extract()[0][-2:])/10
    rating = response.xpath(rating_xpath).extract()
    if len(rating) > 0:
        rating = int(rating[0][-2:])/10
    else:
        rating = None
    return rating


















