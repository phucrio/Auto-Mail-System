import smtplib 
   
my_email="bphucXXX@gmail.com"
password_key="xxxxx"

# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    
# Login with your email and password
my_server.login(my_email, password_key)

from email.mime.multipart import MIMEMultipart
message = MIMEMultipart("alternative")

from email.mime.text import MIMEText


text_content= "Hello, I am a final year student with an Mtech degree in Computer science specializing in Artificial Intelligence. I’m interested in data science roles at your organization."


message.attach(MIMEText(text_content))


from email.mime.image import MIMEImage
import os

# define your location
grade_card_path = 'grade_card.jpg'


# Read the image from location
grade_card_img = open(grade_card_path, 'rb').read()

print(grade_card_img)
# Attach your image
message.attach(MIMEImage(grade_card_img, name=os.path.basename(grade_card_path)))


from email.mime.application import MIMEApplication
resume_file = '...../resume.txt'


# Read the file from location
with open(resume_file, 'rb') as f:
    file = MIMEApplication(
        f.read(),
        name=os.path.basename(resume_file)
    )
    file['Content-Disposition'] = f'attachment filename="{os.path.basename(resume_file)}"'
    message.attach(file)


text_content= """
Hello {recruiter_name}, I hope you are doing well. I’m Jane Doe, an engineering graduate with an Mtech in Computer Science and a specialization in Artificial Intelligence.

I am writing to inquire regarding open roles in {job_role} at {organization}. I have experience performing data analysis and modeling through my internships and research projects. I’m excited to have an opportunity to apply my skills and learn more in the {organization_sector}.

I have attached my grade card and résumé below. Looking forward to hearing from you.

Thanks,
…… """


import csv


with open("job_contacts.csv") as csv_file:
        jobs = csv.reader(csv_file)
        next(jobs)  # Skip header row
        
        for recruiter_name, recruiter_email, organization, organization_sector,job_role in jobs:
            email_text=text_content.format(recruiter_name, recruiter_email,organization, organization_sector, job_role)
            
            # Attaching the personalized text to our message
            message.attach(MIMEText(email_text))
            
            my_server.sendmail(
                from_addr= my_email,
                to_addrs=recruiter_email,
                msg=message
            )




my_server.quit()

