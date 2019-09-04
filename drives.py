# Drives: Social, Stimuli, Fatigue
# Regimes: 'Overwhelmed', 'Homeostatic', 'Under-stimulated'

class Drive:

	#regime = "homeostatic"

	def __init__(self):

		self.previous_activation = 0
		self.activation = self.previous_activation

		self.min_activation = -15
		self.max_activation =  15

		self.regime = "Homeostatic"

	def __repr__(self):

		return "Activation: {0} \nPrevious_activation: {1} \n Regime: {2}".format(self.activation,
																				  self.previous_activation,
																				  self.regime)

	def update_activation(self, new_activation):

		self.previous_activation = self.activation
		self.activation += new_activation

		if self.activation > 15:
			self.activation = 15

		elif self.activation < -15:
			self.activation = -15

		#return self.activation

	def set_current_regime(self):

		if self.activation < -5:
			self.regime = "Overwhelmed"

		elif self.activation >= -5 and self.activation <= 5:
			self.regime = "Homeostatic"

		else:
			self.regime = "Under-stimulated"

		#return self.regime

class Social(Drive):

	def __init__(self):

		super().__init__()

class Stimuli(Drive):

	def __init__(self):

		super().__init__()

class Fatigue(Drive):

	def __init__(self):

		super().__init__()