import time
from settings import BASE_URL


# get next page url
def get_next_page_url(soup):
    # find the element that contains the next page url
    urlListElement = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
    if urlListElement and urlListElement.get('href'):
        # if the url is relative, add the base url
        if urlListElement.get('href').startswith('/'):
            next_url = BASE_URL+urlListElement.get('href')
        else:
            next_url = urlListElement.get('href')
        return next_url
    return None

# get the product title
def get_product_title(item):
    product_title = item.find('span', class_='a-size-medium a-color-base a-text-normal')
    if product_title:
        return product_title.text.strip()
    else:
        return "<missing product title>"

# get the product url
def get_product_url(item):
    product_url = item.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    if product_url and product_url.get('href'):
        # if the url is relative, add the base url
        if product_url.get('href').startswith('/'):
            return BASE_URL+product_url.get('href').strip()
        return product_url.get('href').strip()
    else:
        return "<missing product url>"

# get the product price
def get_product_price(item):
    product_price = item.find('span', class_='a-offscreen')
    if product_price:
        return product_price.text.strip()
    else:
        return "<missing product price>"
    
# get the product solder
def get_product_solder(item):
    product_solder = item.find('a', class_='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style')
    if product_solder:
        return product_solder.text.strip()
    else:
        return "<missing product solder>"
    
# get the product review
def get_product_review(item):
    product_review = item.find('span', class_='a-icon-alt')
    if product_review:
        return product_review.text.strip()
    else:
        return "<missing product review>"
    
# get the product review number
def get_product_review_number(item):
    product_review_number = item.find('span', class_='a-size-base s-underline-text')
    if product_review_number:
        return product_review_number.text.strip()
    else:
        return "<missing product review number>"

# get the product image url
def get_product_image_url(item):
    product_image_url = item.find('img', class_='s-image')
    if product_image_url and product_image_url.get('src'):
        if product_image_url.get('src').startswith('/'):
            return BASE_URL+product_image_url.get('src').strip()
        return product_image_url.get('src').strip()
    else:
        return "<missing product image url>"
    
# get the product information   
def product_extractor(item):
    crawl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    product_title = get_product_title(item)
    product_url = get_product_url(item)
    product_price = get_product_price(item)
    product_solder = get_product_solder(item)
    product_review = get_product_review(item)
    product_review_number = get_product_review_number(item)
    product_image_url = get_product_image_url(item)

    return (product_title, product_url, product_price, product_solder, product_review, product_review_number, product_image_url, crawl_time)   