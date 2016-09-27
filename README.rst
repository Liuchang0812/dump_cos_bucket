Cos Dumps Tool
=====================


INSTALL
------------

::

    pip install cos_dumps_file_list


USAGE
-------------------

::

    ubuntu@VM-72-138-ubuntu:~/dump_bucket_file_list$ cos_dumps -h
    usage: cos_dumps [-h] -b BUCKET -a APPID -i ACCESS_ID -k SECRET_KEY
                     [-o OUTPUT_FILE] [--with-directory]

                     optional arguments:
                       -h, --help            show this help message and exit
                         -b BUCKET, --bucket BUCKET
                                                 your bucket name(required)
          -a APPID, --appid APPID
                                  your appid(required)
          -i ACCESS_ID, --accesskey ACCESS_ID
                                  your accesskey(required)
          -k SECRET_KEY, --secretkey SECRET_KEY
                                  your secretkey(required)
          -o OUTPUT_FILE, --output OUTPUT_FILE
                                  file name that saves contents(default: stdout)
          --with-directory      dump file list with directory(default: False

