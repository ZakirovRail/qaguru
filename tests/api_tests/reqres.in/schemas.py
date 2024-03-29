from voluptuous import Schema, PREVENT_EXTRA, Length, All


def is_email_true(email):
    if "@" in email and "." in email:
        return True
    raise ValueError(f"It's not an email : {email}")


class Schemas:

    user_schema = Schema(
        {
            "id": int,
            "email": All(str, is_email_true),
            "first_name": str,
            "last_name": str,
            "avatar": str,
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    schema_list_users = Schema(
        {
            "page": int,
            "per_page": int,
            "total": int,
            "total_pages": int,
            # "data": All([user_schema], Length(min=1)),
            "data": [user_schema],
            "support": {
                "url": str,
                "text": str
            }
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    list_users_schema = Schema(
        {
            "page": int,
            "per_page": int,
            "total": int,
            "total_pages": int,
            "data": [user_schema],
            "support": {
                "url": str,
                "text": str
            }
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    schema_single_user = Schema(
        {
            "data": {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            "support": {
                "url": str,
                "text": str
            }
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    schema_create_new_user = Schema(
        {
            "name": str,
            "job": str,
            "id": str,
            "createdAt": str,
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    schema_update_user = Schema(
        {
            "name": str,
            "job": str,
            "updatedAt": str,
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    list_users_schema = Schema(
        {
            "page": int,
            "per_page": int,
            "total": int,
            "total_pages": int,
            "data": [user_schema],
            "support": {
                "url": str,
                "text": str
            }
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    new_user_successful_register = Schema(
        {
            "id": int,
            "token": str,
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    new_user_unsuccessful_register = Schema(
        {
            "error": str
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    user_login_successful = Schema(
        {
            "token": str
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    user_login_unsuccessful = Schema(
        {
            "token": str
        },
        extra=PREVENT_EXTRA,
        required=True
    )
