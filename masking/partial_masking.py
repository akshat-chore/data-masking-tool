def mask_phone(phone: str) -> str:
    phone = str(phone)
    return "*" * (len(phone) - 4) + phone[-4:]

def mask_email(email: str) -> str:
    name, domain = email.split("@")
    if len(name) <= 2:
        return "*" * len(name) + "@" + domain
    return name[0] + "*" * (len(name) - 2) + name[-1] + "@" + domain
