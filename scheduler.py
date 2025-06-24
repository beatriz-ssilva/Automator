import schedule
import time
from downloader import download_file
from email_sender import send_email

def job():
    print("Executando tarefa programada...")
    try:
        download_file()
        send_email()
        print("Tarefa concluída com sucesso.\n")
    except Exception as e:
        print(f"Falha na execução da tarefa: {e}")

def start_schedule():
    schedule.every().day.at("09:00").do(job)
    print("Agendador iniciado. Tarefa será executada às 09:00 todos os dias.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Agendador interrompido manualmente.")
