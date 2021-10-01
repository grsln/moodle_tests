class LoginConstants:
    AUTH_ERROR = "Неверный логин или пароль, попробуйте заново."
    LOGIN_URL = "https://qacoursemoodle.innopolis.university/login/index.php"
    LOGOUT_URL = "https://qacoursemoodle.innopolis.university/login/logout.php"
    CONFIRM_MESSAGE = "Вы уже вошли в систему"


class ProfileConstants:
    EDIT_PROFILE = "https://qacoursemoodle.innopolis.university/user/editadvanced.php"
    SUCCESS_SAVE = "Изменения сохранены"
    AVATAR_LINK = "common/robot.jpeg"


class CourseConstants:
    DELETED_COURSE = "был полностью удален"
    SECTION_NUMBER = 52
    COURSE_LANGUAGE = "ru"
    CURRENT_YEAR = 2021
    LAST_YEAR = 2050
    FILE_SIZES_VALUES = [
        0,
        2097152,
        1048576,
        512000,
        102400,
        51200,
        10240,
    ]
