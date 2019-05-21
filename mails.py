import smtplib
import csv

g_user="/"
g_password="/"

emails = []

#load the email, name, repo of all participants
def load_emails():
    with open("emails.csv", "r") as f:
        reader = csv.reader(f)
        for mail in reader:
            emails.append(mail)


#load email text
def load_emailtext():
    with open("email_text.txt", "r") as f:
            return f.read()

#add name, repo to email text
def prepare_emailtext(name, repo, sender):
    text = load_emailtext().replace("[[name]]",name)
    text = text.replace("[[repo]]",repo)
    text =text.replace("[[sender]]", sender)
    return text


#connect to gmail smtp
def connect_to_smtp():
        s = smtplib.SMTP("smtp.gmail.com","587")
        s.ehlo()
        s.starttls()
        s.login(g_user, g_password)
        return s


def main():
    load_emails()
    server = connect_to_smtp()
    for participant in emails:
        text= prepare_emailtext(participant[1],participant[2], g_user )

        server.sendmail(g_user, participant[0],text.encode("ascii", errors="ignore"))
        print("sent to %s with success :)" % participant[0])
    server.close()


if __name__ == "__main__":
    main()
