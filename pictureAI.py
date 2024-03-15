from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

text = "A person on a horse jumps over a broken down airplane."
image = pipe(promt=text, num_inferece_steps=1, guidance_scale=0.0).images[0]
