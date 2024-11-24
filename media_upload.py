# coding:utf-8
from __future__ import print_function

import json
import os
import configparser

from volcengine.util.Functions import Function
from volcengine.vod.VodService import VodService
from volcengine.vod.models.request.request_vod_pb2 import VodUploadMediaRequest

if __name__ == '__main__':
    # 创建 VOD 服务实例
    vod_service = VodService('cn-north-1')
    config_path = os.path.join(os.path.expanduser("~"), ".volc", "config")
    if not os.path.exists(config_path):
        print(f"配置文件不存在: {config_path}")
        exit(1)
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_path)

    # 从配置文件中获取 AK 和 SK
    ak = config.get('default', 'ak')
    sk = config.get('default', 'sk')

    # 设置 AK 和 SK（推荐使用环境变量）
    vod_service.set_ak(ak)
    vod_service.set_sk(sk)

    # 上传的存储空间名称
    space_name = 'hyys-lckj'

    # 视频文件路径
    file_path = 'media/米粉们小米直播间.m4v'  # 确保路径正确

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
         {"TemplateIds": ["transcode template id"], "TemplateType": "transcode"}])
    apply_function = Function.get_add_option_info_func("title1", "tag1", "desc1", 0, False)

    try:
        # 创建上传请求
        req = VodUploadMediaRequest()
        req.SpaceName = space_name
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