# coding:utf-8
from __future__ import print_function
from vod_init import init_vod_service
from volcengine.vod.models.request.request_vod_pb2 import *


if __name__ == '__main__':
    vod_service = init_vod_service()

    try:
        vid = 'v0d361g10064ct1djfaljhtbrd9ikglg'
        status = 'Published'
        req3 = VodUpdateMediaPublishStatusRequest()
        req3.Vid = vid
        req3.Status = status
        resp3 = vod_service.update_media_publish_status(req3)
    except Exception:
        raise
    else:
        print(resp3)
        if resp3.ResponseMetadata.Error.Code == '':
            print('update media publish status success')
        else:
            print(resp3.ResponseMetadata.Error)