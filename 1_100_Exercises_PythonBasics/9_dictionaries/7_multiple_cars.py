'''Multiple Cars
Create a nested dictionary that contains the following data.

Car

type	color	year
sedan	blue	2003
Truck

type	color	year
pickup	red	1998'''

car_types = {
    'car': {
        'type': 'sedan', 
        'color': 'blue', 
        'year': '2003',
    },
    'truck': {
        'type': 'pickup', 
        'color': 'red', 
        'year': '1998',
    },
}

print(car_types)
print(car_types['car']['year']) # test to print an specific value

# {'car': {'type': 'sedan', 'color': 'blue', 'year': '2003'}, 'truck': {'type': 'pickup', 'color': 'red', 'year': '1998'}}