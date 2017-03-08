import random
import urllib.request

def download_web_image(url):
	name = random.randrange(1,1000)
	full_name = str(name) + '.png'
	urllib.request.urlretrieve(url, full_name)

download_web_image('https://2.bp.blogspot.com/-HHTxSAQTmYo/WKwBz3orasI/AAAAAAAABwc/yScHjJCneUI_5njEKytAuBP3I10nzAGegCLcB/s1600/spoj.PNG')
