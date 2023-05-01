from voluptuous import Schema, PREVENT_EXTRA


class Schemas:

    user_schema = Schema(
        {
            "id": int,
            "email": str,
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