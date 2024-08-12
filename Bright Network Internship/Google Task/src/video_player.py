"""A video player class."""

from .video_library import VideoLibrary
import random
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = None
        self.current_video_state = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        unsorted_videos = []
        sorted_videos = []
        print("Here's a list of all available videos: ")

        for video in videos:
            tags = "["

            for tag in video.tags:
                tags += tag + " "
            
            tags = tags.strip()
            tags += "]"
            unsorted_videos += [f"{video._title} ({video.video_id}) {tags}"]
        sorted_videos = sorted(unsorted_videos)

        for video in sorted_videos:
            print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video != None:
            if(self.current_video != None and self.current_video != video):
                previous_video = self.current_video
                print("Playing video: " f"{previous_video._title}")
                print("Stopping video: " f"{previous_video._title}")
                self.current_video = video
                self.current_video_state = "playing"
                print("Playing video: " f"{video._title}")
            else: 
                self.current_video = video
                self.current_video_state = "playing"
                print("Playing video: " f"{video._title}")
        elif(video == None and self.current_video != None):
            print("Playing video: " f"{self.current_video._title}")
            print("Cannot play video: Video does not exist")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.current_video != None:
            video = self.current_video
            if self.current_video_state == "playing":
                print("Stopping video: " f"{video._title}")
                self.current_video = None
                self.current_video = None
            else:
                print("Cannot stop video: No video is currently playing")
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        random_index = random.randrange(len(videos))
        random_video = videos[random_index]
        video = self._video_library.get_video(random_video.video_id)
        if(self.current_video != None):
            previous_video = self.current_video
            print("Playing video: " f"{previous_video._title}")
            print("Stopping video: " f"{previous_video._title}")
            print("Playing video: " f"{video._title}")
            self.current_video = video
            self.current_video_state = "playing"
        else:
            print("Playing video: " f"{video._title}")
            self.current_video = video
            self.current_video_state = "playing"
    def pause_video(self):
        """Pauses the current video."""
        if self.current_video != None:
            video = self.current_video
            if self.current_video_state == "playing":
                self.current_video_state = "pausing"
                print("Pausing video: " f"{video._title}")
            else:
                print("Video already paused: " f"{video._title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current_video != None:
            video = self.current_video
            if self.current_video_state == "pausing":
                self.current_video_state = "playing"
                print("Continuing video: " f"{video._title}")
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self.current_video != None:
            video = self.current_video
            tags = "["
            for tag in video.tags:
                tags += tag + " "
            
            tags = tags.strip()
            tags += "]"
            if(self.current_video_state == "playing"):
                print("Currently playing: " f"{video._title} ({video.video_id}) {tags}")
            else:
                print("Currently playing: " f"{video._title} ({video.video_id}) {tags} - PAUSED")
        else :
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
