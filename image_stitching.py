import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('keble_b.jpg')
img2 = cv2.imread('keble_a.jpg')
img3 = cv2.imread('keble_c.jpg')

def kaze(img):
    kaze = cv2.KAZE_create()
    # find the keypoints and descriptors with ORB
    kps, des = kaze.detectAndCompute(img, None)
    # draw only keypoints location,not size and orientation
    keys = cv2.drawKeypoints(img,kps,color=(0,255,0), flags=0, outImage = None)
    plt.figure()
    plt.imshow(keys),plt.show()
    plt.title('Keypoints detected')
    return keys,kps,des
    
def stitch(img1, img2):
    keys1, kps1, des1 = kaze(img1)
    keys2, kps2, des2 = kaze(img2)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    good = []
    for match in matches:
        if match[0].distance < 0.2*match[1].distance:
            good.append(match[0])
    draw_params = dict(matchColor = (0,255,0),singlePointColor = None,flags = 2)
    img3 = cv2.drawMatches(img1,kps1,img2,kps2,good,None,**draw_params)
    plt.figure()
    plt.imshow(img3)
    plt.title('Features matched')
    plt.show()
    src_pts = np.float32([ kps1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kps2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    
    M, mask = cv2.findHomography(src_pts, dst_pts,cv2.RANSAC,5.0)
    print(M)
    h,w,d = img2.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    #print(pts)
    dstp = cv2.perspectiveTransform(pts,M)
    #print(dstp[3][0][0])
    dst = cv2.warpPerspective(img1,M,(img2.shape[1] + img1.shape[1], img2.shape[0]))
    
    dst[0:img2.shape[0], 0:img2.shape[1]] = img2
    dst = dst[:,0:int(dstp[3][0][0])]
    plt.figure()
    plt.imshow(dst)
    plt.title('Image sticthed')
    plt.show()
    return dst

img4 = stitch(img1,img2)

plt.imshow(img4)
plt.title('Image 1 and 2 stitched')

final_image =stitch(img3 ,img4)
plt.imshow(final_image)
plt.title('Final Stitched Image')
