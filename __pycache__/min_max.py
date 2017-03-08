
def find_max_min(list):
  list.sort()
  if list[0]== list[-1]:
    return[len(list)]
  else:
    return [list[0], list[-1]]
      