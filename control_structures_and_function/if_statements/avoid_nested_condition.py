"""
- When using conditions, when there are too many conditions to check before doing something, check each condition one by one and return an error immediately.
- Do not nest the condition to avoid readers not understanding your code
"""

# Harmful solution
# def process_login_form(request):
#     if request.form.get("username") and request.form.get("password"):
#         if captcha_displayed(request) and captcha_passed(request):
#             if authenticate_user(request.form["username"], request.form["password"]):
#                 current_user.login()
#                 return redirect(HOME_PAGE)
#             else:
#                 return "Unable to authenticate with provided username and password", 403
#         else:
#             if captcha_displayed(requet):
#                 return "Captcha entry failed. Please resubmit", 403
#     else:
#         return "Missing username or password. Both are required", 400


# Idiomatic solution
def process_login_form(request):
    """
    Process login form submission and handle authentication.

    Args:
        request (dict): HTTP request containing form data.

    Returns:
        tuple: Response message (str), HTTP status code (int).
    """

    if "username" not in request.form:
        return "Please enter a value for username", 400

    if "password" not in request.form:
        return "Please enter a value for password", 400

    if captcha_displayed(request) and not captcha_passed(request):
        return "Captcha entry failed. Please resubmit", 403

    if not authenticate_user(request.form["username"], request.form["password"]):
        return "Unable to authenticate with provided username and password", 403

    current_user.login()
    return redirect(HOME_PAGE)
