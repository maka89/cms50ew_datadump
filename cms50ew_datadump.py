import cms50ew

def download(filenm="foo.txt",device="COM3"):
	"""Function to deal with 'download' action argument"""
	oxi = cms50ew.CMS50EW()
	print('Connecting to device ' + str(device) + ' ...')
	if not oxi.setup_device(target=device, is_bluetooth=False):
		raise Exception('Connection attempt unsuccessful.')
	oxi.initiate_device()
	oxi.get_session_count()
	if oxi.sess_available == 'No':
		raise Exception('No stored session data available.')
	oxi.get_session_duration()
	oxi.send_cmd(oxi.cmd_get_session_data)
	counter = 1
	while oxi.download_data():
		print('Downloading data point ' + str(counter) + ' of ' + str(oxi.sess_data_points))
		counter += 1
	print('Downloaded data points:', len(oxi.stored_data))
	print(oxi.stored_data)
	oxi.write_csv(filenm)
download("foo.txt","COM3")