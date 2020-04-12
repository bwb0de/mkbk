#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#


import os

from subprocess import check_output


def check_profile_op(profile):
	if profile == 'all':
		full_path_2_conf_dir = check_output('cd ~/.mkbk/; pwd', shell=True)
		full_path_2_conf_dir = full_path_2_conf_dir.decode("utf-8").replace(os.linesep,'')
		profiles = os.listdir(full_path_2_conf_dir)
	elif profile != 'default':
		profiles = [profile]
	else:
		profiles = ['default']
	return profiles



def create_config_files(profile='default'):
	os.system("mkdir -p ~/.mkbk/{profile}; touch ~/.mkbk/{profile}/backup_folders ~/.mkbk/{profile}/target_folder".format(profile=profile))



def purge_config_files(profile='all'):
	if profile == 'all':
		op = input('Tem certeza que deseja apagar todos os perfis? (s/n): ')
		if op == ('s' or 'S'):
			os.system("rm -fR ~/.mkbk")
			print('Todos os perfis foram excluídos...')
	else:
		os.system("rm -fR ~/.mkbk/{profile}".format(profile=profile))
	create_config_files()



def insert_into_sources(insert_folder, profile):
	create_config_files(profile)
	os.system("echo '{insert_folder}' >> ~/.mkbk/{profile}/backup_folders".format(insert_folder=insert_folder, profile=profile))



def set_target_folder(insert_folder, profile):
	create_config_files(profile)
	os.system("echo '{insert_folder}' > ~/.mkbk/{profile}/target_folder".format(insert_folder=insert_folder, profile=profile))



def get_config_info(profile):
	bk_f = check_output("cat < ~/.mkbk/{}/backup_folders".format(profile), shell=True)
	bk_f = bk_f.decode("utf-8").split(os.linesep)[:-1]
	tg_f = check_output("cat < ~/.mkbk/{}/target_folder".format(profile), shell=True)
	tg_f = tg_f.decode("utf-8").replace(os.linesep,'')
	return (bk_f, tg_f)



def get_all_profiles():
	full_path_2_conf_dir = check_output('cd ~/.mkbk/; pwd', shell=True)
	full_path_2_conf_dir = full_path_2_conf_dir.decode("utf-8").replace(os.linesep,'')
	profiles = os.listdir(full_path_2_conf_dir)
	for profile in profiles:
		nfo = get_config_info(profile)
		show_profile_info(profile, nfo)



def show_profile_info(profile, nfo):
	bk_f, tg_f = nfo[0], nfo[1]
	print('** Configurações do perfil {} **'.format(profile))
	print('Diretórios fontes listados:')
	bk_f = check_output("cat < ~/.mkbk/{}/backup_folders".format(profile), shell=True)
	print(bk_f.decode("utf-8").split(os.linesep)[:-1])
	print('')
	print('Diretório de destino:')
	tg_f = check_output("cat < ~/.mkbk/{}/target_folder".format(profile), shell=True)
	print(tg_f.decode("utf-8").replace(os.linesep,''))
	print('')

