""" 
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n , that they would like to buy. 
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at https://api.coincap.io/v2/assets/bitcoin, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
Be sure to catch any exceptions - https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.
 """


""" 
 RFC 7159 - https://www.rfc-editor.org/errata_search.php?rfc=7159
 """

import sys
import requests

global dict_response

def exchange_bitcoins():
    try:
        args = sys.argv

        if len(args) == 2:
            purchase =  float(args[1])
            # print(sys.argv[1])
            # print("I'm calling API")
            if isinstance(purchase, float):
                response = requests.get(" https://api.coincap.io/v2/assets/bitcoin")

                """ dict_response = requests.get(" https://api.coincap.io/v2/assets/bitcoin")
                for item in dict_response.json():
                    print(item, ':') """     
                 
                # print(response.status_code)
                if response.status_code == 200:
                    # print(response.json())

                    if isinstance(response, str):
                        print("Response: Text")

                    else:
                        # print("\nResponse:JSON")
                        data = response.json()
                        """ for key, value in data['data'].items():
                            print(f"{key}: {value}") """

                        price = float(data['data']['priceUsd']) / 1000 * purchase
                        format_price = '{:,.4f}'.format(price)
                        print(format_price)
                        # print("Pay: " + f'{price: .2f}' + "USD")
                
                else:
                    raise requests.exceptions.InvalidURL
        else:
            raise IndexError       

    except IndexError:
        print("Missing command-line argument")
        sys.exit()

    except requests.RequestException:
        print("Invalid Request!" + " Error: " +  str(response.status_code))
        pass
    except requests.exceptions.InvalidURL:
        print("Invalid RURL!" + "Error: " +  str(response.status_code))

    except ValueError:
         print("Command-line argument is not a number")
         sys.exit()

def main():
    exchange_bitcoins()

main()
