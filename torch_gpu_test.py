import torch

print('is torch cuda available?', torch.cuda.is_available())
print('GPU:', torch.cuda.get_device_name(0))