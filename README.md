# 📦 Automatizador de Tarefas com Python

Automatização de download de arquivos em site e envio automático de e-mails com anexo, agendado via terminal.

## O que esse projeto faz?

- Baixa arquivos PDF de forma automática com Selenium  
- Envia e-mails com o arquivo anexado, via SMTP  
- Roda todos os dias às 9h com a ajuda da biblioteca `schedule`  
- Usa um arquivo `.env` para manter senhas e e-mails protegidos

---

## Tecnologias utilizadas:
- Python
- Selenium
- smtplib
- schedule
- dotenv

---

▶️ Como executar
## 1. Clone o repositório
```bash
Copiar
Editar
git clone https://github.com/beatriz-ssilva/Automator.git
cd Automator
```
## 2. Instale as dependências
```bash
Copiar
Editar
pip install -r requirements.txt
```
## 3. Crie um arquivo .env com suas credenciais de e-mail
```ini
Copiar
Editar
EMAIL_USER=seuemail@gmail.com
EMAIL_PASS=sua_senha_de_app
EMAIL_TO=destinatario@gmail.com
```
- OBS: use uma senha de aplicativo do Gmail para evitar problemas de segurança

## 4. Execute o script principal
```bash
Copiar
Editar
python main.py
```
- OBS: o programa vai agendar a tarefa para rodar todo dia às 09:00 da manhã. Se quiser testar em outro horário, você pode alterar o horário no arquivo scheduler.py


⭐ Esse projeto é parte do meu portfólio, e estou sempre em busca de aprender mais. Obrigada por passar por aqui!
Se esse projeto te ajudou ou inspirou, sinta-se à vontade para dar uma estrela no repositório ou abrir uma issue com sugestões. Me adiciona no LinkedIn, vamos conversar sobre tech e projetos :) 
