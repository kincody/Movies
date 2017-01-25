import media
import fresh_tomatoes
toy_story=media.Movie("Toy Story",
                "A story of a boy and his toys that come to life",
                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                      )
avathar=media.Movie("Avathar",
                "A paraplegic marine dispatched to the moon Pandora on a "
                "unique mission becomes torn between following his "
                "orders and protecting the world he feels is his home. ",
                "https://soemoeroot.files.wordpress.com/2009/12/avatar-film.jpg",
                "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                      )

kung_fu_panda3=media.Movie("kung fu panda3",
                        "Continuing his legendary adventures of awesomeness, "
                        "Po must face two hugely epic, but different "
                        "threats: one supernatural and the other a "
                        "little closer to his home.",
                        "http://www.dreamworks.com/kungfupanda/images/uploads"
                        "/properties/KFP3_Home-Ent-Key-Art_PayOff_Poster.jpg",  
                        "https://www.youtube.com/watch?v=10r9ozshGVE")

school_of_rock=media.Movie("School of rock",
                    "After being kicked out of a rock band, Dewey Finn "
                    "becomes a substitute teacher of a strict "
                    "elementary private school, only to try and turn it "
                    "into a rock band.",
                    "http://www.posters.ws/images/920027/school_of_rock.jpg",  
                    "https://www.youtube.com/watch?v=3PsUJFEBC74")



ant_man=media.Movie("Ant Man",
                    "Con artist Scott gains the ability to shrink in "
                    "scale with the help of a futuristic suit. Now "
                    "he must rise to the occasion of his superhero "
                    "status and protect his secret from unsavoury "
                    "elements.",
                    "http://cdn.collider.com/wp-content/uploads/2015/06/"
                    "ant-man-poster-german.jpg",  
                    "https://www.youtube.com/watch?v=pWdKf3MneyI")



Iron_Man=media.Movie("Iron Man",
                    "After being held captive in an Afghan cave, "
                    "billionaire engineer Tony Stark creates a unique"
                    "weaponized suit of armor to fight evil.",
                    "http://www.adanx.com/imm/posters/i/iron-man-2/"
                    "ironman27.jpg",  
                    "https://www.youtube.com/watch?v=8hYlB38asDY")


#kung_fu_panda3.show_trailer()
movies=[toy_story,avathar,kung_fu_panda3,school_of_rock,ant_man,Iron_Man]                          
fresh_tomatoes.open_movies_page(movies)
