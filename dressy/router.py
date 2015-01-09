class AnalyticsRouter(object):
    """
    A router to control all database operations on models in the
    Analytics application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Analytics models go to analytics_db.
        """
        if model._meta.app_label == 'Analytics':
            return 'analytics_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to analytics_db.
        """
        if model._meta.app_label == 'Analytics':
            return 'analytics_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the Analytics app is involved.
        """
        if obj1._meta.app_label == 'Analytics' or \
           obj2._meta.app_label == 'Analytics':
           return True
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the Analytics app only appears in the 'analytics_db'
        database.
        """
        if db == 'analytics_db':
            return model._meta.app_label == 'Analytics'
        elif model._meta.app_label == 'Analytics':
            return False
        return None
