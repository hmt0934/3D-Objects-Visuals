import os
import json

def generate_json():
    categories = {}
    # Aranacak uzantılar (Hem küçük hem büyük harf destekli)
    valid_extensions = ('.glb', '.gltf', '.stl', '.png', '.jpg', '.jpeg')

    # Mevcut dizini taramaya başla
    for root, dirs, files in os.walk('.'):
        # Gereksiz klasörleri atla
        if any(ignored in root for ignored in ['.git', '.github', '__pycache__']):
            continue

        for file in files:
            if file.lower().endswith(valid_extensions):
                # Klasör yolunu al ve Linux tarzı bölücüye çevir (/)
                rel_path = os.path.relpath(root, '.')
                category_name = "Genel" if rel_path == "." else rel_path

                # Dosya ismi ve uzantısını ayır
                name_parts = os.path.splitext(file)
                model_id = name_parts[0]
                ext = name_parts[1].lower()

                # Dosyanın tam yolunu oluştur
                full_path = os.path.join(rel_path, file).replace('\\', '/')

                if category_name not in categories:
                    categories[category_name] = []

                # Dosya tipini belirle
                file_type = "3d" if ext in ('.glb', '.gltf', '.stl') else "image"

                categories[category_name].append({
                    "id": model_id,
                    "file": full_path,
                    "type": file_type
                })

    # Listeyi kategori ismine göre sırala
    output = [{"category": cat, "models": mods} for cat, mods in sorted(categories.items())]

    # JSON olarak kaydet
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    print(f"data.json başarıyla güncellendi. Toplam {len(output)} kategori bulundu.")

if __name__ == "__main__":
    generate_json()
