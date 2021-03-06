from marshmallow import Schema, fields, post_load


class Authentication():
    """Authentication contains an HTTP Header name along with its value.

    Attributes:
        http_header (str): The HTTP Header name.
        http_header_value (str): The associated HTTP Header value.
    """

    def __init__(self, http_header: str = None, http_header_value: str = None):
        self.http_header = http_header
        self.http_header_value = http_header_value


class AuthenticationSchema(Schema):
    class Meta:
        ordered = True

    http_header = fields.Str(
        required=True, dump_to='httpHeader', load_from='httpHeader')
    http_header_value = fields.Str(
        required=True, dump_to='httpHeaderValue', load_from='httpHeaderValue')

    @post_load
    def to_model(self, data):
        return Authentication(**data)
