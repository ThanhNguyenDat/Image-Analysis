# Image Analysis

## Histogram
**What's in the histogram?**

Like any other histogram, this graph shows the **count** of something. In this case, it's the _number of pixels in the image_ that are either _dark_ (towards the left of the graph) or _lighter_ (towards the right of the graph).

**Why are histograms important**?

-   If you're concerned about whether the image is properly exposed (not too dark and not too bright), then histograms are a great way of checking the distribution of your lighter and darker pixels!
-   If your images are overexposed (too bright) or underexposed (too dark), you can fix exposure with OpenCV in Python (although you may lose some image quality). 
-   This might be important if you're developing an app where users are taking photos and your app is trying to classify the objects inside the image. If it's too dark or too light, the objects may not be recognizable. 

**How do you read the histogram?**

-   On the **x-axis**, the values normally range from 0 (black) to 255 (white). So darker pixels are on the left, and whiter pixels are to the right. In the `matplotlib` chart above, the x-axis goes from 0 to 256, since each pixel is represented as a bin start from 0 to 0.99, and ends with 255 to 255.99.   
-   The **y-axis** shows the number of pixels found in the image on the scale of black to white.

**Observations:**
The grayscale histogram above shows that: 

-   lots of pixels around `x = 30`, which are **darker pixels**.
-   lots of pixels around `x = 200`, which are **lighter pixels**.

**Interpretation:**

-   the image appears to have lots of very dark, and very light pixels, but not a lot of pixels in between. Looking at the image of the Presidents, this is readily apparent -- the darker pixels seem to come from the black suits and the fireplace. A lot of the lighter pixels come from the furniture and walls.
