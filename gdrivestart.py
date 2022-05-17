import sys
import time
import os
# [START storage_file_upload_from_memory]
from google.cloud import storage
from google.oauth2 import service_account

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\DeAndra Peoples\TFODCourse\capstoneprog-b5657215b26d.json"
#client = storage.Client.from_service_account_json(r"C:\Users\DeAndra Peoples\TFODCourse\capstoneprog_access_file.json")
#credentials = service_account.Credentials.from_service_account_file('C:/Users/DeAndra Peoples/TFODCourse/Tensorflow/workspace/images/collectedimages/capstoneprog_access_file.json',
                                                                   # scopes=['email'],
                                                                   # subject='deandrapeoples@gmail.com')
"C:/Users/DeAndra Peoples/TFODCourse/Tensorflow/workspace/images/collectedimages/capstoneprog_access_file.json"
client = storage.Client()
BUCKETS = list(client.list_buckets())
#print(BUCKETS)

def list_blobs(bucket_name, x):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs('capstone2022',prefix='collectedimages')

    for blob in blobs:
        x = x+1
        if x == 1:
            continue
        else:
        #blob = bucket.blob(blob.name)
            blob.download_to_filename(r'C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images'+'/'+ blob.name + '.jpg')
        #print(blob.name)

    #print(x-1)
    return x-1

def download_file():
    time.sleep(5)
    storage_client = storage.Client()
    bucket = storage_client.bucket('capstone2022', prefix='test') 
    blob = bucket.blob('microvid.mp4')
    blob.download_to_filename(r'C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\train\microvid.jpg')

def upload_file():
    client = storage.Client()
    bucket = client.bucket('capstone2022',prefix='test')
    blob = bucket.blob('servervid.mp4')
    blob.upload_from_filename(r"C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\train")

#for x in y:
  # bucket.blob.downlod_to_filename(r'C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\collectedimages')