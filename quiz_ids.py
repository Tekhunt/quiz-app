from typing import List
import psycopg2
from psycopg2 import Error
from urllib.parse import urlparse


def get_quiz_ids(store_input: str) -> List[int]:
    """Returns a list of quiz IDs for the given store.

    Args:
        store_input: The store input, which can be a URL or store name.

    Returns:
        A list of quiz IDs.
    
    Raises:
        psycopg2.Error: If the input is invalid or the store does not exist.
    """
    try:
        if not store_input:
            raise psycopg2.Error("The input cannot be empty. Please provide store name or url")
        
        parsed_store = urlparse(store_input)
        if parsed_store.netloc:
            store_input = parsed_store.netloc
        else:
            store_input = parsed_store.path.strip('/')
        print(store_input)

        with psycopg2.connect(
            user='postgres',
            host='vqb-task.cythzrxvyvrw.us-east-2.rds.amazonaws.com',
            password='qfJ41o7RRoo8kpro',
            port=5432,
            database='whai_production'
        ) as connection:
            if not store_input:
                raise psycopg2.Error("The input cannot be empty.")

            curs = connection.cursor()
            curs.execute("""
            SELECT quizzes.id
            FROM quizzes
            JOIN shops ON quizzes.shop = shops.id
            WHERE shops.shopname = %s
            """, (store_input,))

            quiz_IDs = [id[0] for id in curs.fetchall()]


            if not quiz_IDs:
                raise psycopg2.Error("The store does not exist.")
    except (Exception, Error) as error:
        print(error)
        print("Error while connecting to PostgreSQL", error)

        
    return quiz_IDs
 
print(get_quiz_ids('https://esteas.myshopify.com'))