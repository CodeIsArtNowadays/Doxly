from datetime import datetime
from typing import List

from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base
from src.auth.models import UserModel
from src.core.custom_types import RoleLiteral


class MemberModel(Base):
    __tablename__ = 'members'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    username: Mapped[str] = mapped_column()

    workspaces: Mapped[List['WorkspaceMember']] = relationship('WorkspaceMember', back_populates='user')

    messages = relationship('MessageModel', back_populates='author')
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    

class WorkspaceModel(Base):
    __tablename__ = 'workspaces'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(64))

    users: Mapped[List['WorkspaceMember']] = relationship('WorkspaceMember', back_populates='workspace')

    # channel: Mapped['ChannelModel'] = relationship('ChannelModel', back_populates='workspace') 
    # 
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    

class WorkspaceMember(Base):
    __tablename__ = 'workspace_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('members.user_id'), index=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id'), index=True)

    # Owner - crud/add/delete/set_role | Admin - add/delete | Member - chat + add/delete own docs
    role: Mapped[RoleLiteral] = mapped_column(String(32), default='member')

    # relationship
    user: Mapped[UserModel] = relationship(MemberModel, back_populates='workspaces')
    workspace: Mapped["WorkspaceModel"] = relationship(WorkspaceModel, back_populates='users')

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    