#config file for GPR Database connections

env_mode = "PROD" #PROD or UAT or DEV

if env_mode == "PROD":
	# Settings for GPR Oracle Database connection PROD
	username = ''
	password = ''
	dsnDCS = '' #DCS
	dsnDPE = '' #DPE
	port = 1521
	encoding = 'UTF-8'
elif env_mode == "UAT":
	#Settings for GPR Oracle Database connection UAT
	username = ''
	password = ''
	dsnDPE = ''
	port = 1521
	encoding = 'UTF-8'
elif env_mode == "DEV":
	# Settings for GPR Oracle Database connection DEV
	username = ''
	password = ''
	dsnDPE = ''
	port = 1521
	encoding = 'UTF-8'