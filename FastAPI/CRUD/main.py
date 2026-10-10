from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="Root@2026",
    database="mydatabase"
)

#create a cursor object
cursor = mydb.cursor()
app = FastAPI()

class DBModel(BaseModel):
    username: str
    password: str
    email: str
    

#CRUD Endpoints
#Select All Users

@app.get("/users", status_code=status.HTTP_302_FOUND)
def select_users():
    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    results = cursor.fetchall()
    return results


#Get User by ID
@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):
    select_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(select_query, (user_id,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

#Inset a New User
@app.post("/users", status_code=status.HTTP_201_CREATED)
def insert_user(user: DBModel):
    # Hash the password before storing it in the database
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    
    insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (user.username, user.email, hashed_password)
    
    try:
        cursor.execute(insert_query, values)
        mydb.commit()
        
    except mysql.connector.Error as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    
    return {"message": "User created successfully"}

#Update a User
@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: DBModel):
    # Hash the password before storing it in the database
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    
    update_query = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
    values = (user.username, user.email, hashed_password, user_id)
    
    cursor.execute(update_query, values)
    mydb.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"message": "User updated successfully"}

#Delete a User
@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    delete_query = "DELETE FROM users WHERE id = %s"
    cursor.execute(delete_query, (user_id,))
    mydb.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 
    return {"message": "user deleted successfully"}
