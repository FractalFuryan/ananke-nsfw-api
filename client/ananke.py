import requests

class AnankeClient:
    def __init__(self, base_url: str):
        self.base = base_url.rstrip("/")

    def video(self, nonce: str, frames: int = 60):
        r = requests.post(
            f"{self.base}/v1/generate/video",
            params={"nonce": nonce, "frames": frames}
        )
        r.raise_for_status()
        return r.json()["frames"]

    def video_mp4(self, nonce: str):
        r = requests.post(
            f"{self.base}/v1/generate/video/mp4",
            params={"nonce": nonce}
        )
        r.raise_for_status()
        return r.content
