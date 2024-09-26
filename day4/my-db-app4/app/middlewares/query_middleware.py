from fastapi import Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def advanced_query_middleware(
    db: Session, 
    request: Request, 
    model, 
    default_sort_field="id"
):
    """
    This function processes query parameters to build a dynamic SQLAlchemy query.
    It mimics query features like `select`, `sort`, `page`, `limit`, and filtering.
    """
    
    # Get query parameters from the request
    params = request.query_params

    # Start building a query on the provided model
    query = db.query(model)

    # Handle field selection (`select` parameter)
    select_fields = params.get("select")
    if select_fields:
        select_columns = [getattr(model, field) for field in select_fields.split(",")]
        query = query.with_entities(*select_columns)

    # Handle sorting (`sort` parameter)
    sort_fields = params.get("sort")
    if sort_fields:
        for sort_field in sort_fields.split(","):
            if sort_field.startswith("-"):
                query = query.order_by(text(f"{sort_field[1:]} DESC"))
            else:
                query = query.order_by(text(f"{sort_field} ASC"))
    else:
        query = query.order_by(text(f"{default_sort_field} ASC"))

    # Handle filters (greater than, less than, etc.)
    # Example: ?price[gt]=100&price[lt]=500
    for param in params:
        if param.endswith("[gt]"):
            column_name = param[:-4]  # remove the '[gt]' part
            column = getattr(model, column_name, None)
            if column:
                query = query.filter(column > params[param])
        elif param.endswith("[lt]"):
            column_name = param[:-4]
            column = getattr(model, column_name, None)
            if column:
                query = query.filter(column < params[param])
        elif param.endswith("[gte]"):
            column_name = param[:-5]
            column = getattr(model, column_name, None)
            if column:
                query = query.filter(column >= params[param])
        elif param.endswith("[lte]"):
            column_name = param[:-5]
            column = getattr(model, column_name, None)
            if column:
                query = query.filter(column <= params[param])

    # Handle pagination (`page` and `limit` parameters)
    page = int(params.get("page", 1))
    limit = int(params.get("limit", 10))
    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)


    
    return query

