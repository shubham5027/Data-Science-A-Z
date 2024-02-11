from db_conn import my_cursor, conn

class Transaction:
    count = 0
    def __init__(self, trans_ID: int=None, acct_ID: int=None, transac_type: str=None, ammount: float=None, transac_date: str=None) -> None:
        self.trans_ID = trans_ID
        self.acct_ID = acct_ID
        self.transac_type = transac_type
        self.ammount = ammount
        self.transac_date = transac_date


    def insert_transaction(self) -> str:
        insert_sql = 'INSERT INTO transaction(trans_ID, acct_ID, transac_type, ammount, transac_date) \
          VALUES(%s,%s,%s,%s,%s)'
        val = (self.trans_ID, self.acct_ID, self.transac_type, self.ammount, 
              self.transac_date)
        # val = (1,1,'Deposit',3000,'2023-07-25')
        
        my_cursor.execute(insert_sql, val)
        conn.commit()
        return my_cursor.rowcount+' Transaction created..'


    def __get_all_transactions(self) -> list:
        sql = 'SELECT * FROM transaction'
        my_cursor.execute(sql)
        Transaction.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result
    

    @classmethod
    def get_all_transactions_by_acct_ID(a_ID: int) -> list:
        sql = f'SELECT * FROM transaction WHERE acct_ID = {a_ID}'
        my_cursor.execute(sql)

        result = list(my_cursor.fetchall())
        return result
    
    @classmethod
    def get_all_transactions_count_by_acct_ID(a_ID: int) -> int:
        sql = f'SELECT * FROM transaction WHERE acct_ID = {a_ID}'
        my_cursor.execute(sql)
        Transaction.count = my_cursor.rowcount

        result = list(my_cursor.fetchall())
        return result
    