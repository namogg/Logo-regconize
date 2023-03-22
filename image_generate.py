from PIL import Image, ImageDraw, ImageFilter
import string
import random
import math
background = Image.open("C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/background/6921201_9c482d378a_c.jpg")
logo = Image.open("C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/logo/highlandcoffee.jpg")
train_file = "C:/Users/ADMIN/Documents/TensorFlow/workspace/training_demo/train_generated/1.jpg"
def get_size(background: Image, logo: Image):
    """
    Lấy chiều cao và chiều rộng ảnh 
    Param
    ----------------
    background
    logo

    Return
    ----------------
    - Chiều cao và chiều rộng lần lượt của background và logo nếu ảnh background lớn hơn ảnh logo
    """
    if background.size <= logo.size:
        return 0,0,0,0
    background_height,background_width = background.size
    logo_height,logo_width = logo.size
    return background_height,background_width,logo_height,logo_width 

def draw_box(img,x_min,y_min,x_max,y_max):
    draw = ImageDraw.Draw(img)
    # Draw the bounding box on the image
    draw.rectangle(((x_min, y_min), (x_max, y_max)), outline="green", width=2)
    # Display image with bounding boxes and class labels
    img.show()

def create_train_example(traindir:string ,background:Image,logo:Image):
    """
    Chèn logo vào ảnh
    Param
    ----------------
    - traindir: đường dẫn đến folder để tạo ảnh 
    - background: ảnh background
    - logo: ảnh logo cần chèn

    Return
    ----------------
    - Tọa độ của logo
    """
    bg_height,bg_width,logo_height,logo_width = get_size(background,logo)

    min_height = 0
    min_width = 0
    max_height = bg_height - logo_height
    max_width = bg_width - logo_width
    x = random.randint(min_width, max_width)
    y = random.randint(min_height, max_height)

    background.paste(logo,(y,x))
    background.save(traindir)

    #coordinate transform
    xmin = x
    ymin = bg_height - logo_height - y
    xmax = x + logo_width
    ymax = bg_height - y
    return xmin, ymin, xmax, ymax


create_train_example(train_file,background,logo)
            