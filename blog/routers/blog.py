from typing import List

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_blog_list(db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}')
def delete_blog(id: int, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog_detail(id: int, response: Response, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.detail(id, db)
