from app.db import SessionLocal


# Dependency
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
