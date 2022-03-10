def tournamentWinner(competitions, results):
    
	counter_dict = _counter(competitions, results)
	
	number_of_wins = 0
	winner = ""
	
	for key, val in counter_dict.items():
		if val > number_of_wins:
			number_of_wins = val
			winner = key
		
    return winner


def _counter(competitions, results):
	counter_dict = {}
	
	for idx, entry in enumerate(competitions):
		home_team = entry[0]
		away_team = entry[1]
		
		if results[idx] == 0:
			if away_team in counter_dict:
				counter_dict[away_team] += 3
			else:
				counter_dict[away_team] = 3
		else:
			if home_team in counter_dict:
				counter_dict[home_team] += 3
			else:
				counter_dict[home_team] = 3
				
	return counter_dict
