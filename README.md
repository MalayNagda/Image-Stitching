# Image Stitching

The objective was to stitch three images together. First, keypoints were detected in two images and features were matched between the two. 

<p align="center">
  <img src="images/kps_1__2.png">
</p>
<p align="center">
  <img src="images/features_matched_1n2.png">
</p> 

The matched features were used to calculate the homography matrix. This matrix was used to warp the images and then finally stitch them together.

<p align="center">
  <img src="images/stitched_1n2.png">
</p>

To stitch the third image to this stitched image, the same process is repeated. Keypoints are detected and matched in the stitched image and the third image.

<p align="center">
  <img src="images/kps_3_1n2.png">
</p>

<p align="center">
  <img src="images/features_matched_3_1n2.png">
</p>

Again, the stitched image and third image are warped and stitched together using the calculated homography matrix between the two to get the final stitched image consisting all the three images.

<p align="center">
  <img src="images/final.png">
</p>
