# coding:utf-8
from __future__ import print_function
from vod_init import init_vod_service

import os
import json

from volcengine.util.Functions import Function
from volcengine.vod.models.request.request_vod_pb2 import VodUploadMediaRequest

if __name__ == '__main__':
    # 创建 VOD 服务实
    vod_service = init_vod_service()

    # 上传的存储空间名称
    space_name = 'hyys-lckj'
    # project_name = 'media'

    # 视频文件路径
    file_path = os.path.abspath('media/米粉们小米直播间.m4v')  # 确保路径正确

    # 验证文件是否存在
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        exit(1)
    else:
        print(f"文件存在: {file_path}")

    # 定义功能函数
    get_meta_function = Function.get_meta_func()
    snapshot_function = Function.get_snapshot_func(2.3)
    get_start_workflow_func = Function.get_start_workflow_template_func(
        [{"TemplateIds": ["imp template id"], "TemplateType": "imp"},
         {"TemplateIds": ["  template id"], "TemplateType": "transcode"}])
    apply_function = Function.get_add_option_info_func(title="米粉",classification_id=1731601509,tags= "小米", description="小米米粉直播间", is_hls_index_only=True)

    try:
        # 创建上传请求
        req = VodUploadMediaRequest()
        req.SpaceName = space_name
        # req.ProjectName = project_name
        req.FilePath = file_path
        req.Functions = json.dumps([get_meta_function, snapshot_function, get_start_workflow_func])
        req.CallbackArgs = ''
        req.FileName = os.path.basename(file_path)  # 自动提取文件名
        req.FileExtension = os.path.splitext(file_path)[-1]  # 自动提取文件扩展名
        req.StorageClass = 1
        req.UploadHostPrefer = ''

        # 上传视频
        resp = vod_service.upload_media(req)
    except Exception as e:
        print(f"上传失败: {str(e)}")
        raise
    else:
        # 处理响应
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print("上传成功!")
            print(f"视频 ID: {resp.Result.Data.Vid}")
            print(f"视频封面 URI: {resp.Result.Data.PosterUri}")
            print(f"文件名: {resp.Result.Data.SourceInfo.FileName}")
            print(f"视频高度: {resp.Result.Data.SourceInfo.Height}")
            print(f"视频宽度: {resp.Result.Data.SourceInfo.Width}")
        else:
            print("上传错误:", resp.ResponseMetadata.Error)
            print("请求 ID:", resp.ResponseMetadata.RequestId)