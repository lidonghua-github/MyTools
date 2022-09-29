import os
import shutil
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
# chrome --remote-debugging-port=9527 --user-data-dir="C:\ChromeTmp"

def get_next_page_btn(dr):
    try:
        element = dr.find_element(By.CLASS_NAME, 'readerFooter_button')
    except:
        return None
    return element


def screen_shot_page(src_dir, dst_dir):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    time.sleep(30)
    i = 0
    while True:
        pyautogui.click(x=1770, y=54)
        time.sleep(30)
        list_file = os.listdir(src_dir)
        print(list_file)
        for file_name in list_file:
            shutil.copy(src_dir + file_name, dst_dir + '{}.jpg'.format(i))
            time.sleep(10)
            os.unlink(src_dir + file_name)
            i += 1
        next_btn = get_next_page_btn(driver)
        if next_btn is None:
            break
        next_btn.click()
        time.sleep(30)

    time.sleep(30)
    return i


def crop_all_images(src_dir, dst_dir, num):
    for i in range(0, num + 1):
        img = Image.open(src_dir + '{}.jpg'.format(i))
        width, height = img.size
        box = (455, 0, width - 455, height)
        region = img.crop(box)
        region.save(dst_dir + "crop_{}.jpg".format(i), quality=100, subsampling=0)


def combine_imgs_pdf(src_dir, num):
    sources = []
    output = Image.open(src_dir + "crop_{}.jpg".format(0))
    for i in range(1, num + 1):
        img = Image.open(src_dir + "crop_{}.jpg".format(i))
        sources.append(img)
    output.save(src_dir + 'out.pdf', "pdf", save_all=True, append_images=sources, quality=100, subsampling=0)


if __name__ == '__main__':
    src_dir = r'C:\\Users\\T470\\Downloads\\log\image\\'
    dst_dir = r'C:\\log\\image\\'
    dst_dir_crop = r'C:\\log\image\\crop\\'
    num = screen_shot_page(src_dir, dst_dir)
    crop_all_images(dst_dir, dst_dir_crop, num)
    combine_imgs_pdf(dst_dir_crop, num)
