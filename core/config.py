import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class WakeWordConfig:
    model: str = os.getenv("WAKE_WORD_MODEL", "openwakeword")
    word: str = os.getenv("WAKE_WORD", "jarvis")
    sensitivity: float = float(os.getenv("WAKE_WORD_SENSITIVITY", "0.5"))

@dataclass
class AudioConfig:
    sample_rate: int = int(os.getenv("SAMPLE_RATE", "16000"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "512"))
    channels: int = int(os.getenv("CHANNELS", "1"))

@dataclass
class STTConfig:
    provider: str = os.getenv("STT_PROVIDER", "openai")
    model: str = os.getenv("STT_MODEL", "whisper-1")
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")

@dataclass
class LLMConfig:
    provider: str = os.getenv("LLM_PROVIDER", "ollama")
    model: str = os.getenv("LLM_MODEL", "mistral")
    host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")

@dataclass
class TTSConfig:
    provider: str = os.getenv("TTS_PROVIDER", "piper")
    voice: str = os.getenv("TTS_VOICE", "en_US-ryan-high")

@dataclass
class AppConfig:
    wake_word: WakeWordConfig = WakeWordConfig()
    audio: AudioConfig = AudioConfig()
    stt: STTConfig = STTConfig()
    llm: LLMConfig = LLMConfig()
    tts: TTSConfig = TTSConfig()
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"