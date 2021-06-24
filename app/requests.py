import urllib.request,json
from .models import Book


api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['BOOK_API_KEY']
    base_url = app.config['BOOK_API_BASE_URL']
    

def get_books(time):
    '''
    Function that gets the json response to our url request
    '''
    get_books_url = base_url.format(time,api_key)


    with urllib.request.urlopen(get_books_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)

        book_results = None
        print(get_books_response['results']['books'][0])

        if get_books_response['results']['books']:
            book_results_list = get_books_response['results']['books']
            book_results = process_results(book_results_list)


    return book_results

def process_results(book_list):

    book_results = []
    for book_item in book_list:
        author = book_item.get('author')
        title = book_item.get('title')
        description = book_item.get('description')
        book_image = book_item.get('book_image')
        amazon_product_url = book_item.get('amazon_product_url')

        # if poster:
        book_object = Book(author,title,description,book_image,amazon_product_url)
        book_results.append(book_object)

    return book_results

    def get_book(title):
        get_book_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_book_details_url) as url:
        book_details_data = url.read()
        book_details_response = json.loads(book_details_data)

        book_object = None
        if book_details_response:
            author = book_item.get('author')
            title = book_item.get('title')
            description = book_item.get('description')
            book_image = book_item.get('book_image')
            amazon_product_url = book_item.get('amazon_product_url')

            book_object = Book(author,title,description,book_image,amazon_product_url)

    return book_object

def search_book(book_name):
    search_book_url = 'https://api.thebookdb.org/3/search/book?api_key={}&query={}'.format(api_key,book_name)
    with urllib.request.urlopen(search_book_url) as url:
        search_book_data = url.read()
        search_book_response = json.loads(search_book_data)

        search_book_results = None
        

        if search_book_response['results']['books']:
            search_book_list = search_book_response['results']['books']
            search_book_results = process_results(search_book_list)


    return search_book_results

    
def process_results(book_list):
    '''
    Function  that processes the book result and transform them to a list of Objects
    Args:
        book_list: A list of dictionaries that contain book details
    Returns :
        book_results: A list of book objects
    '''
    book_results = []
    for book_item in book_list:
        author = book_item.get('author')
        title = book_item.get('title')
        description = book_item.get('description')
        book_image = book_item.get('book_image')
        amazon_product_url = book_item.get('amazon_product_url')

    
       