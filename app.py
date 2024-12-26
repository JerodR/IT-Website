from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

# Stripe setup
stripe.api_key = 'your-stripe-secret-key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle Google Form submission data here if needed
        name = request.form['name']
        email = request.form['email']
        issue = request.form['issue']
        # Save or process the form data
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/pay', methods=['POST'])
def pay():
    try:
        # Create a payment intent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=5000,  # Amount in cents ($50)
            currency='usd',
            payment_method=request.form['payment_method'],
            confirm=True
        )
        return redirect(url_for('thank_you'))
    except stripe.error.StripeError as e:
        return str(e), 403

if __name__ == '__main__':
    app.run(debug=True)