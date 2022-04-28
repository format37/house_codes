from aiohttp import web
import os
import pandas as pd
import re


async def call_test(request):
	content = "get ok"
	return web.Response(text=content,content_type="text/html")


def get_code(addr):
    address_street = (re.findall(r'a.*b', addr)[0][1:][:-1]).lower()
    address_house = re.findall(r'c.*d', addr)[0][1:][:-1]
    address_entrance = re.findall(r'e.*f', addr)[0][1:][:-1]
    mask = \
        (1 if address_street=='' else (df.street_low.str.contains(address_street))) & \
        (1 if address_house=='' else (df.address_house==address_house)) & \
        (1 if address_entrance=='' else (df.address_entrance==address_entrance))
    result = sorted(set(df[mask].address_doorcode))
    return len(result) if address_street=='' or address_house=='' or address_entrance=='' else result 


async def call_code(request):	
	addr = request.rel_url.query['addr']
	print(addr)
	content = '<html><body>'
	if addr=='abcdef':
		content += '0'
	else:
		try:
			codes = str(get_code(addr))
			codes = codes.replace("', '","<br>")
			codes = codes.replace("['","")
			codes = codes.replace("']","")
			content += codes
		except Exception as e:
			print(e)
	content += '</body></html>'
	return web.Response(text=content,content_type="text/html")


def main():

	app = web.Application(client_max_size=1024**3)
	app.router.add_route('GET', '/test', call_test)
	app.router.add_route('GET', '/code', call_code)

	web.run_app(
		app,
		port=os.environ.get('PORT', ''),
	)


df = pd.read_csv('data.csv')


if __name__ == "__main__":
    main()
