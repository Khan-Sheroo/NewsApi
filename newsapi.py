import requests

service_url = 'https://newsapi.org/v2/top-headlines'
api_key = 'ec213eb8854a47e4881efd2aea2f72af'


parameters = {
    'language' : 'en',
    'country' : 'us',
    'apiKey' : api_key
}


response = requests.get(service_url, params=parameters)

if response.status_code == 200:
    news_api = response.json()

    articles = news_api['articles']
    for article in articles:
        print(article['title'])
        print(article['content'])
        print(article['url'])
else:
    print(f"Error fetching data:{response.status_code}")


    
