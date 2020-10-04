from django.shortcuts import render
from .models import HotList
from django.core.paginator import Paginator

# list of mobile User Agents
mobile_uas = [
    'w3c ', 'acs-', 'alav', 'alca', 'amoi', 'audi', 'avan', 'benq', 'bird', 'blac',
    'blaz', 'brew', 'cell', 'cldc', 'cmd-', 'dang', 'doco', 'eric', 'hipt', 'inno',
    'ipaq', 'java', 'jigs', 'kddi', 'keji', 'leno', 'lg-c', 'lg-d', 'lg-g', 'lge-',
    'maui', 'maxo', 'midp', 'mits', 'mmef', 'mobi', 'mot-', 'moto', 'mwbp', 'nec-',
    'newt', 'noki', 'oper', 'palm', 'pana', 'pant', 'phil', 'play', 'port', 'prox',
    'qwap', 'sage', 'sams', 'sany', 'sch-', 'sec-', 'send', 'seri', 'sgh-', 'shar',
    'sie-', 'siem', 'smal', 'smar', 'sony', 'sph-', 'symb', 't-mo', 'teli', 'tim-',
    'tosh', 'tsm-', 'upg1', 'upsi', 'vk-v', 'voda', 'wap-', 'wapa', 'wapi', 'wapp',
    'wapr', 'webc', 'winw', 'winw', 'xda', 'xda-'
]
mobile_ua_hints = ['SymbianOS', 'Opera Mini', 'iPhone']

'''
def has_next_4(self):
    return self.number + 4 <= self.paginator.num_pages


def has_previous_4(self):
    return self.number - 4 >= 1

def next_page_number_4(self):
    return math.ceil(self.paginator.validate_number(self.number)/4)*4+1

def previous_page_number_4(self):
    return math.floor((self.paginator.validate_number(self.number)-1)/4)*4-3
'''

def index(request):
    HotLists = HotList.objects.all()
    paginator = Paginator(HotLists, 20)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # [2]
    page_numbers_range = 4

    # [3]
    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range


    # [4]
    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]



    return render(request, 'HotList/index.html', {
        'HotLists': HotLists, 'posts': posts, 'paginator_range': paginator_range

    })




def contents(request, pageid):
    #pageid = HotList.id
    HotLists = HotList.objects.all()
    tttt = HotList.objects.get(id=pageid)
    return render(request, 'HotList/contents.html', {'HotLists': HotLists, 'pageid': pageid, 'tttt': tttt})
    # return render(request, 'HotList/contents.html', {'HotLists': HotLists, 'pageid': pageid})