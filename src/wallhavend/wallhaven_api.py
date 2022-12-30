def make_payload(query,nsfw_flag,target_page):
  """
  Generates a valid data payload for making requests to
  the wallhaven API.

  Params: 
    - query - The search term used.
    - nsfw_flag - 3 digit binary mask for filtering images.
    - target_page - Results from the API are paged, we can target pages individually.
  """
  p = {
    "q": query,
    "purity": nsfw_flag,
    "sorting": "date_added",
    "categories": "111",
    "page": target_page
  }
  return p

def search_url_generator(apikey=None):
  """
  Generates the URL to target for the request. We assume
  the wallhave v1 API base URL and optionally append params
  to it based on the input.
  """
  base_url = "https://wallhaven.cc/api/v1/search"
  
  if apikey is not None:
    base_url += f"?apikey={apikey}"
  
  return base_url
