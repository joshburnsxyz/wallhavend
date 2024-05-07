import argparse
import requests
import os

from rich.progress import track
from .fileio import dir_exists
from .wallhaven_api import make_payload, search_url_generator, process_image

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
  """
  Primary console entrypoint. This function is run when `wallhavend`
  is called from the commandline.
  """
  args = parser.parse_args()
  page_limit = args.pages
  s_url = search_url_generator(apikey=args.key)
  results_page = 1
  nsfw_flag = "100"

  # Check if output directory exists or not
  if not dir_exists("./out"):
    os.mkdir("./out")
  
  # NSFW filter
  if args.nsfw is True:
    nsfw_flag = "111"

  # Get metadata and set page_limit based on page count.
  initial_payload = make_payload(args.query,nsfw_flag,results_page)
  metadata = requests.get(s_url, params=initial_payload).json()["meta"]
  if page_limit is None:
    page_limit = metadata["last_page"]

  # Only loop until page_limit is reached
  while results_page < int(page_limit):
    # Generate query for next page of results
    loop_payload = make_payload(args.query,nsfw_flag,results_page)
    resp = requests.get(s_url, params=loop_payload).json()
    
    # Loop over paged results and save images
    for img in track(resp["data"], description='[green]Processing wallpaper'):
      process_image(img)

    # Increment page number for next cycle
    results_page = results_page + 1
