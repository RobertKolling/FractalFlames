import random
from PIL import Image

# Image size (width, height)
size = (800, 600)

# Create a new image with a black background
img = Image.new("RGB", size, (0, 0, 0))
pixels = img.load()

# Fractal noise parameters
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Generate fractal noise
for x in range(img.width):
    for y in range(img.height):
        value = 0.0
        amplitude = 1.0
        frequency = 1.0
        for i in range(octaves):
            value += amplitude * random.random()
            amplitude *= persistence
            frequency *= lacunarity
        value = (value + 1) / 2
        value = int(value * 255)
        pixels[x, y] = (value, value, value)

# Save the image
img.save("fractal_smoke.png")
