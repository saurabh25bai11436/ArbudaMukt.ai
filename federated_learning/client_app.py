import flwr as fl
import torch
from task import ArbudaNet, train, test

# Hospital-specific data loading (Placeholder)
# trainloader, testloader = load_hospital_data()

class HospitalClient(fl.client.NumPyClient):
    def __init__(self, net, trainloader, testloader):
        self.net = net
        self.trainloader = trainloader
        self.testloader = testloader
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def get_parameters(self, config):
        return [val.cpu().numpy() for _, val in self.net.state_dict().items()]

    def set_parameters(self, parameters):
        params_dict = zip(self.net.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        self.net.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        """Train model locally and return updated weights."""
        self.set_parameters(parameters)
        train(self.net, self.trainloader, epochs=1, device=self.device)
        return self.get_parameters(config={}), len(self.trainloader.dataset), {}

    def evaluate(self, parameters, config):
        """Evaluate global model on local hospital data."""
        self.set_parameters(parameters)
        loss, accuracy = test(self.net, self.testloader, device=self.device)
        return float(loss), len(self.testloader.dataset), {"accuracy": accuracy}

if __name__ == "__main__":
    # Start the client and connect to the central server
    # fl.client.start_numpy_client(server_address="127.0.0.1:8080", client=HospitalClient(...))
    pass
