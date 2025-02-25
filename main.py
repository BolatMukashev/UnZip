import os
import zipfile

def get_unique_filename(directory, filename):
    """Возвращает уникальное имя файла, если такое уже существует в папке."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1

    return new_filename

def unzip_files(directory):
    """Разархивирует все .zip файлы, не допуская перезаписи файлов с одинаковыми именами."""
    if not os.path.exists(directory):
        print("Указанная директория не существует.")
        return

    extract_path = os.path.join(directory, "unzipped_files")  # Общая папка для всех файлов
    os.makedirs(extract_path, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            zip_path = os.path.join(directory, filename)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    new_filename = get_unique_filename(extract_path, os.path.basename(file))  # Уникальное имя
                    file_path = os.path.join(extract_path, new_filename)

                    with zip_ref.open(file) as source, open(file_path, 'wb') as target:
                        target.write(source.read())

                    print(f"Разархивирован: {file} → {new_filename}")

    print("Готово!")

if __name__ == "__main__":
    # directory = input("Введите путь к директории: ").strip()
    directory = r"C:\Users\Astana\Desktop\Client"
    unzip_files(directory)
