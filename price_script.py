"""Read and clean data for customer pricing to write to new csv."""
import csv


def clean_and_write_prices(in_csv, out_csv):
    """Read dirty pricing csv, clean data, then write to output csv."""
    with open(in_csv, encoding='ISO-8859-1') as in_file, open(out_csv, 'w') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        writer.writerow(['customer', 'pricing_rule', 'price'])

        for row in reader:
            if 'Customers Description' in row[0]:
                curr_cust = row[0].strip()
            writer.writerow([curr_cust, row[0], row[1]])
        print('Output complete')


# def separate_sku(in_csv, out_csv):
#     """Separate sku from product description, then write to output csv."""
#     with open(in_csv) as in_file, open(out_csv, 'w') as out_file:
#         reader = csv.reader(in_file)
#         # writer = csv.writer(out_file)
#         # writer.writerow(['customer', 'sku', 'description', 'price'])


def remove_dashes(in_csv, out_csv):
    """Remove dashes for data cleaning by customer."""
    with open(in_csv) as in_file, open(out_csv, 'w') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        writer.writerow(['customer_id', 'customer', 'product', 'price', 'sku'])

        for row in reader:
            new_index_0 = row[0].split('-', 1)[0]
            new_index_1 = row[0].split('-', 1)[-1]
            writer.writerow([new_index_0, new_index_1, row[1], row[2].strip(), row[3]])
        print('All done')


if __name__ == '__main__':
    # change file names when calling function below and make sure paths are correct
    # clean_and_write_prices('csv/Clean_Pricing_Tab_2.csv', 'csv/out.csv')
    # separate_sku('csv/Clean_Pricing_ALL.csv', 'csv/out.csv')
    remove_dashes('csv/Pricing_by_customer.csv', 'csv/output_no_dashes.csv')
