
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lifestyle import settings
from myapp import views

urlpatterns = [
    path('',views.public_home),
    path('forget_password',views.forget_password),
    path('forget_password_post',views.forget_password_post),
    path('login',views.login),
    path('admin_home',views.admin_home),

    path('admin_verify_expert',views.admin_verify_expert),
    path('admin_verify_expert_post',views.admin_verify_expert_post),
    path('admin_verify_expert_post_date',views.admin_verify_expert_post_date),
    path('premium',views.premium),
    path('on_payment_success',views.on_payment_success),
    path('gopremium',views.gopremium),
    path('expert_sent_feedback',views.expert_sent_feedback),


    path('admin_view_user',views.admin_view_user),
    path('admin_view_user_post',views.admin_view_user_post),
    path('admin_view_user_post_date',views.admin_view_user_post_date),

    path('admin_unblock_expert/<int:id>',views.admin_unblock_expert),
    path('admin_block_expert/<int:id>',views.admin_block_expert),

    path('admin_approve_expert/<int:id>',views.admin_approve_expert),
    path('admin_reject_expert/<int:id>',views.admin_reject_expert),

    path('admin_view_feedback', views.admin_view_feedback),
    path('admin_view_feedback_post', views.admin_view_feedback_post),

    path('admin_block_unblock', views.admin_block_unblock),
    path('admin_block_unblock_post', views.admin_block_unblock_post),

    path('admin_view_complaints', views.admin_view_complaints),
    path('admin_view_complaints_post', views.admin_view_complaints_post),

    path('logout', views.logout),
    path('admin_reply/<int:id>', views.admin_reply),
    path('admin_reply_post', views.admin_reply_post),



    # expert
    path('expert_reg', views.expert_reg),
    path('expert_home', views.expert_home),
    path('expert_view_request', views.expert_view_request),
    path('expert_profile', views.expert_profile),
    path('expert_change_password', views.expert_change_password),

    path('expert_sent_complaints', views.expert_sent_complaints),
    path('admin_reply_expert_post', views.admin_reply_expert_post),
    path('admin_reply_expert/<id>', views.admin_reply_expert),

    path('expert_add_tutorial', views.expert_add_tutorial),
    path('delete_tutorial/<id>', views.delete_tutorial),

    path('expert_view_user', views.expert_view_user),
    path('expert_view_user_post', views.expert_view_user_post),

    path('expert_edit_profile_post', views.expert_edit_profile_post),
    path('edit_expert_profile/<int:id>', views.edit_expert_profile),
    path('expert_accept_request/<int:id>', views.expert_accept_request),
    path('chatviewexpert/<int:id>', views.chatviewexpert),



    # user
    path('users_chart', views.users_chart),



    path('user_reg', views.user_reg),
    path('user_home', views.user_home),
    path('user_view_expert', views.user_view_expert),
    path('user_view_tutorial/<id>', views.user_view_tutorial),
    path('user_sent_complaints', views.user_sent_complaints),
    path('user_sent_feedback', views.user_sent_feedback),
    path('user_profile', views.user_profile),
    path('user_change_password', views.user_change_password),
    path('user_view_request', views.user_view_request),
    path('edit_user_profile_post', views.edit_user_profile_post),
    path('edit_user_profile/<id>', views.edit_user_profile),
    path('user_request/<id>', views.user_request),
    path('delete_task/<id>', views.delete_task),
    path('user_add_task', views.user_add_task),
    path('user_add_food', views.user_add_food),
    path('user_calorie_burn_chart', views.user_calorie_burn_chart),
    path('daily_calorie_intake', views.daily_calorie_intake),
    path('today_calories_view', views.today_calories_view),
    path('delete_food/<id>', views.delete_food),

    #     chat

    # user chat with expert
    path('chatwithexpert', views.chatwithexpert, name='chatwithexpert'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

#     expert chat with user

    path('checkalert', views.checkalert, name='checkalert'),
    path('exercises', views.exercises, name='exercises'),
    path('exercises1',views.exercises1, name='exercises1'),
    path('emotion', views.emotion, name='emotion'),
    path('emotion1', views.emotion1, name='emotion1'),
    path('user_event', views.user_event, name='user_event'),
    path('insert_te', views.insert_te, name='insert_te'),
    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('expertchatview', views.expertchatview, name='expertchatview'),
    path('expertcoun_insert_chat/<str:msg>/<int:id>', views.expertcoun_insert_chat, name='expertcoun_insert_chat'),
    path('expertcoun_msg/<int:id>', views.expertcoun_msg, name='expertcoun_msg'),
    path('status_task/<int:id>', views.status_task, name='status_task'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),

    path('admin_view_expert_report', views.admin_view_expert_report),
    path('admin_view_expert_report_post', views.admin_view_expert_report_post),
    path('admin_view_user_report', views.admin_view_user_report),
    path('admin_view_user_report_post', views.admin_view_user_report_post),

    path('admin_view_complaint_report', views.admin_view_complaint_report),
    path('admin_view_complaint_report_post', views.admin_view_complaint_report_post),

    path('admin_view_feedback_report', views.admin_view_feedback_report),
    path('admin_view_feedback_report_post', views.admin_view_feedback_report_post),

    path('user_sent_expert_feedback_post', views.user_sent_expert_feedback_post),
    path('user_sent_expert_feedback/<id>', views.user_sent_expert_feedback),
    path('admin_view_expert_feedback/<id>', views.admin_view_expert_feedback),

]
