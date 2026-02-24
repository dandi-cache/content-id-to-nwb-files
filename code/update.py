import gzip
import json
import pathlib

import requests
import yaml


def _run(base_directory: pathlib.Path, /) -> None:
    url = "https://raw.githubusercontent.com/dandi-cache/content-id-to-dandiset-paths/refs/heads/min/derivatives/content_id_to_dandiset_paths.min.json.gz"
    response = requests.get(url)
    content_id_to_dandiset_paths = json.loads(gzip.decompress(data=response.content))

    content_id_to_nwb_files: dict[str, dict[str, str]] = dict()
    for content_id, dandiset_paths in content_id_to_dandiset_paths.items():
        # Only test the first element and trust the rest
        first_path = next(iter(dandiset_paths.values()))[0]

        suffixes = pathlib.Path(first_path).suffixes
        if ".nwb" not in suffixes:
            continue

        content_id_to_nwb_files[content_id] = dandiset_paths

    with (base_directory / "derivatives" / "content_id_to_nwb_files.yaml").open(mode="w") as file_stream:
        yaml.safe_dump(data=content_id_to_nwb_files, stream=file_stream)


if __name__ == "__main__":
    repo_head = pathlib.Path(__file__).parent.parent

    _run(repo_head)
