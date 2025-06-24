# 📦 Automatizador de Tarefas com Python

Automatização de download de arquivos em site e envio automático de e-mails com anexo, agendado via terminal.

## 🚀 Tecnologias:
- Python 3.x
- Selenium
- smtplib
- schedule
- dotenv

## 📄 Funcionalidades:
✅ Download automático de arquivo via Selenium  
✅ Envio de e-mail automático com anexo  
✅ Agendamento diário às 9h via `schedule`

## 📂 Como usar:

1. Clone o projeto:
```bash
git clone https://github.com/seuusuario/automator.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo `.env`:
```
EMAIL_USER=seuemail@gmail.com
EMAIL_PASS=sua_senha
EMAIL_TO=destinatario@gmail.com
```

4. Execute:
```bash
python main.py
```

## 📌 Observação:
- Certifique-se de ter o **chromedriver** compatível com sua versão do Chrome no PATH.
- Crie a pasta `downloads` na raiz do projeto.

## 💡 Por que este projeto?
Demonstra automação de processos reais, valorizada em ambientes corporativos.
