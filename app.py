from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    company_name = ""
    results = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'search':
            company_name = request.form.get('company_name', '').strip()
            if company_name:
                # 🔥 Remove extra spaces in URLs!
                results = {
                    'company': f"https://www.google.com/search?q={company_name}+company",
                    'careers': f"https://www.google.com/search?q={company_name}+careers",
                    'linkedin': f"https://www.google.com/search?q={company_name}+linkedin+company+page"
                }
        # If action is 'refresh' or anything else → leave company_name="" and results=None

    return render_template('index.html', company_name=company_name, results=results)

# Company data: name, domain, linkedin_slug
COMPANIES = [
    {"name": "Google", "domain": "google.com", "linkedin": "google"},
    {"name": "EY", "domain": "ey.com", "linkedin": "ernstandyoung"},
    {"name": "Stripe", "domain": "stripe.com", "linkedin": "stripe"},
    {"name": "TCS", "domain": "tcs.com", "linkedin": "tata-consultancy-services"},
    {"name": "PwC", "domain": "pwc.com", "careers_path": "/gx/en/careers.html", "linkedin": "pwc"},
    {"name": "Meta", "domain": "meta.com", "linkedin": "meta"},
    {"name": "PayPal", "domain": "paypal.com", "linkedin": "paypal"},
    {"name": "Sutherland Global", "domain": "sutherlandglobal.com", "linkedin": "sutherland-global"},
    {"name": "Zocket", "domain": "zocket.digital", "linkedin": "zocketdigital"},
]

    # New routes for the two info pages
@app.route('/company_links')
def company_links():
    return render_template('company_links.html', companies=COMPANIES)

# NEW: ATS Systems List
ATS_SYSTEMS = [
    {"name": "Greenhouse", "domain": "greenhouse.io", "linkedin": "greenhouse-inc-"},
    {"name": "Lever", "domain": "lever.co", "linkedin": "lever-"},
    {"name": "Workday", "domain": "workday.com", "linkedin": "workday"},
    {"name": "BambooHR", "domain": "bamboohr.com", "linkedin": "bamboohr"},
    {"name": "Zoho Recruit", "domain": "zoho.com/recruit", "linkedin": "zohorecruit"},
    {"name": "SmartRecruiters", "domain": "smartrecruiters.com", "linkedin": "smartrecruiters"},
    {"name": "Jobvite", "domain": "jobvite.com", "linkedin": "jobvite"},
    {"name": "Ashby", "domain": "ashbyhq.com", "linkedin": "ashbyhq"},
    {"name": "Workable", "domain": "workable.com", "linkedin": "workable-software"},
]

@app.route('/ats_links')
def ats_links():
    return render_template('ats_links.html' , ats_systems=ATS_SYSTEMS)

if __name__ == '__main__':
    app.run(debug=True)