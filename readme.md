# Swap Heads using OpenCV

My son took a terrible photo by pulling a face.  But the picture also incudes his brother looking lovely.  So I've decided to swap the head of my son from the photo where he looks nice.  

This is my effort to use python and openCV.

I've used various haarcascades to located the faces.  As this easily detected my son, I've not had to fine tune.  So I've got the locations of his head in both images.  Then I've cut his head off (in the image), resized it so it fits the new image and finally imposed it using the various methods offered by openCV.
