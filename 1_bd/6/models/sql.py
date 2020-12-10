from models.users import User
from models.news import News
from models import db_session
from models.category import Category

db_session.global_init("user_news.db")
session = db_session.create_session()

user_1 = User(name="Siri", email="siri25@mail.ru")
session.add(user_1)
session.commit()

user_2 = User(name='Polina', email='polinka@gmail.ru')
session.add(user_2)
session.commit()

user_3 = User(name='Nikita', email='nikita2003@mail.ru')
session.add(user_3)
session.commit()

news1 = News(news_title="letter", news_content="hello:) i am rabbit")
user_1.news.append(news1)
session.commit()

news2 = News(news_title="present", news_content="rabbit give you a carrot")
news2.user_id = user_1.user_id
# news2.user = user
session.add(news2)
session.commit()

news3 = News(news_title='joke', news_content="its a joke, haha")
news3.user_id = user_2.user_id
session.add(news3)
session.commit()

category1 = Category(name='mem')
news1.categories.append(category1)
session.commit()

category2 = Category(name='drama')
news2.categories.append(category2)
session.commit()

category3 = Category(name='comedy')
news3.categories.append(category3)
session.commit()

#category2 = Category(name='lol')
#category2.news.append(news1)
#session.commit()
