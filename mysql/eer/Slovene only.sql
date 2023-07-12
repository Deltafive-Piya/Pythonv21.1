CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `world`.`slovene_only` AS
    SELECT 
        `world`.`countrylanguage`.`CountryCode` AS `CountryCode`,
        --`world`.`countrylanguage`.`Language` AS `Tongue`
    FROM
        `world`.`countrylanguage`
    WHERE
        (`world`.`countrylanguage`.`Language` = 'Slovene')
    ORDER BY `world`.`countrylanguage`.`Percentage` DESC