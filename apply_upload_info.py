# coding:utf-8
from __future__ import print_function
from vod_init import init_vod_service
from volcengine.vod.VodService import VodService
from volcengine.vod.models.request.request_vod_pb2 import VodApplyUploadInfoRequest

if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = init_vod_service()

    # Configure your Access Key ID (AK) and Secret Access Key (SK) in the environment variables or in the local ~/.volc/config file. For detailed instructions, see https://www.volcengine.com/docs/4/65646.
    # The SDK will automatically fetch the AK and SK from the environment variables or the ~/.volc/config file as needed.
    # During testing, you may use the following code snippet. However, do not store the AK and SK directly in your project code to prevent potential leakage and safeguard the security of all resources associated with your account.
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    space_name = 'hyys-lckj'

    try:
        req = VodApplyUploadInfoRequest()
        req.SpaceName = space_name

        resp = vod_service.apply_upload_info(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp.Result.Data)
            print(resp.Result.Data.UploadAddress.StoreInfos[0].StoreUri)
            print(resp.Result.Data.UploadAddress.StoreInfos[0].Auth)
            print(resp.Result.Data.UploadAddress.UploadHosts[0])
            print(resp.Result.Data.UploadAddress.SessionKey)
        else:
            print(resp.ResponseMetadata.Error)
            print(resp.ResponseMetadata.RequestId)