CREATE DATABASE Teste
default character set utf8
default collate utf8_general_ci;

DROP DATABASE Teste;

USE Teste;

CREATE TABLE cadastros (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    senha INT(4) NOT NULL,
    PRIMARY KEY (id)
)default charset = utf8;

