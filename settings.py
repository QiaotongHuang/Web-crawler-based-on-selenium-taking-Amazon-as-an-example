# Description: This file contains all the settings for the crawler
import os


# website base url
BASE_URL = 'https://www.amazon.com'

# TODO - add more urls to crawl, now only kindle store
url = "https://www.amazon.com/s?k=Kindle+Store&i=digital-text&rh=n%3A133140011%2Cp_n_deal_type%3A23566064011&dc&qid=1706467617&rnid=1248985011&ref=sr_nr_selected_filters_p_72_2&ds=v1%3AZRC4RT1%2BRvrPmt8FTw4mkJ%2Bk3F4sePA2BYDE5yVqA0s" 


# login to Amazon 
LOGIN_URL = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fi%3Ddigital-text%26rh%3Dn%253A133140011%26fs%3Dtrue%26page%3D2%26qid%3D1706307841%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" 
EMAIL = 'your_login_email'
PASSWORD = 'your_login_password'


# Request settings
# timeout for requests
TIMEOUT = 5


# Proxies - never used in this project for now  
proxies = [
    # your list of proxy IP addresses goes here
    # check out https://proxybonanza.com/?aff_id=629
    # for a quick, easy-to-use proxy service
]
proxy_user = ""
proxy_pass = ""
proxy_port = ""


# TODO: image download settings
current_dir = os.path.dirname(os.path.realpath(__file__))
image_dir = os.path.join(current_dir, "/outputs/images")