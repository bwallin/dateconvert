import click
import datetime as dt


@click.command()
@click.argument('yyyymmdd')
def main(yyyymmdd):
    input_date = dt.datetime.strptime(yyyymmdd, '%Y%m%d')
    day_of_year = input_date.strftime('%j')
    print(day_of_year)


if __name__ == '__main__':
    main()
