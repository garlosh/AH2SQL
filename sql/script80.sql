-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.0.31 - MySQL Community Server - GPL
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para ah2sql
DROP DATABASE IF EXISTS `ah2sql`;
CREATE DATABASE IF NOT EXISTS `ah2sql` /*!40100 DEFAULT CHARACTER SET armscii8 COLLATE armscii8_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ah2sql`;

-- Copiando estrutura para procedure ah2sql.adicionar_nome_manual
DROP PROCEDURE IF EXISTS `adicionar_nome_manual`;
DELIMITER //
CREATE PROCEDURE `adicionar_nome_manual`()
BEGIN
	UPDATE `summary`
	LEFT JOIN `item_db` ON `summary`.item = `item_db`.item
	SET `summary`.`nome` = `item_db`.`nome`
	WHERE `summary`.nome IS NULL;
END//
DELIMITER ;

-- Copiando estrutura para tabela ah2sql.item_db
DROP TABLE IF EXISTS `item_db`;
CREATE TABLE IF NOT EXISTS `item_db` (
  `item` char(6) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL,
  `nome` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_bin DEFAULT NULL,
  PRIMARY KEY (`item`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela ah2sql.summary
DROP TABLE IF EXISTS `summary`;
CREATE TABLE IF NOT EXISTS `summary` (
  `item` char(6) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL DEFAULT '',
  `safra` datetime NOT NULL,
  `media` float NOT NULL,
  `mediana` float NOT NULL,
  `desvio` float DEFAULT NULL,
  `contagem` smallint NOT NULL,
  `minimo` float NOT NULL,
  `maximo` float NOT NULL,
  `nome` varchar(50) COLLATE armscii8_bin DEFAULT NULL,
  PRIMARY KEY (`item`,`safra`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Exportação de dados foi desmarcado.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
