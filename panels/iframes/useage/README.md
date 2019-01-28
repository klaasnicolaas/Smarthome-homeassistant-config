# Grafana Useage Dashboard

![Dashboard][dashboard]

Since some of you would like to know how you can just build a usage dashboard like what I have. I decided to share my SQL code with everyone so that it might be easier for everyone to build the same dashboard.

To make this dashboard I used the [InfluxDB][influxdb-addon] and [Grafana][grafana-addon] plugin from the [hass.io][hassio] add-on store.

As you can see on the photo, I have divided my dashboard into sections and given a number, this way you can easily find below which code was used for which part.

**Pay attention!** The code only ensures that the right data comes into your chart, the design is something you still have to set yourself.

Also pay attention to the 2 price variables in the code called:

- ***POWER_PRICE***
- ***GAS_PRICE***

This must be replaced with a value that you pay for your gas and energy bill, in order to generate the right calculations for you.

## Section 1, 3 & 11

```sql
SELECT sum("value")  / 10000 FROM "m3" WHERE ("entity_id" = 'gas_consumption') AND $timeFilter GROUP BY time(1d) fill(null)
```

## Section 2

```sql
SELECT sum("value")  / 1000 FROM "kW" WHERE ("entity_id" = 'power_consumption') AND $timeFilter GROUP BY time(1h) fill(none)
```

## Section 4 & 11

```sql
SELECT sum("value")  * GAS_PRICE / 10000 FROM "m3" WHERE ("entity_id" = 'gas_consumption') AND $timeFilter GROUP BY time(1d) fill(null)
```

## Section 5

```sql
SELECT sum("value")  * GAS_PRICE / 10000 FROM "m3" WHERE ("entity_id" = 'gas_consumption') AND $timeFilter GROUP BY time(30d) fill(null)
```

## Section 6

```sql
SELECT sum("value")  * GAS_PRICE / 10000 FROM "m3" WHERE ("entity_id" = 'gas_consumption') AND $timeFilter GROUP BY time(7d) fill(null)
```

## Section 7 & 12

```sql
SELECT sum("value")  / 1000 FROM "kW" WHERE ("entity_id" = 'power_consumption') AND $timeFilter GROUP BY time(1d) fill(null)
```

## Section 8 & 12

```sql
SELECT sum("value")  * POWER_PRICE / 1000 FROM "kW" WHERE ("entity_id" = 'power_consumption') AND $timeFilter GROUP BY time(1d) fill(null)
```

## Section 9

```sql
SELECT sum("value")  * POWER_PRICE / 1000 FROM "kW" WHERE ("entity_id" = 'power_consumption') AND $timeFilter GROUP BY time(30d) fill(null)
```

## Section 10

```sql
SELECT sum("value")  * POWER_PRICE / 1000 FROM "kW" WHERE ("entity_id" = 'power_consumption') AND $timeFilter GROUP BY time(7d) fill(null)
```

[dashboard]: /extras/img/useage-dashboard.png
[influxdb-addon]: https://github.com/hassio-addons/addon-influxdb
[grafana-addon]: https://github.com/hassio-addons/addon-grafana
[hassio]: https://www.home-assistant.io/hassio/
