#!/usr/bin/python --

"""

	Physoc Email Tool
	designed by Kaspar Snashall
	A huge thank you to Martin Peers fromer tcd student for teacching me so much about python,
	this email sender is strictly for non comercial purposes.

"""

__author__ = "Kaspar Snashall"
__authoremail__ = ""
__version__ = "0.1"

import sys, string, getopt, math, json
import urllib2, base64
import time
from datetime import date, datetime, timedelta
from pprint import pprint
import csv
import pickle
from Mailer import Mailer, textEmailHeader, textEmailFooter, htmlHeader, htmlFooter, sendEmail
from email_settings import smtpServer, smtpPort, sender, password
from settings import recipientList

from bs4 import BeautifulSoup

#
def processArguments():
	"""
		Process commandline arguments
	"""
	global templateFile
	global debug

	templateFile = ""
	debug = False

	# Date range to query database
	global dateRangeStart, dateRangeEnd
	global bstart, bend
	bstart = 0
	bend = 0

	global emailAddresses
	emailAddresses = ['your email address']

	try:
		opts, args = getopt.getopt(sys.argv[1:], "ht:ds:e:", ["help", "template=", "debug", "start=", "end="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		xopt = string.find(opt, '=')
		if xopt > 0:
			opt = opt[:xopt]
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-t", "--template"):
			templateFile = arg
		elif opt in ("-d", "--debug"):
			debug = True
		

#
#
#
def nightlyEmail(emailTxtBody, emailHtmlBody, emailHtmlImages):
	"""
	
	"""
	mailer = Mailer(smtpServer, smtpPort, smtpUser=sender, smtpPassword=password)

	yesterday = date.today()
	emailSubject = ("Physoc Email Proposal %s " % (yesterday))

	emailTxt = textEmailHeader("Physoc Email")
	emailTxt += emailTxtBody
	emailTxt += textEmailFooter()
	emailTxt = ""

	emailHtml = htmlHeader
	emailHtml += emailHtmlBody
	emailHtml += htmlFooter

	mailer.sendEmail(sender, recipientList=recipientList, subject=emailSubject, bodyText=emailTxt, bodyHtml=emailHtml, imagesHtml=emailHtmlImages)
#
#
#
def main():
	"""
		Main Program
	"""
	# Get Arguments from the command line
	processArguments()

	try:
		html = BeautifulSoup(open(templateFile))
	except:
		print " Can't read template file"
		sys.exit(1)

	htmlImages = []

	images = html.findAll('img')

	emailHtmlBody = html.prettify()
	emailTxtBody = ""
	bEmbed = None
	# Sent Email to keep watch on daily import
	if bEmbed:
		nightlyEmail(emailTxtBody, emailHtmlBody, None)
	else:
		nightlyEmail(emailTxtBody, emailHtmlBody, htmlImages)
#
#
#
if __name__ == '__main__':
	main()
#
#
#
