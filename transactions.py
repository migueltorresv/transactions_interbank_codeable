import csv
import argparse

def process_transactions(filename):
    # Initialize balance, highest transaction, and counters for each type
    balance = 0.0
    highest_transaction = {"id": None, "amount": 0.0}
    count = {"Crédito": 0, "Débito": 0}

    # Open the CSV file with UTF-8 encoding
    with open(filename, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            transaction_type = row["tipo"]
            amount = float(row["monto"])
            transaction_id = int(row["id"])

            # Process transactions based on type
            if transaction_type == "Crédito":
                balance += amount
                count["Crédito"] += 1
            elif transaction_type == "Débito":
                balance -= amount
                count["Débito"] += 1

            # Update highest transaction if the current amount is greater
            if amount > highest_transaction["amount"]:
                highest_transaction["amount"] = amount
                highest_transaction["id"] = transaction_id

    # Print report with messages in Spanish
    print("\nReporte de Transacciones")
    print("-" * 50)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {highest_transaction['id']} - {highest_transaction['amount']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {count['Crédito']} Débito: {count['Débito']}")

def main():
    # Create command-line arguments parser with an English description
    parser = argparse.ArgumentParser(description="Procesar un archivo CSV con transacciones bancarias.")
    parser.add_argument("archivo", help="Ruta del archivo CSV de transacciones")
    args = parser.parse_args()

    process_transactions(args.archivo)

if __name__ == "__main__":
    main()
