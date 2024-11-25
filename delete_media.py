# coding:utf-8
from __future__ import print_function


from vod_init import init_vod_service
from volcengine.vod.models.request.request_vod_pb2 import *


if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = init_vod_service()



    try:
        vids = 'v0d361g10064ct1djfaljhtbrd9ikglg'
        callBackArgs = 'CallBackArgs'
        req5 = VodDeleteMediaRequest()
        req5.Vids = vids
        req5.CallbackArgs = callBackArgs
        resp5 = vod_service.delete_media(req5)
    except Exception:
        raise
    else:
        print(resp5)
        if resp5.ResponseMetadata.Error.Code == '':
            print('delete media info success')
        else:
            print(resp5.ResponseMetadata.Error)
