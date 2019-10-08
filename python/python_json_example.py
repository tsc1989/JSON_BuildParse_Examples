#!/usr/bin/env python 

##########################################################
#Example python code for JSON build & parse
##########################################################

import json

class py_json_example:
	def __init__(self):
		pass

	# parse input JSON data
	def json_test_deserialize(self, data):
		jsonData = json.loads(data)
		#check if main object DataBase is present in the data
		if "DataBase" in jsonData:
			print ("\n\nParsed JSON data .....")
			print ("=====================================================")
			#iterate through each entry in DataBase
			for eEntry in jsonData['DataBase']:
				# get Value of each Tag
				Name = eEntry['Name']
				id = eEntry['id']
				Address = eEntry['Address']
				FavouriteColor = eEntry['FavouriteColor']
				Number = eEntry['Number']
				passPortDataHomeCountry = eEntry['PassportData']['HomeCountry']
				passPortDataLivingCountry = eEntry['PassportData']['LivingCountry']
				CommentString = eEntry['CommentString']
				Enable = eEntry['Enable']
				Array = eEntry['DataTupleArray']
				print ("Entry ")
				print ("	Name = " + Name)
				print ("	id = " + id)
				print ("	Address = " +  Address)
				print ("	FavouriteColor = " +  FavouriteColor)
				print ("	Number = " + str(Number))
				print ("	HomeCountry = " +  passPortDataHomeCountry)
				print ("	LivingCountry = " + passPortDataLivingCountry)
				print ("	CommentString =" + CommentString )
				print ("	Enable = " + str(Enable))
				#iterate through each entry in DataTupleArray
				for D in Array:
					print ("	x = "+ str(D['x']) + ", y =" + str(D['y']) + ", z = " + str(D['z']))
			print ("=====================================================")
			

	#build JSON data
	def json_test_serialize(self):
		# Object data as dictionary
		data = {}
		# data['DataBase'] as an array (List)
		data['DataBase'] = []
		for i in range(2):
			Entry = {}
			Entry['Name'] = "Name"+str(i+1)
			Entry['Enable'] = True
			Entry['id'] = str(i+1)
			Entry['Address'] = "street" + str(i+1)
			TupleArry = []
			TupleArry.append(("x"+str(i+1), "y"+str(i+1), "z"+str(i+1)))
			TupleArry.append(("x"+str(i+1), "y"+str(i+1), "z"+str(i+1)))
			Entry['DataTupleArray'] = []
			TagValue = {}
			TagValue['x'] = i +1 
			TagValue['y'] = i +1 
			TagValue['z'] = i +1 
			Entry['DataTupleArray'].append(TagValue)
			Entry['DataTupleArray'].append(TagValue)
			Entry['FavouriteColor'] = "red"
			Entry['Number'] = i+1
			Entry['CommentString'] = "NA"
			passportData = {}
			passportData['HomeCountry'] = "UE"
			passportData['LivingCountry'] = "CA"
			Entry['PassportData'] = passportData
			data['DataBase'].append(Entry)
		print("Serialized data = ")
		print("=====================================================")
		serializedData = json.dumps(data, ensure_ascii=False, indent=4)
		print (serializedData)
		print("=====================================================")
		return serializedData
		

	def run(self):
		#Test JSON serialization / Build
		data = self.json_test_serialize()
		# Test JSON deserialization / Parsing
		self.json_test_deserialize(data)
		

if __name__ == '__main__':
	obj = py_json_example()
	obj.run()
