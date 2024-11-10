from setuptools import setup

APP = ['qr.py']  # Replace with your Python script name
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'qrcode',       # QR code library
        'PIL',          # Pillow (Image handling)
        'IPython',      # IPython (conditional imports in code)
        'PyQt5',        # PyQt5 (GUI)
        'lxml',         # XML parsing
        'colorama',     # Color handling in terminal
        'numpy',        # Numerical operations
        'pytest',       # Testing library (if needed)
        'defusedxml',   # Safe XML handling
        'pkg_resources',# Package resources
        'win32com',     # Windows COM API (only needed if on Windows)
    ],
    #'debug': True,  # Enable debugging to see more output
    'iconfile': 'icon.icns',  # Optional: add an icon if you have one
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

