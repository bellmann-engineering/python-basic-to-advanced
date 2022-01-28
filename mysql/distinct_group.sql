-- create
CREATE TABLE Cars (
  Id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
  model TEXT NOT NULL,
  price DECIMAL,
  kmstand INTEGER,
  baujahr INTEGER
);

-- insert
INSERT INTO Cars VALUES (default, 'Touran', 30000, 12000, 2018);
INSERT INTO Cars VALUES (default, 'Golf', 30000, 80000, 2000);
INSERT INTO Cars VALUES (default, 'ID3', 50000, 9800, 2020);
INSERT INTO Cars VALUES (default, 'ID4', 60000, 800, 2022);
INSERT INTO Cars VALUES (default, 'ID4', 70000, 1800, 2022);

-- fetch 
SELECT * FROM Cars;

-- distinct
SELECT DISTINCT model FROM Cars;

-- group by
SELECT baujahr, COUNT(baujahr) AS AnzahlAutos 
FROM Cars 
-- WHERE baujahr='2022' 
GROUP BY baujahr;

-- having
SELECT baujahr, COUNT(baujahr) AS AnzahlAutos 
FROM Cars 
WHERE baujahr='2022'
GROUP BY baujahr, kmstand
HAVING kmstand > 800;

-- group by having after
SELECT baujahr, SUM(price) AS 'Gesamtpreis'
FROM Cars 
-- WHERE baujahr='2022' 
GROUP BY baujahr;
-- HAVING SUM(price) > 120000;
