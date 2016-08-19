import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime

# configuration
sender = 'hzmiaoyaqi@yx41.popo.infra.mail'
receiver = 'hzmiaoyaqi@yx41.popo.infra.mail'
dirpath = os.path.dirname(os.path.abspath(__file__))

# init note
def preconfig(todo=None):
    with open(dirpath+'/note.txt', 'w+') as f:
        f.write(datetime.now().date().strftime('%Y-%m-%d %a\n'))
        f.write('===\n')
        if todo:
            f.write('Plan of today:\n')
            f.write(todo)
            f.write('\n')
        f.write('\n\n#TODO\n')

# clean up
def daily_report(s):
    msg = MIMEText(s)
    msg['Subject'] = 'Daily report'
    msg['From'] = sender
    msg['To'] = receiver
    server = smtplib.SMTP('localhost')
    returned = server.sendmail(sender, [receiver], msg.as_string())


def cleanup():
    with open(dirpath+'/note.txt', 'r+') as f:
        note = f.read()
        with open(dirpath+'/notebook.txt', 'a+') as nb:
            nb.write(note)
        try:
            work_done_today, todo = note.split('#TODO')
        except Exception:
            work_done_today = None
            todo = None
        daily_report(work_done_today)
    preconfig(todo)

if __name__ == '__main__':
    cleanup()
