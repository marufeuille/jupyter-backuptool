import tarfile
import os
import datetime
import oss2

endpoint = 'http://oss-ap-northeast-1.aliyuncs.com'

accesskey   = os.environ["OSS_ACCESSKEY"] if "OSS_ACCESSKEY" in os.environ.keys() else ""
secretkey   = os.environ["OSS_SECRETKEY"] if "OSS_SECRETKEY" in os.environ.keys() else ""
bucket_name = os.environ["OSS_BUCKETNAME"] if "OSS_BUCKETNAME" in os.environ.keys() else ""
prefix      = os.environ["OSS_FILEPREFIX"] if "OSS_FILEPREFIX" in os.environ.keys() else ""

if accesskey == "" or secretkey == "" or bucket_name == "" or prefix == "":
    raise KeyError("Not such a key")

auth = oss2.Auth(accesskey, secretkey)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

target_dir = "/tmp/"
filename = "{}.tar.gz".format(datetime.datetime.now().strftime("%Y-%m-%d"))
with tarfile.open(target_dir + filename, 'w:gz') as tar:
    tar.add('/data')

with open(target_dir + filename, 'rb') as file:
    bucket.put_object(prefix + "-" + filename, file.read())
