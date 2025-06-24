import schedule
import time
from downloader import download_file
from email_sender import send_email

def job():
    print("Iniciando tarefa agendada...")
    download_file()
    send_email()

def start_schedule():
    schedule.every().day.at("09:00").do(job)
    print("Agendador iniciado. Pressione Ctrl+C para encerrar.")
    while True:
        schedule.run_pending()
        time.sleep(60)
