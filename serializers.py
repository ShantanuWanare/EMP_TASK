from rest_framework import serializers
from .models import EmpQualification
from .models import EmpWorkExperience
from .models import EmpProjects
from .models import EmpPersonalDetails
from .models import EmpAddressDetails
from drf_writable_nested import WritableNestedModelSerializer


class EmpAddressDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpAddressDetails
        fields = ('hno', 'street', 'city', 'state', )

    def create(self, validated_data):
        return EmpAddressDetails.objects.create(**validated_data)


class EmpWorkExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpWorkExperience
        fields = ('companyName', 'fromDate', 'toDate', 'address', )

    def create(self, validated_data):
        return EmpWorkExperience.objects.create(**validated_data)


class EmpQualificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpQualification
        fields = ('qualificationName', 'percentage', )

    def create(self, validated_data):
        return EmpQualification.objects.create(**validated_data)


class EmpProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpProjects
        fields = ('title', 'description', )

    def create(self, validated_data):
        return EmpProjects.objects.create(**validated_data)


class EmpPersonalDetailsModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    EmpAddressDetails = EmpAddressDetailsModelSerializer()
    EmpWorkExperience = EmpWorkExperienceModelSerializer(many=True)
    EmpQualification = EmpQualificationModelSerializer(many=True)
    EmpProjects = EmpProjectsModelSerializer(many=True)
    # EmpPhoto = EmpPhotoModelSerializer()

    class Meta:
        model = EmpPersonalDetails
        fields = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo',
                  'EmpAddressDetails', 'EmpWorkExperience', 'EmpQualification', 'EmpProjects', 'photo')


