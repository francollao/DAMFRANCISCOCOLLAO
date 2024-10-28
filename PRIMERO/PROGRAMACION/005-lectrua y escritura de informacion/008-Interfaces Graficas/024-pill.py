from  PIL import Image
width, height = 1920, 1080
imagen = Image.new('RGB', (width, height), color=(255, 255, 255))

ruta = 'imagen.jpg'
imagen.save(ruta)