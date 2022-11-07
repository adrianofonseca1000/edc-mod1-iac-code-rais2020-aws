#!/usr/bin/env python

import glob
import boto3
import os

BUCKET_NAME = 'datalake-adriano-igti-edc-tf'
FOLDER_NAME = 'raw-data/data'

session = boto3.Session(profile_name='default')
s3 = session.client('s3')

files = glob.glob("data/rais/RAIS_*.txt")

for filename in files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename, key))
    s3.upload_file(filename, BUCKET_NAME, key)

print("All_Done")