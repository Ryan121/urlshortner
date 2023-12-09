import requests
import argparse



def urltester():
    return "test"


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("api_address", type=str, help="The address of the shortening API")
    parser.add_argument("url_to_shorten", type=str, help="Insert the url that requires shortening")
    args = parser.parse_args()
    print('Submitted args: ', args)
    return {"api_address": args.api_address, "url": args.url_to_shorten}

if __name__ == "__main__":
    arguments = get_arguments()
    try:
        response = requests.post(arguments.get('api_address'), json={"url": arguments.get('url')})
        print('Status Code: ', response.status_code, response.json())
    except Exception as e:
        print("log: "+str(e))