from flask import Blueprint, jsonify, request

from link.link import link_blueprint
from link.services.services import LinkService

link_service = LinkService()


@link_blueprint.route("/shorten", methods=["POST"])
def shorten_link():
    """
    This function shortens a long URL and return the result as a JSON response.

    This route accepts a POST request containing a JSON object with a "long_url" field.
    The long URL is passed to the LinkService to generate a shortened URL.

    Returns:
        Response: A JSON response containing the shortened URL information and a status code
    """
    try:
        data = request.json

        # Access the original long URL
        long_url = data.get("long_url")

        if not long_url:
            return jsonify({"error": "Missing or empty 'long_url' field"}), 400

        # Get a Link instance using LinkService
        link = link_service.generate_shorten_url(long_url)

        # Save the link in the database
        link_service.save_link(link)

        # Extract the Link instance information as a JSON
        response = jsonify(link)

        return response, 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
