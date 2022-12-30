import requests

def make_payload(query,nsfw_flag,target_page):
  p = {
    "q": query,
    "purity": nsfw_flag,
    "sorting": "date_added",
    "categories": "111",
    "page": target_page
  }
  return p