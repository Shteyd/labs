import sqlite3


def database_querie(property, querry, data):
    try:
        with sqlite3.connect('./assets/products.db') as db:
            cursor = db.cursor()
            if property == 1:
                cursor.execute(querry, data)
            else:
                cursor.execute(querry)
                return cursor.fetchall()
    finally:
        cursor.close()


def get_data():
    querry = """ SELECT products.product_id, product_name, price, types.type_name, existence.availability, colors.color_name FROM products INNER JOIN
                        existence ON products.availability = existence.id INNER JOIN
                        types ON products.type_id = types.type_id INNER JOIN
                        colors ON products.color_id = colors.color_id"""
    products = [list(row) for row in database_querie(2, querry, None)]
    return products


def add_data(product):
    product = tuple(product)
    querry = """INSERT INTO products (product_name, price, type_id, availability, color_id) VALUES(?, ?, ?, ?, ?)"""
    database_querie(1, querry, product)


def del_data(id):
    querry = """ DELETE FROM products WHERE product_id = ? """
    database_querie(1, querry, (id, ))


def update_data(product):
    querry = """ UPDATE products 
                SET product_name = ?,
                    price = ?,
                    type_id = ?,
                    availability = ?,
                    color_id = ? 
                WHERE product_id = ? """
    database_querie(1, querry, product)
