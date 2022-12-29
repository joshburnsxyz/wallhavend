import argparse
import os

# Create parser 
parser = argparse.ArgumentParser(
                    prog = 'wallhavend',
                    description = 'Grab and use wallpapers from wallhaven.cc',
                    epilog = 'wallhavend - VERSION 0.1.0')

# Flags
parser.add_argument('-k', '--key', metavar="KEY", help="Your wallhaven.cc API key")

def run():
  args = parser.parse_args()

  # Print request URL
  print(f"https://wallhaven.cc/api/v1/search?apikey={args.key}")
  
  
