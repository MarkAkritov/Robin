import json
from datetime import datetime
from time import sleep
from drives import Drive
from affective_appraisal import Appraisal, Behaviour

def read_data(datafile):

	with open(datafile, "r") as file:
		vectors = json.load(file)

	timestamps = sorted([dt for dt in vectors.keys()])

	return vectors, timestamps

def create_objects():

	social  = Drive()
	stimuli = Drive()
	fatigue = Drive()
	behaviours = Behaviour()
	appraisal = Appraisal()

	return social, stimuli, fatigue, behaviours, appraisal

def update_regimes(social, stimuli, fatigue, activations = None):

	if activations is not None:
		social.update_activation(activations["Social"])
		social.set_current_regime()
		stimuli.update_activation(activations["Stimuli"])
		stimuli.set_current_regime()
		fatigue.update_activation(activations["Fatigue"])
		fatigue.set_current_regime()

	regimes = {
		"Social": social.regime,
		"Stimuli": stimuli.regime,
		"Fatigue": fatigue.regime
	}

	return regimes

def get_average_emotions(person):

	emotions = {}
	if "text" in person.keys():
		for key, value in person["face"]["emotions"].items():
			emotions[key] = (person["text"]["emotions"][key] + value)/2
	else:
		emotions = person["face"]["emotions"]
	
	return emotions

def print_info(social, stimuli, fatigue, behaviours, appraisal, full = True):

	if not full:
		print("Emotion: {0}\nBehaviour: {1}".format(appraisal.emotion, behaviours.behaviour))
		print("==============")
	else:
		#print("Social drive:\n", social)
		#print("Stimuli drive:\n", stimuli)
		#print("Fatigue drive:\n", fatigue)
		print("Appraisal:\n", appraisal)
		#print("Behaviour:\n", behaviours)
		# print("==============")
		# print("Emotion: {0}\nBehaviour: {1}".format(appraisal.emotion, behaviours.behaviour))
		print("==============")

def main():

	vectors, timestamps = read_data("scenario_neutral_happy.json") #scenario_happy_sad
	social, stimuli, fatigue, behaviours, appraisal = create_objects()
	regimes = update_regimes(social, stimuli, fatigue)

	for t in timestamps:

		activations, attention = behaviours.generate_behaviour(regimes)
		if attention == "person":
			emotions = get_average_emotions(vectors[t][attention])
			appraisal.update(emotions)
			appraisal.generate_emotion()
		elif attention == "object":
			print("Object interaction not ready yet.")
		else: #attention == None
			print("Robin needs rest.")
			sleep(3)

		regimes = update_regimes(social, stimuli, fatigue, activations)

		print_info(social, stimuli, fatigue, behaviours, appraisal, full = False)

if __name__ == '__main__':
	main()







