import click
import datetime as dt


def convert_to_datetime(yyyymmdd):
    return dt.datetime.strptime(yyyymmdd, '%Y%m%d')


def calculate_day_of_year(yyyymmdd_dt):
    return yyyymmdd_dt.strftime('%j')


@click.command()
@click.argument('yyyymmdd')
@click.option('--print_result', '-p', is_flag=True)
def main(yyyymmdd, print_result):
    yyyymmdd_dt = convert_to_datetime(yyyymmdd)
    day_of_year = calculate_day_of_year(yyyymmdd_dt)
    if print_result:
        print(day_of_year)
    return day_of_year


if __name__ == '__main__':
    main()
