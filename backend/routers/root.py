import logging
import sys
import httpx
from bs4 import BeautifulSoup
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request

sys.path.append("/user_modules")

# jinja2 template
from fastapi.templating import Jinja2Templates

# logger
logger = logging.getLogger(__name__)

# router
router = APIRouter(
    tags=["root"]
)

# jinja2 template
templates = Jinja2Templates(directory="templates")


@router.get("/{user_id}", response_class=HTMLResponse)
def root(request: Request, user_id: int):
    # request
    response = httpx.post(
        "http://scp-jp.wikidot.com/ajax-module-connector.php",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "wikidot_token7=pseudotoken;",
        },
        data={
            "user_id": user_id,
            "moduleName": "users/UserInfoWinModule",
            "wikidot_token7": "pseudotoken",
        }
    )

    date_joined = None

    if response.status_code == httpx.codes.OK:
        data = response.json()
        if "body" in data:
            data = data["body"]
            if "サイトへの登録日" in data:
                data_parsed = BeautifulSoup(data, "html.parser")
                for tr in data_parsed.find_all("tr"):
                    for td in tr.find_all("td"):
                        if "サイトへの登録日" in td.text:
                            odate_elem = tr.find("span", class_="odate")
                            if odate_elem:
                                for c in odate_elem["class"]:
                                    if c.startswith("time_"):
                                        date_joined = int(c.split("_")[1])
                                        break
                            break

    days_from_joined = None
    if date_joined is not None:
        days_from_joined = (datetime.now() - datetime.fromtimestamp(date_joined)).days

    return templates.TemplateResponse("response.html", {"request": request, "days": days_from_joined})
