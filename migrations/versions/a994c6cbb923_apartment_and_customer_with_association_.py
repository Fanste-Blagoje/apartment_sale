"""apartment and customer with association models

Revision ID: a994c6cbb923
Revises: b2f2eadf61da
Create Date: 2021-11-01 20:52:06.164840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a994c6cbb923'
down_revision = 'b2f2eadf61da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_apartment',
    sa.Column('lamella', sa.String(length=20), nullable=False),
    sa.Column('square_footage', sa.Integer(), nullable=False),
    sa.Column('floor', sa.Integer(), nullable=False),
    sa.Column('rooms', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.Enum('north', 'south', 'west', 'east', name='apartmentorientationenum'), nullable=False),
    sa.Column('balconies', sa.Integer(), server_default='0', nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('available', 'reserved', 'sold', name='apartmentstatusenum'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_of_creation', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_of_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_customer',
    sa.Column('type', sa.Enum('individual', 'legal_entity', name='customertypeenum'), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('pib_jmbg', sa.String(length=14), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_of_creation', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_of_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('pib_jmbg')
    )
    op.create_table('tbl_customer_apartment',
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('first_visit', sa.Date(), nullable=True),
    sa.Column('status', sa.Enum('potential', 'reserved', 'purchased', name='customerapartmentstatusenum'), nullable=False),
    sa.Column('customer_price', sa.Integer(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('contract_number', sa.Integer(), nullable=True),
    sa.Column('contract_date', sa.Date(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_of_creation', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_of_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.ForeignKeyConstraint(['apartment_id'], ['tbl_apartment.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['tbl_customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_customer_apartment')
    op.drop_table('tbl_customer')
    op.drop_table('tbl_apartment')
    # ### end Alembic commands ###
