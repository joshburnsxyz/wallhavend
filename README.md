# wallhavend
Simple daemon to handle retrieve and use wallpapers from wallhaven.cc

# Usage

```shell
$ wallhavend [OPTIONS]
```

## Available command-line options

__Options and Settings__

- `--key <API KEY>` or `-k` - Your Wallhaven.cc API key (Required for `-N`).
- `--query <QUERY>` or `-q` - Search term or tag.
- `--pages <LIMIT>` or `-p` - How many pages to run over (API Results are paginated).

__Flags__

- `--nsfw` or `-N` - Enable NSFW images in results.
- `--help` or `-h` - Display help message.

## Installation

1. Download source
2. Use `poetry` to build the wheel package
   ```shell
   $ poetry build
   ```
3. Install wheel with pip
   ```shell
   $ pip install ./path/to/package.whl
   ```
4. Run `wallhavend` command
   ```shell
   $ wallhavend
   ```
