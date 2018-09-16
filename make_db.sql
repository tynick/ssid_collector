DROP DATABASE IF EXISTS ssiddb;

-- ---
-- Database 'temperaturedb'
-- ---

CREATE DATABASE ssiddb;
USE ssiddb;

-- ---
-- Table 'temps'
-- 
-- ---

DROP TABLE IF EXISTS ssids;
    
CREATE TABLE ssids (
	  ssid_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	  ssid varchar(33) NULL DEFAULT NULL,
	  time_taken DATETIME NULL DEFAULT NULL,
	  PRIMARY KEY (ssid_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Procedure to add a new temp 
CREATE PROCEDURE addSSID(new_ssid DECIMAL(5,2), new_time_taken DATETIME)
INSERT INTO temps (temp, light, time_taken) VALUES (new_temp, new_time_taken);
  
  
  

select * from ssids;
