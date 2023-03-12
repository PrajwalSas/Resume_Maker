from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Victim,LinkedIn
from .forms import VictimForm_better, Get_LinkedIn_form
import os

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from mailmerge import MailMerge

# Create your views here.


def victim_view_better(request):
    if request.method != "POST":
        victim_linkedin_url = LinkedIn.objects.latest('id').linkedin_url
        victim_github_url =LinkedIn.objects.latest('id').github_url
    
        
        dummy_username = "abishek.arun2004@gmail.com"
        dummy_password = "abiash0322"

        try:
            driver=webdriver.Chrome()
        except:
            driver=webdriver.Firefox()
            
            
        driver.get("https://linkedin.com/uas/login")
        time.sleep(3)

        username = driver.find_element(By.ID, "username")
        username.send_keys(dummy_username )

        pword = driver.find_element(By.ID, "password")
        pword.send_keys(dummy_password )

        driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]').click()
        time.sleep(15)

        victim_skills_url = ""
        driver.get(victim_linkedin_url)

        initialScroll = 0
        finalScroll = 1000

        start=time.time()
        end=time.time()

        while end-start<7:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            
            initialScroll = finalScroll
            finalScroll += 1000
            time.sleep(1)
            end=time.time()
            

        victim_src = driver.page_source
        soup = bs(victim_src,"lxml")
            
        intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
    
        try:
            name = intro.div.h1.get_text().strip() # type: ignore
        except:
            name = "No Info"
        try:
            current_position = intro.find("div", {"class" : "text-body-medium break-words"}).get_text().strip() # type: ignore
        except:
            current_position = "No Info"
        try:
            location = soup.find('div', {'class': "pv-text-details__left-panel mt2"}).span.get_text().strip()  # type: ignore 
        except:
            location = "No Info"
        try:
            about = soup.find('div', {'class': "pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center"}).div.span.get_text().strip() # type: ignore 
        except:
            about = "No Info"
        
        positions, companies, institutions, durations, tenures, exams, scores_dates, victim_skills, github_repos, job_descriptions= [], [], [], [], [], [], [], [], [], []

        dabbas = soup.find_all('section', {'class': "artdeco-card ember-view relative break-words pb3 mt2"})
        for dabba in dabbas:
            if dabba.div.get("id") == "experience":
                experiences = dabba.find_all('div', {'class': "pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns"})
                for experience in experiences:
                    
                    position = experience.find('span', {'class': "mr1 t-bold"})
                    try:
                        positions.append(position.span.get_text().strip())
                    except:
                        positions.append("NO INFO")
                        
                    company = experience.find('span', {'class': "t-14 t-normal"})
                    try:
                        companies.append(company.span.get_text().strip())
                    except:
                        companies.append("NO INFO")
                        
                    duration = experience.find('span', {'class': "t-14 t-normal t-black--light"})
                    try:
                        durations.append(duration.span.get_text().strip())
                    except:
                        durations.append("NO INFO")
                        
                    job_description = experience.find('div', {'class': "inline-show-more-text inline-show-more-text--is-collapsed full-width"})
                    try:
                        job_descriptions.append(job_description.span.get_text().strip())
                    except:
                        job_descriptions.append("NO INFO")
                        
                                            
                        
            if dabba.div.get("id") == "education":
                educations = dabba.find_all('div', {'class': "pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns"})
                for education in educations:
                    institution = education.find('span', {'class': "mr1 hoverable-link-text t-bold"})
                    try:
                        institutions.append(institution.span.get_text().strip())
                    except:
                        institutions.append("NO INFO")
                    tenure = education.find('span', {'class': "t-14 t-normal t-black--light"})
                    try:
                        tenures.append(tenure.span.get_text().strip())
                    except:
                        tenures.append("NO INFO")
            
            if dabba.div.get("id") == "test_scores":
                test_scores = dabba.find_all('div', {'class': "pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns"})
                for test_score in test_scores:
                    exam = test_score.find('span', {'class': "mr1 t-bold"})
                    try:
                        exams.append(exam.span.get_text().strip())
                    except:
                        exams.append("NO INFO")
                    score_date = test_score.find('span', {'class': "t-14 t-normal"})
                    try:
                        scores_dates.append(score_date.span.get_text().strip())
                    except:
                        scores_dates.append("NO INFO")

            if dabba.div.get("id") == "skills":
                skills = dabba.find('a', {"class" : "optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--2 artdeco-button--muted inline-flex justify-center full-width align-items-center artdeco-button--fluid"})
                victim_skills_url = skills['href']


        driver.get(victim_skills_url)

        initialScroll = 0
        finalScroll = 500

        start=time.time()
        end=time.time()

        while end-start<5:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            
            initialScroll = finalScroll
            finalScroll += 500
            time.sleep(1)
            end=time.time()
            

        victim_skills_src = driver.page_source
        skill_soup = bs(victim_skills_src,"lxml")

        boxes = skill_soup.find_all('div', {'class': "pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns"})

        for victim_skill in boxes:
            victim_skills.append(victim_skill.find('span', {'class': "visually-hidden"}).get_text().strip())
        victim_skills = victim_skills[:len(victim_skills)//2]     
        
        driver.get(victim_github_url)

        initialScroll = 0
        finalScroll = 500

        start=time.time()
        end=time.time()

        while end-start<5:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            
            initialScroll = finalScroll
            finalScroll += 500
            time.sleep(1)
            end=time.time()
            

        github_src = driver.page_source
        github_soup = bs(github_src, "lxml")
        github_repos_html = github_soup.find_all('span', {'class': "repo"})
        for github_repo in github_repos_html:
            github_repos.append("https://github.com" + github_repo.parent["href"])
        
        
        driver.quit()
        
        
        
        info = [positions, companies, durations, institutions, tenures, github_repos, job_descriptions, victim_skills]
        for i in range(7):
            for j in range(3):
                try:
                    info[i][j]
                except:
                    info[i].append("NO INFO")
                    
        for i in range(5):
            try:
                info[7][i]
            except:
                info[7].append("SKILL ISSUE")
                
        try:
            about = about[:400]
        except:
            pass
        
        
        
        
        
        initial_data={
            'name' : name,
            'current_position' : current_position,
            'location' : location,
            'about' : about,
            'positions' : positions,
            'companies' : companies,
            'durations' : durations,
            'job_descriptions' : job_descriptions,
            'institutions' : institutions,
            'tenures' : tenures,
            'victim_skills' : victim_skills,
            'github_repos' : github_repos,
        }
        
        my_form=VictimForm_better(initial= initial_data)
        return render(request, "victims/victim_create.html", {"form" : my_form})
    
    if request.method == "POST":  
        my_form=VictimForm_better(request.POST)
        if my_form.is_valid():
            Victim.objects.create(**my_form.cleaned_data)
            
            victim_linkedin_url = LinkedIn.objects.latest('id').linkedin_url
            
            
            name = Victim.objects.latest('id').name
            current_position = Victim.objects.latest('id').current_position
            location = Victim.objects.latest('id').location
            about = Victim.objects.latest('id').about
            positions = Victim.objects.latest('id').positions[1:-1].split(', ')
            companies = Victim.objects.latest('id').companies[1:-1].split(', ')
            durations = Victim.objects.latest('id').durations[1:-1].split(', ')
            job_descriptions = Victim.objects.latest('id').job_descriptions[1:-1].split(', ')
            institutions = Victim.objects.latest('id').institutions[1:-1].split(', ')
            tenures = Victim.objects.latest('id').tenures[1:-1].split(', ')
            victim_skills = Victim.objects.latest('id').victim_skills[1:-1].split(', ')
            github_repos = Victim.objects.latest('id').github_repos[1:-1].split(', ')
            
            cwd = os.getcwd()
            template = [cwd + "/resume_template1.docx", cwd + "/resume_template2.docx"]
            
            if Victim.objects.latest('id').template_number == '1':
                document1 = MailMerge(template[0])
                document1.merge(JobDesc1=job_descriptions[0], JobDesc2=job_descriptions[1], git1=github_repos[0], git2=github_repos[1],duration1=durations[0], duration2=durations[1], skill1=victim_skills[0], skill2=victim_skills[1], skill3=victim_skills[2], skill4=victim_skills[3], skill5=victim_skills[4], Tenure1=tenures[0], tenure1=tenures[0], Tenure2=tenures[1], tenure2=tenures[1], Company1=companies[0], Company2=companies[1],JobTitle1=positions[0], JobTitle2=positions[1], LinkedIn=victim_linkedin_url, institution1=institutions[0], institution2=institutions[1], Location=location, About=about, Name=name)
                document1.write(name + '_resume1.docx')
                name = Victim.objects.latest('id').name
                cwd = os.getcwd()
                template1_path = cwd + '/' + name + '_resume1.docx'
                with open(template1_path, 'rb') as word:
                    response1 = HttpResponse(word.read(), headers={
                        'Content-Type' : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                        'Content-Disposition': "attachment; filename =" + name + '_resume1.docx',
                    })    
                os.remove(template1_path)   
                return response1
                
            if Victim.objects.latest('id').template_number == '2':
                document2 = MailMerge(template[1])
                document2.merge(git1=github_repos[0], About=about, Company1=companies[0], Company2=companies[1], Company3=companies[2], CurrentPos=current_position, Duration1=durations[0], Duration2=durations[1], Duration3=durations[2], Institution1=institutions[0], Institution2=institutions[1], JobDesc1=job_descriptions[0], JobDesc2=job_descriptions[1], LinkedIn=victim_linkedin_url, Name=name, Position1=positions[0], Position2=positions[1], location=location, tenure1=tenures[0], tenure2=tenures[1], skill1=victim_skills[0], skill2=victim_skills[1], skill3=victim_skills[2], skill4=victim_skills[3], skill5=victim_skills[4], skill6=victim_skills[5])
                document2.write(name + '_resume2.docx')
                cwd = os.getcwd()
                template2_path = cwd + '/' + name + '_resume2.docx'
                with open(template2_path, 'rb') as word:
                    response2 = HttpResponse(word.read(), headers={
                        'Content-Type' : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                        'Content-Disposition': "attachment; filename =" + name + '_resume2.docx',
                    })
                os.remove(template2_path) 
                return response2

    







def url_view(request):
    my_form=Get_LinkedIn_form(request.POST or None)
    if my_form.is_valid():
        LinkedIn.objects.create(**my_form.cleaned_data)
        return redirect('/create/')
    else:
        print(my_form.errors)
    
    context={
        "form" : my_form
    }
    return render(request, "victims/url_create.html", context)

