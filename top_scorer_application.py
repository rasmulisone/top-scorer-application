import random

print("Top scorer application")
while True:
	teamgoals = input("Team goals: ")
	if teamgoals == "exit":
		break
	else:
		teamgoals = int(teamgoals)
	multiplier = float(input("Goal multiplier: "))
	teamname = input("Team name: ")
	percentage = random.randint(20, 50)
	goals = multiplier * ((teamgoals / 100.0) * percentage)
	goals = round(goals)
	print("")
	print(teamname)
	print("Total: " + str(teamgoals))
	print("Top scorer: " + str(goals))
	teamgoals_ = teamgoals - goals
	percentage_ = percentage - random.randint(0, 19)
	goals_ = (2 - multiplier) * ((teamgoals_ / 100.0) * percentage_)
	if goals_ > goals:
		goals_ = goals
	goals_ = round(goals_)
	print("Second top scorer: " + str(goals_))
	ogp = random.randint(0, 10)
	owngoals = (teamgoals / 100.0) * ogp
	owngoals = round(owngoals)
	print("Own goals: " + str(owngoals))
	opgoals = teamgoals - goals - goals_ - owngoals
	print("Goals scored by other players: " + str(opgoals))
	print("")