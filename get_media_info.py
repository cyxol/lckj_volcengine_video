# coding:utf-8
from __future__ import print_function
from vod_init import init_vod_service
from volcengine.vod.models.request.request_vod_pb2 import *


if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = init_vod_service()

    try:
        vids = 'v0d361g10064ct24lq2ljhtf7rj8gge0'
        req = VodGetMediaInfosRequest()
        req.Vids = vids
        resp = vod_service.get_media_infos(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp.Result)
        else:
            print(resp.ResponseMetadata.Error)
