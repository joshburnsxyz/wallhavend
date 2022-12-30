def save_bin_data(file, data):
  """
  Saves binary data to a given file.
  """
  try:
    with open(file, "wb") as bin_file:
      bin_file.write(data)
  except:
    print(f"There was an error writing to {file}")  