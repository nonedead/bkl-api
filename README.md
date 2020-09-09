# Black Krab Logistics API

API for the [Black Krab Logistics](https://gonekrabbing.supply/logistics/) Freight Services provided in [EVE Online](https://www.eveonline.com/)

## API Endpoints

### List All Serviced Systems

Definition: `GET /api/systems`

Response:

-   `200 OK` on success

```json
{
    "message": "success",
    "data": 
    [
        {
            "system": "R10-GN",
            "stations": 
            [
            	"R10-GN – B E A N S T A R",
            ]
        },
        {
            "system": "PNQY-Y",
            "stations": 
            [
                "PNQY-Y – PPG Paints Arena"
            ]
        }
    ]
}
```

### Get system service details

Definition: `GET api/system/<system_name>`
Arguments:

-   `<system-name>` system name as a string. names preferred as is from EVE but lowercase works as well.

Response:

-   `200 OK` on success
-   `404 Not Found` if system is not serviced

Success(`200`):

```json
{
    "message": "success",
    "data": 
    {
        "system_name": "PNQY-Y",
        "stations_available": 
        [
            "PNQY-Y – PPG Paints Arena"
        ],
        
    }
}
```

_more data can be added later such as rates to and from etc._

Not Found(`404`):

```json
{
    "message": "system not serviced",
    "data": {}
}
```

### Get collateral and volume restrictions

Definition: `GET /api/restrictions`

Response:

-   `200 OK` on success

Success(`200`)

```json
{
    "message":"success",
    "data": 
    {
    	"volume_limit": 345000,
        "collateral_limit": 15000000000000
    }
}
```

### Calculate price for contract

Definition: `GET /api/calculate`

Arguments:

-   `origin_system` Origin system name.
-   `destination_system` Destination System Name
-   `volume` Volume of contract as `int`
-   `collateral` Collateral Amount `int`

Response:

-   `200 OK` on success
-   `412 Precondition Failed` if volume or collateral is not accepted
-   `406 Not Acceptable` if system is not serviced

Success(`200`):

```json
{
    "message": "success",
    "data": 
    {
    	"corp": "Black Krab Logistics",
        "reward": 1798587,
        "collateral": 432432,
        "volume": 3429,
        "days_to_expire": 7,
        "days_to_accept": 7,
        "price_per_m3": 800,
        "is_special_price": "yes",
        "origin_system": "I-CUVX",
        "destination_system": "Jita",
    }
}
```

Precondition Failed(`412`): Collateral Over Limit

```json
{
    "message": "collateral not acceptable",
    "data": 
    {
    	"collateral": "limit: 15000000000000",
        "volume": "ok",
    }
}
```

Precondition Failed(`412`): Volume Over Limit

```json
{
    "message": "volume not acceptable",
    "data": 
    {
    	"collateral": "ok",
        "volume": "limit: 345000",
    }
}
```

Precondition Failed(`412`): Both Over Limit

```json
{
    "message": "both not acceptable",
    "data": 
    {
    	"collateral": "limit: 15000000000000",
        "volume": "limit: 345000",
    }
}
```

Not Acceptable(`406`):

```json
{
    "message": "system not serviced",
    "data": 
    {
    	"origin": "Jita",
        "origin_serviced": "yes",
        "destination": "PNQY-Y",
        "destination_services": "no"
    }
}
```
