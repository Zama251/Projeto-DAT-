CREATE DATABASE Banco
default character set utf8
default collate utf8_general_ci;

USE Banco;

CREATE TABLE cadastros(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    senha INT(4) NOT NULL,
    PRIMARY KEY(id)
)default charset = utf8;

CREATE TABLE Transaçoes(
    id_transacao INT NOT NULL AUTO_INCREMENT,
    id_cadastro INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    valor INT(15) NOT NULL,
    PRIMARY KEY(id_transacao)
    FOREIGN KEY (id_cadastro) REFERENCES cadastros(id)
)default charset = utf8;