SELECT * FROM gamers;
-- WHERE clan_id = 3;

-- This should remove uniqueness
ALTER TABLE gamers DROP INDEX gamers.clan_id;

INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Orion','Steel','IronWolf',1);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Birdy','Shadowbourne','Owl',1);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Luna','Ryder','NightRider',1);

INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Aurora','Frost','NorthernLights',2);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Maximus','Silver','SilverRider',2);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Robert','Smesh','Boom',2);

INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Chad','Hawt','Blaze',3);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Bingham','Sanek','Viper',3);
INSERT INTO gamers (f_name, l_name, tag, clan_id)
VALUES ('Chad','Phayer','Fury',3);

