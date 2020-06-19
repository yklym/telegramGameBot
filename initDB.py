# Use this file for migrations
if __name__ == "__main__":
    from db.models.user import Base
    from db.loader import engine

    Base.metadata.create_all(engine)