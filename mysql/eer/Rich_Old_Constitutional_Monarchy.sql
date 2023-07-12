CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `world`.`rich_old_constitutional_monarchy` AS
    SELECT 
        `world`.`countries`.`name` AS `name`,
        `world`.`countries`.`government_form` AS `government_form`,
        `world`.`countries`.`capital` AS `capital`
    FROM
        `world`.`countries`
    WHERE
        ((`world`.`countries`.`government_form` LIKE '%Constitutional Monarchy%')
            AND (`world`.`countries`.`capital` > 200)
            AND (`world`.`countries`.`life_expectancy` > 75))