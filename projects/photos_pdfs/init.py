import fitz  # PyMuPDF
from PIL import Image, ImageOps
import os
import io
import imagehash
import cv2
import numpy as np

def extract_images_from_pdf(pdf_path, output_folder):
    # Открываем PDF файл
    pdf_document = fitz.open(pdf_path)
    
    # Проверяем, есть ли директория, если нет - создаем
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    seen_hashes = set()
    
    # Пробегаем по всем страницам PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        img_list = page.get_images(full=True)
        
        # Пробегаем по всем изображениям на странице
        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image['image']
            image = Image.open(io.BytesIO(image_bytes))

            # Для удаления дубликатов
            img_hash = imagehash.average_hash(image)
            if img_hash in seen_hashes:
                continue
            
            seen_hashes.add(img_hash)

            # Обрезаем изображение по белым границам
            cropped_images = crop_image(image)
            
            for i, cropped_img in enumerate(cropped_images):
                # Поворачиваем изображение в нужное направление
                corrected_image = rotate_image_to_correct_orientation(cropped_img)
                
                image_name = f'{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_num + 1}_img_{img_index}_{i}.png'
                image_path = os.path.join(output_folder, image_name)
                    
                # Сохраняем изображение
                corrected_image.save(image_path)

def rotate_image_to_correct_orientation(image):
    # Преобразуем изображение в черно-белое
    grayscale_image = image.convert("L")

    # Применяем авто-поворот
    corrected_image = ImageOps.exif_transpose(image)
    
    return corrected_image

def crop_image(image, min_width=350, min_height=350):
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # Найти контуры
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cropped_images = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Фильтруем мелкие контуры
        if w >= min_width and h >= min_height:
            # Извлекаем каждый отдельный объект/фотографию в прямоугольнике
            crop = image_np[y:y+h, x:x+w]
            cropped_image = Image.fromarray(crop)
            cropped_images.append(cropped_image)
    
    return cropped_images


def main():
    directory = '/mnt/d/Images/Хроники/фото'
    pdf_files = os.listdir(directory)  # Список ваших PDF файлов
    output_folder = '/mnt/d/Images/Хроники/extracted_old_images'
    
    for pdf_file in pdf_files:
        if pdf_file == 'SCAN0026.pdf':
            pass
        extract_images_from_pdf(f'{directory}/{pdf_file}', output_folder)
    
    print(f"Изображения сохранены в {output_folder}")

if __name__ == "__main__":
    main()
