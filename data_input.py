from datetime import datetime

STATUSES = {"open", "interview", "rejected", "offer"}
DATE_FORMAT = "%d-%m-%Y"


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)

    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)


def get_company():
    company = input("Enter company name: ")
    if company != "":
        return company
    print("Invalid company name.")
    return get_company()


def get_position():
    position = input("Enter position title: ")
    if position != "":
        return position
    print("Invalid position title.")
    return get_position()


def get_location():
    location = input("Enter company's location: ")
    if location != "":
        return location
    print("Invalid location.")
    return get_location()


def get_status():
    status = input("Enter job status: ")
    if status.lower() in STATUSES:
        return status
    print("Invalid status. Must be one of: [open, interview, rejected, offer]")
    return get_status()


def get_description():
    description = input("Enter job description (optional): ")
    return description
