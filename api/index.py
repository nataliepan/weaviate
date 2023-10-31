"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_mail import Mail
from server import db, mail
from flask_cors import CORS
from dotenv import load_dotenv
from IPython.display import Image, Audio, Video
import json
import weaviate

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)

    # Connect to Weaviate
    client = weaviate.Client(
        url="http://localhost:8080",
    )

    # @app.route("/api/json")
    # def hello_json():
    #     return jsonify({"message": f"Hello, World! {OPENAI_API_KEY}."})

    # # app.config.from_object("config.Config")

    # # api = Api(app=app)

    # return app

    def json_print(data):
        print(json.dumps(data, indent=2))

    def display_media(item):
        path = item["path"]

        if(item["mediaType"] == "image"):
            display(Image(path))

        elif(item["mediaType"] == "video"):
            display(Video(path))
            
        elif(item["mediaType"] == "audio"):
            display(Audio(path))

    @app.route("/api/text2media")
    def text_to_media(q):
        # Search for media with "dog with stick", "cat playing with mouse", "dog high five", "puppy"
        response = (
            client.query
            .get("Craigslist", "name path desc url mediaType")
            .with_near_text(
                #{"concepts": "dog with stick"}
                {"concepts": "tesla model X with red color"}
                # {"concepts": "dog high five"}
                # {"concepts": "puppy"}
            )
            .with_limit(10)
            .with_additional('distance')
            .do()
        )

        # Print results
        result = response["data"]["Get"]["Craigslist"]

        # json_print(result)

        final_results = []

        for r in result:
            if r['_additional']['distance'] < 0.5:
                final_results.append(r)

        # if final_results:
        #     # Display the first result
        #     display_media(final_results[0])
        # else:
        #     print(f"No results found")

        return final_results
        # json_print(result)

        # Display the first result
        # display_media(result[0])

    # app.config.from_object("config.Config")

    # api = Api(app=app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
