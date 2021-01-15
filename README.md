# Definitive-Keylogger
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

This is a simple project used to create a useful keylog in python.



## Modules used:
- smtplib for create a smtp connection for send email to every machine with internet.
- os The OS module in python provides functions for interacting with the operating system.
- pynput used for import keyboard and mouse.
- email  a package used for parsing, handling and generating email messages.

## Project Structure:
- `Listener function:`
  - used to listen any on_press events   
- `on_ press function:`
  - used to detect any keypress of your pc
- `write_on files function:`
  - for write all keypress into a file txt
- `geo_location function:`
  - used to retrieve information about location
- `smtp function:`
  - used to send file attacchements and information about your ip, hostname machine and geo_location
---

### Remember
  Environment variables like (DB_USERS and DB_PASSWORD) used for smtp authentication must import in your pc system in windows you can use this link to do that: [WINDOWS](https://www.youtube.com/watch?v=IolxqkL7cD8&ab_channel=CoreySchafer), in linux/MACOS see this: [MACOS&LINUX](https://www.youtube.com/watch?v=5iWhQWVXosU&t=81s&ab_channel=CoreySchafer)
