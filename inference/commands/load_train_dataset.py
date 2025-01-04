import argparse
import asyncio
import csv

from database.connection import db
from database.models.dataset import dataset


async def _import_train_dataset(items):
    await db.connect()

    while len(items) > 0:
        q = dataset.insert(items[:1000])
        items = items[1000:]
        await db.execute(q)

    await db.disconnect()


def get_age_range(x):
    if 0 <= x < 18:
        return "0-18"

    if 18 <= x < 25:
        return "18-25"

    if 25 <= x < 40:
        return "25-40"

    if 40 <= x < 65:
        return "40-65"

    return "65+"


def main():
    parser = argparse.ArgumentParser(
        description=
        "Loads the training dataset for Mountains vs Beaches preference"
    )
    parser.add_argument(
        '-p',
        '--path',
        help="Path",
        type=str,
        required=True,
        dest='path',
    )

    args = parser.parse_args()
    print(f"Importing mountain vs beaches dataset with path {args.path}")

    items = []

    with open(args.path, 'r', encoding="utf-8") as f:
        input_file = csv.DictReader(f)
        for row in input_file:
            new_item = {}
            for key, value in row.items():
                if key in ["Pets", "Environmental_Concerns", "Preference"]:
                    new_item[key.lower()] = value == "1"
                elif key in [
                    "Income",
                    "Travel_Frequency",
                    "Vacation_Budget",
                    "Proximity_to_Mountains",
                    "Proximity_to_Beaches",
                ]:
                    new_item[key.lower()] = int(value)
                else:
                    new_item[key.lower()] = value

            age = int(new_item.pop("age"))
            new_item["age_range"] = get_age_range(age)

            items.append(new_item)

        print(f"Amount of items to import: {len(items)}")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(_import_train_dataset(items))


if __name__ == '__main__':
    main()
