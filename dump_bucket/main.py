from __future__ import unicode_literals, print_function
from argparse import ArgumentParser
from qcloud_cos import CosClient, ListFolderRequest
import sys
from logging import getLogger, basicConfig, DEBUG, INFO

basicConfig(level=INFO, stream=sys.stdout)
logger = getLogger('__name__')

def dfs_(client, appid, bucket, path,max_retry=5, with_dir=True, file=sys.stdout):
    logger.info("try to dump file list under {}".format(path))

    _finish = False
    _context = u''
    while not _finish:
        request = ListFolderRequest(bucket_name=bucket, cos_path=path, context=_context)
        ret = client.list_folder(request)

        logger.debug(str(ret))

        if ret['code'] != 0:
            logger.warning("request failed: {}".format(str(ret)))
            max_retry -= 1
        else:
            _finish = not ret['data']['has_more']
            _context = ret['data']['context']
            for item in ret['data']['infos']:
                if 'filelen' in item:
                    # file
                    file.write("/{appid}/{bucket}{prefix}{filename}\n".format(appid=appid, bucket=bucket, prefix=path, filename=item['name']))
                else:
                    _sub_dir = "{prefix}{filename}/".format(prefix=path, filename=item['name'])
                    if with_dir:
                        file.write("/{appid}/{bucket}{path}\n".format(appid=appid, bucket=bucket, path=_sub_dir))

                    dfs_(client, appid, bucket, _sub_dir, max_retry, with_dir, file)
                    # directory

        if max_retry == 0:
            _finish = True
            logger.error("reach max retry times, finish this directory {}".format(path))

    logger.info("finish directory {}".format(path))

def dumps_file_list(opt):

    # create cos client
    client = CosClient(appid=opt.appid, secret_id=opt.access_id, secret_key=opt.secret_key)
    import os 
    print(os.getcwd())
    if opt.output_file == "-":
        _file = sys.stdout
    else:
        _file = open(opt.output_file, 'w') 

    dfs_(client, opt.appid, opt.bucket, '/', with_dir=opt.with_directory, file=_file)


def _main():
    parse = ArgumentParser()

    parse.add_argument('-b', '--bucket', dest='bucket', required=True, help='your bucket name(required)', type=unicode)
    parse.add_argument('-a', '--appid', dest='appid', required=True, help='your appid(required)', type=int)
    parse.add_argument('-i', '--accesskey', dest='access_id', required=True, help='your accesskey(required)', type=unicode)
    parse.add_argument('-k', '--secretkey', dest='secret_key', required=True, help='your secretkey(required)', type=unicode)
    parse.add_argument('-o', '--output', dest='output_file', default='-', help='file name that saves contents(default: stdout)')
    parse.add_argument('--with-directory', dest='with_directory', default=False, action='store_true', help='dump file list with directory(default: False')
    opt = parse.parse_args()

    dumps_file_list(opt)

if __name__ == '__main__':
    _main()
