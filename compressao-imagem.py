from PIL import Image

#Carrega imagem original
imagem = Image.open('img.jpg')

#Salva nova imagem com tamanho menor
imagem.save('img_menor.jpg', 'JPEG', optimize=True, quality=10)