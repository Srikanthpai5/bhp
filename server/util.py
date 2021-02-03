import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


# 1

def get_location_names():
	return __locations

# 2

def load_saved_artifacts():
	print(" Loading saved artifacts.... start..")
	global __locations
	global __data_columns

	with open("./artifacts/columns.json" , 'r') as f:
		__data_columns = json.load(f)['data_columns']
		__locations = __data_columns[3:]

	global __model
	with open("./artifacts/banglore_home_prices_model.pickle" , "rb") as f:
		__model = pickle.load(f)
	print("\n ..  Loading saved artifacts ..  done... \n")

# 3

def get_estimated_price(location,sqft,bhk,bath):
	try:
		loc_index = __data_columns.index(location.lower())
	except:
		loc_index = -1

	x = np.zeros(len(__data_columns))
	x[0] = sqft
	x[1] = bath
	x[2] = bhk
	if loc_index >= 0:
		x[loc_index] = 1
	return round(__model.predict([x])[0], 2)



if __name__ == '__main__':
	load_saved_artifacts()
	print(get_location_names())
	print(get_estimated_price('1st Phase JP Nagar' , 1000 , 3 , 3))
	print(get_estimated_price('7st Phase JP Nagar' , 1200 , 2 , 2))
	print(get_estimated_price('anjanapura' , 1200 , 3 , 3))
	print(get_estimated_price('Indiranagar' , 1200 , 3 , 3))
	
	
	
	
	