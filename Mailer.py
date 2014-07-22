#
#
#
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

import smtplib, sys

class Mailer:
	"""
		
	"""
	def __init__(self, smtpServer, smtpPort=None, smtpUser=None, smtpPassword=None):
		"""
			
		"""
		self.smtpServer = smtpServer
		self.smtpPort = smtpPort
		self.smtpUser = smtpUser
		self.smtpPassword = smtpPassword

	def sendEmail(self, sender, recipientList, subject, bodyText, bodyHtml, imagesHtml):
		"""
			send email - both text and html using smtp
			
			http://stackoverflow.com/questions/19171742/send-e-mail-to-gmail-with-inline-image-using-python
			http://code.activestate.com/recipes/473810-send-an-html-email-with-embedded-image-and-plain-t/
		"""

		session = smtplib.SMTP(self.smtpServer, self.smtpPort)
		if self.smtpUser is not None:
			session.ehlo()
			session.starttls()
			session.login(self.smtpUser, self.smtpPassword)

		for recipient in recipientList:
			# Create the root message and fill in the from, to, and subject headers
			msgRoot = MIMEMultipart('related')
			msgRoot['Subject'] = subject
			msgRoot['From'] = sender
			msgRoot['To'] = recipient
			msgRoot.preamble = 'This is a multi-part message in MIME format.'

			# Encapsulate the plain and HTML versions of the message body in an
			# 'alternative' part, so message agents can decide which they want to display.
			msgAlternative = MIMEMultipart('alternative')
			msgRoot.attach(msgAlternative)

			msgText = MIMEText(bodyText)
			msgAlternative.attach(msgText)

			# Reference images in the IMG SRC attribute by the ID we give them below
			msgText = MIMEText(bodyHtml, 'html')
			msgAlternative.attach(msgText)

			# This example assumes the image is in the current directory
			#fp = open('figure.png', 'rb')
			#msgImage = MIMEImage(fp.read())
			#fp.close()

			# Define the image's ID as referenced above
			#msgImage.add_header('Content-ID', '<%s>' % imagesHtml[0][1])
			#msgRoot.attach(msgImage)

			#msg = MIMEMultipart('alternative')
			#msg['Subject'] = subject
			#msg['From'] = sender
			#msg['To'] = recipient

			#msg_alternative = MIMEMultipart('alternative')
			#msg.attach(msg_alternative)

			#msg.attach(MIMEText(bodyText, _charset='latin-1'))
			#msg.attach(MIMEText(bodyHtml, 'html', _charset='latin-1'))
			#msg.attach(MIMEText(bodyHtml, _subtype='html'))

			#body = MIMEText('<p>Test Image<img src="cid:testimage" /></p>', _subtype='html')
			#msg.attach(body)

			#with open("figure.png", 'rb') as file:
			#	img = MIMEImage(file.read(), 'png')
			#	#img.add_header('Content-Id', '<testimage>')
			#	img.add_header('Content-Id', '<%s>' % imagesHtml[0][1])
			#	msg.attach(img)
			if imagesHtml is not None:
				for i in imagesHtml:
					msgImage = MIMEImage(i[0], 'png')
					msgImage.add_header('Content-Id', '<%s>' % i[1])
					msgRoot.attach(msgImage)

			smtpResult = session.sendmail(sender, recipient, msgRoot.as_string())

			if smtpResult:
				for recipient in smtpResult.keys():
					errstr = "Could not deliver mail to: %s\n \
					            \
					            Server said: %s\n \
					            %s\n" % (recipient, smtpResult[recipient][0], smtpResult[recipient][1])
					raise smtplib.SMTPException, errstr

		session.quit()
#
#
#
htmlHeader = """\
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" style="font-family: Arial;-webkit-text-size-adjust: none;margin: 0;padding: 0;background-color: #000000;width: 100%;align:center;">
<center align='center'>
	
   <table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="backgroundTable" style="margin: 0;padding: 0;background-color: #000000;height: 100%;width: 100%;">
        <div align='center'>
			<img src="http://www.maths.tcd.ie/~physoc/img/logonew.png" align='middle'> 
		</div>

"""

text_example = """\
                            <div style="text-align: center;width: 70%;padding: 0 15%;">
                                <p style="font-size: 15px; color: #000;"><strong>Some Title</strong></p>
                                <p style="font-size: 12px; color: #7b7b7b;">
                                    Some text
                                </p>
                            </div>
"""

image_text_example = """\
                            <div style="width: 100%;">
                                <table>
                                    <tr>
                                        <td style="text-align: center; width: 50%;padding: 25px 0 25px 0;">
                                            <img src="someimage.png" alt="Some Title" style=" margin-left: 40px;border: none;"/>
                                        </td>
                                        <td style="text-align: left; width: 50%;padding: 0 40px 0 38px;">
                                            <p style="font-size: 15px; color: #000;">Some Title</p>
                                            <p style="font-size: 12px; color: #7b7b7b;">
                                                Some text
                                            </p>
                                        </td>
                                    </tr>
                                </table>
                            </div>
"""

text_image_example = """\
                            <div style="width: 100%;">
                                <table>
                                    <tr>
                                        <td style="text-align: left; width: 50%;padding: 50px 30px 25px 40px;">
                                            <p style="font-size: 15px; color: #000;">Some Title</p>
                                            <p style="font-size: 12px; color: #7b7b7b;">
                                                Some Text
                                            </p>
                                        </td>
                                        <td style="text-align: center; width: 50%;">
                                            <img src="someimage.png" alt="Some title" style=" margin-right: 40px;border: none;width: 150px;padding-top: 30px;"/>
                                        </td>
                                    </tr>
                                </table>
                            </div>
"""

htmlFooter = """\
                            

		<div align='center'
        <p "font-family:arial;color:white;font-size:15px;text-align:center;padding:5px;>
        If you like this give me a reply email! Regards your friendly neighbourhood nerd Kaspar!
        </p>
        </div>
        <div align='center'>
        <p "font-family:arial;color:white;font-size:15px;text-align:center;padding:5px;>

        Physoc 2014-2015<p>
        <p "font-family:arial;color:white;font-size:15px;text-align:center;padding:5px;>
        &copy; KasparSnashall
        </div>
        <br>              
    </table>
</center>
</body>
</html>
"""

#
starLine = "************************************************************************************************************\n"
endStar = '*%78s\n' % ' '
#
def textEmailHeader(t):
	"""
		Return text email header
	"""
	mssg = "\n"
	mssg += starLine
	mssg += endStar
	mssg += ("*%s%s                             \n" % ("                                    ",t))
	mssg += endStar
	mssg += starLine
	return mssg
#
def textEmailFooter():
	"""
		Return text email header
	"""
	mssg = "\n"
	mssg += starLine
	return mssg
#
def sendEmail(subject, bodyText, bodyHtml, addresses):
	"""
        send email - both text and html using smtp
    """
	smtpServer = 'localhost'
	sender = 'someemailadress'
	subjectMsg = subject 

	mailer = Mailer(smtpServer, smtpUser=None, smtpPassword=None)
	mailer.sendEmail(sender, addresses, subjectMsg, bodyText, bodyHtml)
#
#
#
