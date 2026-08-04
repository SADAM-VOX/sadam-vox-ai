from pathlib import Path
import subprocess
import tempfile
import shutil


class NoiseEngine:
    """
    DeepFilterNet Engine
    """

    def __init__(self):
        self.model = "DeepFilterNet"

    def process(self, input_file: str):

        input_path = Path(input_file)

        output_dir = tempfile.mkdtemp()

        command = [
            "deepFilter",
            str(input_path),
            "-o",
            output_dir
        ]

        subprocess.run(command)

        output_file = Path(output_dir) / input_path.name

        if not output_file.exists():
            raise Exception("Noise removal failed")

        return str(output_file)
