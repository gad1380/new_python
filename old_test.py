import random

recommendation_history = []
restaurants = ["Laut", "Random String", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

def recommend(restaurants):
	random.shuffle(restaurants)
	for choice in restaurants:
		if choice not in recommendation_history[-4:]:
			recommendation_history.append(choice)
			return choice
