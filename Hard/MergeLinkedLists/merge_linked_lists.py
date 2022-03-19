# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	place_holder = LinkedList(None)
	tmp = place_holder
	
	while headOne and headTwo:
		if headOne.value < headTwo.value:
			tmp.next = headOne
			headOne = headOne.next
		else:
			tmp.next = headTwo
			headTwo = headTwo.next
		tmp = tmp.next
		
	if headOne is None:
		tmp.next = headTwo
	if headTwo is None:
		tmp.next = headOne
		
	return place_holder.next
