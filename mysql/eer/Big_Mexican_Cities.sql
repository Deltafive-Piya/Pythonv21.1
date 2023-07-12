CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `world`.`big_mexican_cities` AS
    SELECT 
        `world`.`cities`.`name` AS `country name`,
        --`world`.`cities`.`population` AS `pop`
    FROM
        `world`.`cities`
    WHERE
        ((`world`.`cities`.`country_code` = 'MEX')
            AND (`world`.`cities`.`population` > 500000))
    ORDER BY `world`.`cities`.`population` DESC