import os
from pathlib import Path


mcDir = os.path.join(os.getenv('HOME'), '.cobalt') # type: ignore
objectsDir = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'assets', 'objects')) # type: ignore
libsDir = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'libraries')) # type: ignore
versionsDir = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'versions')) # type: ignore
