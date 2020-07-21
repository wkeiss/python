# count to choose
def count2choose(count, things):
	if count >= len(things):
		print(things[count % len(things) - 1])
	else:
		print(things[count])
		
# count2choose(9, ['cindy', 'tree', 'men', 'love'])

# count2choose(1000, ['cindy', 'tree', 'men', 'love'])