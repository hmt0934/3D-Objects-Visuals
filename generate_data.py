import os
import json

def generate_json():
    categories = {}

    # Mevcut dizindeki her şeyi tara
    for root, dirs, files in os.walk('.'):
        # .git ve gizli klasörleri atla
        if '.git' in root or '.github' in root:
            continue

        for file in files:
            if file.lower().endswith('_on.png'):
                # Klasör ismini al (root . ise 'Genel' yap)
                rel_path = os.path.relpath(root, '.')
                category_name = "Genel_Koleksiyon" if rel_path == "." else rel_path

                model_id = file.replace('_on.png', '').replace('_on.PNG', '')
                full_path = os.path.join(rel_path, model_id).replace('\\', '/')

                if category_name not in categories:
                    categories[category_name] = []

                categories[category_name].append({
                    "id": model_id,
                    "fullPath": full_path
                })

    # Listeye dönüştür
    output = [{"category": cat, "models": mods} for cat, mods in categories.items()]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_json()
