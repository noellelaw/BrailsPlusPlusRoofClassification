"""
brails_filters.py
================
Example showing the use of BRAILS module that crops building images from panos.

 Purpose: Testing 1) get_class method of Importer
                  2) get_footprints using scraper provided
                  3) get_images using StreetView for subset of footprints
                  4) filter method of HouseView
"""

import os
import argparse
from pathlib import Path
from brails import Importer
import cv2

# This script needs a Google API Key to run.
# We suggest placing your API key in file apiKey.txt in the same directory as
# this script if you plan to commit changes to this example. This way, you do
# not risk accidentally uploading your API key (apiKey.txt is in .gitignore,
# so you have work to do to get it uploaded)
# TODO: Fix path to automatically find root please and pass in dataset folder as parameter
DATASET_FOLDER = "/Users/noellelaw/Desktop/CERALab/BuildingClassificationDataset/RoofClassificationData"
API_KEY_DIR = "/Users/noellelaw/Desktop/CERALab/BuildingClassificationDataset/BrailsPlusPlusRoofClassification/apiKey.txt"
if os.path.exists(API_KEY_DIR):
    with open(API_KEY_DIR, 'r', encoding='utf-8') as file:
        api_key = file.readline().strip()  # Read first line & strip whitespace
else:
    raise FileNotFoundError('API key file not found. Please ensure the file'
                            f' exists at: {API_KEY_DIR}')


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Demonstrate Importer.")
    parser.add_argument('scraper', type=str, help="Footprint Scraper") # "USA_FootprintScraper",
    #parser.add_argument('location', type=str,  help="Location") # "Tiburon, CA"

    # Parse the arguments
    args = parser.parse_args()

    importer = Importer()

    locations = [
            "Honolulu, HI", "San Juan, PR", "Tiburon, CA", "Manhattan, NY", 
        ]
    for location in locations:
        region_boundary_class = importer.get_class("RegionBoundary")
        region_boundary_object = region_boundary_class({"type": "locationName", "data": location})
        scraper_class = importer.get_class(args.scraper)
        scraper = scraper_class({"length": "ft"})
        inventory = scraper.get_footprints(region_boundary_object)
        print(f"num assets found: {len(inventory.inventory)} for {location} using {args.scraper}")    

        # Subsample from the extracted assets to keep the image downloading step quick.
        # Here, we are randomly sampling 10 buildings using a random seed value of 100:
        small_inventory = inventory.get_random_sample(100, 100)


        # Get street level imagery for the selected subset using GoogleStreetview:
        google_satellite_class = importer.get_class("GoogleSatellite")
        google_satellite = google_satellite_class()
        images_satellite = google_satellite.get_images(small_inventory, "tmp/satellite/")

        images_satellite.print_info()

        # Crop the obtained imagery such that they include just the buildings of
        # interest:
        filter_house = importer.get_class('RoofView')
        image_filter = filter_house({})
        filtered_images_satellite = image_filter.filter(images_satellite, 'tmp/filtered_images')
        print('\nCropped images are available in ',
            Path(filtered_images_satellite.dir_path).resolve())   

    # Set the directory you want to search
    directory = Path('tmp/filtered_images')

    # Find all image files with common extensions
    # Delete images that are non existent due to low conf?
    # See if there is a faster way to do this
    images, filenames, keys_to_delete = [], [], []
    images.extend(directory.rglob('*.jpg'))
    filenames = [str(image).split('/')[-1] for image in images]

    for idx, (key, img) in enumerate(filtered_images_satellite.images.items()):
        if img.filename not in filenames:
            # There has to be a better way
            keys_to_delete.append(key)

    for key in keys_to_delete:
        filtered_images_satellite.remove(key)


    filtered_images_satellite.print_info() 
    


    print('RoofMaterial PREDICTIONS')
    my_class = importer.get_class('RoofMaterialLLM')
    my_classifier = my_class()
    predictions = my_classifier.predict(filtered_images_satellite, text_prompts=my_classifier.text_prompts, classes=my_classifier.classes)
    print(predictions)
    curr_dir = "tmp/filtered_images/"

    for idx, (key, img) in enumerate(filtered_images_satellite.images.items()):
        filename = img.filename
        pred = predictions[key]
        img_path = os.path.join(curr_dir, filename)
        img = cv2.imread(img_path) 
        save_path = os.path.join(DATASET_FOLDER,pred,filename)
        cv2.imwrite(save_path, img)


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()    
