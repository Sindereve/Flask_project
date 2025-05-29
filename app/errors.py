# app/errors.py
from flask import render_template, request, jsonify


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']


def register_error_handlers(app, bp):
    # Глобальные обработчики для всего приложения
    @app.errorhandler(404)
    def handle_app_404(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def handle_app_500(error):
        return render_template('500.html'), 500

    # Обработчики ошибок для API
    @bp.errorhandler(404)
    def handle_api_404(error):
        if wants_json_response():
            return jsonify({'error': 'Not Found'}), 404
        return render_template('errors/404.html'), 404

    @bp.errorhandler(500)
    def handle_api_500(error):
        from app import db
        db.session.rollback()
        if wants_json_response():
            return jsonify({'error': 'Internal Server Error'}), 500
        return render_template('errors/500.html'), 500