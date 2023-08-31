def solution(word, pages):
    word = word.lower()
    length = len(word)
    p_info = dict()

    cnt = 0
    for p in pages:
        sent = p.split('\n')
        head = sent[sent.index('<head>')+1: sent.index('</head>  ')]
        for s in head:
            if '<meta property="og:url" content="https://' in s:
                url = s[s.index('"https://')+len('"https://'): s.index('"/>')]
                p_info[url] = {'b_score': 0 , 'c_link': [], 'index': cnt}
                break

        body = sent[sent.index('<body>')+1: sent.index('</body>')]

        for s in body:
            s = s.lower()
            sentence = s
            count = 0
            while True:
                index = sentence.find(word)
                if index == -1:
                    break
                    
                if index == 0:
                    if len(word) > len(sentence)-1:
                        count+=1
                    else:
                        if not sentence[len(word)].isalpha():
                            count+=1
                else:
                    if not sentence[index - 1].isalpha():
                        if index+len(word) > len(sentence)-1:
                            count+=1
                        else:
                            if not sentence[index+len(word)].isalpha():
                                count += 1
            
                sentence = sentence[index + len(word)-1:]

            p_info[url]['b_score']+=count


        for s in body:
            if '<a href="' not in s:
                continue

            try:
                while True:
                    start = s.index('<a href="https://') + len('<a href="https://')
                    end = start + s[start:].index('">')

                    link = s[start:end].strip()

                    if link != url:
                        p_info[url]['c_link'].append(link)
                    s = s[end + 3:]
            except:
                pass

        cnt+=1


    final = dict()
    for k, v in p_info.items():
        if k in final:
            final[k][0] += v['b_score']
        else:
            final[k] = [v['b_score'], v['index']]

        for target in v['c_link']:
            if target not in p_info:
                continue

            if target in final:
                final[target][0]+=p_info[k]['b_score'] / len(p_info[k]['c_link'])
            else:
                final[target] = [p_info[k]['b_score'] / len(p_info[k]['c_link']), p_info[target]['index']]

    answer = sorted(final.items(), key= lambda x : (-x[1][0], x[1][1]))[0][1][1]
    return answer
  
a = solution(word='blind', pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\])
print(a)
# 0 
                                    
