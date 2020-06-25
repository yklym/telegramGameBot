# Use this file for migrations
if __name__ == "__main__":
    from db.models import Base
    from db.loader import engine
    Base.metadata.create_all(engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
