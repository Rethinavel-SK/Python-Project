# Tamil Music Platform 🎵

A modern, mood-based Tamil music streaming platform built with Django and MongoDB. Users can discover music based on their current mood, create playlists, and enjoy a Spotify-like streaming experience.

## Features ✨

### 🎭 Mood-Based Music Discovery
- **காதல் (Romance)** - Love songs and romantic melodies
- **மகிழ்ச்சி (Happy)** - Upbeat and celebration songs
- **சோகம் (Sad)** - Emotional and melancholic tracks
- **ஆற்றல் (Energetic)** - Motivational and workout music
- **அமைதி (Peaceful)** - Calm and relaxing tunes
- **நாஸ்டால்ஜியா (Nostalgic)** - Classic and memory-evoking songs
- **பக்தி (Devotional)** - Spiritual and religious music

### 🎵 Music Streaming Features
- **Audio Player** - Full-featured music player with play/pause/skip controls
- **Search** - Find songs by title, artist, or album
- **Favorites** - Save and manage your favorite songs
- **Recently Played** - Track your listening history
- **Playlists** - Create and manage custom playlists

### 👤 User Features
- **User Registration & Login** - Secure authentication system
- **User Profiles** - Personalized profiles with preferences
- **Mood Preferences** - Set favorite genres and moods
- **Listening Statistics** - Track total listening time

### 🎨 Modern UI/UX
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Dark Theme** - Easy on the eyes streaming interface
- **Spotify-like Design** - Familiar and intuitive user experience
- **Real-time Player** - Fixed bottom music player

## Technology Stack 🛠️

- **Backend**: Django 5.2.1 (Python)
- **Database**: MongoDB with PyMongo
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Audio**: HTML5 Audio API
- **Icons**: Font Awesome 6

## Project Structure 📁

```
tamil_music_platform/
├── manage.py
├── requirements.txt
├── populate_data.py
├── README.md
├── tamil_music_platform/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── music/                    # Music app
│   ├── models.py            # Song model
│   ├── views.py             # Music views
│   └── urls.py
├── users/                   # User management
│   ├── models.py            # UserProfile model
│   ├── views.py             # Auth views
│   └── urls.py
├── playlists/               # Playlist management
│   ├── models.py            # Playlist & MoodGenerator
│   ├── views.py
│   └── urls.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── music/
│   ├── users/
│   └── playlists/
└── static/                  # CSS, JS, Images
    ├── css/style.css
    ├── js/music-player.js
    └── images/
```

## Installation & Setup 🚀

### Prerequisites
- Python 3.8+
- MongoDB (local or cloud)
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd tamil_music_platform
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB
Make sure MongoDB is running on `localhost:27017` or update the connection string in `settings.py`.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Populate Sample Data
```bash
python populate_data.py
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Run the Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the platform!

## Usage Guide 📖

### For Users
1. **Register/Login** - Create an account or sign in
2. **Explore Moods** - Click on mood cards to discover music
3. **Search Music** - Use the search bar to find specific songs
4. **Play Music** - Click play buttons to start streaming
5. **Create Playlists** - Build custom playlists
6. **Manage Favorites** - Like songs to save them

### For Developers
- **Add Songs**: Use the `populate_data.py` script or admin interface
- **Customize Moods**: Modify `MOOD_MAPPINGS` in `playlists/models.py`
- **Styling**: Update `static/css/style.css` for UI changes
- **Player Features**: Extend `static/js/music-player.js`

## API Endpoints 🔌

- `POST /api/play/<song_id>/` - Play a song
- `POST /api/favorite/<song_id>/` - Toggle favorite status
- `GET /search/` - Search songs
- `GET /mood/<mood>/` - Get mood-based playlist

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Future Enhancements 🔮

- [ ] Audio file upload and storage
- [ ] Social features (follow users, share playlists)
- [ ] Advanced recommendation algorithms
- [ ] Mobile app development
- [ ] Lyrics display and synchronization
- [ ] Artist profiles and albums
- [ ] Music visualization
- [ ] Offline listening capability

## License 📄

This project is licensed under the MIT License.

## Support 💬

For questions or support, please open an issue on GitHub.

---

**Enjoy discovering Tamil music based on your mood! 🎵✨**
