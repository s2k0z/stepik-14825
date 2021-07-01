def app(environ, start_response):
    query_items = environ['QUERY_STRING'].split('&')
    response_data = [bytes(i + '\n', 'utf-8') for i in query_items]

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(sum(map(len, response_data))))
    ]

    start_response(status, response_headers)

    return response_data
    