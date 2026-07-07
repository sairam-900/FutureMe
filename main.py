from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os
import random

# Load .env
load_dotenv()

app = Flask(__name__)

# Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        name = data["name"]
        age = data["age"]
        education = data["education"]
        short_term = data["short_term"]
        long_term = data["long_term"]
        future_goal = data["future_goal"]

        prompt = f"""
You are an AI Career Predictor.

User Details

Name : {name}
Age : {age}
Education : {education}

Short Term Goal :
{short_term}

Long Term Goal :
{long_term}

Future Goal :
{future_goal}

Give the response in this format exactly.

Prediction:
(Write around 180-250 words.)

Year1:
(one sentence)

Year5:
(one sentence)

Year10:
(one sentence)

Success:
(one integer between 75 and 99)
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        prediction = ""
        year1 = ""
        year5 = ""
        year10 = ""
        success = random.randint(80, 97)

        lines = text.split("\n")

        mode = ""

        for line in lines:

            line = line.strip()

            if line.startswith("Prediction"):
                mode = "prediction"
                continue

            elif line.startswith("Year1"):
                mode = "year1"
                continue

            elif line.startswith("Year5"):
                mode = "year5"
                continue

            elif line.startswith("Year10"):
                mode = "year10"
                continue

            elif line.startswith("Success"):
                try:
                    success = int(line.split(":")[1].strip())
                except:
                    pass
                mode = ""
                continue

            if mode == "prediction":
                prediction += line + "\n"

            elif mode == "year1":
                year1 += line + " "

            elif mode == "year5":
                year5 += line + " "

            elif mode == "year10":
                year10 += line + " "

        return jsonify({
            "name": name,
            "age": age,
            "education": education,
            "prediction": prediction.strip(),
            "timeline_1y": year1.strip(),
            "timeline_5y": year5.strip(),
            "timeline_10y": year10.strip(),
            "success_rate": success
        })

    except Exception as e:

        return jsonify({

            "name": data.get("name", ""),
            "age": data.get("age", ""),
            "education": data.get("education", ""),
            "prediction": "Unable to generate prediction. " + str(e),
            "timeline_1y": "Keep learning consistently and build practical skills.",
            "timeline_5y": "Become experienced in your chosen career path.",
            "timeline_10y": "Achieve leadership and financial stability.",
            "success_rate": random.randint(80,95)

        })


if __name__ == "__main__":
    app.run(debug=True)