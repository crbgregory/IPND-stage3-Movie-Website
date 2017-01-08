import fresh_tomatoes
import media

citizen_kane = media.Movie("Citizen Kane",
                            "A film examines the life and legacy of Charles Foster Kane.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Citizenkane.jpg/220px-Citizenkane.jpg",
                            "https://www.youtube.com/watch?v=8dxh3lwdOFw")

jackie = media.Movie("Jackie",
                    "A 2016 biographical drama film about Jacqueline Kennedy directed by Pablo Larraín and written by Noah Oppenheim.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Jackie_%282016_film%29.png/220px-Jackie_%282016_film%29.png",
                    "https://www.youtube.com/watch?v=jjClaFDhSCs")

live_by_night = media.Movie("Live by Night",
                            "A crime novel by Dennis Lehane that was published in 2012. It won a 2013 Edgar Award for novel of the year.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Live_by_Night.jpg/220px-Live_by_Night.jpg",
                            "https://www.youtube.com/watch?v=ClcQUlXcCKw")

doctor_strange = media.Movie("Doctor Strange",
                            "A 2016 American superhero film featuring the Marvel Comics character of the same name.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg",
                            "https://www.youtube.com/watch?v=HSzx-zryEgM")

billys_walk = media.Movie("Billy Lynn's Long Halftime Walk",
                            "a 2016 war drama film based on the novel of the same name by Ben Fountain..",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Billy_Lynn%27s_Long_Halftime_Walk_poster.png/220px-Billy_Lynn%27s_Long_Halftime_Walk_poster.png",
                            "https://www.youtube.com/watch?v=mUULFJ_I048")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                            "An upcoming British fantasy film directed by David Yates and distributed by Warner Bros.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png/220px-Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                            "https://www.youtube.com/watch?v=ViuDsy7yb8M")

movies = [citizen_kane, jackie, live_by_night, doctor_strange, billys_walk, fantastic_beasts]

fresh_tomatoes.open_movies_page(movies)
