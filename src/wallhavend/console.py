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
  payload = {
    "q": args.query,
    "purity": nsfw_flag
  }

  wallhaven_search_request = requests.get(base_url, params=payload)
  data = wallhaven_search_request.json()