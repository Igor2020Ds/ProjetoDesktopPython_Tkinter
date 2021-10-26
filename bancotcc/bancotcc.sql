-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 03-Out-2021 às 21:23
-- Versão do servidor: 10.4.18-MariaDB
-- versão do PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bancotcc`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cliente`
--

CREATE TABLE `cliente` (
  `Idcliente` varchar(6) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `Telefone` varchar(50) NOT NULL,
  `Endereco` varchar(80) DEFAULT 'Brasil',
  `data_compra` date DEFAULT NULL,
  `valor` decimal(5,2) DEFAULT NULL,
  `ProdComprado` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `estoque`
--

CREATE TABLE `estoque` (
  `Id_Produto` varchar(15) NOT NULL,
  `Status_Produto` enum('Em Estoque','Em Falta') DEFAULT NULL,
  `Nome_Produto` varchar(40) NOT NULL,
  `Status_de_Solicitacao` enum('Solictado','Em dia') DEFAULT NULL,
  `Qualidade` enum('OK','DEFECT') DEFAULT NULL,
  `Data_de_Entrada` date DEFAULT NULL,
  `Data_de_Saida` date DEFAULT NULL,
  `Qtd_solicitada` varchar(50) NOT NULL,
  `Qtd_cadastrada` varchar(50) NOT NULL,
  `Qtd_Saida` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `fornecedores`
--

CREATE TABLE `fornecedores` (
  `Id_fornecedor` varchar(15) NOT NULL,
  `Id_Entregador` varchar(8) NOT NULL,
  `Nome_Entregador` varchar(40) NOT NULL,
  `Status_entrega` enum('Recebida','Aguardando') DEFAULT NULL,
  `Qualidade` enum('OK','DEFECT') DEFAULT NULL,
  `Data_pedido` date DEFAULT NULL,
  `Data_Entrega` date DEFAULT NULL,
  `Qtd_solicitado` varchar(50) NOT NULL,
  `Qtd_entregue` varchar(50) NOT NULL,
  `Fabricante` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `fornecedores`
--

INSERT INTO `fornecedores` (`Id_fornecedor`, `Id_Entregador`, `Nome_Entregador`, `Status_entrega`, `Qualidade`, `Data_pedido`, `Data_Entrega`, `Qtd_solicitado`, `Qtd_entregue`, `Fabricante`) VALUES
('Faber3', 'F024', 'Miguel Mccartney', 'Recebida', 'OK', '2021-08-30', '2021-09-04', '200', '200', 'FaberCastell');

-- --------------------------------------------------------

--
-- Estrutura da tabela `orcamento`
--

CREATE TABLE `orcamento` (
  `solicitante` varchar(30) NOT NULL,
  `data_solicitacao` date NOT NULL,
  `produto_solicitado` varchar(80) NOT NULL,
  `quantidade` varchar(10) NOT NULL,
  `valor_total` decimal(10,0) NOT NULL,
  `preferencia_fabricante` enum('Sim','Nao') DEFAULT NULL,
  `fabricante` varchar(30) NOT NULL,
  `proposta` enum('Fechada','Cancelada') DEFAULT NULL,
  `id_proposta` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `painel_administrativo`
--

CREATE TABLE `painel_administrativo` (
  `Id_adm` varchar(15) NOT NULL,
  `Nome_adm` varchar(30) NOT NULL,
  `criacao_nome_de_usuario` varchar(50) NOT NULL,
  `criacao_id_de_usuario` varchar(80) NOT NULL,
  `data_criacao` date NOT NULL,
  `turno_funcionario` enum('Manha','Inter','Noite') DEFAULT NULL,
  `Salario` decimal(5,2) NOT NULL,
  `codigo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `painel_administrativo`
--

INSERT INTO `painel_administrativo` (`Id_adm`, `Nome_adm`, `criacao_nome_de_usuario`, `criacao_id_de_usuario`, `data_criacao`, `turno_funcionario`, `Salario`, `codigo`) VALUES
('ADM92', 'Felipe Camargo', 'Felipe Brunelli', 'user0606', '2021-09-18', 'Noite', '999.99', 'fb48');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `usuario` (
  `nome` varchar(30) NOT NULL,
  `codigo` varchar(5) NOT NULL,
  `numero_cracha` varchar(8) NOT NULL,
  `funcao` enum('Lider','Liderado') DEFAULT NULL,
  `data_acesso` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

CREATE TABLE `vendas` (
  `codigo_venda` varchar(10) NOT NULL,
  `data_venda` date DEFAULT NULL,
  `vedendor` varchar(30) NOT NULL,
  `Idcliente` varchar(6) NOT NULL,
  `valor` decimal(5,2) DEFAULT NULL,
  `saida` enum('Retirada','Entrega') NOT NULL,
  `Id_produto` varchar(80) NOT NULL,
  `quantidade` varchar(10) DEFAULT '0000'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `vendas`
--

INSERT INTO `vendas` (`codigo_venda`, `data_venda`, `vedendor`, `Idcliente`, `valor`, `saida`, `Id_produto`, `quantidade`) VALUES
('v1', '2021-09-18', 'Gustavo Salles', '151502', '28.00', 'Retirada', '126', '8');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`Idcliente`);

--
-- Índices para tabela `estoque`
--
ALTER TABLE `estoque`
  ADD PRIMARY KEY (`Id_Produto`);

--
-- Índices para tabela `fornecedores`
--
ALTER TABLE `fornecedores`
  ADD PRIMARY KEY (`Id_fornecedor`);

--
-- Índices para tabela `orcamento`
--
ALTER TABLE `orcamento`
  ADD PRIMARY KEY (`id_proposta`);

--
-- Índices para tabela `painel_administrativo`
--
ALTER TABLE `painel_administrativo`
  ADD PRIMARY KEY (`Id_adm`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`codigo_venda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
