# coding:utf-8
from __future__ import print_function
from vod_init import init_vod_service

def get_video_url(vid, space_name):
    """
    获取视频播放 URL
    :param vid: 视频的 VID
    :param space_name: VOD 的空间名称
    :return: 视频播放链接列表
    """
    vod_service = init_vod_service()

    try:
        # 调用 VOD 接口获取播放信息
        response = vod_service.get_play_info({
            "SpaceName": space_name,
            "Vid": vid
        })

        # 检查响应状态
        if response['ResponseMetadata']['Error']['Code'] == '':
            play_info_list = response['Result']['PlayInfoList']
            urls = []
            for play_info in play_info_list:
                urls.append({
                    "definition": play_info['Definition'],
                    "url": play_info['MainPlayUrl']
                })
            return urls
        else:
            error_message = response['ResponseMetadata']['Error'].get('Message', '未知错误')
            print(f"获取视频信息失败，错误码: {response['ResponseMetadata']['Error']['Code']}, 错误信息: {error_message}")
            return None
    except Exception as e:
        print(f"发生异常: {e}")
        return None

if __name__ == "__main__":
    # 替换为您的视频 VID 和空间名
    vid = "v0d361g10064ct1djfaljhtbrd9ikglg"  # 示例 VID
    space_name = "hyys-lckj"  # 示例空间名

    # 获取视频 URL 列表
    video_urls = get_video_url(vid, space_name)
    if video_urls:
        print("视频播放链接：")
        for video in video_urls:
            print(f"清晰度: {video['definition']}, 播放链接: {video['url']}")
    else:
        print("未能获取到视频播放链接。")
