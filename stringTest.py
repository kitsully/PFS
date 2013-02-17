def plain_name(path):
	if (path.find("/") == -1):
		return True
	else:
		return True


def first(path):
	loc = path.find("/")
	return path[:loc]
	# print loc


def rest(path):
	loc = path.find("/")
	return path[loc:]




print first("right/wrong/left")
print first("hahahahahahahaha/no")


print rest("right/wrong/left")
print rest("hahahahahahahaha/no")








# for wd
# global wd
# wd = # whatever directory I'm changing to