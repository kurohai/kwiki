from sdmsapp import metadata, Base, Table

# required tables

class arcustmr(Base):
    __table__ = Table('arcustmr', metadata, autoload=True, schema='dsgi')
    def __repr__(self):
        return str(self.cust_no)


class sainvlin(Base):
    __table__ = Table('sainvlin', metadata, autoload=True, schema='dsgi')
    def __repr__(self):
        return str(self.cust_no)


class sainvhdr(Base):
    __table__ = Table('sainvhdr', metadata, autoload=True, schema='dsgi')
    def __repr__(self):
        return str(self.cust_no)


# new unknown tables

class division(Base):
    __table__ = Table('division', metadata, autoload=True, schema='dsgi')
    # def __repr__(self):
    #     me = ' '.join([(k,v) for k,v in self.items()])
    #     return str(me)

# class invoice_summary(Base):
#     __table__ = Table('invoice_summary', metadata, autoload=True, schema='dsgi')
#     def __repr__(self):
#         return str(self.cust_no)

class arhistry(Base):
    __table__ = Table('arhistry', metadata, autoload=True, schema='dsgi')
    # def __repr__(self):
    #     return str(self.cust_no)

class artransf(Base):
    __table__ = Table('artransf', metadata, autoload=True, schema='dsgi')
    # def __repr__(self):
    #     return str(self.cust_no)
