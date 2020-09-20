from selenium import webdriver

import os
import time

import requests

url_template = "https://www.bing.com/images/search?q={}"

images_container_id = "mmComponent_images_2"
overlay_iframe_id = "OverlayIFrame"
image_container_class = "imgContainer"
next_image_button_id = "navr"


def scrape_images(search_query):
    export_directory = os.path.dirname(os.path.realpath(__file__)) + "/scraper_output"
    if not os.path.exists(export_directory):
        os.mkdir(export_directory)

    url = url_template.format("+".join(search_query.split(" ")))

    driver = webdriver.Firefox()
    driver.get(url)

    image_container = driver.find_element_by_id(images_container_id)
    first_image = image_container.find_element_by_tag_name("img")
    first_image.click()

    time.sleep(5)
    driver.switch_to_frame(overlay_iframe_id)
    t = 0
    while True:
        next_image_button = driver.find_element_by_id(next_image_button_id)
        image_element = driver.find_element_by_class_name(image_container_class).find_element_by_tag_name("img")
        image_source = image_element.get_attribute("src")

        if any(extension in image_source for extension in ["png", "jpg"]):
            try:
                image_request = requests.get(image_source)
                #file_name = export_directory + "/" + image_source.split("/")[-1].split("?")[0] #name the picture with original name
                file_name =  export_directory + "/" +  str(t) + ".jpg"
                file = open(file_name, "wb")
                file.write(image_request.content)
                file.close()
            except:
                print("This shit failed.")

        next_image_button.click()
        t+=1

def main():
    scrape_images("Lionfish")


if __name__ == '__main__':
    main()