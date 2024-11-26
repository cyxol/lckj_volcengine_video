from volcengine.vod.VodService import VodService
from vod_init import init_vod_service

# 查询未发布的视频信息
def get_unpublished_videos(vod_service: VodService):
    params = {
        "PageNo": 1,
        "PageSize": 100,  # 分页大小
        "Status": "Unpublished"  # 未发布的状态
    }

    all_unpublished_videos = []
    try:
        while True:
            response = vod_service.get_media_list(params)
            videos = response.get("Result", {}).get("MediaList", [])
            all_unpublished_videos.extend(videos)

            # 检查是否还有下一页
            if len(videos) < params["PageSize"]:
                break

            params["PageNo"] += 1

        return all_unpublished_videos
    except Exception as e:
        print(f"Error fetching unpublished videos: {e}")
        return []

if __name__ == "__main__":
    # 替换为您的 AccessKey 和 SecretKey

    vod_service = init_vod_service()
    from vod_init import init_vod_service
    unpublished_videos = get_unpublished_videos(vod_service)

    # 打印未发布的视频信息
    for video in unpublished_videos:
        print(f"Video ID: {video.get('Vid')}, Title: {video.get('Title')}, Status: {video.get('Status')}")
    print(f"Total unpublished videos: {len(unpublished_videos)}")
