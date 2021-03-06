# This file was originally auto-generated by Django's inspectdb command.
# The following changes were made manually:
#
# - Made the ids AutoFields (since they are defined as AUTOINCREMENT)
# - Renamed models to be singular
#   - Added verbose_name_plural if necessary
# - Added ForeignKeys
#   - Removed _id suffix on field name
#   - Added target model
#   - Added on_delete argument based on whether or not NULL is allowed
#   - Added related_names
#   - Set db_index, etc. based on the presence of indexes
# - Added ManyToManyFields
#   - Only added related_name if there was extra information in the table
# - Rearranged the order of models
# - Added field defaults
# - In a few cases, and based on the actual data, changed TextFields to limited-length CharFields
# - Usage.percent was interpreted by inspectdb as a TextField. Changed to FloatField.
#
# References
# - https://openfootball.github.io/schema/
# - https://github.com/openfootball/schema.sql/blob/master/NOTES.md

from django.db import models


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    kind = models.TextField()
    lat = models.TextField(blank=True, null=True)
    lng = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "places"


class Continent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    slug = models.TextField()
    key = models.CharField(max_length=2, unique=True)
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="continents")
    alt_names = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "continents"


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    slug = models.TextField()
    key = models.TextField(unique=True)
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="countries")
    code = models.TextField(unique=True)
    alt_names = models.TextField(blank=True, null=True)
    hist_names = models.TextField(blank=True, null=True)
    pop = models.IntegerField()
    area = models.IntegerField()
    continent = models.ForeignKey(Continent, models.SET_NULL, blank=True, null=True, db_index=False, related_name="countries")
    country = models.ForeignKey("self", models.SET_NULL, blank=True, null=True, db_index=False, related_name="territories")  # Seems to be used for territories with parent countries.
    s = models.BooleanField(default=False)
    c = models.BooleanField(default=False)
    d = models.BooleanField(default=False)
    m = models.BooleanField(default=False)
    motor = models.TextField(blank=True, null=True)
    alpha2 = models.TextField(blank=True, null=True)
    alpha3 = models.TextField(blank=True, null=True)
    num = models.TextField(blank=True, null=True)
    fifa = models.TextField(blank=True, null=True)
    ioc = models.TextField(blank=True, null=True)
    fips = models.TextField(blank=True, null=True)
    net = models.TextField(blank=True, null=True)
    wikipedia = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries"
        verbose_name_plural = "countries"


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="states")
    code = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    nuts = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="states")
    level = models.IntegerField(default=1)
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "states"
        unique_together = (("key", "country"),)


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="parts")
    code = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    nuts = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, models.CASCADE, db_index=False, related_name="parts")
    level = models.IntegerField(default=2)
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "parts"


class County(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="counties")
    code = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    nuts = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, models.CASCADE, db_index=False, related_name="counties")
    part = models.ForeignKey(Part, models.SET_NULL, blank=True, null=True, db_index=False, related_name="counties")
    level = models.IntegerField(default=2)
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "counties"
        verbose_name_plural = "counties"


class Muni(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="munis")
    code = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    nuts = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, models.CASCADE, db_index=False, related_name="munis")
    county = models.ForeignKey(County, models.SET_NULL, blank=True, null=True, db_index=False, related_name="munis")
    level = models.IntegerField(default=3)
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "munis"


class Metro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="metros")
    code = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="metros")
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "metros"


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="cities")
    code = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="cities")
    state = models.ForeignKey(State, models.SET_NULL, blank=True, null=True, db_index=False, related_name="cities")
    part = models.ForeignKey(Part, models.SET_NULL, blank=True, null=True, db_index=False, related_name="cities")
    county = models.ForeignKey(County, models.SET_NULL, blank=True, null=True, db_index=False, related_name="cities")
    muni = models.ForeignKey(Muni, models.SET_NULL, blank=True, null=True, db_index=False, related_name="cities")
    metro = models.ForeignKey(Metro, models.SET_NULL, blank=True, null=True, db_index=False, related_name="cities")
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cities"
        verbose_name_plural = "cities"


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    key = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="districts")
    code = models.TextField(blank=True, null=True)
    alt_names = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, models.CASCADE, db_index=False, related_name="districts")
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "districts"


class Assoc(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField(unique=True)
    title = models.TextField()
    since = models.IntegerField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True, db_index=False, related_name="assocs")
    national = models.BooleanField(default=False)
    continental = models.BooleanField(default=False)
    intercontinental = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    descendants = models.ManyToManyField("self", symmetrical=False, through="AssocAssoc", through_fields=("assoc1", "assoc2"), related_name="ancestors")

    class Meta:
        managed = False
        db_table = "assocs"


# Used to represent ancestor relationships (e.g. FIFA is the ancestor of all other associations)
class AssocAssoc(models.Model):
    id = models.AutoField(primary_key=True)
    assoc1 = models.ForeignKey(Assoc, models.CASCADE, db_index=True, related_name="+")
    assoc2 = models.ForeignKey(Assoc, models.CASCADE, db_index=True, related_name="+")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "assocs_assocs"
        unique_together = (("assoc1", "assoc2"),)


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=3, unique=True)
    title = models.TextField()
    title2 = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="teams")
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True, db_index=False, related_name="teams")
    club = models.BooleanField(default=False)  # "basically a reverse copy of the national flag and, thus, redundant"
    since = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)
    assoc = models.ForeignKey(Assoc, models.SET_NULL, blank=True, null=True, db_index=False, related_name="teams")
    national = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teams"


class League(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    title = models.TextField()
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True, db_index=False, related_name="leagues")
    club = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "leagues"


class Season(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    title = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "seasons"


class Ground(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField(unique=True)
    title = models.TextField()
    synonyms = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="grounds")
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True, db_index=False, related_name="grounds")
    since = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "grounds"


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField(unique=True)
    league = models.ForeignKey(League, models.CASCADE, db_index=False, related_name="events")
    season = models.ForeignKey(Season, models.CASCADE, db_index=False, related_name="events")
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    team3 = models.BooleanField(default=True)  # This should be False if it's a knockout event with no 3rd place match
    sources = models.TextField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    grounds = models.ManyToManyField(Ground, through="EventGround", related_name="events")
    teams = models.ManyToManyField(Team, through="EventTeam", related_name="events")

    class Meta:
        managed = False
        db_table = "events"


class EventGround(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE, db_index=True, related_name="+")
    ground = models.ForeignKey(Ground, models.CASCADE, db_index=False, related_name="+")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "events_grounds"
        unique_together = (("event", "ground"),)


class EventTeam(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE, db_index=True, related_name="+")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="+")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "events_teams"
        unique_together = (("event", "team"),)


class EventStanding(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE, db_index=False, related_name="event_standings")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    teams = models.ManyToManyField(Team, through="EventStandingEntry", related_name="event_standings")

    class Meta:
        managed = False
        db_table = "event_standings"


class EventStandingEntry(models.Model):
    id = models.AutoField(primary_key=True)
    event_standing = models.ForeignKey(EventStanding, models.CASCADE, db_index=False, related_name="event_standing_entries")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="event_standing_entries")
    pos = models.IntegerField(blank=True, null=True)
    played = models.IntegerField(blank=True, null=True)
    won = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)
    drawn = models.IntegerField(blank=True, null=True)
    goals_for = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "event_standing_entries"
        verbose_name_plural = "event standing entries"


class Round(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE, db_index=True, related_name="rounds")
    title = models.TextField()
    title2 = models.TextField(blank=True, null=True)
    pos = models.IntegerField()
    knockout = models.BooleanField(default=False)
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    auto = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "rounds"


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE, db_index=True, related_name="groups")
    title = models.TextField()
    pos = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    teams = models.ManyToManyField(Team, through="GroupTeam", related_name="groups")

    class Meta:
        managed = False
        db_table = "groups"


class GroupTeam(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, models.CASCADE, db_index=True, related_name="+")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="+")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "groups_teams"
        unique_together = (("group", "team"),)


class GroupStanding(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, models.CASCADE, db_index=False, related_name="group_standings")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    teams = models.ManyToManyField(Team, through="GroupStandingEntry", related_name="group_standings")

    class Meta:
        managed = False
        db_table = "group_standings"


class GroupStandingEntry(models.Model):
    id = models.AutoField(primary_key=True)
    group_standing = models.ForeignKey(GroupStanding, models.CASCADE, db_index=False, related_name="group_standing_entries")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="group_standing_entries")
    pos = models.IntegerField(blank=True, null=True)
    played = models.IntegerField(blank=True, null=True)
    won = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)
    drawn = models.IntegerField(blank=True, null=True)
    goals_for = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "group_standing_entries"
        verbose_name_plural = "group standing entries"


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField(unique=True, blank=True, null=True)
    round = models.ForeignKey(Round, models.CASCADE, db_index=True, related_name="games")
    pos = models.IntegerField()
    group = models.ForeignKey(Group, models.SET_NULL, blank=True, null=True, db_index=True, related_name="games")
    team1 = models.ForeignKey(Team, models.CASCADE, db_index=True, related_name="games_as_team1")
    team2 = models.ForeignKey(Team, models.CASCADE, db_index=True, related_name="games_as_team2")
    play_at = models.DateTimeField()
    postponed = models.BooleanField(default=False)
    play_at_v2 = models.DateTimeField(blank=True, null=True)
    play_at_v3 = models.DateTimeField(blank=True, null=True)
    ground = models.ForeignKey(Ground, models.SET_NULL, blank=True, null=True, db_index=False, related_name="games")
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True, db_index=False, related_name="games")
    knockout = models.BooleanField(default=False)
    home = models.BooleanField(default=True)
    score1 = models.IntegerField(blank=True, null=True)
    score2 = models.IntegerField(blank=True, null=True)
    score1et = models.IntegerField(blank=True, null=True)
    score2et = models.IntegerField(blank=True, null=True)
    score1p = models.IntegerField(blank=True, null=True)
    score2p = models.IntegerField(blank=True, null=True)
    score1i = models.IntegerField(blank=True, null=True)
    score2i = models.IntegerField(blank=True, null=True)
    score1ii = models.IntegerField(blank=True, null=True)
    score2ii = models.IntegerField(blank=True, null=True)
    next_game = models.ForeignKey("self", models.SET_NULL, blank=True, null=True, db_index=True, related_name="prev_games")
    prev_game = models.ForeignKey("self", models.SET_NULL, blank=True, null=True, db_index=True, related_name="next_games")
    winner = models.IntegerField(blank=True, null=True)  # 0 is a tie, 1 is team1, and 2 is team2
    winner90 = models.IntegerField(blank=True, null=True)  # same as winner but after 90 minutes
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "games"


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    name = models.TextField()
    synonyms = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    born_at = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True, db_index=False, related_name="persons")
    state = models.ForeignKey(State, models.SET_NULL, blank=True, null=True, db_index=False, related_name="persons")
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True, db_index=False, related_name="persons")
    nationality_id = models.IntegerField(blank=True, null=True)  # ForeignKey to Country? No data, so can't tell.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "persons"


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, models.CASCADE, db_index=False, related_name="goals")
    game = models.ForeignKey(Game, models.CASCADE, db_index=False, related_name="goals")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="goals")
    minute = models.IntegerField(blank=True, null=True)
    offset = models.IntegerField(default=0)  # the number of minutes into extra time when the goal was scored
    score1 = models.IntegerField(blank=True, null=True)
    score2 = models.IntegerField(blank=True, null=True)
    penalty = models.BooleanField(default=False)
    owngoal = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "goals"


class Roster(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, models.CASCADE, db_index=False, related_name="rosters")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="rosters")
    event = models.ForeignKey(Event, models.SET_NULL, blank=True, null=True, db_index=False, related_name="rosters")
    pos = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "rosters"


class AlltimeStanding(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    title = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    teams = models.ManyToManyField(Team, through="AlltimeStandingEntry", related_name="alltime_standings")

    class Meta:
        managed = False
        db_table = "alltime_standings"


class AlltimeStandingEntry(models.Model):
    id = models.AutoField(primary_key=True)
    alltime_standing = models.ForeignKey(AlltimeStanding, models.CASCADE, db_index=False, related_name="alltime_standing_entries")
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="alltime_standing_entries")
    pos = models.IntegerField(blank=True, null=True)
    played = models.IntegerField(blank=True, null=True)
    won = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)
    drawn = models.IntegerField(blank=True, null=True)
    goals_for = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    recs = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "alltime_standing_entries"
        verbose_name_plural = "alltime standing entries"


class Badge(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, models.CASCADE, db_index=False, related_name="badges")
    league = models.ForeignKey(League, models.CASCADE, db_index=False, related_name="badges")
    season = models.ForeignKey(Season, models.CASCADE, db_index=False, related_name="badges")
    title = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "badges"


class CountryCode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    kind = models.TextField()
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="country_codes")

    class Meta:
        managed = False
        db_table = "country_codes"
        unique_together = (("name", "kind"),)


class Lang(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    name = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "langs"


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    msg = models.TextField()
    level = models.TextField()
    app = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    tid = models.TextField(blank=True, null=True)
    ts = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "logs"


class Name(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    place = models.ForeignKey(Place, models.CASCADE, db_index=False, related_name="names")
    place_kind = models.TextField()
    lang = models.TextField(default="en")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "names"


class Prop(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField()
    value = models.TextField()
    kind = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "props"


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.TextField(unique=True)
    slug = models.TextField()
    name = models.TextField(blank=True, null=True)
    grade = models.IntegerField(default=1)
    parent = models.ForeignKey("self", models.SET_NULL, blank=True, null=True, db_index=False, related_name="children")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tags"


# taggable_id and taggable_type essentially define a generic key, though not
# in the format that Django uses.
class Tagging(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, models.CASCADE, db_index=True, related_name="taggings")
    taggable_id = models.IntegerField()
    taggable_type = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "taggings"
        index_together = (("taggable_id", "taggable_type"),)
        unique_together = (("taggable_id", "taggable_type", "tag"),)


class Usage(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, models.CASCADE, db_index=False, related_name="usages")
    lang = models.ForeignKey(Lang, models.CASCADE, db_index=False, related_name="usages")
    official = models.BooleanField(default=True)
    minor = models.BooleanField(default=False)
    percent = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "usages"


class Zone(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = "zones"
