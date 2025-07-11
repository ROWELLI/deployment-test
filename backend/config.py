# 나중에 웹 만들 때 사용
WINDOW_SIZE = "1600x900"

# 각 공정의 시간(분), 처리량, 불량(%), 딜레이(일), 비율(1:x)
COMPOSITING =   {'time': 8*60, 'throughput':2,   'reject': 0,   'delay':1, 'ratio':1}
LAMI =          {'time': 3*60, 'throughput':522, 'reject':0,    'delay':1, 'ratio':261}
LQ_INSPECTION = {'time': 30,   'throughput':522, 'reject':0.05, 'delay':1, 'ratio':1}
ETCHING =       {'time': 2*60, 'throughput':208, 'reject':0,    'delay':1, 'ratio':1}
EQ_INSPECTION = {'time': 2*60, 'throughput':208, 'reject':0.05, 'delay':1, 'ratio':1}
TRANSCRIPTION = {'time': 8*60, 'throughput':30,  'reject':0,    'delay':1, 'ratio':1/6}

processes = {
    'COMPOSITING': COMPOSITING,
    'LAMI': LAMI,
    'LQ_INSPECTION': LQ_INSPECTION,
    'ETCHING': ETCHING,
    'EQ_INSPECTION': EQ_INSPECTION,
    'TRANSCRIPTION': TRANSCRIPTION
}

# output 폴더 근데 이제 결과가 csv파일 한개라 안써도 될지도?
OUTPUT_LOCATON = './output'

