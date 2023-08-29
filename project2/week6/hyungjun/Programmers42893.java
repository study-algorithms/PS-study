import java.util.*;

class Page {
    String url;
    int base;
    int outboundCnt;
    List<String> refs;
    double matchingScore;
    
    
    Page(String url, int base, List<String> refs){
        this.url = url;
        this.base = base;
        this.outboundCnt = refs.size();
        this.refs = refs;
    }
    
    double getLinkScore() {
        return (double) base / outboundCnt;
    }
    
}

class Solution {
    private String urlTag = "<meta property=\"og:url\" content=";
    private String aTag = "<a href="; 
    
    public String getUrl(String page) {
        int i = page.indexOf(urlTag);
        String url = "";
        for (int j=i+urlTag.length(); j<page.length(); j++){
            String c = Character.toString(page.charAt(j));
            if (c.equals(">")) {
                url = url.substring(0, url.length()-1);
                break;
            }
            url += c;
        }
        return url;
    }
    
    public List<String> findAllRef(String page) {
        List<String> allRef = new ArrayList<>();
        int index = 0;
        while (index != -1) {
            index = page.indexOf(aTag, index);
            if (index == -1) continue;
            String outlink = "";
            for (int j=index+aTag.length(); j < page.length(); j++) {
                String c = Character.toString(page.charAt(j));
                if (c.equals(">")) {
                    allRef.add(outlink);
                    outlink = "";
                    index = j+1;
                    break;
                }
                outlink += c;
            }
        }
        return allRef;
    }
    
    public int getWordCount(String page, String word) {
        int index = 0;
        int count = 0;
        while (index != -1) {
            index = page.indexOf(word, index);
            if (index == -1) continue;
            char c = page.charAt(index + word.length());
            if (!Character.isLetter(c)) {
                count += 1;
                index += word.length();
            } else {
                for (int j = index + word.length()+1; j<page.length();j++){
                    if (!Character.isLetter(page.charAt(j))) {
                        index = j;
                        break;
                    }
                }   
            }
        }
        return count;
    }
    
    public int solution(String word, String[] pages) {
        int answer = 0;
        word = word.toLowerCase();
        for (int i=0; i<pages.length; i++){
            pages[i] = pages[i].toLowerCase();
        }
        List<Page> pageList = new ArrayList<>();
        HashMap<String, Integer> pageUrlToIndex = new HashMap<>();
        
        for (int i = 0; i < pages.length; i++) {
            String page = pages[i];
            String url = getUrl(page);
            int base = getWordCount(page, word);
            List<String> refs = findAllRef(page);
            Page newPage = new Page(url, base, refs);
            
            pageUrlToIndex.put(url, i);
            pageList.add(newPage);
        }
        
        for (Page page: pageList) {
            page.matchingScore += (double) page.base;
            for (String outPage : page.refs) {
                if (pageUrlToIndex.containsKey(outPage)) {
                    pageList.get(pageUrlToIndex.get(outPage)).matchingScore += page.getLinkScore();    
                }
            }
        }
        
        double maximumMatchingScore = 0.0;
        for (int i = 0; i < pageList.size(); i++) {
            Page page = pageList.get(i);
            if (maximumMatchingScore < page.matchingScore) {
                maximumMatchingScore = page.matchingScore;
                answer = i;
            }
        }

        return answer;
    }
}
