# from rest_framework_simplejwt.tokens import RefreshToken
# import random
#
# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#
#
#     return {
#         'refresh' : str(refresh),
#         'access' : str(refresh.access_token),
#     }
#
# def generate_random_6_digits():
#     return random.randint(100000, 999999)