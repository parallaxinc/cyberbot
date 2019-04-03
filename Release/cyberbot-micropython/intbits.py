# microbit-module: intbits@0.8.0
class bit():
	def get(v, i):
		z = (v >> i) & 1
		return z
	def set_val(v, i, b):
		if b > 0:
			b = b & 1
			z = b << i
			v |= z
		else:
			z = ~(1 << i)
			v = v & z
		return v