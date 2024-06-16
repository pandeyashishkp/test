from google.cloud import storage
import pathlib

app = Flask(__name__)

class ReadConfigFile:
    def __init__(self):
        self.config_file = ""

class GCSBucketDeletion:
    def __init__(self, *args, **kwargs):
        self.project        = kwargs['project']
        self.gcspath        = pathlib.Path(kwargs['gcspath']).parts[0]
        self.remaining_path = str(pathlib.Path(kwargs['gcspath']).parts[1:])
        self.client         = storage.Client(project=self.project)
        self.bucket         = self.client.bucket(self.gcspath)
    
    def _gcs_deletion(self):
        if self.remaining_path == '.':
            self.path = "workflows/"
        else:
            self.path = f"{self.remaining_path}/workflows"
        blobs = self.bucket.list_blobs(prefix=self.path)
        for blob in blobs:
            blob.delete()


if __name__ == '__main__':
    gcs = GCSBucketDeletion(project='ash11123', gcspath='ash11123')