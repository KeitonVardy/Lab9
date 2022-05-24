import requests
import ctypes

def download_image_from_url(image_url, save_path):
    """
    Downloads image from a specified image to a specified destination

    :param1 image_url: URL of image to download
    :param2 save_path: Location to be saved at
    :returns: Success message with image or failed message with error code
    """

    print("Downloading image from URL...", end='')
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print('Success!')

    else:
        print('Failed, Response code: ', response.status_code)
        return


def set_desktop_background_image(image_path):
    """
    Sets desktop background to the selected image

    :param1 image_path: path for the desired image
    :returns: desktop image changed
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)