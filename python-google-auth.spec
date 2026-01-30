%define module google-auth
%define oname google_auth

Name:		python-google-auth
Version:	2.48.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Google Authentication Library
URL:		https://pypi.org/project/google-auth/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(aiohttp) >= 3.6.2
BuildRequires:	python%{pyver}dist(cachetools) >= 2.0.0
BuildRequires:	python%{pyver}dist(cryptography) >= 38.0.3
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyasn1-modules) >= 0.2.1
BuildRequires:	python%{pyver}dist(pyjwt) >= 2.0
BuildRequires:	python%{pyver}dist(pyopenssl) >= 20.0.0
BuildRequires:	python%{pyver}dist(requests) >= 2.20.0
BuildRequires:	python%{pyver}dist(rsa) >= 3.1.4
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(urllib3)
BuildRequires:	python%{pyver}dist(wheel)
Requires:		python%{pyver}dist(cachetools) >= 2.0.0
Requires:		python%{pyver}dist(pyasn1-modules) >= 0.2.1
Requires:		python%{pyver}dist(rsa) >= 3.1.4
Requires:		python%{pyver}dist(urllib3)
Recommends:		python%{pyver}dist(pyjwt) >= 2.0
Recommends:		python%{pyver}dist(aiohttp) >= 3.6.2
Recommends:		python%{pyver}dist(cryptography) >= 38.0.3
Recommends:		python%{pyver}dist(pyopenssl) >= 20.0.0
Recommends:		python%{pyver}dist(requests) >= 2.20.0

%description
This library simplifies using Google’s various
server-to-server authentication mechanisms to
access Google APIs.

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info/

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/google/auth
%{py_sitedir}/google/oauth2
%{py_sitedir}/%{oname}-%{version}*-info
