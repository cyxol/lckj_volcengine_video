# coding:utf-8
from __future__ import print_function

import json
from vod_init import init_vod_service
from volcengine.util.Functions import Function

from volcengine.const.Const import *
from volcengine.vod.models.request.request_vod_pb2 import VodUploadMaterialRequest

if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = init_vod_service()


    space_name = 'hyys-lckj'
    file_path = 'material/米粉们小米直播间素材.m4v'

    get_meta_function = Function.get_meta_func()
    snapshot_function = Function.get_snapshot_func(2.3)
    add_option_function = Function.get_add_material_option_info_func(title='素材测试视频', tags='test',
                                                                     description='素材测试，视频文件',
                                                                     category=CATEGORY_VIDEO, record_type=2,
                                                                     format_input='m4v')

    try:
        req = VodUploadMaterialRequest()
        req.FileType = FILE_TYPE_MEDIA
        req.SpaceName = space_name
        req.FilePath = file_path
        req.Functions = json.dumps([get_meta_function, snapshot_function, add_option_function])
        req.CallbackArgs = ''
        req.FileExtension = '.m4v'
        req.UploadHostPrefer = ''

        resp = vod_service.upload_material(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp.Result.Data)
            print(resp.Result.Data.Mid)
            print(resp.Result.Data.PosterUri)
            print(resp.Result.Data.SourceInfo.FileName)
            print(resp.Result.Data.SourceInfo.Height)
            print(resp.Result.Data.SourceInfo.Width)
        else:
            print(resp.ResponseMetadata.Error)
            print(resp.ResponseMetadata.RequestId)
