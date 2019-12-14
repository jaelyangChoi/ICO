from flask import request, redirect, url_for, session, Blueprint

filter_mode_bp = Blueprint('filter_mode', __name__)


@filter_mode_bp.route('/filter_mode', methods=['POST'])
def filter_mode():
    session['mode'] = request.form['mode']
    return redirect(url_for('news'))


def mode_info():
    if session['mode'] == 'off':
        return 'ICO Service 켜기'
    else:
        return 'ICO Service 끄기'
