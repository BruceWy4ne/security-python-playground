-- ============================================
-- PostgreSQL Security Lab - Investigation Queries
-- ============================================


-- 1. View all users
SELECT *
FROM users;


-- 2. View all failed login attempts
SELECT *
FROM login
WHERE status = 'failed';


-- 3. Find failed login attempts with usernames
SELECT
    users.username,
    login.status,
    login.attempted,
    login.ip
FROM login
JOIN users
    ON users.id = login.user_id
WHERE login.status = 'failed';


-- 4. Find users with more than 2 failed login attempts
SELECT
    users.username,
    COUNT(login.attempted)
FROM login
JOIN users
    ON users.id = login.user_id
WHERE login.status = 'failed'
GROUP BY users.username
HAVING COUNT(login.attempted) > 2;


-- 5. Show all login attempts from newest to oldest
SELECT *
FROM login
ORDER BY attempted DESC;


-- 6. Show the 5 oldest login attempts
SELECT *
FROM login
ORDER BY attempted
LIMIT 5;


-- 7. Count failed login attempts per IP address
SELECT
    ip,
    COUNT(status)
FROM login
WHERE status = 'failed'
GROUP BY ip;