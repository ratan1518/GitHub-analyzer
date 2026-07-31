from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <title>GitHub Profile Analyzer</title>
    <style>
      :root { color-scheme: dark; }
      body {
        margin: 0;
        font-family: Inter, Arial, sans-serif;
        background: linear-gradient(135deg, #0f0c29, #1a1040 40%, #24243e);
        color: #f8fafc;
        min-height: 100vh;
        display: grid;
        place-items: center;
      }
      .card {
        max-width: 720px;
        padding: 2rem;
        border-radius: 24px;
        background: rgba(15, 23, 42, 0.8);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255,255,255,0.12);
      }
      h1 { margin-top: 0; font-size: 2rem; }
      p { line-height: 1.6; color: #cbd5e1; }
      code { background: rgba(255,255,255,0.08); padding: 0.2rem 0.4rem; border-radius: 6px; }
    </style>
  </head>
  <body>
    <main class=\"card\">
      <h1>GitHub Profile Analyzer</h1>
      <p>This deployment is now served through Vercel using a lightweight Flask app.</p>
      <p>The project has been adapted for Vercel deployment with a simple web entry point.</p>
      <p>Use the root URL for this landing page, or extend the app with your preferred analysis endpoints.</p>
    </main>
  </body>
</html>
"""


@app.get("/")
def index():
    return HTML_PAGE


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
