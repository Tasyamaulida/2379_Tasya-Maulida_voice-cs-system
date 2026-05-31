import csv
import os
import time

from app.llm import get_chatbot_response

input_file = "results_sst.csv"
output_file = "results_llm.csv"

processed = set()

if os.path.exists(output_file):

    with open(
        output_file,
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.reader(f)

        next(reader, None)

        for row in reader:

            if row:

                processed.add(row[0])

mode = "a" if os.path.exists(output_file) else "w"

with open(
    output_file,
    mode,
    newline="",
    encoding="utf-8"
) as outfile:

    writer = csv.writer(outfile)

    if mode == "w":

        writer.writerow([
            "transcript",
            "response"
        ])

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as infile:

        reader = csv.reader(infile)

        next(reader, None)

        for row in reader:

            if not row:
                continue

            transcript = row[-1]

            if transcript in processed:
                continue

            response = get_chatbot_response(
                transcript
            )

            if response == "ERROR_QUOTA":

                print("\nSEMUA API KEY HABIS")
                print("LANJUTKAN BESOK")

                break

            print("=" * 50)
            print("Transcript:")
            print(transcript)

            print("\nResponse:")
            print(response)

            writer.writerow([
                transcript,
                response
            ])

            outfile.flush()

            time.sleep(3)

print("\nSELESAI")