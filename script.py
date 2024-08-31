current_cycle = 0
osc_list = []

def onReceiveOSC(dat, rowIndex, message, byteData, timeStamp, address, args, peer):
	global current_cycle
	global osc_list
	global note_list
	global scale_list
	osc_table = op('osc_table')
	osc_dict_table = op('osc_dict_table')
	
	# OSCメッセージをリストに分割
	osc = message.split()
	# リストの中にある " を全て削除
	osc = [x.replace('"', '') for x in osc]
		
	try:
		# oscをkeyとvalueに分割して辞書osc_dictに格納
		osc_dict = {}
		# 最初の要素はaddress
		osc_dict['address'] = osc[0]
		# 2番目以降はkeyとvalueのペア
		for i in range(1, len(osc), 2):
			osc_dict[osc[i]] = osc[i + 1]

		# osc_dictをosc_dict_tableに書き込み
		osc_dict_table.clear()
		for key in osc_dict:
			osc_dict_table.appendRow([key, osc_dict[key]])			
		
		#osc_dictの中のcycleを取得
		cycle = osc_dict['cycle']

		# cycleが変わったら初期化
		if cycle != current_cycle:
			current_cycle = cycle		
			osc_list.clear()
			osc_table.clear()
		
		# osc_listにoscを追加
		osc_list.append(osc)

		# osc_listをosc_tableに書き込み
		osc_table.clear()
		for i in range(len(osc_list)):
			osc_table.appendRow()
			current_list = osc_list[i]
			for j in range(len(current_list)):
				osc_table.appendCol()
				osc_table[i, j] = current_list[j]
	except:
		pass
		
	return	

	