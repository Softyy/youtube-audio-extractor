from setuptools import setup 
  
setup( 
    name='youtube_audio', 
    version='0.1', 
    description='Download the audio of youtube videos as mp3\'s', 
    author='Chris Adkins', 
    author_email='chris@cjadkins.com', 
    packages=['youtube_audio'], 
    install_requires=[ 
        'typer',
        'yt_dlp',
    ], 
) 