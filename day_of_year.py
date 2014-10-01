import click
import datetime as dt


def convert_to_datetime(yyyymmdd):
    return dt.datetime.strptime(yyyymmdd, '%Y%m%d')


def calculate_day_of_year(yyyymmdd_dt):
    return yyyymmdd_dt.strftime('%j')


@click.command()
@click.argument('yyyymmdd')
def main(yyyymmdd):
    yyyymmdd_dt = convert_to_datetime(yyyymmdd)
    day_of_year = calculate_day_of_year(yyyymmdd_dt)
    print(day_of_year)


if __name__ == '__main__':
    main()
