# coding:utf-8
from __future__ import print_function


from vod_init import init_vod_service
from volcengine.vod.models.request.request_vod_pb2 import *
from volcengine.vod.VodService import VodService

if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = init_vod_service()

    # Configure your Access Key ID (AK) and Secret Access Key (SK) in the environment variables or in the local ~/.volc/config file. For detailed instructions, see https://www.volcengine.com/docs/4/65646.
    # The SDK will automatically fetch the AK and SK from the environment variables or the ~/.volc/config file as needed.
    # During testing, you may use the following code snippet. However, do not store the AK and SK directly in your project code to prevent potential leakage and safeguard the security of all resources associated with your account.
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    try:
        req4 = VodUpdateMediaInfoRequest()
        req4.Vid = 'v0d361g10064ct24lq2ljhtf7rj8gge0'
        req4.Title.value = '米粉们小米直播间'
        req4.Description.value = '小米直播间的米粉们大家注意了'
        req4.Tags.value = '小米,米粉'
        req4.ClassificationId.value = 1731601509
        resp4 = vod_service.update_media_info(req4)
    except Exception:
        raise
    else:
        print(resp4)
        if resp4.ResponseMetadata.Error.Code == '':
            print('update media info success')
        else:
            print(resp4.ResponseMetadata.Error)