#!/usr/bin/env python
"""
Simple startup script for Tamil Music Platform
This script will help you get started even if there are some dependency issues
"""

import os
import sys
import subprocess

def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("🎵 TAMIL MUSIC PLATFORM 🎵")
    print("=" * 60)
    print("A mood-based Tamil music streaming platform")
    print("Built with Django and MongoDB")
    print("=" * 60)
    print()

def check_python():
    """Check Python version"""
    print("✓ Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"  Python {version.major}.{version.minor}.{version.micro} - Please upgrade to Python 3.8+")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\n✓ Checking dependencies...")
    required_packages = ['django', 'pymongo']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  {package} - OK")
        except ImportError:
            print(f"  {package} - MISSING")
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies(missing_packages):
    """Install missing dependencies"""
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✓ Dependencies installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False
    return True

def setup_project():
    """Setup the Django project"""
    print("\n🔧 Setting up project...")
    
    # Create media and static directories
    os.makedirs('media', exist_ok=True)
    os.makedirs('media/audio', exist_ok=True)
    os.makedirs('media/covers', exist_ok=True)
    print("  Created media directories")
    
    # Try to run migrations
    try:
        print("  Running Django migrations...")
        subprocess.check_call([sys.executable, 'manage.py', 'migrate', '--run-syncdb'])
        print("  ✓ Migrations completed")
    except subprocess.CalledProcessError:
        print("  ⚠️  Migrations failed (this is OK for now)")
    
    return True

def populate_sample_data():
    """Populate with sample data"""
    print("\n🎵 Adding sample Tamil songs...")
    try:
        subprocess.check_call([sys.executable, 'populate_data.py'])
        print("  ✓ Sample data added successfully!")
    except subprocess.CalledProcessError:
        print("  ⚠️  Sample data population failed (you can add songs manually)")

def start_server():
    """Start the Django development server"""
    print("\n🚀 Starting Tamil Music Platform...")
    print("   Server will be available at: http://localhost:8000")
    print("   Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        subprocess.call([sys.executable, 'manage.py', 'runserver'])
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thank you for using Tamil Music Platform!")

def show_instructions():
    """Show usage instructions"""
    print("\n📖 QUICK START GUIDE:")
    print("-" * 30)
    print("1. Open your browser and go to: http://localhost:8000")
    print("2. Click on mood cards to discover Tamil songs")
    print("3. Use the search bar to find specific songs")
    print("4. Register an account to create playlists and save favorites")
    print("5. Click play buttons to start streaming music")
    print()
    print("🎭 Available Moods:")
    print("   • காதல் (Romance) - Love songs")
    print("   • மகிழ்ச்சி (Happy) - Upbeat songs")
    print("   • சோகம் (Sad) - Emotional songs")
    print("   • ஆற்றல் (Energetic) - Motivational songs")
    print("   • அமைதி (Peaceful) - Calm songs")
    print("   • நாஸ்டால்ஜியா (Nostalgic) - Classic songs")
    print("   • பக்தி (Devotional) - Spiritual songs")
    print()

def main():
    """Main function"""
    print_banner()
    
    # Check Python version
    if not check_python():
        sys.exit(1)
    
    # Check and install dependencies
    missing = check_dependencies()
    if missing:
        if not install_dependencies(missing):
            print("\n❌ Please install dependencies manually:")
            print(f"   pip install {' '.join(missing)}")
            sys.exit(1)
    
    # Setup project
    setup_project()
    
    # Populate sample data
    populate_sample_data()
    
    # Show instructions
    show_instructions()
    
    # Ask user if they want to start the server
    try:
        response = input("🚀 Start the server now? (y/n): ").lower().strip()
        if response in ['y', 'yes', '']:
            start_server()
        else:
            print("\n✓ Setup complete! Run 'python manage.py runserver' when ready.")
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled.")

if __name__ == '__main__':
    main()
