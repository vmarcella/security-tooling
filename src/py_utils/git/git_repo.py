import subprocess
from functools import lru_cache


@lru_cache(maxsize=1)
def get_root_location() -> str:
    """
    Return the absolute path of where the git repository is located.
    """

    try:
        root = subprocess.check_output("git rev-parse --show-toplevel", shell=True)
    except subprocess.CalledProcessError:
        raise IOError("Current working directory is not in a git repository")
    return root.decode("utf-8").strip()
