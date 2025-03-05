from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# אחסון נתוני הזמנות
orders = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # קבלת נתוני ההזמנה מהטופס
        order = {
            "תאריך ושעה": request.form["datetime"],
            "כתובת איסוף": request.form["pickup_address"],
            "כתובת יעד": request.form["dropoff_address"],
            "מספר טיסה": request.form.get("flight_number", ""),
            "מספר נוסעים": request.form["passengers"],
            "מספר מזוודות": request.form["suitcases"],
            "מספר טלפון": request.form["phone"],
            "הערות": request.form.get("notes", "")
        }
        
        # שמירת ההזמנה
        orders.append(order)
        
        return redirect(url_for("index"))

    return render_template("index.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
