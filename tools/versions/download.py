import sys
import os
import requests
from pathlib import Path
from typing import List, Optional, Union



def download(link, file_name, path, callback = None):
    Path(path).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(Path(os.path.join(path, file_name))):
        with open(os.path.join(path, file_name), "wb") as f:
            print("Downloading %s" % file_name)
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    callback(done)
                    #sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    #sys.stdout.flush()
    callback(100)
