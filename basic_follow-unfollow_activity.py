from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''

session = InstaPy(username=insta_username,
                  password=insta_password,
                  split_db=True,
                  headless_browser=False,
                  want_check_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.follow_user_followers([''], amount=50, randomize=True, interact=True)

    photo_comments = ['Nice shot! @{}',
                      'Awesome! @{}',
                      'Cool :thumbsup:',
                      'Just incredible :open_mouth:',
                      'What camera did you use @{}?',
                      'Love your posts @{}',
                      'Looks awesome @{}',
                      'Nice @{}',
                      ':raised_hands: Yes!',
                      'I can feel your passion @{} :muscle:']