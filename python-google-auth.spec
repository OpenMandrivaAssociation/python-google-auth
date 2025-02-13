Name:		python-google-auth
Version:	2.38.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/google-auth/google_auth-%{version}.tar.gz
Summary:	Google Authentication Library
URL:		https://pypi.org/project/google-auth/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Google Authentication Library

%files
%{py_sitedir}/google
%{py_sitedir}/google_auth-*.*-info
