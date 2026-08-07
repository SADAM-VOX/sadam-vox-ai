import librosa


class AudioService:

    def info(self, file_path: str):

        audio, sr = librosa.load(
            file_path,
            sr=None,
            mono=False
        )

        duration = librosa.get_duration(
            y=audio,
            sr=sr
        )

        channels = 1

        if len(audio.shape) > 1:
            channels = audio.shape[0]

        return {
            "duration": duration,
            "sample_rate": sr,
            "channels": channels
        }
