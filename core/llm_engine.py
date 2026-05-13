import numpy as np
import pyaudio
import soundfile as sf
from typing import Callable, Optional
from threading import Thread, Event
from core.config import AudioConfig

class AudioProcessor:
    def __init__(self, config: AudioConfig):
        self.config = config
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.audio_buffer = []
        
    def start_recording(self, callback: Callable[[np.ndarray], None]):
        """Start recording audio in background"""
        self.is_recording = True
        
        def record():
            self.stream = self.p.open(
                format=pyaudio.paFloat32,
                channels=self.config.channels,
                rate=self.config.sample_rate,
                input=True,
                frames_per_buffer=self.config.chunk_size,
            )
            
            while self.is_recording:
                try:
                    data = self.stream.read(self.config.chunk_size, exception_on_overflow=False)
                    audio_chunk = np.frombuffer(data, dtype=np.float32)
                    callback(audio_chunk)
                except Exception as e:
                    print(f"Audio recording error: {e}")
                    
        thread = Thread(target=record, daemon=True)
        thread.start()
        
    def stop_recording(self):
        """Stop recording audio"""
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            
    def save_audio(self, filename: str, audio_data: np.ndarray):
        """Save audio to file"""
        sf.write(filename, audio_data, self.config.sample_rate)
        
    def load_audio(self, filename: str) -> np.ndarray:
        """Load audio from file"""
        data, sr = sf.read(filename)
        return data