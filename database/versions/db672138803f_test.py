"""test

Revision ID: db672138803f
Revises: 
Create Date: 2023-11-25 18:09:21.161695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db672138803f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dormitories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('patronymic', sa.String(length=50), nullable=True),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('passwd', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('dormitories')
    # ### end Alembic commands ###
