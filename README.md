# ---------------------------------- CREATE TABLE --------------------------------------- 

CREATE TABLE `em_order` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ORDER_ID` varchar(30) DEFAULT NULL,
  `PROCESS_INST_ID` varchar(30) DEFAULT NULL,
  `WORK_ORDER_STATUS` varchar(30) DEFAULT NULL,
  `DEAL_STATUS` varchar(30) DEFAULT NULL,
  `ORDER_TYPE_ID` varchar(30) DEFAULT NULL,
  `CREATE_OPER_ID` varchar(30) DEFAULT NULL,
  `DEL_FLAG` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `idx_order_id` (`ORDER_ID`),
  KEY `idx_process_inst_id` (`PROCESS_INST_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=54866 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE ee_work_order (
	ID INT(30) AUTO_INCREMENT PRIMARY KEY,
	ORDER_ID VARCHAR(30),
	PROCESS_INST_ID VARCHAR(30),
	WORK_ORDER_ID VARCHAR(30),
	WORK_ORDER_STATUS VARCHAR(30),
	INDEX idx_order_id (ORDER_ID),
	INDEX idx_process_inst_id (PROCESS_INST_ID),
	INDEX idx_work_order_id (WORK_ORDER_ID)
);

drop TABLE ee_work_order;

CREATE TABLE ee_work_order_participant (
	ID INT(30) AUTO_INCREMENT PRIMARY KEY,
	ORDER_ID VARCHAR(30),
	PROCESS_INST_ID VARCHAR(30),
	WORK_ORDER_ID VARCHAR(30),
	WORK_ORDER_STATUS VARCHAR(30),
	INDEX idx_order_id (ORDER_ID),
	INDEX idx_process_inst_id (PROCESS_INST_ID),
	INDEX idx_work_order_id (WORK_ORDER_ID)
);

CREATE TABLE dic_value (
	ID INT(30) AUTO_INCREMENT PRIMARY KEY,
	DICT_CODE VARCHAR(30),
	VALUE VARCHAR(30),
	DEL_FLAG INT(1),
	INDEX idx_dict_code (DICT_CODE),
	INDEX idx_value (VALUE)
);





DELIMITER //  
  
CREATE PROCEDURE InsertEmorder(IN num_same_id INT, IN num_diff_id INT)  
BEGIN  
    DECLARE i INT DEFAULT 1;  
    DECLARE j INT DEFAULT 1;  
  
    -- 插入具有相同ORDER_ID的行  
    WHILE i <= num_same_id DO  
        INSERT INTO em_order (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_STATUS, DEAL_STATUS, ORDER_TYPE_ID, CREATE_OPER_ID)  
        VALUES   
        ('same_test_id_123456789',  
         CONCAT('PI_', FLOOR(RAND() * 1000000)),  
         CONCAT('WS_', FLOOR(RAND() * 100)),  
         CONCAT('DS_', FLOOR(RAND() * 10)),  
         CONCAT('OT_', FLOOR(RAND() * 1000)),  
         CONCAT('CO_', FLOOR(RAND() * 10000)));  
        SET i = i + 1;  
    END WHILE;  
  
    -- 插入具有不同ORDER_ID的行  
    WHILE j <= num_diff_id DO  
        INSERT INTO em_order (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_STATUS, DEAL_STATUS, ORDER_TYPE_ID, CREATE_OPER_ID)  
        VALUES   
        (CONCAT('DIFF_', FLOOR(RAND() * 1000000000)),  
         CONCAT('PI_', FLOOR(RAND() * 1000000)),  
         CONCAT('WS_', FLOOR(RAND() * 100)),  
         CONCAT('DS_', FLOOR(RAND() * 10)),  
         CONCAT('OT_', FLOOR(RAND() * 1000)),  
         CONCAT('CO_', FLOOR(RAND() * 10000)));  
        SET j = j + 1;  
    END WHILE;  
END //  






DELIMITER //  
  
CREATE PROCEDURE InsertEWO(IN num_same_id INT, IN num_diff_id INT)  
BEGIN  
    DECLARE i INT DEFAULT 1;  
    DECLARE j INT DEFAULT 1;  
  
    -- 插入具有相同ORDER_ID的行  
    WHILE i <= num_same_id DO  
        INSERT INTO ee_work_order (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_ID, WORK_ORDER_STATUS)  
        VALUES (  
            'same_test_id_123456789',  -- 假设所有订单使用相同的ORDER_ID作为示例  
            CONCAT('PI_', FLOOR(RAND() * 1000000)),  
            CONCAT('WO_', FLOOR(RAND() * 1000000)),  -- 为WORK_ORDER_ID生成随机值  
            CONCAT('WS_', FLOOR(RAND() * 100))  
        );  
        SET i = i + 1;  
    END WHILE;  
  
    -- 插入具有不同ORDER_ID的行  
    WHILE j <= num_diff_id DO  
        INSERT INTO ee_work_order (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_ID, WORK_ORDER_STATUS)  
        VALUES (  
            CONCAT('DIFF_', FLOOR(RAND() * 1000000000)),  -- 假设所有订单使用相同的ORDER_ID作为示例  
            CONCAT('PI_', FLOOR(RAND() * 1000000)),  
            CONCAT('WO_', FLOOR(RAND() * 1000000)),  -- 为WORK_ORDER_ID生成随机值  
            CONCAT('WS_', FLOOR(RAND() * 100))  
        ); 
        SET j = j + 1;  
    END WHILE;  
END // 










DELIMITER //  
  
CREATE PROCEDURE InsertEWOP(IN num_same_id INT, IN num_diff_id INT)  
BEGIN  
    DECLARE i INT DEFAULT 1;  
    DECLARE j INT DEFAULT 1;  
  
    -- 插入具有相同ORDER_ID的行  
    WHILE i <= num_same_id DO  
        INSERT INTO ee_work_order_participant (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_ID, WORK_ORDER_STATUS)  
            VALUES (  
                'same_test_id_123456789',  
                CONCAT('PI_', FLOOR(RAND() * 1000000)),  
								CONCAT('WO_', FLOOR(RAND() * 1000000)),  
                CONCAT('PS_', FLOOR(RAND() * 100))  -- 为WORK_ORDER_STATUS生成随机值  
            );  
        SET i = i + 1;  
    END WHILE;  
  
    -- 插入具有不同ORDER_ID的行  
    WHILE j <= num_diff_id DO  
        INSERT INTO ee_work_order_participant (ORDER_ID, PROCESS_INST_ID, WORK_ORDER_ID, WORK_ORDER_STATUS)  
            VALUES (  
                CONCAT('DIFF_', FLOOR(RAND() * 1000000000)),  
                CONCAT('PI_', FLOOR(RAND() * 1000000)),  
								CONCAT('WO_', FLOOR(RAND() * 1000000)),  
                CONCAT('PS_', FLOOR(RAND() * 100))  -- 为WORK_ORDER_STATUS生成随机值  
            );  
        SET j = j + 1;  
    END WHILE;  
END // 
  
DELIMITER ;
















INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_6', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_7', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_8', 0, 'name');
INSERT INTO `test_schema`.`dic_value` (`DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_9', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_5', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_4', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_3', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_2', 0, 'name');
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES ( 'ORDER_STATUS', 'DS_1', 0, 'name');



INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);
INSERT INTO `test_schema`.`dic_value` ( `DICT_CODE`, `VALUE`, `DEL_FLAG`, `NAME`) VALUES (' ORDER_TYPE_ID', NULL, 0, NULL);



delete from em_order where id > 50000





select em.*
from em_order em 
left join ee_work_order ewo on em.order_id = ewo.order_id and em.process_inst_id = ewo.process_inst_id and ewo.work_order_status = 'DOING'
left join ee_work_order_participant ewop on em.order_id = ewop.order_id and ewo.work_order_id = ewop.work_order_id
where em.del_flag = 0
and em.deal_status != 'DS_0'
and em.create_oper_id = 'sysadmin'



UPDATE ee_work_order set work_order_status='DOING'

UPDATE em_order set create_oper_id='sysadmin'

UPDATE em_order set DEL_FLAG=0







