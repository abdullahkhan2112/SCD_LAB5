# data_structures.py

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # Example data processing logic
        processed_data = [item * 2 for item in self.data]
        return processed_data

if __name__ == "__main__":
    # Example usage of DataProcessor class
    input_data = [1, 2, 3, 4, 5]
    processor = DataProcessor(input_data)
    result = processor.process_data()

    print(f"Input Data: {input_data}")
    print(f"Processed Data: {result}")
