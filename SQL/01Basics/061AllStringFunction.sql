SELECT
    -- 1. LENGTH of a string
    LENGTH('Khushal Sharma') AS name_length,
    char_length('Khushal Sharma') AS char_length,

        -- Diff between length and char length
    length('漢'), char_length('漢'),

    -- 2. LOWER and UPPER
    LOWER('Khushal Sharma') AS name_lowercase,
    UPPER('Khushal Sharma') AS name_uppercase,

    -- 3. TRIM, LTRIM, RTRIM
    TRIM('   Hello World   ') AS trimmed,
    LTRIM('   Hello') AS left_trimmed,
    RTRIM('World   ') AS right_trimmed,

    -- 4. SUBSTRING (from position 1, length 6)
    SUBSTRING('Khushal Sharma', 1, 6) AS first_name_part,

    -- 5. REPLACE
    REPLACE('Hello Khushal', 'Khushal', 'World') AS replaced,

    -- 6. CONCAT
    CONCAT('Khushal', ' ', 'Sharma') AS full_name,

    -- 7. INSTR (position of substring)
    INSTR('Khushal Sharma', 'Sharma') AS position_of_last_name,

    -- 8. LEFT and RIGHT
    LEFT('Khushal', 3) AS left_part,
    RIGHT('Sharma', 3) AS right_part,

    -- 9. LPAD and RPAD
    LPAD('7', 4, '0') AS padded_left,
    RPAD('7', 4, 'x') AS padded_right,

    -- 10. REVERSE
    REVERSE('Khushal') AS reversed_name,

    -- 11. FORMAT (MySQL only)
    FORMAT(1234567.891, 2) AS formatted_number;
