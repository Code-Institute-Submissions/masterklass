from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Course, Lesson, Category, Comment
from .forms import CourseForm, UpdateCategoryForm, LessonForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def getCourses(request):
    """A view to return a list of all courses. Can be filtered passing a query string."""

    categories = Category.objects.all()
    currentCategory = ""
    courses = Course.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]

            queries = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(category__slug__icontains=query)
            categoryQ = Q(slug__icontains=query)
            courses = courses.filter(queries)
            currentCategory = categories.filter(categoryQ)
    else:
        currentCategory = categories

    context = {
        "courses": courses,
        "categories": categories,
        "currentCategory": currentCategory,
        "searchTerm": query,
    }

    return render(request, "courses/courses.html", context)


@login_required
def courseDetail(request, course_id):
    """ A view to show all lessons within a course """

    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('position')
    comments = Comment.objects.filter(course=course)

    if request.method == 'POST':

        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            newComment = commentForm.save(commit=False)
            newComment.author = request.user
            newComment.course = course

            newComment.save()

            return redirect("course_detail", course.id)
    else:
        commentForm = CommentForm()

    context = {
        'course': course,
        'lessons': lessons,
        'comments': comments,
        'commentForm': commentForm,
    }

    return render(request, 'courses/course_detail.html', context)


@staff_member_required
@login_required
def manageCategory(request):
    """ A view to create, update and delete a category. """

    categories = Category.objects.all()
    categoryForm = UpdateCategoryForm()

    if request.method == "POST":
        if request.POST.__contains__("addBtn"):

            categoryForm = UpdateCategoryForm(request.POST)

            if categoryForm.is_valid():
                categoryForm.save()

                message = "Category added successfully."
                messages.success(request, message)

                return redirect("manage_category")

        elif request.POST.__contains__("updateBtn"):

            category = categories.filter(
                id=request.POST.get('categoryId')).first()
            categoryForm = UpdateCategoryForm(request.POST, instance=category)

            if categoryForm.is_valid():
                categoryForm.save()

                message = "Category updated successfully."
                messages.success(request, message)

                return redirect("manage_category")

        elif request.POST.__contains__("deleteBtn"):

            categories.filter(id=request.POST.get('categoryId')).delete()

            message = "Category deleted successfully."
            messages.success(request, message)

            return redirect("manage_category")
    else:
        categoryForm = UpdateCategoryForm()

    context = {
        "categories": categories,
        "categoryForm": categoryForm,
    }

    return render(request, "courses/manage_category.html", context)


@staff_member_required
@login_required
def manageCourse(request):
    """ A view to manage a course """

    categories = Category.objects.all()
    courses = Course.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
    }

    return render(request, "courses/manage_course.html", context)


@staff_member_required
@login_required
def addCourse(request):
    """ A view to add a course """

    courseForm = CourseForm()
    if request.method == "POST":

        courseForm = CourseForm(request.POST, request.FILES)

        if courseForm.is_valid():
            courseForm.save()

            message = "Course added successfully."
            messages.success(request, message)

            return redirect("manage_course")

    context = {
        "courseForm": courseForm,
    }

    return render(request, "courses/add_course.html", context)


@staff_member_required
@login_required
def updateCourse(request, id):
    """ A view to update and delete a course """

    course = get_object_or_404(Course, pk=id)
    courseForm = CourseForm()

    if request.method == "POST":
        if request.POST.__contains__("updateBtn"):
            courseForm = CourseForm(
                request.POST, request.FILES, instance=course)

            if courseForm.is_valid():
                courseForm.save()

                message = "Course updated successfully."
                messages.success(request, message)

                return redirect("manage_course")

        elif request.POST.__contains__("deleteBtn"):
            course.delete()

            message = "Course deleted successfully."
            messages.success(request, message)

            return redirect("manage_course")
    else:
        courseForm = CourseForm(instance=course)

    context = {
        "courseForm": courseForm,
        "course": course,
    }

    return render(request, "courses/update_course.html", context)


@staff_member_required
@login_required
def manageLesson(request):
    """ A view to manage a course """

    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    context = {
        "courses": courses,
        "lessons": lessons,
    }

    return render(request, "courses/manage_lesson.html", context)


@staff_member_required
@login_required
def addLesson(request):
    """ A view to add a course """

    lessonForm = LessonForm()
    if request.method == "POST":

        lessonForm = LessonForm(request.POST)

        if lessonForm.is_valid():
            lessonForm.save()

            message = "Lesson added successfully."
            messages.success(request, message)

            return redirect("manage_lesson")

    context = {
        "lessonForm": lessonForm,
    }

    return render(request, "courses/add_lesson.html", context)


@staff_member_required
@login_required
def updateLesson(request, id):
    """ A view to update and delete a course """

    lesson = get_object_or_404(Lesson, pk=id)
    lessonForm = LessonForm()

    if request.method == "POST":
        if request.POST.__contains__("updateBtn"):
            lessonForm = LessonForm(request.POST, instance=lesson)

            if lessonForm.is_valid():
                lessonForm.save()

                message = "Lesson updated successfully."
                messages.success(request, message)

                return redirect("manage_lesson")

        elif request.POST.__contains__("deleteBtn"):
            lesson.delete()

            message = "Lesson deleted successfully."
            messages.success(request, message)

            return redirect("manage_lesson")
    else:
        lessonForm = LessonForm(instance=lesson)

    context = {
        "lessonForm": lessonForm,
    }

    return render(request, "courses/update_lesson.html", context)
