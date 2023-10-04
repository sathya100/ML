from transformers import pipeline
import csv

# Load the sentiment classification model
pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

# Open the CSV file and iterate through rows
with open(r"D:\py\merix1.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Initialize label counts for the current row
        label_counts = {
            "neutral": 0,
            "approval": 0,
            "love": 0,
            "excitement": 0,
            "curiosity": 0,
            "admiration": 0,
            "caring":0
        }
        total_count=0
        # Iterate through cells in the row
        for cell in row:
            if cell.strip():
                try:
                    sentiment_result = pipe(cell)[0]  # Assuming you only want the top result
                    analyzed_label = sentiment_result["label"]
                    
                    # Increment the corresponding label count for the current row
                    for label in label_counts:
                        if label in analyzed_label:
                            label_counts[label] += 1
                            total_count+=1
                except RuntimeError:
                    pass

        # Print the label counts for the current row
        
        for label, count in label_counts.items():
            print(f"{label.capitalize()}: {count}")
        print(f"Total Count: {total_count}\n")
        print("\n")

