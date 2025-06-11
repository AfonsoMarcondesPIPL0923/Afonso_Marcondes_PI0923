USE SISTEMA_LOGIN;

-- Inserção de utilizadores com SHA2-256
INSERT INTO utilizadores (nome, email, password_hash) VALUES
('João Silva', 'joao@example.com', SHA2('123456', 256)),
('Maria Santos', 'maria@example.com', SHA2('qwerty', 256)),
('Carlos Costa', 'carlos@example.com', SHA2('password123', 256));

-- Simulação de logins
INSERT INTO historico_acessos (utilizador_id) VALUES
(1),
(2),
(1),
(3);

-- Atualização do último acesso
UPDATE utilizadores
SET ultimo_acesso = (
    SELECT MAX(data_acesso)
    FROM historico_acessos
    WHERE historico_acessos.utilizador_id = utilizadores.id
);
