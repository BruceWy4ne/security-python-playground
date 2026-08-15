INSERT INTO users (username, email, pass, created)
VALUES
('Bruce', 'bruce@gmail.com', 'abc123', '2026-08-01'),
('Alice', 'alice@gmail.com', 'xyz456', '2026-08-02'),
('Nick', 'nick@gmail.com', 'pass789', '2026-08-03'),
('Bat', 'bat@gmail.com', 'bat123', '2026-08-05'),
('spider', 'sp@gmail.com', 'man123', '2026-07-03');


INSERT INTO login (user_id, status, attempted, ip)
VALUES
(1, 'success', '2026-08-12', '192.168.59.1'),
(2, 'failed',  '2026-08-11', '192.178.59.1'),
(1, 'success', '2026-08-12', '192.168.29.1'),
(1, 'success', '2026-08-12', '193.168.59.1'),
(2, 'failed',  '2026-08-12', '192.111.59.1'),
(2, 'failed',  '2026-08-07', '178.168.59.1'),
(2, 'failed',  '2026-08-12', '192.168.90.5'),
(3, 'success', '2026-08-12', '192.168.33.3'),
(3, 'failed',  '2026-08-06', '195.165.59.1'),
(4, 'success', '2026-08-11', '199.999.99.9'),
(4, 'success', '2026-08-12', '190.160.59.1'),
(4, 'failed',  '2026-07-12', '152.168.59.1');