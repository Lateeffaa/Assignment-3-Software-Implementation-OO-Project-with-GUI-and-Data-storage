class ManagementSystem:
    def loadInfo(self):
        try:
            with open("data.pickle", "rb") as f:
                data = pickle.load(f)
                if isinstance(data, tuple) and len(data) == 6:
                    return data
                else:
                    raise ValueError("Invalid data format in pickle file")
        except FileNotFoundError:
            return ([], [], [], [], [], [])
        except ValueError as e:
            print(e)  # Print the error message
            return ([], [], [], [], [], [])

    def saveInfo(employees, events, clients, guests, suppliers, venues):
        with open("data.pickle", "wb") as f:
            pickle.dump((employees, events, clients, guests, suppliers, venues), f)
