import torch

print("CUDA available: ", torch.cuda.is_available())
print("CUDA devices: ", torch.cuda.device_count())
print("current CUDA device: ", torch.cuda.current_device())
print("CUDA device 0 id: ", torch.cuda.device(0))
print("CUDA device 0 name: ", torch.cuda.get_device_name(0))