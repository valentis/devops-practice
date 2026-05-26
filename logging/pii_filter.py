import re

EMAIL_RE = re.compile(r"([\w.+-]{1,3})[\w.+-]*(@[\w-]+\.[\w.-]+)")
PHONE_RE = re.compile(r"(01\d)-?(\d{3,4})-?(\d{4})")

def mask_pii(text: str) -> str:
    text = EMAIL_RE.sub(lambda m: m.group(1) + "***" + m.group(2), text)
    text = PHONE_RE.sub(lambda m: m.group(1) + "-****-" + m.group(3), text)
    return text

class PiiFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.msg = mask_pii(str(record.msg))
        record.args = tuple(mask_pii(str(a)) for a in (record.args or ()))
        return True
