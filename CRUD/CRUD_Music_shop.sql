#Create
DELIMITER $$
CREATE DEFINER=`root`@`localhost` 
PROCEDURE `C_MediaType`(IN MediaType TEXT)
BEGIN
INSERT INTO media_types (Name)
VALUE (MediaType);
commit;
END$$
DELIMITER ;


#Read
DELIMITER $$
CREATE DEFINER=`root`@`localhost` 
PROCEDURE `R_MediaType`(IN mediaID TEXT)
BEGIN
   SELECT *
   FROM media_types
   WHERE MediaTypeId = mediaID;
END$$
DELIMITER ;


#Update
DELIMITER $$
CREATE DEFINER=`root`@`localhost` 
PROCEDURE `U_MediaType`(IN mediaID TEXT, IN NewMediaType TEXT)
BEGIN
   UPDATE media_types
   SET Name = NewMediaType
   WHERE MediaTypeId = mediaID;
   commit;
END$$
DELIMITER ;


#Delete
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `D_MediaType`(IN mediaID TEXT)
BEGIN
   DELETE FROM media_types
   WHERE MediaTypeId = mediaID;
   commit;
END$$
DELIMITER ;



#Testam komandas

#use music_shop;

#call C_MediaType('mp1');
#call R_MediaType('7');
#call U_MediaType('7', 'mp3');
#call D_MediaType('6');
#call D_MediaType('7');


#select * from media_types;

