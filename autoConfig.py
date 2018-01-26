#encoding=utf-8
## debug/test purpose
demotextfilename = u'csvtest.csv'
autocommentsfilename = u"D:/Documents/Alero/sunyang/东风/AUTO/auto2_2/auto2_2.csv"

## project information
DEV_PROJECT_ROOT = 'D:/pythonprojects/ACSpiders'
RUNTIME_PROJECT_ROOT = '/opt/pythonvirt/autocool/ACSpiders'
PROJECT_ROOT = '%s'%DEV_PROJECT_ROOT

## mongodb configuration
dbhost = u'localhost'
dbport = 27017
dbdatabase = u'csp'
username = ''#u'autocool' #''#
password = ''#u'mongoac2017' #''#
db_contents_coll = u'contents'
db_users_coll = u'users'
db_spiders_coll = u'spiders'

## image file location
IMAGE_HOUSE_LOCAL_DIR = '/opt/image/house/image2/' #'D:/Temp/'#
IMAGE_HOUSE_LOCAL_TEMP_DIR = '/opt/image/house/tmp/' #'D:/Temp/'#
IMAGE_LOCAL_DIR = '/opt/image/car/image/' #'D:/Temp/'#
IMAGE_LOCAL_TEMP_DIR = '/opt/image/car/tmp/' #'D:/Temp/'#

IMAGE_HOUSE_URL_PREFIX = 'http://www.kequantech.com/image2/'
IMAGE_URL_PREFIX = 'http://www.kequantech.com/image/'

DEFAULT_THUMBNAIL_BASEDIR = '/opt/image/car/thumbnail/' # 'D:/Temp/'
DEFAULT_THUMBNAIL_PREFIX = 'http://www.kequantech.com/image/thumbnail/'
DEFAULT_THUMBNAIL_URL = 'http://www.kequantech.com/image/thumbnail/808954-89494a1349eb8af98677bd98c933d8da.jpeg'

IMAGE_SJS_URL = 'http://static.shenjianshou.cn/image/'

## nlp dictionaries
## jieba dictionaries usage
AUTODICTS = ['%s/dicts/autodicts/autobrands.txt'%PROJECT_ROOT, '%s/dicts/autodicts/autofactories.txt'%PROJECT_ROOT,
             '%s/dicts/autodicts/automodels.txt'%PROJECT_ROOT ,'%s/dicts/autodicts/autoparts.txt'%PROJECT_ROOT]
## jieba stopword properties
STOPWORDS = '%s/dicts/stopwords/stopwords.txt'%PROJECT_ROOT
# 结巴分词后的停用词性 [标点符号、连词、助词、副词、介词、时语素、‘的’、数词、方位词、代词]
STOPWORD_FLAGS = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
STOPWORD_NOUN_FLAGS = ['n', 'nz', 'nr', 'ns']


## generated clean text (no html tags) directory
CLEAN_CONTENT_DIRECTORY = '/opt/text/contents/' #'D:/pythonprojects/ACSpiders/dicts/text'
IDF_FILE = '/opt/text/idf/autoidf.txt' #'D:/pythonprojects/ACSpiders/dicts/idfgen/autoidf.txt'
IGNORED_CHARS = {u'', u' ', u'', u'。', u'：', u'，', u'）', u'（', u'！', u'?', u'”', u'“',
                 u'《',u'》',u'•',u'【',u'】',u'...',u'#',u'：',u'|',u'+',u'-',u'*',u'/', u'@'
                 ,u'▼ '}

## spiders and data sources -- from shenjianshou, having their own collections
##家装
#houzz
SJS_HOUZZ_SOURCE = u'家装-houzz.com'
SJS_HOUZZ_SPIDER = u'837398'    # 爬虫ID
SJS_HOUZZ_COLL = u'contents-837398'
#dwellingdecor
SJS_DWELLINGDECOR_SOURCE = u'家装-dwellingdecor.com'
SJS_DWELLINGDECOR_SPIDER = u'838398'    # 爬虫ID
SJS_DWELLINGDECOR_COLL = u'contents-838398'
#homedesigning
SJS_HOMEDESIGNING_SOURCE = u'家装-home-designing.com'
SJS_HOMEDESIGNING_SPIDER = u'838013'    # 爬虫ID
SJS_HOMEDESIGNING_COLL = u'contents-838013'
#homedit
SJS_HOMEDIT_SOURCE = u'家装-homedit.com'
SJS_HOMEDIT_SPIDER = u'838472'    # 爬虫ID
SJS_HOMEDIT_COLL = u'contents-838472'
#decoist
SJS_DECOIST_SOURCE = u'家装-decoist.com'
SJS_DECOIST_SPIDER = u'838729'    # 爬虫ID
SJS_DECOIST_COLL = u'contents-838729'

##auto
#微信
SJS_WECHAT_GJC_SOURCE = u'车酷-微信文章爬取-关键词'
SJS_WECHAT_GJC_SPIDER = u'801169'    # 爬虫ID
SJS_WECHAT_GJC_COLL = u'contents-801169'
#头条
SJS_TOUTIAO_SOURCE = u'车酷-今日头条新闻文章采集爬虫'
SJS_TOUTIAO_SPIDER = u'808634'    # 爬虫ID
SJS_TOUTIAO_COLL = u'contents-808634'
#界面
SJS_JIEMIAN_SOURCE = u'车酷-界面文章采集（按分类）爬虫-汽车分类'
SJS_JIEMIAN_SPIDER = u'808954'    # 爬虫ID
SJS_JIEMIAN_COLL = u'contents-808954'
#知乎
SJS_ZHIHU_SOURCE = u'车酷-知乎问答采集爬虫-豪华车/跑车/改装车/进口车'
SJS_ZHIHU_SPIDER = u'808964'    # 爬虫ID
SJS_ZHIHU_COLL = u'contents-808964'
#新浪汽车
SJS_SINA_SOURCE = u'车酷-新浪汽车新车资讯爬虫'
SJS_SINA_SPIDER = u'808970'    # 爬虫ID
SJS_SINA_COLL = u'contents-808970'

## spiders and data sources -- self-development, using the db_contents_coll directly
SOGOUWECHAT_GZH_SOURCE = u'sogou-wechat-gzh'
SOGOUWECHAT_GZH_SPIDER = u'sogou-wechat-spider'

SOGOUWECHAT_HOT_SOURCE = u'sogou-wechat-gzh'
SOGOUWECHAT_HOT_SPIDER = u'sogou-wechat-spider'
SOGOUWECHAT_HOT_URL_TEMPLATE = u'http://index.sogou.com/index/media/wechat?kwdNamesStr={keywords}&timePeriodType={period}&dataType={datatype}&queryType=INPUT'

WEIBO_SPIDER =  u'weibo-mobile-spider'
WEIBO_SOURCE =  u'weibo-mobile'
##网页版搜索 s.weibo.com
WEIBO_SEARCH_PREFIX = u'http://s.weibo.com/weibo/{}&Refer=index'
WEIBO_SEARCH_HOT_PREFIX = u'http://s.weibo.com/list/relpage?search={}'
##移动版搜索
WEIBO_MOBILE_SEARCH_TEMPLATE = 'https://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D{}&type=all&queryVal={}&title={}&v_p=11&ext=&fid=100103type%3D1%26q%3D{}&next_cursor=&page='


TYREPLUS_SOURCE = u'tyreplus-chijia-homepage'
TYREPLUS_HOMEPAGE_URL = u'http://www.tyreplus.com.cn/'
TYREPLUS_NEWS_URL = u'http://www.tyreplus.com.cn/About_tyreplus/news/'
TYREPLUS_PROMOTIONS_URL = u'http://www.tyreplus.com.cn/About_tyreplus/Promotion/'
