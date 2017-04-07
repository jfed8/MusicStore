import requests

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red

def ApiRequest(url, color, *error):
    print(color, "\n>>>>>New Request's URL: ", url)
    ret = requests.get(url)
    try:
        print(color, ret.json())
    except:
        print (color, ret, error)

# Call Number 1
ApiRequest('http://localhost:8000/api/api_products/153?product_name=a&category_name=inst', R) #Returns 3 products
ApiRequest('http://localhost:8000/api/api_products/153?min_price=100', W) #Returns 2 products
ApiRequest('http://localhost:8000/api/api_products/?min_price=15&max_price=', R) #Returns 6 products
ApiRequest('http://localhost:8000/api/api_products/153?max_price=10&category_name=hey', W, "Fails because 'hey' doesn't match any categories")
ApiRequest('http://localhost:8000/api/api_products/?min_price=d', R, "Fails because invalid min_price")
