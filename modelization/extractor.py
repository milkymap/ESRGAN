import torch as th 
import torch.nn as nn 

from torchvision.models import vgg19

class Extractor:
	def __init__(self):
		# use the 34-th layer before activation_map
		# you can find explanation of this choice on the paper
		# Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network 
		# link : https://arxiv.org/pdf/1609.04802.pdf
		self.body = nn.Sequential(
			*list(vgg19(pretrained=True).features.children())[:35]
		).eval()

	def forward(self, X):
		return self.body(X)

	def __call__(self, X):
		return self.forward(X)

if __name__ == '__main__':
	E = Extractor()
	print(E.body)