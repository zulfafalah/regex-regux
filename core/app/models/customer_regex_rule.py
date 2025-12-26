from sqlalchemy import Column, Integer, String
from ..database import Base


class CustomerRegexRule(Base):
    __tablename__ = "customer_regex_rule"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    customer_name = Column(String)
    pattern = Column(String, index=True)
    group = Column(String)
    field = Column(String)
    description = Column(String, nullable=True)