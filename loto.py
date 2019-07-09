from helper import *
import pyximport
pyximport.install(build_dir=”./build”)
import speaking
def check(data):
	diaphuong = ['NAM','TRUNG','MIỀN BẮC','AN GIANG','BÌNH DƯƠNG','BÌNH ĐỊNH','BẠC LIÊU','BÌNH PHƯỚC','BẾN TRE','BÌNH THUẬN','CÀ MAU','CẦN THƠ','ĐẮC LẮC','ĐỒNG NAI','ĐÀ NẴNG','ĐẮC NÔNG','ĐỒNG THÁP','GIA LAI','THÀNH PHỐ','HẬU GIANG','KIÊN GIANG','KHÁNH HÒA','KON TUM','LONG AN','LÂM ĐỒNG','NINH THUẬN','PHÚ YÊN','QUẢNG BÌNH','QUẢNG NGÃI','QUẢNG NAM','QUẢNG TRỊ','SÓC TRĂNG','TIỀN GIANG','TÂY NINH','HUẾ','TRÀ VINH','VĨNH LONG','VŨNG TÀU']
	diaphuong_=np.array(diaphuong)
	rss = ['https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss','https://xskt.com.vn/rss-feed/mien-trung-xsmt.rss','https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss','https://xskt.com.vn/rss-feed/an-giang-xsag.rss','https://xskt.com.vn/rss-feed/binh-duong-xsbd.rss','https://xskt.com.vn/rss-feed/binh-dinh-xsbdi.rss','https://xskt.com.vn/rss-feed/bac-lieu-xsbl.rss','https://xskt.com.vn/rss-feed/binh-phuoc-xsbp.rss','https://xskt.com.vn/rss-feed/ben-tre-xsbt.rss','https://xskt.com.vn/rss-feed/binh-thuan-xsbth.rss','https://xskt.com.vn/rss-feed/ca-mau-xscm.rss','https://xskt.com.vn/rss-feed/can-tho-xsct.rss','https://xskt.com.vn/rss-feed/dac-lac-xsdlk.rss','https://xskt.com.vn/rss-feed/dong-nai-xsdn.rss','https://xskt.com.vn/rss-feed/da-nang-xsdng.rss','https://xskt.com.vn/rss-feed/dac-nong-xsdno.rss','https://xskt.com.vn/rss-feed/dong-thap-xsdt.rss','https://xskt.com.vn/rss-feed/gia-lai-xsgl.rss','https://xskt.com.vn/rss-feed/tp-hcm-xshcm.rss','https://xskt.com.vn/rss-feed/hau-giang-xshg.rss','https://xskt.com.vn/rss-feed/kien-giang-xskg.rss','https://xskt.com.vn/rss-feed/khanh-hoa-xskh.rss','https://xskt.com.vn/rss-feed/kon-tum-xskt.rss','https://xskt.com.vn/rss-feed/long-an-xsla.rss','https://xskt.com.vn/rss-feed/lam-dong-xsld.rss','https://xskt.com.vn/rss-feed/ninh-thuan-xsnt.rss','https://xskt.com.vn/rss-feed/phu-yen-xspy.rss','https://xskt.com.vn/rss-feed/quang-binh-xsqb.rss','https://xskt.com.vn/rss-feed/quang-ngai-xsqng.rss','https://xskt.com.vn/rss-feed/quang-nam-xsqnm.rss','https://xskt.com.vn/rss-feed/quang-tri-xsqt.rss','https://xskt.com.vn/rss-feed/soc-trang-xsst.rss','https://xskt.com.vn/rss-feed/tien-giang-xstg.rss','https://xskt.com.vn/rss-feed/tay-ninh-xstn.rss','https://xskt.com.vn/rss-feed/thua-thien-hue-xstth.rss','https://xskt.com.vn/rss-feed/tra-vinh-xstv.rss','https://xskt.com.vn/rss-feed/vinh-long-xsvl.rss','https://xskt.com.vn/rss-feed/vung-tau-xsvt.rss']
	loc = pos_tag(data)
#	print(loc)
	m = np.array(loc)
	n = np.intersect1d(diaphuong_,m)
	nn = str(n[0])
	print('Địa phuong: '+nn)
	o = diaphuong.index(nn)
	url = str(rss[o])
	d = feedparser.parse(url)
	if 'CŨ HƠN' in data:
		tg = d['entries'][1]['title'] 
		kq = d['entries'][1]['description']
#		print(kq)
	else:
		tg = d['entries'][0]['title'] 
		kq = d['entries'][0]['description']
		print(kq)
	kq = kq.replace(']',': ')
	kq = kq.replace('ĐB:','Giải đặc biệt:')
	kq = kq.replace('1:','Giải nhất:')
	kq = kq.replace('2:','Giải nhì:')
	kq = kq.replace('3:','Giải ba:')
	kq = kq.replace('4:','Giải tư:')
	kq = kq.replace('5:','Giải năm:')
	kq = kq.replace('6:','Giải sáu:')
	kq = kq.replace('7:','Giải bảy:')
	x = kq.split("[")
	speaking.speak(tg)
	ketqua = '. '.join(x)
	ketqua = ketqua.replace('\n','. ')
	speaking.speak(ketqua)
	return ketqua
	print (ketqua)