def total_salary(path):
    """
    Функція зчитує дані про заробітні плати розробників із текстового файлу
    та повертає загальну і середню суму заробітної плати.

    :param path: шлях до текстового файлу
    :return: кортеж (загальна сума, середня заробітна плата)
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line}")
                    continue

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return (0, 0)


# Використання
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
