import librosa
import numpy as np
import soundfile as sf


class VoiceEnhancer:
    """
    الإصدار الأول من محرك تحسين الصوت.
    هذا الإصدار يبني البنية الأساسية،
    وسيتم إضافة الذكاء الاصطناعي الحقيقي إليه تدريجياً.
    """

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def load_audio(self, path):
        audio, sr = librosa.load(path, sr=self.sample_rate, mono=True)
        return audio, sr

    def normalize(self, audio):
        peak = np.max(np.abs(audio))
        if peak == 0:
            return audio
        return audio / peak

    def enhance(self, input_path, output_path):
        audio, sr = self.load_audio(input_path)

        # المرحلة الأولى:
        # تطبيع مستوى الصوت فقط
        enhanced = self.normalize(audio)

        sf.write(output_path, enhanced, sr)

        return {
            "status": "success",
            "input": input_path,
            "output": output_path,
            "sample_rate": sr
        }
