from crewai_tools import YoutubeChannelSearchTool

def get_youtube_tool(channel_handle: str):
    if channel_handle.strip():
        if not channel_handle.startswith('@'):
            channel_handle = '@' + channel_handle
        return YoutubeChannelSearchTool(youtube_channel_handle=channel_handle)
    return None