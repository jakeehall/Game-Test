from pathlib import Path
import sys
import pygame


# Base path
# Supports:
# * PyInstaller executable
# * Development (running from source)
def _get_base_path():
    if getattr(sys, "frozen", False):
        # Running as PyInstaller executable
        return Path(sys._MEIPASS)
    # Running in development
    return Path(__file__).resolve().parents[2]


BASE_PATH = _get_base_path()
ASSETS_PATH = BASE_PATH / "assets"


# Internal caches
_image_cache = {}
_sound_cache = {}
_font_cache = {}


# Path helper
def asset_path(*parts):
    return ASSETS_PATH.joinpath(*parts)


# Image loading
def load_image(name, convert_alpha=True):
    if name in _image_cache:
        return _image_cache[name]

    path = asset_path("img", name)
    image = pygame.image.load(path)

    if convert_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()

    _image_cache[name] = image
    return image


# Sound loading
def load_sound(name):
    if name in _sound_cache:
        return _sound_cache[name]

    path = asset_path("sfx", name)
    sound = pygame.mixer.Sound(path)

    _sound_cache[name] = sound
    return sound


# Music loading (streamed)
# Usage:
# pygame.mixer.music.load(load_music("bg.mp3"))
def load_music(name):
    return asset_path("music", name)


# Font loading
def load_font(name, size):
    key = (name, size)

    if key in _font_cache:
        return _font_cache[key]

    path = asset_path("fonts", name)
    font = pygame.font.Font(path, size)

    _font_cache[key] = font
    return font


# Utility (Debug)
def print_paths():
    print("BASE_PATH:", BASE_PATH)
    print("ASSETS_PATH:", ASSETS_PATH)