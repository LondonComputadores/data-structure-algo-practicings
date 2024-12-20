def rgb_to_grayscale(image):
    """
    Converte uma imagem colorida (lista de listas de tuplas RGB) para níveis de cinza.
    """
    grayscale_image = []
    for row in image:
        grayscale_row = []
        for pixel in row:
            r, g, b = pixel
            # Fórmula para converter RGB para escala de cinza
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_row.append(gray)
        grayscale_image.append(grayscale_row)
    return grayscale_image

def grayscale_to_binary(image, threshold=128):
    """
    Converte uma imagem em níveis de cinza (lista de listas de inteiros) para uma imagem binarizada.
    """
    binary_image = []
    for row in image:
        binary_row = []
        for pixel in row:
            # Aplicando o limiar para binarização
            binary_pixel = 1 if pixel >= threshold else 0
            binary_row.append(binary_pixel)
        binary_image.append(binary_row)
    return binary_image

# Exemplo de uso
color_image = [
    [(123, 234, 45), (34, 56, 78)],
    [(255, 0, 0), (0, 255, 0)]
]

grayscale_image = rgb_to_grayscale(color_image)
binary_image = grayscale_to_binary(grayscale_image)

print("Imagem em níveis de cinza:")
for row in grayscale_image:
    print(row)

print("\nImagem binarizada:")
for row in binary_image:
    print(row)