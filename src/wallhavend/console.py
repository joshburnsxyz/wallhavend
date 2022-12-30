import argparse
import requests

from .wallhaven_api import make_payload, search_url_generator
from .fileio import save_bin_data

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
  page_limit = args.pages
  s_url = search_url_generator(apikey=args.key)
  results_page = 1
  nsfw_flag = "100"
  
  # NSFW filter
  if args.nsfw is True:
    nsfw_flag = "111"

  # Generate payload for request
  initial_payload = make_payload(args.query,nsfw_flag,results_page)

  # Get metadata
  wallhaven_metadata_request = requests.get(s_url, params=initial_payload)
  metadata = wallhaven_metadata_request.json()["meta"]
 
  # If page_limit doesnt get an upfront value
  # set it to the number of pages of results
  if page_limit is None:
    page_limit = metadata["last_page"]

  # Only loop until page_limit is reached
  while results_page < page_limit:
    # Generate query for next page of results
    loop_payload = make_payload(args.query,nsfw_flag,results_page)
    resp = requests.get(s_url, params=loop_payload).json()
    
    # Loop over paged results and save images
    for img in resp["data"]:
      img_type = img["file_type"].split("/")[1]
      img_name = img["id"]
      img_file = f"./out/{img_name}.{img_type}"
      img_content = requests.get(img["path"], stream=True).content
      save_bin_data(img_file,img_content)
      
    # Increment page number for next cycle
    results_page = results_page + 1