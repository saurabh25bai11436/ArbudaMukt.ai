import flwr as fl
from flwr.server.strategy import FedAvg

def main():
    # FedAvg weights updates based on the local dataset size of each hospital
    strategy = FedAvg(
        fraction_fit=1.0,      # Sample 100% of available clients for training
        fraction_evaluate=0.5, # Sample 50% for evaluation
        min_fit_clients=2,     # Minimum 2 hospitals needed to start
        min_available_clients=2,
    )

    print(" ArbudaMukt Central Server Starting...")
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=5), # 5 global communication rounds
        strategy=strategy,
    )

if __name__ == "__main__":
    main()
