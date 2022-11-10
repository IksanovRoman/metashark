from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from openpyxl import Workbook
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from university.models import *
from university.permissions import IsAdminOrReadOnly
from university.serializers import *


def excel(request):

    direction_queryset = Direction_of_studying.objects.all()
    students_queryset = Student.objects.all()

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-report.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    workbook = Workbook()

    worksheet = workbook.create_sheet(title="Направления", index=0)
    worksheet2 = workbook.create_sheet(title="Студенты", index=1)


    # Define the titles for worksheet
    columns = [
        'ID',
        'Куратор',
        'Направление',
        'Дисциплины',
    ]


    columns2 = [
        'ID',
        'Имя',
        'Фамилия',
        'Отчество',
        'Группа',
    ]

    row_num2 = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=1, column=col_num)
        cell.value = column_title


    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns2, 1):
        cell = worksheet2.cell(row=1, column=col_num)
        cell.value = column_title

    row_num = 2
    # Iterate through all directions
    for direction in direction_queryset:

        # Define the data for each cell in the row
        try:
            curator = direction.get_curator.first_name + " " + direction.get_curator.last_name
        except ObjectDoesNotExist:
            curator = "Нет куратора"

        row = [
            direction.pk,
            curator,
            direction.direction,
        ]
        row2 = direction.get_dir.all()

        # Assign the data for each cell of the row
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

        for col_num, cell_value in enumerate(row2, 1):
            cell = worksheet.cell(row=row_num, column=len(row)+1)
            cell.value = cell_value.subject_name
            row_num += 1

    # Iterate through all directions
    for student in students_queryset:
        row_num += 1

        # Define the data for each cell in the row
        row = [
            student.pk,
            student.first_name,
            student.last_name,
            student.patronymic,
            student.studying_group_id,
        ]

        # Assign the data for each cell of the row
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet2.cell(row=row_num, column=col_num)
            cell.value = cell_value

    #set auto width to cells
    for column_cells in worksheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        worksheet.column_dimensions[column_cells[0].column_letter].width = length

    workbook.save(response)

    return response


class DirectionAPIViewCreate(ListCreateAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class DirectionAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminUser,)


class SubjectAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializerView


class SubjectAPICreate(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)


class SubjectAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)


class StudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerView


class StudentAPICreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        queryset = Student.objects.filter(studying_group=self.request.data['studying_group']).count()
        if queryset > 20:
            raise ValidationError('В этой группе 20 человек')
        serializer.save()


class StudentAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class GroupAPIView(ListAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializerCreateView
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GroupAPICreate(CreateAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GroupAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
