from collections.abc import AsyncGenerator
import uuid
from sqlalchem import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.dealects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship