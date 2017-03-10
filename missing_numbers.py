def find_missing(list1,list2):
  #missing_number is initialized to zero
	missing_number = 0
	#check if list1 is smaller and find and  display missing number 
	if len(list1) < len(list2):
		miss = (set(list2) - set(list1))
		missing_number = miss.pop()
		return missing_number
	#check if list2 is smaller and find and  display missing number 
	if len(list2) < len(list1):
		miss = (set(list1) - set(list2))
		missing_number = miss.pop()
		return missing_number
	else:
	  return 0