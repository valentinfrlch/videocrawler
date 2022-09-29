# take a url as argument
# crawl a page with javascript
import requests_html


def crawler(video):
    # make a request then render the page
    url = "https://hdtoday.cc/search/" + video
    session = requests_html.HTMLSession()
    r = session.get(url)
    # render the page
    html = r.html.render()
    return html
    
print(crawler("Bullet Train"))
