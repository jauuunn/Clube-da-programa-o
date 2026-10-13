CREATE DATABASE IF NOT EXISTS clube2026_2;
USE clube2026_2;

CREATE TABLE aeroporto (
  codigo int(5) NOT NULL PRIMARY KEY,
  descricao varchar(30) DEFAULT NULL,
  telefone char(10) DEFAULT NULL,
  endereco varchar(30) DEFAULT NULL
);

CREATE TABLE cia (
  codigo int(5) NOT NULL PRIMARY KEY,
  nome varchar(30) DEFAULT NULL,
  status char(1) DEFAULT NULL
);

CREATE TABLE tipo_aeronave (
  codigo int(5) NOT NULL PRIMARY KEY,
  descricao varchar(30) DEFAULT NULL,
  peso int(5) DEFAULT NULL,
  qtd_pass int(3) DEFAULT NULL
);

CREATE TABLE cia_aeroporto (
  codigo_cia int(5) NOT NULL,
  codigo_aeroporto int(5) NOT NULL,
  dt_inicio_operacao date DEFAULT NULL,
  PRIMARY KEY (codigo_cia, codigo_aeroporto),
  CONSTRAINT FK_cod_cia_1 FOREIGN KEY (codigo_cia) REFERENCES cia (codigo),
  CONSTRAINT FK_codigo_aeroporto FOREIGN KEY (codigo_aeroporto) REFERENCES aeroporto (codigo)
);

CREATE TABLE cia_tipo_aeronave (
  codigo_cia int(5) NOT NULL,
  codigo_tipo_aer int(5) NOT NULL,
  Data_aquisicao date DEFAULT NULL,
  status char(1) DEFAULT NULL,
  PRIMARY KEY (codigo_cia, codigo_tipo_aer),
  CONSTRAINT FK_codigo_cia FOREIGN KEY (codigo_cia) REFERENCES cia (codigo),
  CONSTRAINT FK_codigo_tipo_aer FOREIGN KEY (codigo_tipo_aer) REFERENCES tipo_aeronave (codigo)
);

INSERT INTO aeroporto (codigo, descricao, telefone, endereco) VALUES
(1, 'tom jobim', '2196980315', 'rua joao'),
(2, 'santos dumont', '2198765498', 'estr. afonsio');

INSERT INTO cia (codigo, nome, status) VALUES
(1, 'gol', 'A'),
(2, 'azul', 'A'),
(3, 'latam', 'A'),
(4, 'united', 'A');

INSERT INTO tipo_aeronave (codigo, descricao, peso, qtd_pass) VALUES
(1, 'boing 737', 2000, 130),
(2, 'boing 747', 2300, 135),
(3, 'boing 767', 2100, 140),
(4, 'airbus A320', 2400, 150),
(5, 'airbus A330', 2500, 160),
(6, 'airbus A340', 2550, 165);