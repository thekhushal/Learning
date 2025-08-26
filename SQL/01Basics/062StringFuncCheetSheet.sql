SELECT
    -- 1. LENGTH vs CHAR_LENGTH
    LENGTH('Khushal Sharma') AS byte_length,
    CHAR_LENGTH('Khushal Sharma') AS char_length,
    LENGTH('漢') AS length_han, 
    CHAR_LENGTH('漢') AS char_length_han,

    -- 2. LOWER and UPPER
    LOWER('Khushal Sharma') AS name_lower,
    UPPER('Khushal Sharma') AS name_upper,

    -- 3. TRIM, LTRIM, RTRIM, Leading, Traling, Both
    TRIM('   Hello World   ') AS trimmed,
    LTRIM('   Hello') AS left_trimmed,
    RTRIM('World   ') AS right_trimmed,
    trim(leading 'z' from 'zzzSQLzzz'),
    trim(trailing 'z' from 'zzzSQLzzz'),
    trim(both 'z' from 'zzzSQLzzz'),

    -- 4. SUBSTRING / SUBSTR
    SUBSTRING('Khushal Sharma', 1, 6) AS first_name_part,
    SUBSTR('Khushal Sharma', 9, 6) AS last_name_part,

    -- 5. REPLACE
    REPLACE('Hello Khushal', 'Khushal', 'World') AS replaced,

    -- 6. CONCAT and CONCAT_WS
    CONCAT('Khushal', ' ', 'Sharma') AS full_name,
    CONCAT_WS('-', '2025', '08', '20') AS concat_with_separator,

    -- 7. INSTR / LOCATE / POSITION
    INSTR('Khushal Sharma', 'Sharma') AS instr_pos,
    LOCATE('Sharma', 'Khushal Sharma') AS locate_pos,
    POSITION('Sharma' IN 'Khushal Sharma') AS position_pos,

    -- 8. LEFT and RIGHT
    LEFT('Khushal', 3) AS left_part,
    RIGHT('Sharma', 3) AS right_part,

    -- 9. LPAD and RPAD
    LPAD('7', 4, '0') AS padded_left,
    RPAD('7', 4, 'x') AS padded_right,

    -- 10. REVERSE and REPEAT
    REVERSE('Khushal') AS reversed_name,
    REPEAT('Hi', 3) AS repeated_str,

    -- 11. STRCMP (string compare)
    STRCMP('apple', 'banana') AS strcmp_example1, -- -1
    STRCMP('banana', 'apple') AS strcmp_example2, -- 1
    STRCMP('apple', 'apple') AS strcmp_example3, -- 0

    -- 12. ASCII and CHAR
    ASCII('A') AS ascii_value_of_A,
    CHAR(65, 66, 67) AS char_from_ascii, -- gives 'ABC'

    -- 13. HEX and UNHEX
    HEX('MySQL') AS hex_value,
    UNHEX('4D7953514C') AS unhex_value,

    -- 14. FORMAT (numeric formatting)
    FORMAT(1234567.891, 2) AS formatted_number;
