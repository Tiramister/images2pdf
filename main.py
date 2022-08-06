import os
import img2pdf

dirname = "./"
imgs = []

for r, _, f in os.walk(dirname):
  for filename in f:
    if filename.endswith(".jpg") or filename.endswith(".png"):
      imgs.append(os.path.join(r, filename))
imgs.sort()

with open("output.pdf", "wb") as f:
  f.write(img2pdf.convert(imgs))
