# 어제 날짜 생성
today = datetime.today()
yesterday = today - timedelta(days=1)
target_date = yesterday.strftime("%Y%m%d")
yesterday_str = yesterday.strftime("%Y-%m-%d")

# API URL 생성
key = env('API_KEY')
url = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key={key}&targetDt={target_date}"

# XML 데이터를 가져옴
response = requests.get(url)
xml_data = response.content
soup = BeautifulSoup(xml_data, 'xml')

# 영화 정보 추출
movies = soup.find_all('dailyBoxOffice')
movie_list = []
for movie in movies:
    rank = movie.find('rank').text
    movieNm = movie.find('movieNm').text
    openDt = movie.find('openDt').text
    audiAcc = movie.find('audiAcc').text
    movie_list.append({'rank': rank, 'movieNm': movieNm, 'openDt': openDt, 'audiAcc': audiAcc})