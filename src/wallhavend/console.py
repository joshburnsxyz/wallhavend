import argparse
import requests

# Create parser 
parser = argparse.ArgumentParser(
                    prog = 'wallhavend',
                    description = 'Grab and use wallpapers from wallhaven.cc',
                    epilog = 'wallhavend - VERSION 0.1.0')

# Flags
parser.add_argument('-k', '--key', metavar="KEY", help="Your wallhaven.cc API key")
parser.add_argument('-q', '--query', metavar="QUERY", help="Search term, or tag")
parser.add_argument('-N', '--nsfw', action="store_true", help="Allow NSFW images to be returned in results")
parser.add_argument('-p', '--pages', metavar="LIMIT", help="Set a limit on how many pages the API can return (24 images per page)")

def run():
  args = parser.parse_args()
  base_url = "https://wallhaven.cc/api/v1/search"
  nsfw_flag = "100"

  # Append API Key to request URL if available
  if args.key is not None:
    base_url += f"?apikey={args.key}"

  # NSFW filter
  if args.nsfw is True:
    nsfw_flag = "111"

  # Generate payload for request
  results_page = 1
  page_limit = args.pages
  initial_payload = {
    "q": args.query,
    "purity": nsfw_flag,
    "sorting": "date_added",
    "categories": "111",
    "page": results_page
  }

  # Get metadata
  wallhaven_metadata_request = requests.get(base_url, params=initial_payload)
  metadata = wallhaven_metadata_request.json()["meta"]
 
  # If page_limit doesnt get an upfront value
  # set it to the number of pages of results
  if page_limit is None:
    page_limit = metadata["last_page"]

  while results_page < page_limit:
    loop_payload = initial_payload
    loop_payload["page"] = results_page
    resp = requests.get(base_url, params=loop_payload).json()
    for img in resp["data"]:
      img_bin_data = requests.get(img["path"]).text
      img_file = open(f"./{img["id"]}", "w+")
      img_file.write(img_bin_data)
      img_file.close()
    results_page = results_page + 1