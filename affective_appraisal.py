class Appraisal:

	def __init__(self):

		self.arousal = 0	# Level of being awake 
		self.valence = 0	# Level of being attracted
		self.stance  = 0	# Level of being open for interaction

		# Range for arousal, valence and stance
		self.max =  1
		self.min = -1

		# Initial emotion
		self.emotion = "Neutral"

	def __repr__(self):

		return "Arousal: {0} \nValence: {1} \nStance:  {2} \nEmotion: {3}".format(self.arousal, 
											  self.valence, 
											  self.stance, 
											  self.emotion)

	def set_min_max(self):

		if self.arousal < self.min:
			self.arousal = self.min
		elif self.arousal > self.max:
			self.arousal = self.max

		if self.valence < self.min:
			self.valence = self.min
		elif self.valence > self.max:
			self.valence = self.max

		if self.stance < self.min:
			self.stance = self.min
		elif self.stance > self.max:
			self.stance = self.max

	def update(self, emotions):

		AVS = [0, 0, 0]

		for key, value in emotions.items():
			
			if key == "angry":
				AVS[0] += value
				AVS[1] -= value
				AVS[2] -= value

			elif key == "disgust":
				AVS[0] -= value
				AVS[1] -= value
				AVS[2] -= value

			elif key == "fear":
				AVS[0] += value
				AVS[1] -= value
				AVS[2] += value

			elif key == "happy":
				AVS[0] += value
				AVS[1] += value
				AVS[2] += value

			elif key == "sad":
				AVS[0] -= value
				AVS[1] -= value
				AVS[2] += value

			elif key == "surprise":
				AVS[0] += value
				AVS[1] += value
				#AVS[2] -= value

			elif key == "neutral":
				AVS[0] -= value
				AVS[1] += value
				AVS[2] -= value

			else:
				pass

		self.arousal += AVS[0]
		self.valence += AVS[1]
		self.stance  += AVS[2]

		Appraisal.set_min_max(self)
		#Appraisal.generate_emotion(self)

	def generate_emotion(self):

		if (self.arousal <= 0.5 and self.arousal >= -0.5) and (self.valence <= 0.5 and self.valence >= -0.5) and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Neutral"

		elif self.arousal > 0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Surprise"

		elif self.arousal < -0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Tired"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence > 0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Happy"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence < -0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Sad"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance > 0.5:
			self.emotion = "Attentive"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance < -0.5:
			self.emotion = "Stern"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence < -0.5 and self.stance > 0.5:
			self.emotion = "Fear"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence < -0.5 and self.stance < -0.5:
			self.emotion = "Anger"

		elif self.arousal < -0.5 and self.valence < -0.5 and self.stance < -0.5:
			self.emotion = "Disgust"

		elif self.arousal < -0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance < -0.5:
			self.emotion = "Stern"

		elif self.arousal < -0.5 and self.valence > 0.5 and self.stance < -0.5:
			self.emotion = "Neutral"

		elif self.arousal < -0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance > 0.5:
			self.emotion = "Neutral"

		elif self.arousal > 0.5 and self.valence > 0.5 and self.stance > 0.5:
			self.emotion = "Happy"

		elif self.arousal > 0.5 and self.valence < -0.5 and self.stance < -0.5:
			self.emotion = "Fear"

		elif self.arousal > 0.5 and self.valence < -0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Stern"

		elif self.arousal > 0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance < -0.5:
			self.emotion = "Attentive"

		elif self.arousal < -0.5 and self.valence > 0.5 and self.stance > 0.5:
			self.emotion = "Attentive"

		elif self.arousal < -0.5 and self.valence > 0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Neutral"

		elif self.arousal < -0.5 and self.valence > 0.5 and self.stance < -0.5:
			self.emotion = "Tired"

		elif self.arousal > 0.5 and self.valence < -0.5 and self.stance > 0.5:
			self.emotion = "Attentive"

		elif self.arousal > 0.5 and (self.valence <= 0.5 and self.valence >= -0.5) and self.stance > 0.5:
			self.emotion = "Sad"

		elif self.arousal > 0.5 and self.valence > 0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Attentive"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence > 0.5 and self.stance > 0.5:
			self.emotion = "Surprise"

		elif self.arousal < -0.5 and self.valence < -0.5 and (self.stance <= 0.5 and self.stance >= -0.5):
			self.emotion = "Stern"

		elif self.arousal < -0.5 and self.valence < -0.5 and self.stance > 0.5:
			self.emotion = "Sad"

		elif (self.arousal <= 0.5 and self.arousal >= -0.5) and self.valence > 0.5 and self.stance < -0.5:
			self.emotion = "Attentive"

		elif self.arousal > 0.5 and self.valence > 0.5 and self.stance < -0.5:
			self.emotion = "Surprise"

		else:
			self.emotion = "Other"

		return self.emotion


class Behaviour:

	def __init__(self):

		#self.regimes = regimes	#dict
		#self.emotion = emotion	#string
		#self.objects = objects	#dict

		self.behaviour = """Search for social interaction."""
		self.attention = "person"

	def __repr__(self):

		return "Behaviour: {0} \nAttention: {1}".format(self.behaviour, self.attention)

	def generate_behaviour(self, regimes):

		if regimes["Fatigue"] == "Overwhelmed":
			self.behaviour = """Avoid stimulis and social interaction, need to rest."""
			self.attention = None

		elif regimes["Fatigue"] == "Homeostatic" or regimes["Fatigue"] == "Under-stimulated":
			if regimes["Social"] == "Overwhelmed":
				if regimes["Stimuli"] == "Homeostatic" or regimes["Stimuli"] == "Under-stimulated":
					self.behaviour = """Avoid social interaction, search for stimuli to show interest."""
					self.attention = "object"
				elif regimes["Stimuli"] == "Overwhelmed":
					self.behaviour = """Avoid social interaction and stimuli, do sommething."""
					self.attention = None
			elif regimes["Social"] == "Homeostatic":
				if regimes["Stimuli"] == "Homeostatic" or regimes["Stimuli"] == "Overwhelmed":
					self.behaviour = """Avoid stimuli, search for social interaction."""
					self.attention = "person"
				elif regimes["Stimuli"] == "Under-stimulated":
					self.behaviour = """Search for stimuli."""
					self.attention = self.objects.object
			elif regimes["Social"] == "Under-stimulated":
				self.behaviour = """Search for social interaction."""
				self.attention = "person"

		# if self.regimes["Fatigue"] == "Under-stimulated":
		# 	pass	

		if self.attention is None:
			self.activations = {
				"Social":  -1,
				"Stimuli": -1,
				"Fatigue": -1
			}

		elif self.attention == "person":
			self.activations = {
				"Social":  -1,
				"Stimuli":  1,
				"Fatigue":  1
			}

		else:
			self.activations = {
				"Social":   1,
				"Stimuli": -1,
				"Fatigue":  1
			}

		return self.activations, self.attention
