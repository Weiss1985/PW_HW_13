"""ad updated at 2

Revision ID: a269c49c0797
Revises: 65870c973d9d
Create Date: 2024-02-20 21:19:50.814161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a269c49c0797'
down_revision: Union[str, None] = '65870c973d9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###
