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
      * { box-sizing: border-box; }
      body {
        margin: 0;
        font-family: Inter, Arial, sans-serif;
        background: linear-gradient(135deg, #0f0c29, #1a1040 40%, #24243e);
        color: #f8fafc;
        min-height: 100vh;
      }
      .wrap {
        max-width: 1200px;
        margin: 0 auto;
        padding: 3rem 1.25rem 4rem;
      }
      .hero {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 2rem;
        align-items: center;
        padding: 2rem;
        border-radius: 28px;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 25px 60px rgba(0,0,0,0.25);
      }
      h1 { font-size: clamp(2rem, 4vw, 3.2rem); margin: 0 0 0.75rem; }
      .lead { font-size: 1.05rem; line-height: 1.7; color: #cbd5e1; margin-bottom: 1.25rem; }
      .pill {
        display: inline-block;
        padding: 0.45rem 0.7rem;
        border-radius: 999px;
        background: rgba(108, 99, 255, 0.25);
        border: 1px solid rgba(108, 99, 255, 0.4);
        color: #e9d5ff;
        font-weight: 700;
        margin-bottom: 1rem;
      }
      .panel {
        padding: 1.2rem;
        border-radius: 20px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
      }
      .panel h3 { margin-top: 0; }
      form { display: flex; gap: 0.75rem; margin-top: 0.9rem; flex-wrap: wrap; }
      input {
        flex: 1;
        min-width: 220px;
        padding: 0.9rem 1rem;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255,255,255,0.08);
        color: white;
        font-size: 1rem;
      }
      button {
        background: linear-gradient(135deg, #6C63FF, #EC4899);
        color: white;
        border: none;
        padding: 0.92rem 1.15rem;
        border-radius: 12px;
        font-weight: 700;
        cursor: pointer;
      }
      .stats {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 1.5rem;
      }
      .stat {
        padding: 1rem;
        border-radius: 16px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
      }
      .stat strong { display: block; font-size: 1.2rem; margin-bottom: 0.25rem; }
      .features {
        margin-top: 1.5rem;
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
      }
      .feature {
        padding: 1rem;
        border-radius: 18px;
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(255,255,255,0.08);
      }
      .feature h4 { margin-top: 0; margin-bottom: 0.4rem; }
      .feature p { margin: 0; color: #cbd5e1; line-height: 1.6; }
      @media (max-width: 900px) {
        .hero { grid-template-columns: 1fr; }
        .stats, .features { grid-template-columns: 1fr; }
      }
    </style>
  </head>
  <body>
    <main class=\"wrap\">
      <section class=\"hero\">
        <div>
          <div class=\"pill\">🔭 GitHub Profile Analyzer</div>
          <h1>Understand a developer’s coding style, career story, and team fit.</h1>
          <p class=\"lead\">This project turns public GitHub activity into actionable insights such as personality signals, language patterns, commit quality, repo health, and role recommendations.</p>
          <form>
            <input type=\"text\" placeholder=\"Enter a GitHub username\" />
            <button type=\"button\">Analyze Profile</button>
          </form>
        </div>
        <div class=\"panel\">
          <h3>What this analyzer reveals</h3>
          <ul>
            <li>Commit behavior and coding personality</li>
            <li>Language and technology focus</li>
            <li>Repo health and collaboration signals</li>
            <li>Career evolution and job-role fit</li>
          </ul>
        </div>
      </section>

      <section class=\"stats\">
        <div class=\"stat\"><strong>AI-driven</strong>Insights powered by repository analysis</div>
        <div class=\"stat\"><strong>Visual reports</strong>Charts, timelines, and profile summaries</div>
        <div class=\"stat\"><strong>Ready for deployment</strong>Hosted through Vercel with a Flask backend</div>
      </section>

      <section class=\"features\">
        <div class=\"feature\"><h4>Personality Signals</h4><p>Discover patterns in commit timing, coding habits, and project themes.</p></div>
        <div class=\"feature\"><h4>Repo Health</h4><p>Review maintenance quality, activity balance, and sustainability signals.</p></div>
        <div class=\"feature\"><h4>Career Mapping</h4><p>Trace language evolution, focus areas, and likely adjacent roles.</p></div>
      </section>
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
