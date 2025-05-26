
-- task-2
INSERT INTO book VALUES (NULL, 'Мастер и Маргарита', 'Булгаков М.А.', 670.99,3);

insert into book values(1,'Мастер и Маргарита','Булгаков М.А.',670.99,3);

INSERT INTO book (
	title,
	author,
	price,
	amount
) VALUES (
	'Мастер и Маргарита',
	'Булгаков М.А.',
	670.99,
	3
);

-- task-3

INSERT INTO book (title, author, price, amount)
VALUES
    ('Белая гвардия', 'Булгаков М.А.', 540.50 , 5),
    ('Идиот', 'Достоевский Ф.М.', 460, 10),
    ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);


INSERT INTO book (title, author, price, amount)
VALUES
    ('Стихотворения и поэмы', 'Есенин С.А.', 650.00 , 15);


SELECT * FROM book;


SELECT author, title, price FROM book;


SELECT title AS Название, amount 
FROM book;

SELECT title AS Название, author AS Автор
FROM book;


SELECT title, amount, 
     1.65 * amount AS pack 
FROM book;

-- НДС-18 без округления 

SELECT title, price, 
    (price*18/100)/(1+18/100) AS tax, 
    price/(1+18/100) AS price_tax 
FROM book;

-- НДС-18 с округлением 

SELECT title, 
    price, 
    ROUND((price*18/100)/(1+18/100),2) AS tax, 
    ROUND(price/(1+18/100),2) AS price_tax 
FROM book;


-- скидка 30% с округлением 
SELECT title, author, amount, 
    ROUND(price * 0.7,2) AS new_price
FROM book;S




SELECT author, title,    
    ROUND(IIF(author = "Булгаков М.А.", price * 1.1, IIF (author = "Есенин С.А.", price * 1.05, price)),2) AS new_price
FROM book;


-- task

SELECT author, title,    
    ROUND(IF(author = "Булгаков М.А.", price * 1.1, IF (author = "Есенин С.А.", price * 1.05, price)),2) AS new_price
FROM book;

-- task 6

SELECT author, title, price
FROM book
WHERE amount < 10;

-- task 7

SELECT title, author, price , amount
FROM book
WHERE (price < 500 or price > 600) and price * amount >= 5000;