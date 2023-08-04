package project2.week3.hyungjun;

import java.util.*;
import java.util.stream.*;

public class ProgrammersBestAlbum {
    public class Song {
        private int id;
        private int play;
        private String genre;

        public Song(int id, int play, String genre) {
            this.id = id;
            this.play = play;
            this.genre = genre;
        }

        public int getId() {
            return id;
        }

        public int getPlay() {
            return play;
        }

        public String getGenre() {
            return genre;
        }
    }
    
    private int sum(List<Song> songs) {
        return songs.stream().mapToInt(Song::getPlay).sum();
    }

    public int[] solution(String[] genres, int[] plays) {

        List<Song> songs = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            songs.add(new Song(i, plays[i], genres[i]));
        }
        List<Integer> album = songs.stream()
            .collect(Collectors.groupingBy(Song::getGenre))
            .entrySet()
            .stream()
            .sorted((a, b) -> sum(b.getValue()) - sum(a.getValue()))
            .flatMap(x -> x.getValue().stream().sorted((a, b) -> b.getPlay() != a.getPlay() ? b.getPlay() - a.getPlay() : a.getId() - b.getId()).limit(2))
            .map(Song::getId).collect(Collectors.toList());
        return album.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        ProgrammersBestAlbum programmersBestAlbum = new ProgrammersBestAlbum();
        programmersBestAlbum.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500});
    }
}