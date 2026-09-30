import os

from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

from routes.ai_routes import ai_bp


# Load environment variables from .env
load_dotenv()


app = Flask(__name__)

# Register AI API routes
app.register_blueprint(ai_bp, url_prefix="/api/ai")


@app.route("/")
def home():
    """
    Open the EduGenie web application.
    """
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def health():
    """
    Check whether the Flask backend is running.
    """
    return jsonify({
        "success": True,
        "message": "EduGenie backend is running",
        "status": "OK"
    })


@app.errorhandler(404)
def page_not_found(error):
    """
    Handle unknown routes.
    """
    return jsonify({
        "success": False,
        "message": "The requested route was not found."
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle server errors.
    """
    return jsonify({
        "success": False,
        "message": "Internal server error."
    }), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))

    print()
    print("=" * 55)
    print("        EduGenie - AI Learning Assistant")
    print("=" * 55)
    print(f"Server running at: http://127.0.0.1:{port}")
    print(f"Health check:      http://127.0.0.1:{port}/api/health")
    print("=" * 55)
    print()

    app.run(
        host="127.0.0.1",
        port=port,
        debug=True
    )