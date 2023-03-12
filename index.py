from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Phone Number Area Code Lookup</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f2f2f2;
      }
      #content {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        border-radius: 5px;
      }
      h1 {
        color: blue;
        font-family: Arial, Helvetica, sans-serif;
        text-align: center;
        margin-bottom: 30px;
      }
      label {
        font-weight: bold;
      }
      input[type="text"] {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
      }
      button[type="submit"] {
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      button[type="submit"]:hover {
        background-color: #45a049;
      }
      .result {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 20px;
        color: green;
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        border-radius: 5px;
        background-color: #e6f9ff;
      }
    </style>
  </head>
  <body>
    <div id="content">
      <h1>Phone Number Area Code Lookup</h1>
      {% if result %}
        <div class="result">
          The phone number {{ phone_number }} is in the {{ result }} area.
        </div>
      {% endif %}
      <form method="post">
        <label for="phone_number">Enter a phone number:</label>
        <input type="text" id="phone_number" name="phone_number" required autofocus>
        <button type="submit" title="Lookup area code">Submit</button>
      </form>
    </div>
  </body>
</html>
"""

area_codes_to_names = {
    "051": "Southern Region",
    "052": "Southern Region",
    "053": "Central Region",
    "054": "Central Region",
    "055": "Northern Region",
    "02": "Jerusalem and surrounding areas",
    "03": "Tel Aviv and surrounding areas",
    "04": "Haifa and the North",
    "08": "Central Region",
    "09": "Central Region",
    "077": "Central Region",
    "97255": "Central Region",
    "97254": "Central Region",
    "9723": "Tel Aviv and surrounding areas",
    "9722": "Jerusalem and surrounding areas",
    "9751": "Palestinian Authority",
    "1800": "Toll-free number",
    "1700": "Premium-rate number"
}

def extract_numbers(s):
    """Extract all digits from a string."""
    return ''.join(filter(str.isdigit, s))

def get_area_name(phone_number):
    """Return the area name for a given phone number."""
    phone_number = extract_numbers(phone_number)
    if len(phone_number) not in [9, 10, 12]:
        return "Invalid phone number"
    if phone_number.startswith("05") and len(phone_number) == 10:
        area_code = phone_number[0:3]
    elif phone_number.startswith("972"):
        area_code = phone_number[0:5]
        phone_number = "+" + str(phone_number)
    elif phone_number.startswith('0') and len(phone_number) == 9:
        area_code = phone_number[0:2]
    else:
        return "Invalid phone number"

    if area_code not in area_codes_to_names:
        return "Invalid area code"
    else:
        area_name = area_codes_to_names[area_code]
        return area_name


@app.route("/", methods=["GET", "POST"])
def lookup():
    if request.method == "POST":
        phone_number = request.form.get("phone_number")
        area_name = get_area_name(phone_number)
        return render_template_string(template, phone_number=phone_number, result=area_name)
    return render_template_string(template)

if __name__ == "__main__":
    app.run()

