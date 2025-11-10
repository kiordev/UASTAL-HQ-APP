import os

# Словарь тем с параметрами
THEME_MAP = {
    "Класична тема": {
        "dark": "#090040",
        "semi": "#471396",
        "light": "#B13BFF",
        "accent": "#FFCC00",
        "accent_light": "#FFE166",
        "white": "#FFFFFF",
        "navigationbar" : "#B13BFF",
    },
    "Амазонський папуга": {
        "dark": "#FFE600",
        "semi": "#00B919",
        "light": "#33A1FD",
        "accent": "#007BFF",
        "accent_light": "#33A1FD",
        "white": "#FFFFFF",
        "navigationbar" : "#00B919",
    },
    "Зимова меланхолія": {
        "dark": "#2C2C2C",
        "semi": "#616161",
        "light": "#A0A0A0",
        "accent": "#A2CFFF",
        "accent_light": "#0F93FF",
        "white": "#FFFFFF",
        "navigationbar" :"#A0A0A0",
    },
    "Зелений ананасік": {
        "dark": "#573800",
        "semi": "#585300",
        "light": "#AA790E",
        "accent": "#00B909",
        "accent_light": "#00FF0D",
        "white": "#EEFFA3",
        "navigationbar" : "#AA790E",
    },
    "Linkin Park From Zero": {
        "dark": "#324139",
        "semi": "#000000",
        "light": "#F892FC",
        "accent": "#D321C4",
        "accent_light": "#EFC774",
        "white": "#F3F3F3",
        "navigationbar" : "#F892FC",
    },
    "3-й Армійський корпус": {
        "dark": "#000000",
        "semi": "#FF9900",
        "light": "#FF9900",
        "accent": "#FF9900",
        "accent_light": "#FF9900",
        "white": "#FFFFFF",
        "navigationbar" : "#FF9900",
    },
}

SETTINGS_FILE = "theme.txt"
DEFAULT_THEME = "Класична тема"

def get_selected_theme():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return f.read().strip() or DEFAULT_THEME
    return DEFAULT_THEME

current_theme_name = get_selected_theme()
_current = THEME_MAP.get(current_theme_name, THEME_MAP[DEFAULT_THEME])

# Глобальные переменные для всего проекта:
dark = _current["dark"]
semi = _current["semi"]
light = _current["light"]
accent = _current["accent"]
accent_light = _current["accent_light"]
white = _current["white"]
navigationbar = _current["navigationbar"]
