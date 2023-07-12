CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `world`.`major_tongues` AS
    SELECT 
        `world`.`languages`.`language` AS `language`,
        --`world`.`languages`.`percentage` AS `percentage`
    FROM
        `world`.`languages`
    WHERE
        (`world`.`languages`.`percentage` > 89)
    ORDER BY `world`.`languages`.`percentage` DESC