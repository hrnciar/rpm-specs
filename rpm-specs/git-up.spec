%global srcname git-up

Name:           git-up
Version:        2.0.1
Release:        2%{?dist}
Summary:        A more friendly "git pull" in python

License:        MIT
URL:            https://pypi.python.org/pypi/git-up
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/msiemens/PyGitUp/master/LICENCE

BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3dist(click)
BuildRequires: python3dist(colorama)
BuildRequires: python3dist(gitpython)
BuildRequires: python3dist(nose)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(six)
BuildRequires: python3dist(termcolor)
BuildRequires: python3dist(pytest)
BuildRequires: git-core

%{?python_provide:%python_provide python3-%{srcname}}

%global _description %{expand:
Provides a more convenient git pull in python.}

%description %_description

%prep
%autosetup -n %{srcname}-%{version}
cp %{S:1} .

%build
%py3_build

%install
%py3_install

#%check
#git config --global user.email "koji@fedoraproject.org"
#git config --global user.name "Koji Build System"
#PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version}

# Note that there is no %%files section for the unversioned python module
%files 
%license LICENCE
%doc README.rst
%{python3_sitelib}/git_up-*.egg-info/
%{python3_sitelib}/PyGitUp/
%{_bindir}/git-up

%changelog
* Mon Oct  5 2020 Martin Jackson <mhjacks@swbell.net> - 2.0.1-2
- Add explicit dep on setuptools.

* Sat Aug 29 2020 Martin Jackson <mhjacks@swbell.net> - 2.0.1-1
- New upstream release.  Relaxes dep on colorama.

* Sun Aug 23 2020 Martin Jackson <mhjacks@swbell.net> - 1.6.1-6
- Comment out %check for now.  Change in git broke them.  Will be fixed in upstream 2.0.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Martin Jackson <mhjacks@swbell.net> - 1.6.1-1
- Initial release
