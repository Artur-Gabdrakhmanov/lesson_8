from demoqa_tests.model.pages import practice_form


def test_practice_form():
    practice_form.open()

    # WHEN
    practice_form.input_info(name='Chev', surname='Chelios', email='test_090@gmail.com',
                             mobile='7298965483', address='Moscow')

    practice_form.select_gender('Male')
    practice_form.select_birthday(day='08', month='11', year='1980')
    practice_form.input_subject('Economics')
    practice_form.select_hobbies('Music', 'Sports')
    practice_form.upload_picture('resources/1.png')
    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.assert_of_registered_user(
        'Chev Chelios',
        'test_090@gmail.com',
        'Male',
        '7298965483',
        '08 December,1980',
        'Economics',
        'Music, Sports',
        '1.png',
        'Moscow',
        'NCR Delhi'
    )
