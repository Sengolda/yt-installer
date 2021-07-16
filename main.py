import youtube_dl
from youtube_search import YoutubeSearch
import click

ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'file.mp3',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
}

@click.command()
@click.option("--query","-q")
def downloader(query):
    results = YoutubeSearch(str(query), max_results=1).to_dict()
    id = results[0].get("id")
    url = "https://www.youtube.com/watch?v="+str(id)
    click.echo("Done, the install has started.")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([id])
    
    click.echo("Finished installing.")


if __name__ == "__main__":
    downloader()