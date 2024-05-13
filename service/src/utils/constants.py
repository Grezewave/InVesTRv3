
BASE_PROMPT = '''
to calculate what investiment is the best, we need to calculate the profit of each cycle of records. i have a json that has 3 fields, the field investments shows the cycles of initial applications in some investments founds, the applications shows the cycles of money injestions on founds, and the field returns shows the recorded total value of the found in each date cycle.

To calculate the gross profit in a return record, we need to take the value of the return in the date, and subtract the return in last date of this found, and subtract the applied money between this period

The json:
{
  "investments": [
    {
      "id": "BUTIA TOP CREDITO PRIVADO FIC FIRF",
      "cycles": [
        {
          "value": "565.46",
          "date": "2023-12-17"
        }
      ]
    },
    {
      "id": "BTG PACTUAL HEDGE FUNDO DE INVESTIMENTO RENDA",
      "cycles": [
        {
          "value": "2189.77",
          "date": "2023-12-17"
        }
      ]
    }
  ],
  "applications": [
    {
      "id": "BUTIA TOP CREDITO PRIVADO FIC FIRF",
      "cycles": [
        {
          "value": "1000",
          "date": "2024-02-29"
        },
        {
          "value": "1000",
          "date": "2024-03-12"
        }
      ]
    },
    {
      "id": "BTG PACTUAL HEDGE FUNDO DE INVESTIMENTO RENDA",
      "cycles": [
        {
          "value": "1000",
          "date": "2023-12-29"
        },
        {
          "value": "500",
          "date": "2024-03-12"
        }
      ]
    }
  ],
  "returns": [
    {
      "id": "BUTIA TOP CREDITO PRIVADO FIC FIRF",
      "cycles": [
        {
          "value": "565.96",
          "date": "2023-12-20"
        },
        {
          "value": "567.71",
          "date": "2023-12-29"
        },
        {
          "value": "571.26",
          "date": "2024-01-18"
        },
        {
          "value": "573.98",
          "date": "2024-01-31"
        }
      ]
    },
    {
      "id": "BTG PACTUAL HEDGE FUNDO DE INVESTIMENTO RENDA",
      "cycles": [
        {
          "value": "2193.21",
          "date": "2023-12-20"
        },
        {
          "value": "2202.08",
          "date": "2023-12-29"
        },
        {
          "value": "3219.70",
          "date": "2024-01-18"
        },
        {
          "value": "3236.95",
          "date": "2024-01-31"
        }
      ]
    }
  ]
}


the profit on the cycle of date "2024-01-18" of "BTG PACTUAL HEDGE FUNDO DE INVESTIMENTO RENDA" is equal to 3219.70-2202.08-1000. The profit in percentage is the groos profit divided by (return in last date of this found + applied money between this period) times 100. in this case, is )(3219.70-2202.08-1000)/(2202.08+1000))*100. Use this to calculate what whas requested after.
'''