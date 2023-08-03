from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import UserReqeuest
from laundryadmin.models import Company
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

class Update_req(APIView):
    def post(self, request):
        response = {
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'Something went wrong'
        }
        try:
            data = request.data
            uuid = data.get('uuid')
            if not uuid:
                response['message'] = 'User Request ID is missing'
                response['status'] = status.HTTP_400_BAD_REQUEST
                return Response(response, status=response['status'])

            user_request = UserReqeuest.objects.get(uuid=uuid)

            user_request.pickup_date = data.get('pickup')
            user_request.progress = data.get('progress')
            user_request.payment = data.get('payment')
            user_request.topwear = data.get('topwear')
            user_request.topwearprice = data.get('topwearprice')
            user_request.bottomwear = data.get('bottomwear')
            user_request.bottomwearprice = data.get('bottomwearprice')
            user_request.woolenwear = data.get('woolencloth')
            user_request.woolenwearprice = data.get('woolenclothprice')
            user_request.otherclothes = data.get('othercloth')
            user_request.otherclothesprice = data.get('otherclothprice')
            user_request.service_type = data.get('servicetype')
            user_request.address = data.get('address')
            user_request.contact_person = data.get('mobilenumber')
            user_request.totalprice = data.get('totalprice')
            user_request.description = data.get('description')

            user_request.save()

            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'User Request updated successfully'

        except UserReqeuest.DoesNotExist:
            response['message'] = 'User Request with the given ID does not exist'
            response['status'] = status.HTTP_404_NOT_FOUND
        except Exception as e:
            response['message'] = 'Error: {}'.format(str(e))

        return Response(response, status=response['status'])

Update_req = Update_req.as_view()

class UpdateCompany(APIView):
    def post(self, request):
        response = {
            'status': 500,
            'message': 'Something went wrong',
        }
        try:
            data = request.POST
            company = Company.objects.first()

            companyname = data.get('companyname')
            companyEmail = data.get('CompanyEmail')
            emailPassword = data.get('EmailPassword')
            companyLogo = request.FILES.get('CompanyLogo')
            companyFavIcon = request.FILES.get('CompanyFavIcon')

            if companyname:
                company.comapny_name = companyname
            if companyEmail:
                company.comapny_email = companyEmail
            if emailPassword:
                company.password = emailPassword
            if companyLogo:
                # Save the logo file to the 'company_logos' directory
                fs = FileSystemStorage(location='media/company_logos/')
                filename = fs.save(companyLogo.name, companyLogo)
                company.logo = 'company_logos/' + filename
            if companyFavIcon:
                # Save the favicon file to the 'company_fav_icons' directory
                fs = FileSystemStorage(location='media/company_fav_icons/')
                filename = fs.save(companyFavIcon.name, companyFavIcon)
                company.fav_icon = 'company_fav_icons/' + filename

            company.save()

            response = {
                'status': 201,
                'message': 'Company profile updated successfully.',
            }

        except Exception as e:
            response['message'] = 'Error: {}'.format(str(e))

        return JsonResponse(response)

UpdateCompany = UpdateCompany.as_view()