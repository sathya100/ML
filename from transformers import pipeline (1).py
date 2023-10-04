# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions") 
import csv



# Open the CSV file and iterate through rows
with open(r"D:\py\merix1.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        analyzed_row = []

        # Iterate through cells in the row
        for cell in row:
            if cell.strip():
               try : # Check if cell is not empty after stripping whitespace
                sentiment_result = pipe(cell)
                analyzed_row.append(sentiment_result)
               except  RuntimeError:
                 analyzed_row.append(sentiment_result)
            else:
                analyzed_row.append([])  # Empty list for empty cells

        print(analyzed_row)
