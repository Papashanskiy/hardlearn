import fitz  # PyMuPDF
from PIL import Image
import os
import io
import imagehash

def extract_images_from_pdf(pdf_path, output_folder):
    # Открываем PDF файл
    pdf_document = fitz.open(pdf_path)
    
    # Проверяем есть ли директория, если нет - создаем
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
            
            # Считаем хэш изображения, чтобы идентифицировать дубликаты
            img_hash = imagehash.average_hash(image)
            
            if img_hash not in seen_hashes:
                seen_hashes.add(img_hash)
                image_name = f'page_{page_num + 1}_img_{img_index}.png'
                image_path = os.path.join(output_folder, image_name)
                
                # Сохраняем изображение
                image.save(image_path)

def main():
    directory = '/mnt/d/Images/Хроники/фото'
    pdf_files = os.listdir(directory)  # Список ваших PDF файлов
    output_folder = '/mnt/d/Images/Хроники/extracted_old_images_by_4'
    
    for pdf_file in pdf_files:
        extract_images_from_pdf(f'{directory}/{pdf_file}', output_folder)
    
    print(f"Изображения сохранены в {output_folder}")

if __name__ == "__main__":
    main()
