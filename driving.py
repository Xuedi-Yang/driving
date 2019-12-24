country = input('What is your citizenship?')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can get a driver license')
	else:
		print('You cannot get a driver license')
elif country == 'America':
	if age >= 16:
		print('You can get a driver license')
	else:
		print('You cannot get a driver license')
else:
	print('You can only write down Taiwan or America')