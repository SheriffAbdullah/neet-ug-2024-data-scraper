import asyncio
import aiohttp
import aiofiles
import os
from tqdm import tqdm

url_base = 'https://neetfs.ntaonline.in/NEET_2024_Result/'
save_path = 'PDF_DATA_NEW'  # Replace with your desired save path

start_num = 100000
end_num = 999999

async def download_pdf_from_url(url, save_path, session, pbar):
    filename = url.split('/')[-1]
    save_file = os.path.join(save_path, filename)
    try:
        async with session.get(url) as response:
            if response.status == 200:
                async with aiofiles.open(save_file, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
                        pbar.update(len(chunk))  # Update progress bar based on bytes downloaded
            else:
                print(f"Failed to download {url}. Status code: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Aiohttp exception occurred while downloading {url}: {str(e)}")
    except Exception as e:
        print(f"Exception occurred while downloading {url}: {str(e)}")

async def download_all_pdfs():
    tasks = []
    pbar = tqdm(total=end_num - start_num + 1, miniters=1)
    async with aiohttp.ClientSession() as session:
        for i in range(start_num, end_num + 1):
            url = f"{url_base}{i}.pdf"
            tasks.append(download_pdf_from_url(url, save_path, session, pbar))
        await asyncio.gather(*tasks)

    # Close tqdm manually after the tasks are completed
    pbar.close()

if __name__ == "__main__":
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(download_all_pdfs())
    finally:
        loop.close()
