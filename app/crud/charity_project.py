from datetime import timedelta
from typing import Optional, List, Dict

from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_project_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id
    
    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict]:
        """Возращает список закрытых проектов отфильрованных по скорости сбора средств"""
        projects = await session.execute(
            select(
            CharityProject.name,
            CharityProject.description,
            # SQLite не поддерживает человеческие вычисления даты в запросе,
            # это единственный вариант который вернет промежуток времени в секундах
            ((func.julianday(CharityProject.close_date) - func.julianday(CharityProject.create_date))* 86400).label('time'),
            ).where(
                CharityProject.fully_invested == true()
            ).order_by('time')
        )
        projects = projects.all()
        # Т.к напрямую после запроса нельзя изменить sqlalchemy.row
        # пришлось собрать новый список уже с в форматом ДД:ЧЧ:ММ:СС
        projects = [
            {
                'name': project.name,
                'description': project.description,
                'time': str(timedelta(seconds=project.time))
            }
            for project in projects
        ]
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
