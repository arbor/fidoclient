class EdmApiError(Exception):
    pass


class EdmApiServerError(EdmApiError):
    pass


class EdmApiClientError(EdmApiError):
    pass
