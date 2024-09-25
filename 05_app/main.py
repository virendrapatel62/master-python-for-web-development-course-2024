
from app.models import student
from app.utils.logger import log
from app.db import db

db.create_connection()
log("Application started")
student = student.Student()
log("Application is going to exit")
