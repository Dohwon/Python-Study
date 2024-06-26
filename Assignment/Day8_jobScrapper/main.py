from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.remoteok import extract_remoteok_jobs
from file import save_to_file

# print(extract_remoteok_jobs("python"))
# print(extract_wwr_jobs("python"))


app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html", name="dowon")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword is None:
        return redirect("/")
    if keyword not in db:
        remoteok = extract_remoteok_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = remoteok + wwr
        db[keyword] = jobs
    else:
        jobs = db[keyword]
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")
