Name:           codespell
Version:        1.17.1
Release:        6%{?dist}
Summary:        Fix common misspellings in text files

License:        GPLv2 and CC-BY-SA 3.0
URL:            https://github.com/codespell-project/codespell/
Source0:        https://github.com/codespell-project/codespell/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest

# git snapshot up to 81f5c59a720204bea120ae0deaf95ded4a727a67
Patch0: codespell-usage-dict.patch

%description
codespell fixes common misspellings in text files. It's designed primarily for
checking misspelled words in source code, but it can be used with other files
as well.

%prep
%autosetup -n %{name}-%{version} -S git_am
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/codespell_lib/tests

%check
%{__python3} setup.py test

%files
%doc README.rst
%{_bindir}/codespell
%{python3_sitelib}/codespell_lib
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-5
+ codespell-1.17.1-5
- Replace Python version globs with macros to support 3.10

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-4
+ codespell-1.17.1-4
- Bump version to match f32 branch

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-3
+ codespell-1.17.1-3
- Fix usage dictionary not being distributed

* Mon Jun 15 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-2
+ codespell-1.17.1-2
- Add usage dictionary

* Wed Jun 10 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-1
+ codespell-1.17.1-1
- Update to 1.17.1
- Fix Python 3.8 warning (#1840693)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Wolfgang Stöggl <c72578@yahoo.de> - 1.16.0-1
- New upstream version 1.16.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Bastien Nocera <bnocera@redhat.com> - 1.15.0-2
+ codespell-1.15.0-2
- Fix some review comments

* Tue Jun 18 2019 hadess <bnocera@redhat.com> - 1.15.0-1
- Initial package.
