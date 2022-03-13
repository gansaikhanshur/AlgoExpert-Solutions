def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	output = 0
	tandem_pair = []
	
	if fastest:
		redShirtSpeeds.sort(reverse=True)
		blueShirtSpeeds.sort()
		for idx in range(len(redShirtSpeeds)):
			tandem_pair.append([redShirtSpeeds[idx], blueShirtSpeeds[idx]])
	else:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort()
		for idx in range(len(redShirtSpeeds)):
			tandem_pair.append([redShirtSpeeds[idx], blueShirtSpeeds[idx]])
	
	for pair in tandem_pair:
		output += max(pair)
	
    return output


