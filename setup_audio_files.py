#!/usr/bin/env python
"""
Audio Files Setup Guide for Tamil Music Platform
This script helps you organize and add actual Tamil song files to your platform.
"""

import os
import sys
import django
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tamil_music_platform.settings')
django.setup()

from music.models import Song

def setup_audio_directories():
    """Create necessary directories for audio files"""
    
    print("🎵 Tamil Music Platform - Audio Setup Guide")
    print("=" * 50)
    
    # Create media directories
    media_root = Path('media')
    audio_dir = media_root / 'audio' / 'songs'
    covers_dir = media_root / 'images' / 'covers'
    
    # Create directories if they don't exist
    audio_dir.mkdir(parents=True, exist_ok=True)
    covers_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Created audio directory: {audio_dir}")
    print(f"✅ Created covers directory: {covers_dir}")
    
    return audio_dir, covers_dir

def create_sample_audio_structure():
    """Create sample directory structure for organizing Tamil songs"""
    
    audio_dir, covers_dir = setup_audio_directories()
    
    # Create mood-based subdirectories
    moods = [
        'romantic',  # காதல்
        'happy',     # மகிழ்ச்சி
        'sad',       # சோகம்
        'energetic', # ஆற்றல்
        'peaceful',  # அமைதி
        'nostalgic', # நாஸ்டால்ஜியா
        'devotional' # பக்தி
    ]
    
    for mood in moods:
        mood_dir = audio_dir / mood
        mood_dir.mkdir(exist_ok=True)
        print(f"📁 Created mood directory: {mood_dir}")
        
        # Create a README file with instructions
        readme_file = mood_dir / 'README.txt'
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(f"""
Tamil Music Platform - {mood.title()} Songs Directory

Instructions:
1. Add your {mood} Tamil song files (.mp3, .wav, .m4a) to this directory
2. Use clear, descriptive filenames (e.g., "Vennilave_Vennilave.mp3")
3. Ensure files are properly encoded and not corrupted
4. Recommended format: MP3, 128-320 kbps
5. Maximum file size: 10MB per song

Example files for {mood} mood:
- Song_Title_Artist_Name.mp3
- Another_Song_Title.mp3

Note: Make sure you have proper rights to use these audio files.
""")
    
    return audio_dir, covers_dir

def update_songs_with_audio_paths():
    """Update existing songs in database with proper audio file paths"""
    
    print("\n🎶 Updating song database with audio file paths...")
    
    # Sample mapping of songs to audio files
    song_audio_mapping = {
        'Vennilave Vennilave': 'romantic/Vennilave_Vennilave.mp3',
        'Munbe Vaa': 'romantic/Munbe_Vaa.mp3',
        'Kadhal Rojave': 'romantic/Kadhal_Rojave.mp3',
        'Rowdy Baby': 'happy/Rowdy_Baby.mp3',
        'Vaathi Coming': 'energetic/Vaathi_Coming.mp3',
        'Kolaveri Di': 'happy/Kolaveri_Di.mp3',
        'Kannazhaga': 'sad/Kannazhaga.mp3',
        'Thalli Pogathey': 'sad/Thalli_Pogathey.mp3',
        'Aalaporan Tamizhan': 'energetic/Aalaporan_Tamizhan.mp3',
        'Pudhu Vellai Mazhai': 'nostalgic/Pudhu_Vellai_Mazhai.mp3'
    }
    
    # Get all songs from database
    all_songs = Song.get_all()
    updated_count = 0
    
    for song in all_songs:
        if song.title in song_audio_mapping:
            # Update the song with audio file path
            audio_path = f"/media/audio/songs/{song_audio_mapping[song.title]}"
            
            # Update in MongoDB
            Song.update_by_id(str(song._id), {
                'file_path': audio_path,
                'cover_image': f"/media/images/covers/{song.title.replace(' ', '_')}.jpg"
            })
            
            print(f"✅ Updated: {song.title} -> {audio_path}")
            updated_count += 1
    
    print(f"\n🎵 Updated {updated_count} songs with audio file paths")

def create_audio_upload_guide():
    """Create a comprehensive guide for adding audio files"""
    
    guide_content = """
# Tamil Music Platform - Audio Files Setup Guide

## 📁 Directory Structure
```
media/
├── audio/
│   └── songs/
│       ├── romantic/          # காதல் songs
│       ├── happy/             # மகிழ்ச்சி songs  
│       ├── sad/               # சோகம் songs
│       ├── energetic/         # ஆற்றல் songs
│       ├── peaceful/          # அமைதி songs
│       ├── nostalgic/         # நாஸ்டால்ஜியா songs
│       └── devotional/        # பக்தி songs
└── images/
    └── covers/                # Album cover images
```

## 🎵 Adding Tamil Songs

### Step 1: Prepare Your Audio Files
- **Format**: MP3, WAV, or M4A
- **Quality**: 128-320 kbps (MP3 recommended)
- **Size**: Maximum 10MB per file
- **Naming**: Use clear names (e.g., "Vennilave_Vennilave.mp3")

### Step 2: Organize by Mood
Place songs in appropriate mood directories:
- **romantic/**: Love songs, romantic melodies
- **happy/**: Upbeat, joyful songs
- **sad/**: Emotional, melancholic songs
- **energetic/**: High-energy, motivational songs
- **peaceful/**: Calm, relaxing songs
- **nostalgic/**: Classic, memory-evoking songs
- **devotional/**: Spiritual, religious songs

### Step 3: Add Cover Images
- Place album covers in `media/images/covers/`
- **Format**: JPG, PNG (JPG recommended)
- **Size**: 300x300px to 1000x1000px
- **Naming**: Match song title (e.g., "Vennilave_Vennilave.jpg")

### Step 4: Update Database
Run the update script to link audio files to songs:
```bash
python setup_audio_files.py
```

## 🎶 Popular Tamil Songs to Add

### Romantic (காதல்)
- Vennilave Vennilave - Minsara Kanavu
- Munbe Vaa - Sillunu Oru Kaadhal
- Kadhal Rojave - Roja
- Nenjukkul Peidhidum - Vaaranam Aayiram
- Maruvaarthai Pesadhey - Enai Noki Paayum Thota

### Happy (மகிழ்ச்சி)
- Rowdy Baby - Maari 2
- Kolaveri Di - 3
- Yaaradi Nee Mohini - Yaaradi Nee Mohini
- Chinna Chinna Aasai - Roja

### Energetic (ஆற்றல்)
- Vaathi Coming - Master
- Aalaporan Tamizhan - Mersal
- Beast Mode - Beast
- Kutti Story - Master

### Sad (சோகம்)
- Kannazhaga - 3
- Thalli Pogathey - Achcham Yenbadhu Madamaiyada
- Oru Maalai - Ghajinikanth

### Nostalgic (நாஸ்டால்ஜியா)
- Pudhu Vellai Mazhai - Roja
- Vinnaithandi Varuvaaya - Vinnaithandi Varuvaaya
- Ilamai Thirumbudhe - Punnagai Mannan

## ⚖️ Legal Considerations
- Ensure you have proper rights to use audio files
- Use royalty-free music or properly licensed content
- Consider using Creative Commons licensed Tamil music
- For commercial use, obtain proper licensing

## 🔧 Technical Notes
- Audio files are served from `/media/audio/songs/`
- Cover images are served from `/media/images/covers/`
- The platform supports MP3, WAV, and M4A formats
- Files are streamed directly to the browser's audio player

## 🚀 Testing Your Setup
1. Add a few sample audio files to the directories
2. Restart the Django server
3. Click play buttons on the website
4. Check browser console for any audio loading errors

## 📞 Troubleshooting
- **Audio not playing**: Check file format and path
- **Files not found**: Verify directory structure
- **Slow loading**: Optimize file sizes (use 128-192 kbps MP3)
- **Browser issues**: Test in different browsers

Happy listening! 🎵
"""
    
    with open('AUDIO_SETUP_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print("📖 Created comprehensive audio setup guide: AUDIO_SETUP_GUIDE.md")

def main():
    """Main setup function"""
    
    try:
        # Create directory structure
        audio_dir, covers_dir = create_sample_audio_structure()
        
        # Update songs in database
        update_songs_with_audio_paths()
        
        # Create setup guide
        create_audio_upload_guide()
        
        print("\n" + "="*50)
        print("🎵 SETUP COMPLETE!")
        print("="*50)
        print(f"📁 Audio directory: {audio_dir.absolute()}")
        print(f"🖼️  Covers directory: {covers_dir.absolute()}")
        print("📖 Setup guide: AUDIO_SETUP_GUIDE.md")
        print("\nNext steps:")
        print("1. Add your Tamil song files to the mood directories")
        print("2. Add cover images to the covers directory")
        print("3. Restart the Django server")
        print("4. Test audio playback on the website")
        print("\n🎶 Enjoy your Tamil music platform!")
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
