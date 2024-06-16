from google.cloud import storage
import pathlib
from flask import Flask


app = Flask(__name__)

class ReadConfigFile:
    def __init__(self):
        self.config_file = ""

class GCSBucketDeletion:
    def __init__(self, *args, **kwargs):
        self.project        = kwargs['project']
        self.gcspath        = pathlib.Path(kwargs['gcspath']).parts[0]
        self.remaining_path = str(pathlib.Path(kwargs['gcspath']).parts[1:])
        self.path           = f"{self.remaining_path}/workflows/"
        self.client         = storage.Client(project=self.project)
        self.bucket         = self.client.bucket(self.gcspath)
    
    def _gcs_deletion(self):
        blobs = self.bucket.list_blobs(prefix=self.path)
        for blob in blobs:
            blob.delete()


if __name__ == '__main__':
    gcs = GCSBucketDeletion(project='ash11123', gcspath='ash11123')
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)