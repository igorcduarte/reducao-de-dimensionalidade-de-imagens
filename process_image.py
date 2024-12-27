from PIL import Image
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
        
    with Image.open(image_path) as img:

        img = img.convert('RGB')

        image_data = list(img.getdata())
        return image_data, img.width, img.height

def rgb_to_grayscale(image_data, width, height):
    grayscale = []
    for pixel in image_data:
        gray_value = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
        grayscale.append(gray_value)
    return grayscale

def grayscale_to_binary(grayscale_data, threshold=127):
    binary = []
    for pixel in grayscale_data:
        binary_value = 255 if pixel > threshold else 0
        binary.append(binary_value)
    return binary

def save_grayscale_image(grayscale_data, width, height, output_path):

    img = Image.new('L', (width, height))
    img.putdata(grayscale_data)
    img.save(output_path)

def save_binary_image(binary_data, width, height, output_path):

    img = Image.new('1', (width, height)) 
    img.putdata(binary_data)
    img.save(output_path)

def process_image(input_path, threshold=127):
    
    base_name = os.path.splitext(input_path)[0]
    grayscale_path = f"{base_name}_grayscale.png"
    binary_path = f"{base_name}_binary.png"
    
    print(f"Carregando imagem: {input_path}")
    image_data, width, height = load_image(input_path)
    
    print("Convertendo para escala de cinza...")
    grayscale_data = rgb_to_grayscale(image_data, width, height)
    save_grayscale_image(grayscale_data, width, height, grayscale_path)
    
    print("Convertendo para imagem binária...")
    binary_data = grayscale_to_binary(grayscale_data, threshold)
    save_binary_image(binary_data, width, height, binary_path)
    
    print("\nProcessamento concluído!")
    print(f"Imagem em escala de cinza salva em: {grayscale_path}")
    print(f"Imagem binária salva em: {binary_path}")

def main():
    image_path = "images\lena.jpg"
    threshold = 127
    
    try:
        process_image(image_path, threshold)
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    main()