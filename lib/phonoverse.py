import requests
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Set

# Exceptions
class PhonoVerseError(Exception): pass
class APIError(PhonoVerseError): pass
class ValidationError(PhonoVerseError): pass

# Data Models
@dataclass
class Translation:
    original_text: str
    translated_text: str
    source_language: str
    target_language: str
    mood: str
    timestamp: datetime = datetime.now()

# Constants
SUPPORTED_LANGUAGES: Set[str] = {
    "en", "es", "fr", "de", "it", "pt", "nl", "ru", "zh", "ja", "ko",
    "ar", "hi", "tr", "pl", "vi", "th", "id", "ms"
}

SUPPORTED_MOODS: Set[str] = {
    "neutral", "formal", "casual", "friendly", "professional",
    "humorous", "serious", "poetic"
}

# Main Client
class PhonoVerse:
    def __init__(self, base_url: str = "https://phonoverse.x10.bz"):
        self.base_url = base_url.rstrip('/')
        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://phonoverse.x10.bz',
            'Referer': 'https://phonoverse.x10.bz/app/'
        })

    def translate_text(self, text: str, from_lang: str, to_lang: str, mood: str = "neutral") -> Translation:
        # Validate inputs
        if from_lang not in SUPPORTED_LANGUAGES:
            raise ValidationError(f"Unsupported source language: {from_lang}")
        if to_lang not in SUPPORTED_LANGUAGES:
            raise ValidationError(f"Unsupported target language: {to_lang}")
        if mood.lower() not in SUPPORTED_MOODS:
            raise ValidationError(f"Unsupported mood: {mood}")
        
        try:
            response = self._session.post(
                f"{self.base_url}/app/api.php?action=translate",
                json={
                    "text": text,
                    "from": from_lang,
                    "to": to_lang,
                    "mood": mood
                }
            )
            response.raise_for_status()
            data = response.json()
            
            if "error" in data:
                raise APIError(data["error"])
                
            return Translation(
                original_text=text,
                translated_text=data["translation"],
                source_language=from_lang,
                target_language=to_lang,
                mood=mood
            )
            
        except requests.exceptions.RequestException as e:
            raise APIError(f"API request failed: {str(e)}")

    def get_supported_languages(self) -> Set[str]:
        """Get the set of supported languages"""
        return SUPPORTED_LANGUAGES.copy()

    def get_supported_moods(self) -> Set[str]:
        """Get the set of supported moods"""
        return SUPPORTED_MOODS.copy()
