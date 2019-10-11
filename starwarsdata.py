from lista import Lista
class Personaje:
    def __init__(self, name, eye_color, films, 
        gender, height, homeworld, species, starships, vehicles):
        """Crea un personaje de StarWars"""
        self.name = name
        self.eye_color = eye_color
        self.films = films
        self.gender = gender
        self.height = height
        self.homeworld = homeworld
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
    
    def __str__(self):
        return repr(self.name)

    def __repr__(self):
        return self.__str__()

# personajes = Lista()
# personajes.append(Personaje( 'Luke Skywalker', 'blue', [5, 3, 6, 4, 7], 'male', '172', 'Tatooine', ['Human'], ['X-wing', 'Imperial shuttle'], ['Snowspeeder', 'Imperial Speeder Bike']) )
# personajes.append(Personaje( 'C-3PO', 'yellow', [5, 2, 1, 3, 6, 4], 'n/a', '167', 'Tatooine', ['Droid'], [], []) )
# personajes.append(Personaje( 'R2-D2', 'red', [5, 2, 1, 3, 6, 4, 7], 'n/a', '96', 'Naboo', ['Droid'], [], []) )
# personajes.append(Personaje( 'Darth Vader', 'yellow', [5, 3, 6, 4], 'male', '202', 'Tatooine', ['Human'], ['TIE Advanced x1'], []) )
# personajes.append(Personaje( 'Leia Organa', 'brown', [5, 3, 6, 4, 7], 'female', '150', 'Alderaan', ['Human'], [], ['Imperial Speeder Bike']) )
# personajes.append(Personaje( 'Owen Lars', 'blue', [2, 3, 4], 'male', '178', 'Tatooine', ['Human'], [], []) )
# personajes.append(Personaje( 'Beru Whitesun lars', 'blue', [2, 3, 4], 'female', '165', 'Tatooine', ['Human'], [], []) )
# personajes.append(Personaje( 'R5-D4', 'red', [4], 'n/a', '97', 'Tatooine', ['Droid'], [], []) )
# personajes.append(Personaje( 'Biggs Darklighter', 'brown', [4], 'male', '183', 'Tatooine', ['Human'], ['X-wing'], []) )
# personajes.append(Personaje( 'Obi-Wan Kenobi', 'blue-gray', [5, 2, 1, 3, 6, 4], 'male', '182', 'Stewjon', ['Human'], ['Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor', 'Belbullab-22 starfighter'], ['Tribubble bongo']) )
# personajes.append(Personaje( 'Anakin Skywalker', 'blue', [2, 1, 3], 'male', '188', 'Tatooine', ['Human'], ['Trade Federation cruiser', 'Jedi Interceptor', 'Naboo fighter'], ['Zephyr-G swoop bike', 'XJ-6 airspeeder']) )
# personajes.append(Personaje( 'Wilhuff Tarkin', 'blue', [3, 4], 'male', '180', 'Eriadu', ['Human'], [], []) )
# personajes.append(Personaje( 'Chewbacca', 'blue', [5, 3, 6, 4, 7], 'male', '228', 'Kashyyyk', ['Wookiee'], ['Millennium Falcon', 'Imperial shuttle'], ['AT-ST']) )
# personajes.append(Personaje( 'Han Solo', 'brown', [5, 6, 4, 7], 'male', '180', 'Corellia', ['Human'], ['Millennium Falcon', 'Imperial shuttle'], []) )
# personajes.append(Personaje( 'Greedo', 'black', [4], 'male', '173', 'Rodia', ['Rodian'], [], []) )
# personajes.append(Personaje( 'Jabba Desilijic Tiure', 'orange', [1, 6, 4], 'hermaphrodite', '175', 'Nal Hutta', ['Hutt'], [], []) )
# personajes.append(Personaje( 'Wedge Antilles', 'hazel', [5, 6, 4], 'male', '170', 'Corellia', ['Human'], ['X-wing'], ['Snowspeeder']) )
# personajes.append(Personaje( 'Jek Tono Porkins', 'blue', [4], 'male', '180', 'Bestine IV', ['Human'], ['X-wing'], []) )
# personajes.append(Personaje( 'Yoda', 'brown', [5, 2, 1, 3, 6], 'male', '66', 'unknown', ["Yoda's species"], [], []) )
# personajes.append(Personaje( 'Palpatine', 'yellow', [5, 2, 1, 3, 6], 'male', '170', 'Naboo', ['Human'], [], []) )
# personajes.append(Personaje( 'Boba Fett', 'brown', [5, 2, 6], 'male', '183', 'Kamino', ['Human'], ['Slave 1'], []) )
# personajes.append(Personaje( 'IG-88', 'red', [5], 'none', '200', 'unknown', ['Droid'], [], []) )
# personajes.append(Personaje( 'Bossk', 'red', [5], 'male', '190', 'Trandosha', ['Trandoshan'], [], []) )
# personajes.append(Personaje( 'Lando Calrissian', 'brown', [5, 6], 'male', '177', 'Socorro', ['Human'], ['Millennium Falcon'], []) )
# personajes.append(Personaje( 'Lobot', 'blue', [5], 'male', '175', 'Bespin', ['Human'], [], []) )
# personajes.append(Personaje( 'Ackbar', 'orange', [6, 7], 'male', '180', 'Mon Cala', ['Mon Calamari'], [], []) )
# personajes.append(Personaje( 'Mon Mothma', 'blue', [6], 'female', '150', 'Chandrila', ['Human'], [], []) )
# personajes.append(Personaje( 'Arvel Crynyd', 'brown', [6], 'male', 'unknown', 'unknown', ['Human'], ['A-wing'], []) )
# personajes.append(Personaje( 'Wicket Systri Warrick', 'brown', [6], 'male', '88', 'Endor', ['Ewok'], [], []) )
# personajes.append(Personaje( 'Nien Nunb', 'black', [6], 'male', '160', 'Sullust', ['Sullustan'], ['Millennium Falcon'], []) )
# personajes.append(Personaje( 'Qui-Gon Jinn', 'blue', [1], 'male', '193', 'unknown', ['Human'], [], ['Tribubble bongo']) )
# personajes.append(Personaje( 'Nute Gunray', 'red', [2, 1, 3], 'male', '191', 'Cato Neimoidia', ['Neimodian'], [], []) )
# personajes.append(Personaje( 'Finis Valorum', 'blue', [1], 'male', '170', 'Coruscant', ['Human'], [], []) )
# personajes.append(Personaje( 'Jar Jar Binks', 'orange', [2, 1], 'male', '196', 'Naboo', ['Gungan'], [], []) )
# personajes.append(Personaje( 'Roos Tarpals', 'orange', [1], 'male', '224', 'Naboo', ['Gungan'], [], []) )
# personajes.append(Personaje( 'Rugor Nass', 'orange', [1], 'male', '206', 'Naboo', ['Gungan'], [], []) )
# personajes.append(Personaje( 'Ric Olié', 'blue', [1], 'male', '183', 'Naboo', [], ['Naboo Royal Starship'], []) )
# personajes.append(Personaje( 'Watto', 'yellow', [2, 1], 'male', '137', 'Toydaria', ['Toydarian'], [], []) )
# personajes.append(Personaje( 'Sebulba', 'orange', [1], 'male', '112', 'Malastare', ['Dug'], [], []) )
# personajes.append(Personaje( 'Quarsh Panaka', 'brown', [1], 'male', '183', 'Naboo', [], [], []) )
# personajes.append(Personaje( 'Shmi Skywalker', 'brown', [2, 1], 'female', '163', 'Tatooine', ['Human'], [], []) )
# personajes.append(Personaje( 'Darth Maul', 'yellow', [1], 'male', '175', 'Dathomir', ['Zabrak'], ['Scimitar'], ['Sith speeder']) )
# personajes.append(Personaje( 'Bib Fortuna', 'pink', [6], 'male', '180', 'Ryloth', ["Twi'lek"], [], []) )
# personajes.append(Personaje( 'Ayla Secura', 'hazel', [2, 1, 3], 'female', '178', 'Ryloth', ["Twi'lek"], [], []) )
# personajes.append(Personaje( 'Dud Bolt', 'yellow', [1], 'male', '94', 'Vulpter', ['Vulptereen'], [], []) )
# personajes.append(Personaje( 'Gasgano', 'black', [1], 'male', '122', 'Troiken', ['Xexto'], [], []) )
# personajes.append(Personaje( 'Ben Quadinaros', 'orange', [1], 'male', '163', 'Tund', ['Toong'], [], []) )
# personajes.append(Personaje( 'Mace Windu', 'brown', [2, 1, 3], 'male', '188', 'Haruun Kal', ['Human'], [], []) )
# personajes.append(Personaje( 'Ki-Adi-Mundi', 'yellow', [2, 1, 3], 'male', '198', 'Cerea', ['Cerean'], [], []) )
# personajes.append(Personaje( 'Kit Fisto', 'black', [2, 1, 3], 'male', '196', 'Glee Anselm', ['Nautolan'], [], []) )
# personajes.append(Personaje( 'Eeth Koth', 'brown', [1, 3], 'male', '171', 'Iridonia', ['Zabrak'], [], []) )
# personajes.append(Personaje( 'Adi Gallia', 'blue', [1, 3], 'female', '184', 'Coruscant', ['Tholothian'], [], []) )
# personajes.append(Personaje( 'Saesee Tiin', 'orange', [1, 3], 'male', '188', 'Iktotch', ['Iktotchi'], [], []) )
# personajes.append(Personaje( 'Yarael Poof', 'yellow', [1], 'male', '264', 'Quermia', ['Quermian'], [], []) )
# personajes.append(Personaje( 'Plo Koon', 'black', [2, 1, 3], 'male', '188', 'Dorin', ['Kel Dor'], ['Jedi starfighter'], []) )
# personajes.append(Personaje( 'Mas Amedda', 'blue', [2, 1], 'male', '196', 'Champala', ['Chagrian'], [], []) )
# personajes.append(Personaje( 'Gregar Typho', 'brown', [2], 'male', '185', 'Naboo', ['Human'], ['Naboo fighter'], []) )
# personajes.append(Personaje( 'Cordé', 'brown', [2], 'female', '157', 'Naboo', ['Human'], [], []) )
# personajes.append(Personaje( 'Cliegg Lars', 'blue', [2], 'male', '183', 'Tatooine', ['Human'], [], []) )
# personajes.append(Personaje( 'Poggle the Lesser', 'yellow', [2, 3], 'male', '183', 'Geonosis', ['Geonosian'], [], []) )
# personajes.append(Personaje( 'Luminara Unduli', 'blue', [2, 3], 'female', '170', 'Mirial', ['Mirialan'], [], []) )
# personajes.append(Personaje( 'Barriss Offee', 'blue', [2], 'female', '166', 'Mirial', ['Mirialan'], [], []) )
# personajes.append(Personaje( 'Dormé', 'brown', [2], 'female', '165', 'Naboo', ['Human'], [], []) )
# personajes.append(Personaje( 'Dooku', 'brown', [2, 3], 'male', '193', 'Serenno', ['Human'], [], ['Flitknot speeder']) )
# personajes.append(Personaje( 'Bail Prestor Organa', 'brown', [2, 3], 'male', '191', 'Alderaan', ['Human'], [], []) )
# personajes.append(Personaje( 'Jango Fett', 'brown', [2], 'male', '183', 'Concord Dawn', ['Human'], [], []) )
# personajes.append(Personaje( 'Zam Wesell', 'yellow', [2], 'female', '168', 'Zolan', ['Clawdite'], [], ['Koro-2 Exodrive airspeeder']) )
# personajes.append(Personaje( 'Dexter Jettster', 'yellow', [2], 'male', '198', 'Ojom', ['Besalisk'], [], []) )
# personajes.append(Personaje( 'Lama Su', 'black', [2], 'male', '229', 'Kamino', ['Kaminoan'], [], []) )
# personajes.append(Personaje( 'Taun We', 'black', [2], 'female', '213', 'Kamino', ['Kaminoan'], [], []) )
# personajes.append(Personaje( 'Jocasta Nu', 'blue', [2], 'female', '167', 'Coruscant', ['Human'], [], []) )
# personajes.append(Personaje( 'Ratts Tyerell', 'unknown', [1], 'male', '79', 'Aleen Minor', ['Aleena'], [], []) )
# personajes.append(Personaje( 'R4-P17', 'red, blue', [2, 3], 'female', '96', 'unknown', [], [], []) )
# personajes.append(Personaje( 'Wat Tambor', 'unknown', [2], 'male', '193', 'Skako', ['Skakoan'], [], []) )
# personajes.append(Personaje( 'San Hill', 'gold', [2], 'male', '191', 'Muunilinst', ['Muun'], [], []) )
# personajes.append(Personaje( 'Shaak Ti', 'black', [2, 3], 'female', '178', 'Shili', ['Togruta'], [], []) )
# personajes.append(Personaje( 'Grievous', 'green, yellow', [3], 'male', '216', 'Kalee', ['Kaleesh'], ['Belbullab-22 starfighter'], ['Tsmeu-6 personal wheel bike']) )
# personajes.append(Personaje( 'Tarfful', 'blue', [3], 'male', '234', 'Kashyyyk', ['Wookiee'], [], []) )
# personajes.append(Personaje( 'Raymus Antilles', 'brown', [3, 4], 'male', '188', 'Alderaan', ['Human'], [], []) )
# personajes.append(Personaje( 'Sly Moore', 'white', [2, 3], 'female', '178', 'Umbara', [], [], []) )
# personajes.append(Personaje( 'Tion Medon', 'black', [3], 'male', '206', 'Utapau', ["Pau'an"], [], []) )
# personajes.append(Personaje( 'Finn', 'dark', [7], 'male', 'unknown', 'unknown', ['Human'], [], []) )
# personajes.append(Personaje( 'Rey', 'hazel', [7], 'female', 'unknown', 'unknown', ['Human'], [], []) )
# personajes.append(Personaje( 'Poe Dameron', 'brown', [7], 'male', 'unknown', 'unknown', ['Human'], ['T-70 X-wing fighter'], []) )
# personajes.append(Personaje( 'BB8', 'black', [7], 'none', 'unknown', 'unknown', ['Droid'], [], []) )
# personajes.append(Personaje( 'Captain Phasma', 'unknown', [7], 'female', 'unknown', 'unknown', [], [], []) )
# personajes.append(Personaje( 'Padmé Amidala', 'brown', [2, 1, 3], 'female', '165', 'Naboo', ['Human'], ['H-type Nubian yacht', 'Naboo star skiff', 'Naboo fighter'], []) )

personajes = Lista()
personajes.append(Personaje( 'Luke Skywalker', 'blue', Lista(5, 3, 6, 4, 7), 'male', '172', 'Tatooine', Lista('Human'), Lista('X-wing', 'Imperial shuttle'), Lista('Snowspeeder', 'Imperial Speeder Bike')) )
personajes.append(Personaje( 'C-3PO', 'yellow', Lista(5, 2, 1, 3, 6, 4), 'n/a', '167', 'Tatooine', Lista('Droid'), Lista(), Lista()) )
personajes.append(Personaje( 'R2-D2', 'red', Lista(5, 2, 1, 3, 6, 4, 7), 'n/a', '96', 'Naboo', Lista('Droid'), Lista(), Lista()) )
personajes.append(Personaje( 'Darth Vader', 'yellow', Lista(5, 3, 6, 4), 'male', '202', 'Tatooine', Lista('Human'), Lista('TIE Advanced x1'), Lista()) )
personajes.append(Personaje( 'Leia Organa', 'brown', Lista(5, 3, 6, 4, 7), 'female', '150', 'Alderaan', Lista('Human'), Lista(), Lista('Imperial Speeder Bike')) )
personajes.append(Personaje( 'Owen Lars', 'blue', Lista(2, 3, 4), 'male', '178', 'Tatooine', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Beru Whitesun lars', 'blue', Lista(2, 3, 4), 'female', '165', 'Tatooine', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'R5-D4', 'red', Lista(4), 'n/a', '97', 'Tatooine', Lista('Droid'), Lista(), Lista()) )
personajes.append(Personaje( 'Biggs Darklighter', 'brown', Lista(4), 'male', '183', 'Tatooine', Lista('Human'), Lista('X-wing'), Lista()) )
personajes.append(Personaje( 'Obi-Wan Kenobi', 'blue-gray', Lista(5, 2, 1, 3, 6, 4), 'male', '182', 'Stewjon', Lista('Human'), Lista('Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor', 'Belbullab-22 starfighter'), Lista('Tribubble bongo')) )
personajes.append(Personaje( 'Anakin Skywalker', 'blue', Lista(2, 1, 3), 'male', '188', 'Tatooine', Lista('Human'), Lista('Trade Federation cruiser', 'Jedi Interceptor', 'Naboo fighter'), Lista('Zephyr-G swoop bike', 'XJ-6 airspeeder')) )
personajes.append(Personaje( 'Wilhuff Tarkin', 'blue', Lista(3, 4), 'male', '180', 'Eriadu', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Chewbacca', 'blue', Lista(5, 3, 6, 4, 7), 'male', '228', 'Kashyyyk', Lista('Wookiee'), Lista('Millennium Falcon', 'Imperial shuttle'), Lista('AT-ST')) )
personajes.append(Personaje( 'Han Solo', 'brown', Lista(5, 6, 4, 7), 'male', '180', 'Corellia', Lista('Human'), Lista('Millennium Falcon', 'Imperial shuttle'), Lista()) )
personajes.append(Personaje( 'Greedo', 'black', Lista(4), 'male', '173', 'Rodia', Lista('Rodian'), Lista(), Lista()) )
personajes.append(Personaje( 'Jabba Desilijic Tiure', 'orange', Lista(1, 6, 4), 'hermaphrodite', '175', 'Nal Hutta', Lista('Hutt'), Lista(), Lista()) )
personajes.append(Personaje( 'Wedge Antilles', 'hazel', Lista(5, 6, 4), 'male', '170', 'Corellia', Lista('Human'), Lista('X-wing'), Lista('Snowspeeder')) )
personajes.append(Personaje( 'Jek Tono Porkins', 'blue', Lista(4), 'male', '180', 'Bestine IV', Lista('Human'), Lista('X-wing'), Lista()) )
personajes.append(Personaje( 'Yoda', 'brown', Lista(5, 2, 1, 3, 6), 'male', '66', 'unknown', Lista("Yoda's species"), Lista(), Lista()) )
personajes.append(Personaje( 'Palpatine', 'yellow', Lista(5, 2, 1, 3, 6), 'male', '170', 'Naboo', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Boba Fett', 'brown', Lista(5, 2, 6), 'male', '183', 'Kamino', Lista('Human'), Lista('Slave 1'), Lista()) )
personajes.append(Personaje( 'IG-88', 'red', Lista(5), 'none', '200', 'unknown', Lista('Droid'), Lista(), Lista()) )
personajes.append(Personaje( 'Bossk', 'red', Lista(5), 'male', '190', 'Trandosha', Lista('Trandoshan'), Lista(), Lista()) )
personajes.append(Personaje( 'Lando Calrissian', 'brown', Lista(5, 6), 'male', '177', 'Socorro', Lista('Human'), Lista('Millennium Falcon'), Lista()) )
personajes.append(Personaje( 'Lobot', 'blue', Lista(5), 'male', '175', 'Bespin', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Ackbar', 'orange', Lista(6, 7), 'male', '180', 'Mon Cala', Lista('Mon Calamari'), Lista(), Lista()) )
personajes.append(Personaje( 'Mon Mothma', 'blue', Lista(6), 'female', '150', 'Chandrila', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Arvel Crynyd', 'brown', Lista(6), 'male', 'unknown', 'unknown', Lista('Human'), Lista('A-wing'), Lista()) )
personajes.append(Personaje( 'Wicket Systri Warrick', 'brown', Lista(6), 'male', '88', 'Endor', Lista('Ewok'), Lista(), Lista()) )
personajes.append(Personaje( 'Nien Nunb', 'black', Lista(6), 'male', '160', 'Sullust', Lista('Sullustan'), Lista('Millennium Falcon'), Lista()) )
personajes.append(Personaje( 'Qui-Gon Jinn', 'blue', Lista(1), 'male', '193', 'unknown', Lista('Human'), Lista(), Lista('Tribubble bongo')) )
personajes.append(Personaje( 'Nute Gunray', 'red', Lista(2, 1, 3), 'male', '191', 'Cato Neimoidia', Lista('Neimodian'), Lista(), Lista()) )
personajes.append(Personaje( 'Finis Valorum', 'blue', Lista(1), 'male', '170', 'Coruscant', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Jar Jar Binks', 'orange', Lista(2, 1), 'male', '196', 'Naboo', Lista('Gungan'), Lista(), Lista()) )
personajes.append(Personaje( 'Roos Tarpals', 'orange', Lista(1), 'male', '224', 'Naboo', Lista('Gungan'), Lista(), Lista()) )
personajes.append(Personaje( 'Rugor Nass', 'orange', Lista(1), 'male', '206', 'Naboo', Lista('Gungan'), Lista(), Lista()) )
personajes.append(Personaje( 'Ric Olié', 'blue', Lista(1), 'male', '183', 'Naboo', Lista(), Lista('Naboo Royal Starship'), Lista()) )
personajes.append(Personaje( 'Watto', 'yellow', Lista(2, 1), 'male', '137', 'Toydaria', Lista('Toydarian'), Lista(), Lista()) )
personajes.append(Personaje( 'Sebulba', 'orange', Lista(1), 'male', '112', 'Malastare', Lista('Dug'), Lista(), Lista()) )
personajes.append(Personaje( 'Quarsh Panaka', 'brown', Lista(1), 'male', '183', 'Naboo', Lista(), Lista(), Lista()) )
personajes.append(Personaje( 'Shmi Skywalker', 'brown', Lista(2, 1), 'female', '163', 'Tatooine', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Darth Maul', 'yellow', Lista(1), 'male', '175', 'Dathomir', Lista('Zabrak'), Lista('Scimitar'), Lista('Sith speeder')) )
personajes.append(Personaje( 'Bib Fortuna', 'pink', Lista(6), 'male', '180', 'Ryloth', Lista("Twi'lek"), Lista(), Lista()) )
personajes.append(Personaje( 'Ayla Secura', 'hazel', Lista(2, 1, 3), 'female', '178', 'Ryloth', Lista("Twi'lek"), Lista(), Lista()) )
personajes.append(Personaje( 'Dud Bolt', 'yellow', Lista(1), 'male', '94', 'Vulpter', Lista('Vulptereen'), Lista(), Lista()) )
personajes.append(Personaje( 'Gasgano', 'black', Lista(1), 'male', '122', 'Troiken', Lista('Xexto'), Lista(), Lista()) )
personajes.append(Personaje( 'Ben Quadinaros', 'orange', Lista(1), 'male', '163', 'Tund', Lista('Toong'), Lista(), Lista()) )
personajes.append(Personaje( 'Mace Windu', 'brown', Lista(2, 1, 3), 'male', '188', 'Haruun Kal', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Ki-Adi-Mundi', 'yellow', Lista(2, 1, 3), 'male', '198', 'Cerea', Lista('Cerean'), Lista(), Lista()) )
personajes.append(Personaje( 'Kit Fisto', 'black', Lista(2, 1, 3), 'male', '196', 'Glee Anselm', Lista('Nautolan'), Lista(), Lista()) )
personajes.append(Personaje( 'Eeth Koth', 'brown', Lista(1, 3), 'male', '171', 'Iridonia', Lista('Zabrak'), Lista(), Lista()) )
personajes.append(Personaje( 'Adi Gallia', 'blue', Lista(1, 3), 'female', '184', 'Coruscant', Lista('Tholothian'), Lista(), Lista()) )
personajes.append(Personaje( 'Saesee Tiin', 'orange', Lista(1, 3), 'male', '188', 'Iktotch', Lista('Iktotchi'), Lista(), Lista()) )
personajes.append(Personaje( 'Yarael Poof', 'yellow', Lista(1), 'male', '264', 'Quermia', Lista('Quermian'), Lista(), Lista()) )
personajes.append(Personaje( 'Plo Koon', 'black', Lista(2, 1, 3), 'male', '188', 'Dorin', Lista('Kel Dor'), Lista('Jedi starfighter'), Lista()) )
personajes.append(Personaje( 'Mas Amedda', 'blue', Lista(2, 1), 'male', '196', 'Champala', Lista('Chagrian'), Lista(), Lista()) )
personajes.append(Personaje( 'Gregar Typho', 'brown', Lista(2), 'male', '185', 'Naboo', Lista('Human'), Lista('Naboo fighter'), Lista()) )
personajes.append(Personaje( 'Cordé', 'brown', Lista(2), 'female', '157', 'Naboo', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Cliegg Lars', 'blue', Lista(2), 'male', '183', 'Tatooine', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Poggle the Lesser', 'yellow', Lista(2, 3), 'male', '183', 'Geonosis', Lista('Geonosian'), Lista(), Lista()) )
personajes.append(Personaje( 'Luminara Unduli', 'blue', Lista(2, 3), 'female', '170', 'Mirial', Lista('Mirialan'), Lista(), Lista()) )
personajes.append(Personaje( 'Barriss Offee', 'blue', Lista(2), 'female', '166', 'Mirial', Lista('Mirialan'), Lista(), Lista()) )
personajes.append(Personaje( 'Dormé', 'brown', Lista(2), 'female', '165', 'Naboo', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Dooku', 'brown', Lista(2, 3), 'male', '193', 'Serenno', Lista('Human'), Lista(), Lista('Flitknot speeder')) )
personajes.append(Personaje( 'Bail Prestor Organa', 'brown', Lista(2, 3), 'male', '191', 'Alderaan', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Jango Fett', 'brown', Lista(2), 'male', '183', 'Concord Dawn', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Zam Wesell', 'yellow', Lista(2), 'female', '168', 'Zolan', Lista('Clawdite'), Lista(), Lista('Koro-2 Exodrive airspeeder')) )
personajes.append(Personaje( 'Dexter Jettster', 'yellow', Lista(2), 'male', '198', 'Ojom', Lista('Besalisk'), Lista(), Lista()) )
personajes.append(Personaje( 'Lama Su', 'black', Lista(2), 'male', '229', 'Kamino', Lista('Kaminoan'), Lista(), Lista()) )
personajes.append(Personaje( 'Taun We', 'black', Lista(2), 'female', '213', 'Kamino', Lista('Kaminoan'), Lista(), Lista()) )
personajes.append(Personaje( 'Jocasta Nu', 'blue', Lista(2), 'female', '167', 'Coruscant', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Ratts Tyerell', 'unknown', Lista(1), 'male', '79', 'Aleen Minor', Lista('Aleena'), Lista(), Lista()) )
personajes.append(Personaje( 'R4-P17', 'red, blue', Lista(2, 3), 'female', '96', 'unknown', Lista(), Lista(), Lista()) )
personajes.append(Personaje( 'Wat Tambor', 'unknown', Lista(2), 'male', '193', 'Skako', Lista('Skakoan'), Lista(), Lista()) )
personajes.append(Personaje( 'San Hill', 'gold', Lista(2), 'male', '191', 'Muunilinst', Lista('Muun'), Lista(), Lista()) )
personajes.append(Personaje( 'Shaak Ti', 'black', Lista(2, 3), 'female', '178', 'Shili', Lista('Togruta'), Lista(), Lista()) )
personajes.append(Personaje( 'Grievous', 'green, yellow', Lista(3), 'male', '216', 'Kalee', Lista('Kaleesh'), Lista('Belbullab-22 starfighter'), Lista('Tsmeu-6 personal wheel bike')) )
personajes.append(Personaje( 'Tarfful', 'blue', Lista(3), 'male', '234', 'Kashyyyk', Lista('Wookiee'), Lista(), Lista()) )
personajes.append(Personaje( 'Raymus Antilles', 'brown', Lista(3, 4), 'male', '188', 'Alderaan', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Sly Moore', 'white', Lista(2, 3), 'female', '178', 'Umbara', Lista(), Lista(), Lista()) )
personajes.append(Personaje( 'Tion Medon', 'black', Lista(3), 'male', '206', 'Utapau', Lista("Pau'an"), Lista(), Lista()) )
personajes.append(Personaje( 'Finn', 'dark', Lista(7), 'male', 'unknown', 'unknown', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Rey', 'hazel', Lista(7), 'female', 'unknown', 'unknown', Lista('Human'), Lista(), Lista()) )
personajes.append(Personaje( 'Poe Dameron', 'brown', Lista(7), 'male', 'unknown', 'unknown', Lista('Human'), Lista('T-70 X-wing fighter'), Lista()) )
personajes.append(Personaje( 'BB8', 'black', Lista(7), 'none', 'unknown', 'unknown', Lista('Droid'), Lista(), Lista()) )
personajes.append(Personaje( 'Captain Phasma', 'unknown', Lista(7), 'female', 'unknown', 'unknown', Lista(), Lista(), Lista()) )
personajes.append(Personaje( 'Padmé Amidala', 'brown', Lista(2, 1, 3), 'female', '165', 'Naboo', Lista('Human'), Lista('H-type Nubian yacht', 'Naboo star skiff', 'Naboo fighter'), Lista()) )
