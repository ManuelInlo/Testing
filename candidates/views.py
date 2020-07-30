from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Candidate, Comment
from .forms import CandidateForm

@login_required


def candidates(request):
    if request.method == 'POST':
        #TODO:Buscar en base de datos
        query = request.POST.get('query')
        candidate_list = Candidate.objects.filter(first_name__contains=query)
        return render(request, 'candidates/index.html', { 'candidate_list': candidate_list })
    else:
        candidate_list = Candidate.objects.all()
        return render(request, 'candidates/index.html', { 'candidate_list': candidate_list })
@login_required
def candidates_add(request):
    if request.method == 'POST':
        #TODO: Guardar en base
        form = CandidateForm(request.POST)

        if form.is_valid():
            candidate = form.save(commit = False)
            #TODO: Advance validations (regex)
            candidate.save()

            # TODO: crear un log
            comment = Comment(
                candidate = candidate,
                recruiter = request.user,
                description = 'Candidato recien creado',
                status = candidate.status
            )

            comment.save()

            return redirect('candidates')
    else:
        form = CandidateForm()
        return render(request, 'candidates/add.html', { 'form': form })       
@login_required
def candidates_profile(request, pk):
    #Buscar un candidato
    candidate = get_object_or_404(Candidate, pk=pk)

   # taday = date.today()
    #days_in_year = 365.2425    
    #age = int((date.today() - birth_date).days / days_in_year)

    #return render(request, 'candidates/profile.html', { 'candidate': candidate, 'age': age })

    comment_list = Comment.objects.filter(candidate=candidate, )
    return render(request, 'candidates/profile.html', { 'candidate': candidate, 'comments':comment_list})
@login_required
def candidates_edit(request, pk):
    if request.method == 'POST':
        #TODO: ACTUALIZAR CANDIDATE
        candidate = get_object_or_404(Candidate, pk=pk)

        email_before = candidate.email

        form = CandidateForm(request.POST, instance=candidate)

        

        if form.is_valid():
            form.save()

            comment = Comment(
                candidate = candidate,
                recruiter = request.user,
                #description = f"Candidate information updated. Email before: { meil_before}, Email after: {form_after}",
                status = candidate.status
            )

            comment.save()

            return redirect('candidates')
    else:         
        candidate = get_object_or_404(Candidate, pk=pk)
        form = CandidateForm(request.POST or None, instance=candidate)
        return render(request, 'candidates/edit.html', { "form": form, "pk": pk })