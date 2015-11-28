Summary:	Django-skypehub is an app to use skype in remote api
Name:		python-django-skypehub
Version:	0.2.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
URL:		https://bitbucket.org/tokibito/django-skypehub/
Source0:	django-skypehub-%{version}.tar.bz2
# Source0-md5:	371824253928953b362bc85d0a696030
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-django
Requires:	python-skype
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Django-skypehub is an app to use skype in remote api.

%prep
%setup -q -n django-skypehub-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/skypehub
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/django_skypehub-%{version}-*.egg-info
%endif
