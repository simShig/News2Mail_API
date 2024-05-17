import requests
from send_email import send_email

topic = "cyber"

api_key = os.getenv("News2Mail_API_apiKey")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

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
