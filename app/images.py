from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit()
imagekit.private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
imagekit.public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
imagekit.url_endpoint=os.getenv("IMAGEKIT_URL"),
