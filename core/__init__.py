"""
Voice Chatbot Core Module
Provides core functionality for the multiplatform voice chatbot
"""

from .config import Config, AudioConfig, ModelConfig
from .audio_processor import AudioProcessor
from .wake_word_engine import WakeWordEngine
from .stt_engine import STTEngine
from .llm_engine import LLMEngine
from .tts_engine import TTSEngine
from .chatbot import VoiceChatbot

__version__ = "0.1.0"
__all__ = [
    "Config",
    "AudioConfig",
    "ModelConfig",
    "AudioProcessor",
    "WakeWordEngine",
    "STTEngine",
    "LLMEngine",
    "TTSEngine",
    "VoiceChatbot",
]
