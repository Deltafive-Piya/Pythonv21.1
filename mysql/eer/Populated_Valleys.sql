CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `world`.`populated_valleys` AS
    SELECT 
        `world`.`countries`.`name` AS `name`,
        `world`.`countries`.`population` AS `pop`
    FROM
        `world`.`countries`
    WHERE
        ((`world`.`countries`.`surface_area` < 501)
            AND (`world`.`countries`.`population` > 100000))
	ORDER BY
		population DESC