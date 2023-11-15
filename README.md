# M-Pesa Fee Calculator

Find out M-Pesa charges with this form.

## Features

- Calculate M-Pesa fees for various transaction types:
- Sending to Registered M-Pesa Users
- Withdrawing from an Agent
- Sending to Unregistered Users
- Sending to Other Networks
- ATM Withdrawal

## How to Use

1. Navigate to the application URL.
2. Select the transaction type and enter the amount.
3. Click "Calculate" to get the M-Pesa fee for your transaction.

You can see and use the application at [https://nasonga.com/mpesa-charges/](https://nasonga.com/mpesa-charges/)
.

## Development

Developers are welcome to contribute. Here's how you can set up a development environment:

1. Clone the repository.
2. Set up a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
3. pip install -r requirements.txt
4. Set local .env
5. python manage.py makemigrations and python manage.py migrate
6. python manage.py runserver
7. Access at http://127.0.0.1:8000/calculate-fee/

## Future Improvements

- Connect Daraja API.
- Improve the user interface.
- Enable Transactions.

## License

This project is licensed under the GNU General Public License (GPL) version 3.