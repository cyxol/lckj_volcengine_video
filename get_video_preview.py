# coding:utf-8
import logging
from vod_init import init_vod_service

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_video_preview(vid, space_name):

    vod_service = init_vod_service()

    try:
        # 调用 VOD 接口获取视频信息
        response = vod_service.get_media_infos({
                    "SpaceName": space_name,
                    "Vid": vid
                })


        # 检查响应状态
        if response['ResponseMetadata']['Error']['Code'] == '':
            base_info = response['Result']['BaseInfo']
            preview_url = base_info.get('PosterUrl', None)  # 获取视频的封面图 URL
            if preview_url:
                logging.info(f"视频封面图 URL: {preview_url}")
                return preview_url
            else:
                logging.warning("未找到视频封面图 URL。")
                return None
        else:
            error_message = response['ResponseMetadata']['Error'].get('Message', '未知错误')
            logging.error(f"获取视频信息失败，错误码: {response['ResponseMetadata']['Error']['Code']}, 错误信息: {error_message}")
            return None
    except Exception as e:
        logging.exception("获取视频预览时发生异常")
        return None

if __name__ == "__main__":
    # 替换为您的视频 VID 和空间名
    vid = "v0d361g10064ct1djfaljhtbrd9ikglg"  # 示例 VID
    space_name = "hyys-lckj"  # 示例空间名

    # 获取视频预览图 URL
    preview_url = get_video_preview(vid, space_name)
    if preview_url:
        logging.info(f"视频预览图 URL: {preview_url}")
    else:
        logging.warning("未能获取到视频预览图 URL。")
