import crawler
import export

# main program entry
if __name__ == "__main__":
    print("Crawling started")
    # get the data from crawler
    urlList = crawler.get_url_list()
    rows = crawler.crawl_start(urlList)
    # write the data to csv file
    export.write_to_csv(rows)
    print("Crawling finished")