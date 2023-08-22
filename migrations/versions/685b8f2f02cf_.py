"""empty message

Revision ID: 685b8f2f02cf
Revises: 
Create Date: 2023-08-21 15:37:58.859303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '685b8f2f02cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mega_sena',
    sa.Column('concurso', sa.Integer(), nullable=False),
    sa.Column('data_do_sorteio', sa.String(), nullable=True),
    sa.Column('bola1', sa.Integer(), nullable=True),
    sa.Column('bola2', sa.Integer(), nullable=True),
    sa.Column('bola3', sa.Integer(), nullable=True),
    sa.Column('bola4', sa.Integer(), nullable=True),
    sa.Column('bola5', sa.Integer(), nullable=True),
    sa.Column('bola6', sa.Integer(), nullable=True),
    sa.Column('ganhadores_6_acertos', sa.Integer(), nullable=True),
    sa.Column('cidade_uf', sa.String(), nullable=True),
    sa.Column('rateio_6_acertos', sa.String(), nullable=True),
    sa.Column('ganhadores_5_acertos', sa.Integer(), nullable=True),
    sa.Column('rateio_5_acertos', sa.String(), nullable=True),
    sa.Column('ganhadores_4_acertos', sa.Integer(), nullable=True),
    sa.Column('rateio_4_acertos', sa.String(), nullable=True),
    sa.Column('acumulado_6_acertos', sa.String(), nullable=True),
    sa.Column('arrecadacao_total', sa.String(), nullable=True),
    sa.Column('estimativa_premio', sa.String(), nullable=True),
    sa.Column('acumulado_sorteio_especial_mega_da_virada', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('concurso')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mega_sena')
    # ### end Alembic commands ###