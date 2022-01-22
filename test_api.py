import datetime

import requests

END_POINT = 'https://pda.weather.gov.hk/locspc/android_data/fnd_e.xml'


def get_date_the_day_after_tomorrow(fmt='%Y%m%d'):
    today = datetime.date.today()
    two_day = datetime.timedelta(days=2)
    target_date = today + two_day
    return target_date.strftime(fmt)


def request_9_day_forecast_data():
    return requests.get(END_POINT)


if __name__ == '__main__':
    resp = request_9_day_forecast_data()
    assert resp.status_code == 200

    forecast_detail = resp.json()['forecast_detail']
    data = None
    forecast_date = get_date_the_day_after_tomorrow()
    for detail in forecast_detail:
        if detail['forecast_date'] == forecast_date:
            data = detail
            break

    if data is None:
        raise Exception("Response did not contain the forecast data of the date: %s" % forecast_date)

    relative_humidity = '%s - %s%%' % (data['min_rh'], data['max_rh'])
    print(relative_humidity)
    print_str = "The day after tomorrow's date is %s, and the relative humidity is %s" % (
        forecast_date, relative_humidity)
    print(print_str)
