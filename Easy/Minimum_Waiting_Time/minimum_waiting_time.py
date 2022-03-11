def minimumWaitingTime(queries):
    minimum_time = 0
	seen = []
	queries.sort()
	
	for entry in queries:
		minimum_time += sum(seen)
		seen.append(entry)
		
	
    return minimum_time
