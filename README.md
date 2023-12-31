# RSA
В данном репозитории представлена реализация алгоритма асимметричного шифрования RSA. Проект выполнен на языке Python.

### Криптосистема RSA
Данная криптосистема является первой криптосистемой с открытым ключом. Она
основывается на сложности проблемы факторизации целых чисел, то есть разложения
целых чисел на простые множители.

### Алгоритм RSA. Описание
RSA (аббревиатура от фамилий создателей: Rivest, Shamir и Adleman) — один из самых
популярных алгоритмов ассиметричного шифрования. Криптосистема RSA стала первой
системой, пригодной и для шифрования, и для цифровой подписи.

### Последовательность шагов алгоритма RSA
1. Выбрать два больших простых числа p и q;
2. Вычислить: n = p * q, f = (p - 1) * (q - 1);
3. Выбрать случайное число e, взаимно простое с f и n;
4. Определить такое число d, для которого является истинным выражение: (e * d) mod
(f) = 1;
5. Числа e и n — это открытый ключ, а числа d и n — это закрытый ключ;
Открытым ключом зашифровывают сообщение, а закрытым — расшифровывают. Пара
чисел закрытого ключа держится в секрете.
Шифрование производится по формуле: C(i) = (M(i)e) mod n;
Дешифрование производится по формуле: M(i) = (C(i)d) mod n.

### Программная реализация шифра RSA
В программе каждая функция, используемая в шифровании и дешифровании RSA была
реазилована отдельно, а именно: нахождение модуля алгоритма, функции Эйлера,
экспоненты шифрования, экспоненты дешифрования, функция проверки числа на
простоту, функция проверяющая являются ли два числа взаимно простыми, алгоритм
Евклида, а также расширенный алгоритм Евклида и другие. Данные фукнции находят свое
применение в программе поэтапно. На вход программа принимает пару простых чисел «p»
и «q», либо генерирует их самостоятельно на основе случайного выбора чисел в заданном
по умолчанию диапазоне, затем создает пару публичного и приватного ключей;
производит шифрование и дешифрование текста с последующим выводом в консоль и
записью результата в файл «RSA».
