USE sakila;

-- ============================================================
-- 🔹 1. LENGTH vs CHAR_LENGTH
-- ============================================================

-- CHAR_LENGTH() returns number of characters
SELECT first_name, CHAR_LENGTH(first_name)
FROM actor;

-- Difference between LENGTH and CHAR_LENGTH
-- LENGTH() → returns length in BYTES
-- CHAR_LENGTH() → returns length in CHARACTERS
SELECT LENGTH('漢'), CHAR_LENGTH('漢') FROM dual;
-- Output: LENGTH=3 (bytes), CHAR_LENGTH=1 (character)

-- ============================================================
-- 🔹 2. LOWER and UPPER
-- ============================================================

SELECT first_name, 
       LOWER(first_name), 
       UPPER(LOWER(first_name)) 
FROM actor;

-- Here 'lower' is a function 
-- It can also be nested as we did in the third field

-- ============================================================
-- 🔹 3. CONCAT and CONCAT_WS
-- ============================================================

-- Example: Show full name of ED CHASE using CONCAT
SELECT first_name, last_name,
       CONCAT(first_name, '-', last_name), -- joins with '-'
       CONCAT_WS('-', first_name, last_name) -- CONCAT_WS automatically adds separator
FROM actor;

-- ============================================================
-- 🔹 4. SUBSTR / SUBSTRING
-- ============================================================

-- Syntax: SUBSTR(column, start_position, length)
-- NOTE: Indexing starts from 1 (not 0 like Python).
-- NOTE: Provide starting index + length (not start and end index).

-- Example with string literal
SELECT SUBSTR('CHETA-SINGH', 5, 3) FROM dual;
-- Output: 'A-S' (5th char is 'A', and length=3 → "A-S")

-- Using on table data
SELECT first_name, 
       SUBSTR(first_name, 2),    -- substring from 2nd char till end
       SUBSTR(first_name, 1, 1), -- first character
       SUBSTR(first_name, 1, 3), -- first 3 characters
       SUBSTR(first_name, -3),   -- last 3 characters (negative indexing)
       SUBSTR(first_name, -5, 3) -- substring starting 5th from end, length 3
FROM actor;

-- ============================================================
-- 🔹 5. INSTR (search for substring position)
-- ============================================================

SELECT first_name, 
       INSTR(first_name, 'e') 
FROM actor;

-- INSTR returns the index of mentioned character (starting at 1).
-- Returns first occurrence even if multiple exist.
-- Returns 0 if not found.
-- NOTE: SQL indexing starts at 1, not 0.

-- ============================================================
-- 🔹 6. LOCATE and POSITION (similar to INSTR)
-- ============================================================

SELECT
       LOCATE('a', 'banana') AS locate_example, -- 2
       LOCATE('a', 'banana', 3) AS locate_example, -- 4
       POSITION('a' IN 'banana') AS position_example -- 1
FROM actor;

-- With locate you can also give starting position
-- LOCATE and POSITION behave like INSTR.
-- Return 0 if not found.

-- ============================================================
-- 🔹 7. LPAD and RPAD
-- ============================================================

SELECT first_name, 
       LPAD(first_name, 5, '!') 
FROM actor;

-- LPAD adds characters to LEFT if length < desired
-- Parameters:
--   1. Field or value
--   2. Desired length
--   3. Padding character

SELECT first_name, 
       RPAD(first_name, 5, '!') 
FROM actor;

-- RPAD works the same but adds to the RIGHT

-- ============================================================
-- 🔹 8. TRIM, LTRIM, RTRIM
-- ============================================================

SELECT 
   '    dual     ' AS original,
   TRIM('    dual     ') AS trimmed,
   LTRIM('   Hello') AS left_trimmed,
   RTRIM('World   ') AS right_trimmed 
FROM dual;

-- ============================================================
-- 🔹 9. TRIM (LEADING | TRAILING | BOTH with custom char)
-- ============================================================

SELECT 'Trim',
       TRIM(LEADING 'z' FROM 'zzzSQLzzz') AS trim_leading, -- Output: 'SQLzzz'
       TRIM(TRAILING 'z' FROM 'zzzSQLzzz') AS trim_trailing, -- Output: 'zzzSQL'
       TRIM(BOTH 'z' FROM 'zzzSQLzzz') AS trim_both -- Output: 'SQL'
FROM dual;

-- ============================================================
-- 🔹 10. REPLACE
-- ============================================================

SELECT first_name, 
       REPLACE(first_name, 'E','A') AS replaced_name
FROM actor;

-- REPLACE(string, from_str, to_str)

-- ============================================================
-- 🔹 11. REVERSE
-- ============================================================

SELECT first_name, 
       REVERSE(first_name) AS reversed_name
FROM actor;

-- Reverses the string

-- ============================================================
-- 🔹 12. REPEAT
-- ============================================================

SELECT REPEAT('Hi', 3) AS repeated_string FROM dual;
-- Output: 'HiHiHi'

-- ============================================================
-- 🔹 13. STRCMP (string comparison)
-- ============================================================

SELECT 
   STRCMP('apple', 'banana') AS cmp1, -- -1 (apple < banana)
   STRCMP('banana', 'apple') AS cmp2, -- 1  (banana > apple)
   STRCMP('apple', 'apple')  AS cmp3  -- 0  (equal)
FROM dual;

-- It does lexicographical comparison to decide which string is smaller and which is bigger

-- ============================================================
-- 🔹 14. ASCII and CHAR
-- ============================================================

SELECT 
   ASCII('A') AS ascii_value,    -- 65
   CHAR(65,66,67) AS char_value; -- 'ABC'

-- ============================================================
-- 🔹 15. HEX and UNHEX
-- ============================================================

SELECT 
   HEX('MySQL') AS hex_value,       -- '4D7953514C'
   UNHEX('4D7953514C') AS str_value; -- 'MySQL'

-- ============================================================
-- 🔹 16. DUAL table
-- ============================================================

-- The DUAL table is a dummy table used when no actual table is required
SELECT 'hey', 'hello' FROM dual;

-- ============================================================
-- 🔹 17. (Note: MySQL does NOT have a direct SPLIT function)
-- ============================================================

-- Instead, we simulate using SUBSTRING_INDEX or string functions.
-- Example: Split email into username and domain

SELECT 
   SUBSTRING_INDEX('user@example.com', '@', 1) AS username,  -- 'user'
   SUBSTRING_INDEX('user@example.com', '@', -1) AS domain    -- 'example.com'
FROM dual;
