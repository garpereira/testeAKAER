select nome, orders.id from customers, orders where orders.id_customers = customers.id and orders_date >= "2016-01-01" and orders_date < "2016-07-01";

select produtcs.name, categories.name from produtcs, categories where amount > 100 and categories.id in (1,2,3,6,9) order by categories.id ASC;

select categories.name, sum(producs.amount) from categories, products where categories.id = products.id_categories;