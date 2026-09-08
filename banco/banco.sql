CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE livros (
    id int primary key auto_increment,
    titulo varchar (100) not null,
    autor varchar(100) not null,
    ano year not null,
    quantidade_disponivel int not null
);

CREATE TABLE usuario (
    id int primary key auto_increment, 
    nome varchar(100) not null,
    email varchar(100) not null,
    telefone varchar(11) not null
);

CREATE TABLE emprestimo (
    id int primary key auto_increment,
    livro_id int not null,
    usuario_id int not null,
    data_emprestimo date not null,
    data_devolucao date,
    status enum ('emprestado', 'devolvido'),
    constraint id_livro foreign key (livro_id) references livros(id),
    constraint id_usuario foreign key (usuario_id) references usuario(id)
    
);
-- Alguns dados para o banco, ou você mesmo pode fazer
INSERT INTO livros (titulo, autor, ano, quantidade_disponivel) VALUES
('Dom Casmurro', 'Machado de Assis', 1899, 5),
('O Cortiço', 'Aluísio Azevedo', 1890, 3),
('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881, 4),
('Grande Sertão: Veredas', 'Guimarães Rosa', 1956, 2),
('Capitães da Areia', 'Jorge Amado', 1937, 6),
('1984', 'George Orwell', 1949, 7),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943, 10),
('A Hora da Estrela', 'Clarice Lispector', 1977, 3),
('Vidas Secas', 'Graciliano Ramos', 1938, 4),
('Iracema', 'José de Alencar', 1865, 2);

INSERT INTO usuario (nome, email, telefone) VALUES
('Ana Silva', 'ana.silva@email.com', '11987654321'),
('Bruno Souza', 'bruno.souza@email.com', '11976543210'),
('Carla Mendes', 'carla.mendes@email.com', '21965432109'),
('Diego Costa', 'diego.costa@email.com', '21954321098'),
('Elaine Rocha', 'elaine.rocha@email.com', '31943210987'),
('Fábio Lima', 'fabio.lima@email.com', '31932109876'),
('Gabriela Nunes', 'gabriela.nunes@email.com', '41921098765'),
('Henrique Alves', 'henrique.alves@email.com', '41910987654'),
('Isabela Ferreira', 'isabela.ferreira@email.com', '51909876543'),
('João Pereira', 'joao.pereira@email.com', '51898765432');

INSERT INTO emprestimo (livro_id, usuario_id, data_emprestimo, data_devolucao, status) VALUES
(1, 3, '2026-07-01', '2026-07-15', 'devolvido'),
(2, 5, '2026-07-10', NULL, 'emprestado'),
(4, 1, '2026-07-20', '2026-08-01', 'devolvido'),
(6, 8, '2026-08-01', NULL, 'emprestado'),
(9, 10, '2026-08-05', NULL, 'emprestado');