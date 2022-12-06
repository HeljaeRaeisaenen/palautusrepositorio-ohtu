from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, *query) -> None:
        self._query = query

    def build(self):
        return And(*self._query)
    
    def playsIn(self, team):
        return QueryBuilder(*self._query, PlaysIn(team))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(*self._query, HasAtLeast(value, attr))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(*self._query, HasFewerThan(value, attr))
    
    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))