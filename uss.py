import os
import cv2
import numpy as np
from PIL import Image
from skimage import exposure
from skimage.filters import unsharp_mask
from skimage.restoration import denoise_tv_chambolle
from skimage.transform import resize










def save_processed_image(processed_image, output_dir, idx, function_name):
    output_filename = f"{output_dir}/processed_image_{idx}_{function_name}.jpg"
    cv2.imwrite(output_filename, processed_image.astype(np.uint8))

# Create the output directory if it doesn't exist
output_dir = 'output/enhanced_images'
os.makedirs(output_dir, exist_ok=True)

# Iterate over the image list
for idx, im in enumerate(image_list):
    # Convert PIL image to OpenCV format
    cv_image = np.array(im)

    # Apply different image enhancement functions
    sharpened_image = sharpen_image(cv_image)
    enhance_contrast_image = enhance_contrast(cv_image)
    super_resolution_image = super_resolution(cv_image)
    denoised_image = denoise_image(cv_image)
    color_corrected_image = color_correction(cv_image)

    # Save the processed images
    save_processed_image(sharpened_image, output_dir, idx, 'sharpened')
    save_processed_image(enhance_contrast_image, output_dir, idx, 'enhance_contrast')
    save_processed_image(super_resolution_image, output_dir, idx, 'super_resolution')
    save_processed_image(denoised_image, output_dir, idx, 'denoised')
    save_processed_image(color_corrected_image, output_dir, idx, 'color_corrected')

# Notify user that processing is complete
print("Image processing complete. Processed images saved in 'output/enhanced_images' directory.")
