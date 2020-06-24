# what it's called on pypi
%global srcname easyargs
# what it's imported as
%global libname easyargs
# name of egg info directory
%global eggname easyargs
# package name fragment
%global pkgname easyargs

%global _description \
A project designed to make command line argument parsing easy.  There are many\
ways to create a command line parser in python: argparse, docopt, click.  These\
are all great options, but require quite a lot of configuration and sometimes\
you just need a function to be called.  Enter easyargs.  Define the function\
that you want to be called, decorate it and let easyargs work out the command\
line.

%if 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif

%bcond_without python3

%bcond_without tests


Name:           python-%{srcname}
Version:        0.9.4
Release:        12%{?dist}
Summary:        Making argument parsing easy
License:        MIT
URL:            https://github.com/stedmeister/easyargs
Source0:        %pypi_source
BuildArch:      noarch


%description %{_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  python2-six
%endif
Requires:       python2-six
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-six
%endif
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info
find -name \*.py | xargs sed -i -e '1 {/^#!/d}'


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose}
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Carl George <carl@george.computer> - 0.9.4-6
- Disable python2 subpackage on F30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Carl George <carl@george.computer> - 0.9.4-2
- Correct misplaced six requirement

* Thu Jul 06 2017 Carl George <carl@george.computer> - 0.9.4-1
- Initial package
