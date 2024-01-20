import requests
from send_email import send_email

topic = "technology"

api_key = "2e0b30c80a604166bb7ac41c350cd78c"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + "\n" + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
# print(body)