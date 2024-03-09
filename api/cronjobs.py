import os
from django_cron import CronJobBase, Schedule
from apiclient.discovery import build
import apiclient
from .models import YtVideos
from yt_api import settings
from datetime import datetime, timedelta

class FetchYoutubeVideosCronJob(CronJobBase):
    RUN_INTERVAL_MINS = 5  # Runs every 5 minutes
    schedule = Schedule(run_every_mins=RUN_INTERVAL_MINS)
    code = 'test'  # Unique code for the cron job why we are using this code because we are using the same code in the settings.py file

    def do(self):
        api_keys = settings.GOOGLE_API_KEYS
        current_time = datetime.now()
        time_threshold = current_time - timedelta(minutes=5)

        for api_key in api_keys:
            try:
                youtube_service = build("youtube", "v3", developerKey=api_key)
                search_request = youtube_service.search().list(
                    q="cricket",
                    part="snippet",
                    order="date",
                    maxResults=50,
                    publishedAfter=(time_threshold.replace(microsecond=0).isoformat()+'Z')
                )
                search_response = search_request.execute()
                self.process_search_results(search_response)
                break  # Exit loop if successful
            except apiclient.errors.HttpError as err:
                status_code = err.resp.status
                if status_code not in (400, 403):
                    break

    def process_search_results(self, response):
        for item in response.get('items', []):
            video_id = item.get('id', {}).get('videoId', '')
            published_datetime = item.get('snippet', {}).get('publishedAt', '')
            title = item.get('snippet', {}).get('title', '')
            description = item.get('snippet', {}).get('description', '')
            thumbnails_url = item.get('snippet', {}).get('thumbnails', {}).get('default', {}).get('url', '')
            channel_id = item.get('snippet', {}).get('channelId', '')
            channel_title = item.get('snippet', {}).get('channelTitle', '')

            # Create a video object in the database
            YtVideos.objects.create(
                video_id=video_id,
                titles=title,
                desc=description,
                publishersDate=published_datetime,
                thumbnails=thumbnails_url,
                chnl_id=channel_id,
                chnl_title=channel_title
            )
