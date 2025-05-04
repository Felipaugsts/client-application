from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ViewSet):
    """
    ViewSet para manipulação de jobs com actions personalizadas.
    """

    # GET /api/jobs/fetch-jobs/
    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny], url_path='fetch-jobs')
    def fetch_all_jobs(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    # GET /api/jobs/fetch-job/<id>/
    @action(detail=True, methods=['get'], permission_classes=[permissions.AllowAny], url_path='fetch-job')
    def fetch_job(self, request, pk=None):
        job = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    # DELETE /api/jobs/<id>/delete-job/
    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticated], url_path='delete-job')
    def delete_job(self, request, pk=None):
        job = get_object_or_404(Job, pk=pk)

        # Verifica se o usuário atual é o dono do job
        if job.user != request.user:
            return Response(
                {'detail': 'Você não tem permissão para excluir este job.'},
                status=status.HTTP_403_FORBIDDEN
            )

        job.delete()
        return Response({'detail': 'Job excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)

    # POST /api/jobs/create-job/
    @action(detail=False, methods=['post'], url_path='create-job')
    def create_job(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # ⚠️ Adiciona o usuário aqui!
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT /api/jobs/<id>/edit-job/
    @action(detail=True, methods=['put'], permission_classes=[permissions.IsAuthenticated], url_path='edit-job')
    def edit_job(self, request, pk=None):
        job = get_object_or_404(Job, pk=pk)

        if job.user != request.user:
            return Response(
                {'detail': 'Você não tem permissão para editar este job.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)