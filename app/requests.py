import urllib.request,json
from .models import Book

#getting api key 
api_key = None

def configure_request(app):
    global api_key
    api_key = app.config['BOOK_API_KEY']

def search_book(book_name):
    search_book_url = 'http://api.book.com/3/search/book?api_key{}&query={}'.format(api_key, book_name)
    with urllib.request.urlopen(search_book_url) as url:
        search_book_data = url.read()
        search_book_response = json.loads(search_book_data)

        search_book_results = None

        if search_book_response['results']:
            search_book_list = search_book_response['results']
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
        title = book_item.get('original_title')
        author = book_item.get('author')
        description = book_item.get('description')
        book_image =book_item.get('book_image_path')
        published_date =book_item.get('published_date') 
        

        if book_image:

            book_object = Book(title,author,description,book_image,published_date)
            book_results.append(book_object)

    return book_results 

