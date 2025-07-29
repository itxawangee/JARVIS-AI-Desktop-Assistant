# Jarvis Ai Desktop Assistant 🤖🎙️

A voice assistant with speech recognition and AI capabilities, designed to understand local English/Urdu mixed speech patterns.


## Features ✨

- 🎤 Voice commands with Pakistani accent support
- 🔊 Text-to-speech with desi tone
- 🔍 Wikipedia knowledge queries
- 🌐 Web searches (Google/YouTube)
- 🎵 YouTube music playback
- 🤖 Two interaction modes (Voice/Text)

## Installation 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/itxawangee/JARVIS-AI-Desktop-Assistant.git
   
   ```

2. **Install dependencies** (auto-installs on first run, or manually):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jarvis**:
   ```bash
   python jarvis.py
   ```

## System Requirements 💻

| Component | Requirement |
|-----------|-------------|
| OS        | Windows 10/11, macOS, Linux |
| Python    | 3.8+        |
| RAM       | 4GB minimum |
| Storage   | 100MB free  |
| Internet  | Required    |

## Usage Guide 📖

### Basic Commands:
```plaintext
"Jarvis, who is [person]?"
"Jarvis, what is [topic]?"
"Jarvis, search in google for [query]"
"Jarvis, search in youtube for [video]"
"Jarvis, music on youtube [song]"
```

### Modes:
1. **Text Mode**: Type commands after selecting option 1
2. **Voice Mode**: Speak commands after selecting option 2 (recommended)

## Project Structure 📂

```
jarvis-voice-assistant/
├── Engine/
│   ├── STT.py        # Speech-to-text processing
│   └── TTS.py        # Text-to-speech engine
├── Brain/
│   └── Brain.py      # Query processing logic
├── requirements.txt  # Dependencies
└── jarvis.py         # Main application
```

## Troubleshooting ⚠️

| Issue | Solution |
|-------|----------|
| Microphone not working | Check system permissions |
| Slow responses | Ensure good internet connection |
| Installation errors | Run `pip install --upgrade pip` first |
| Accent not recognized | Speak clearly with short phrases |

## Contributing 🤝

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

For support or questions:
- Email: akrashnoor@gmail.com
- Phone: +92 311 5459380

---

Made by Akrash Noor | © 2023 Jarvis Assistant Project
```
