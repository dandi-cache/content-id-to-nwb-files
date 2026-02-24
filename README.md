# DANDI Cache: Content ID → NWB files

A subset of `content-id-to-dandiset-paths` which have been identified to be NWB files (HDF5 or Zarr).

Updated frequently.

Primarily for use by developers.



## One-time use

If you only plan to use this cache infrequently or from disparate locations, you can directly download the latest version of the cache as a minified and compressed JSON file:

### Python API (recommended)

```python
import gzip
import json
import requests

url = "https://raw.githubusercontent.com/dandi-cache/content-id-to-nwb-files/refs/heads/min/derivatives/content_id_to_nwb_files.min.json.gz"
response = requests.get(url)
content_id_to_nwbfiles = json.loads(gzip.decompress(data=response.content))
```

### Save to file

```bash
curl https://raw.githubusercontent.com/dandi-cache/content-id-to-nwb-files/refs/heads/min/derivatives/content_id_to_nwb_files.min.json.gz -o content_id_to_nwb_files.min.json.gz
```



## Repeated use

If you plan on using this cache regularly, clone this repository:

```bash
git clone https://github.com/dandi-cache/content-id-to-nwb-files.git
```

Then set up a CRON on your system to pull the latest version of the cache at your desired frequency.

For example, through `crontab -e`, add:

```bash
0 0 * * * git -C /path/to/content-id-to-nwb-files pull
```

This will minimize data overhead by only loading the most recent changes.
