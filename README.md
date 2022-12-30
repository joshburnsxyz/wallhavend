# wallhavend
Simple daemon to handle retrieve and use wallpapers from wallhaven.cc

# Usage

```shell
$ wallhavend [OPTIONS]
```

## Available command-line options

__Options and Settings__

- `--key <API KEY>` | `-k` - Your Wallhaven.cc API key (Required for `-N`).
- `--query <QUERY>` | `-q` - Search term or tag.
- `--pages <LIMIT>` | `-p` - How many pages to run over (API Results are paginated).

__Flags__

- `--nsfw` | `-N` - Enable NSFW images in results