import logging
import sys

from fastapi import APIRouter

from crud.redis import RedisCrud

sys.path.append("/user_modules")

# jinja2 template
# from fastapi.templating import Jinja2Templates

# logger
logger = logging.getLogger(__name__)

# router
router = APIRouter(
    tags=["root"]
)


# jinja2 template
# templates = Jinja2Templates(directory="templates")


@router.get("/")
def root():
    return "Hello World!"


@router.get("/redis")
def redis():
    with RedisCrud() as sess:
        sess.set("test", 1)
        return sess.get("test")
