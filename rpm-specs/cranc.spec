%global debug_package %{nil}

Name:		cranc
Version:	1.1.0
Release:	4%{?dist}
Summary:	Pagure CLI for handling pull requests

License:	GPLv3
URL:		https://pagure.io/cranc
Source0:	https://releases.pagure.org/cranc/cranc-%{version}.tar.gz

BuildArch:	noarch
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-black
%endif
BuildRequires:	python3-devel
Requires:	python3-click
Requires:	python3-libpagure
Requires:	python3-requests
Requires:	python3-pygit2
Requires:	python3-git-url-parse

%description
Cranc is a Pagure command line interface tool

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v
%endif


%files
%doc README.rst
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/cranc
%{_bindir}/cranc


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Lenka Segura <lenka@sepu.cz> - 1.1.0
- Drop pbr dependency
- update to version 1.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Lenka Segura <lenka@sepu.cz> - 1.0.1
- update to version 1.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2-3
- python-cranc renamed to cranc
- typos fixed (BuildRequires
- changelog fixed

* Mon Feb 25 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2-2
- Python2 removed
- %%{_bindir} used
- cranc specified for %%{python3_sitelib}
- version-release info corrected in changelog

* Tue Feb 19 2019 Lenka Segura <lenka@sepu.cz> - 0.2.2
- Update to 0.2.2
