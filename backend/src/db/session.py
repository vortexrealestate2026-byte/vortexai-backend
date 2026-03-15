from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

# Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    future=True
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

def get_session():
    """
    FastAPI dependency — yields a DB session and ensures cleanup.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_sync_session():
    """
    For workers, scripts, and background tasks.
    Returns a session instead of yielding it.
    """
    return SessionLocal()
