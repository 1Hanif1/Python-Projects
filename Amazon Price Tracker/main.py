import os
from bs4 import BeautifulSoup
from smtplib import SMTP
from requests import get
from dotenv import load_dotenv
load_dotenv(dotenv_path="./envvar.env")

BOT_EMAIL = os.environ['BOT_EMAIL']
BOT_PASSWORD = os.environ['BOT_PASSWORD']
TO_EMAIL = os.environ['TO_EMAIL']

# Product URL
URL = "https://www.amazon.in/Noise-ColorFit-Bezel-Less-TruView-Gunmetal/dp/B093HCLPJ5/ref=sr_1_2_sspa?adgrpid=58530665003&ext_vrnc=hi&gclid=CjwKCAiAsNKQBhAPEiwAB-I5zV7nWT6QTL1UF7AXwBsIENJrKsJAh5iXOcd81eezdpl32_qAuyRWLRoCdpEQAvD_BwE&hvadid=398060159515&hvdev=c&hvlocphy=9062263&hvnetw=g&hvqmt=e&hvrand=4637571641330317015&hvtargid=kwd-780606477041&hydadcr=24542_1971411&keywords=noise+colorfit+pro+3&qid=1645542254&smid=A14CZOWI0VEHLG&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSFhBREdaSEQ3WDdLJmVuY3J5cHRlZElkPUEwNDE2MDgyMkZUWUJUSEpZMzNMViZlbmNyeXB0ZWRBZElkPUEwNDgxMzM4TlY0UkJMVUVPQVE2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

# Product's desired price
desired_price = 2500

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = get(url=URL, headers=header)
response.raise_for_status()
html = response.text

Soup = BeautifulSoup(html, "html.parser")
price_string = Soup.select_one(
    selector="span.apexPriceToPay span")\
    .getText()\
    .split(".")[0]

price = int(price_string
            .replace("₹", "")
            .replace(",", "")
            )


def send_email(message: str):
    with SMTP(host="smtp.gmail.com") as email:
        email.starttls()
        email.login(user=BOT_EMAIL, password=BOT_PASSWORD)
        email.sendmail(from_addr=BOT_EMAIL,
                       to_addrs=TO_EMAIL, msg=message)


if price < desired_price:
    message = f"Subject:Product below desired price :)\n\nThe product you were looking out for is below {desired_price}.\n URL: {URL}"
    send_email(message)
