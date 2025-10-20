def get_cats_info(path):
    """
    Функція зчитує дані про котів із текстового файлу
    та повертає список словників із інформацією про кожного кота.

    :param path: шлях до текстового файлу
    :return: список словників з ключами "id", "name", "age"
    """
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) != 3:
                    continue

                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
        return []
    
    return cats


# Використання:
if __name__ == "__main__":
    info = get_cats_info("cats_file.txt")
    print(info)