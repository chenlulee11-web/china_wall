"""initial_schema - create all tables

Revision ID: 460317442c62
Revises:
Create Date: 2026-06-10 00:56:54.011718
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '460317442c62'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('events',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('date_end', sa.Date(), nullable=True),
        sa.Column('date_precision', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('tags', sa.JSON(), nullable=True),
        sa.Column('importance', sa.Integer(), nullable=True),
        sa.Column('wiki_qid', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_events_category'), 'events', ['category'], unique=False)
    op.create_index(op.f('ix_events_date'), 'events', ['date'], unique=False)
    op.create_index(op.f('ix_events_wiki_qid'), 'events', ['wiki_qid'], unique=False)

    op.create_table('event_titles',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=10), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_event_titles_language'), 'event_titles', ['language'], unique=False)

    op.create_table('event_descriptions',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=10), nullable=False),
        sa.Column('summary', sa.Text(), nullable=True),
        sa.Column('content', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_event_descriptions_language'), 'event_descriptions', ['language'], unique=False)

    op.create_table('event_locations',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('lng', sa.Float(), nullable=True),
        sa.Column('country', sa.String(length=10), nullable=True),
        sa.Column('names', sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('event_id'),
    )

    op.create_table('event_sources',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=10), nullable=False),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('title', sa.Text(), nullable=True),
        sa.Column('publisher', sa.String(), nullable=True),
        sa.Column('reliability', sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('event_perspectives',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('country_code', sa.String(length=10), nullable=False),
        sa.Column('language', sa.String(length=10), nullable=False),
        sa.Column('viewpoint', sa.Text(), nullable=False),
        sa.Column('source_url', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_event_perspectives_country_code'), 'event_perspectives', ['country_code'], unique=False)

    op.create_table('event_media',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('media_type', sa.String(length=20), nullable=True),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('caption', sa.JSON(), nullable=True),
        sa.Column('credit', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('event_media')
    op.drop_table('event_perspectives')
    op.drop_table('event_sources')
    op.drop_table('event_locations')
    op.drop_table('event_descriptions')
    op.drop_table('event_titles')
    op.drop_table('events')
