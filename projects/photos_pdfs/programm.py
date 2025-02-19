import fitz  # PyMuPDF
from PIL import Image
import os
import io
import imagehash
import cv2
import torch
import numpy as np
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.data import MetadataCatalog


def setup_predictor():
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml"))
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.3  # Установите порог
    cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"  # Используем GPU, если доступно

    predictor = DefaultPredictor(cfg)
    return predictor


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
            cropped_images = detect_and_crop(image, setup_predictor())
            
            for i, cropped_img in enumerate(cropped_images):
                image_name = f'{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_num + 1}_img_{img_index}_{i}.png'
                image_path = os.path.join(output_folder, image_name)
                
                # Сохраняем изображение
                cropped_img.save(image_path)
                

def detect_and_crop(image, predictor):
    image_np = np.array(image)
    outputs = predictor(image_np)
    
    instances = outputs["instances"]
    pred_boxes = instances.pred_boxes
    
    cropped_images = []
    for box in pred_boxes:
        x1, y1, x2, y2 = map(int, box.cpu().numpy())
        crop = image_np[y1:y2, x1:x2]
        cropped_image = Image.fromarray(crop)
        cropped_images.append(cropped_image)
    
    return cropped_images


def main():
    directory = '/mnt/d/Images/Хроники/фото'
    pdf_files = os.listdir(directory)  # Список ваших PDF файлов
    output_folder = '/mnt/d/Images/Хроники/extracted_old_images_v8'
    
    for pdf_file in pdf_files:    
        print(f'Process file {pdf_file}')
        extract_images_from_pdf(f'{directory}/{pdf_file}', output_folder)
    
    print(f"Изображения сохранены в {output_folder}")


if __name__ == "__main__":
    main()
