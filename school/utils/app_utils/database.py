# to use later


# from django.core.exceptions import ObjectDoesNotExist
# from graphql import GraphQLError


# def get_model_object(model, column, value, message=None):
#     try:
#         model.objects.get(**{column: value})
#     except ObjectDoesNotExist as e:
#         if message is not None:
#             raise GraphQLError(message)
#         raise e
