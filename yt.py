import os
import yt_dlp as youtube_dl
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def hex_to_rgb(hex_color):
    """Converte a cor hex para RGB."""
    hex_color = hex_color.lstrip('#')
    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))

def rgb_to_hex(rgb_color):
    """Converte a cor RGB para hex."""
    return f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}"

def gradient_text(text, start_color, end_color, length):
    """Cria um texto com gradiente de cor."""
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    gradient = Text()
    text_length = min(length, len(text))
    for i in range(text_length):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * (i / text_length))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * (i / text_length))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * (i / text_length))
        color = rgb_to_hex((r, g, b))
        gradient.append(text[i], style=color)

    if len(text) > length:
        gradient.append(text[length:], style=start_color)

    return gradient

def download_video(url, output_format):
    """Baixa o vídeo ou áudio do YouTube usando yt-dlp."""
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '/storage/emulated/0/Download/downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    if output_format == 'mp3':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        console.print(gradient_text("Download concluído!", "#ff0000", "#ffff00", 40))
    except Exception as e:
        console.print(gradient_text(f"Erro: {str(e)}", "#ff0000", "#ffff00", 40))

def display_menu():
    """Exibe o menu principal com gradiente de cores."""
    console.print(Panel(gradient_text("===== YouTube Downloader =====", "#ff0000", "#ffff00", 60), style="bold white"))

    console.print(gradient_text("1. Baixar Vídeo/Áudio do YouTube", "#ff0000", "#ffff00", 40))
    console.print(gradient_text("2. Informações do Desenvolvedor", "#ff0000", "#ffff00", 40))
    console.print(gradient_text("3. Canal do Telegram", "#ff0000", "#ffff00", 40))
    console.print(gradient_text("0. Sair", "#ff0000", "#ffff00", 40))

def display_dev_info():
    """Exibe informações do desenvolvedor."""
    dev_info = "Desenvolvedor: killerkingMD👑\nContato: paulohacker40@gmail.com"
    console.print(Panel(gradient_text(dev_info, "#ff0000", "#ffff00", 60), title="Informações do Desenvolvedor", style="bold green"))

def display_telegram_info():
    """Exibe informações do canal do Telegram."""
    telegram_info = "Canal do Telegram: https://t.me/kingApplicationspremium"
    console.print(Panel(gradient_text(telegram_info, "#ff0000", "#ffff00", 60), title="Canal do Telegram", style="bold green"))

def main():
    """Função principal para executar o script."""
    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            video_url = input("Insira a URL do vídeo do YouTube: ")
            output_format = input("Escolha o formato (mp3 ou mp4): ").lower()
            download_video(video_url, output_format)
            input("Pressione Enter para voltar ao menu principal...")
        elif choice == '2':
            display_dev_info()
            input("Pressione Enter para voltar ao menu principal...")
        elif choice == '3':
            display_telegram_info()
            input("Pressione Enter para voltar ao menu principal...")
        elif choice == '0':
            console.print(gradient_text("Saindo...", "#ff0000", "#ffff00", 40))
            break
        else:
            console.print(gradient_text("Opção inválida. Tente novamente.", "#ff0000", "#ffff00", 40))
            input("Pressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    main()
