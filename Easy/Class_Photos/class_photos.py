def classPhotos(redShirtHeights, blueShirtHeights):
		
    redShirtHeights.sort()
	blueShirtHeights.sort()
	
	for idx in range(0, len(redShirtHeights) - 1):
		if redShirtHeights[idx] >= blueShirtHeights[idx] and redShirtHeights[idx + 1] <= blueShirtHeights[idx + 1]:
			return False
		if blueShirtHeights[idx] >= redShirtHeights[idx] and blueShirtHeights[idx + 1] <= redShirtHeights[idx + 1]:
			return False
	return True
