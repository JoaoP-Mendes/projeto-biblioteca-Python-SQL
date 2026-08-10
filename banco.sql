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