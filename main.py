from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Hàm kết nối database
def get_conn():
    return sqlite3.connect("northwind.db")

@app.get("/")
def home():
    return {"message": "Northwind API đang hoạt động"}

@app.get("/customers")
def get_customers():
    try:
        conn = get_conn()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM Customer LIMIT 10").fetchall()
        data = [dict(row) for row in result]
        return {"data": data}
    except Exception as e:
        print("❌ Lỗi xảy ra:", e)
        return {"error": str(e)}



