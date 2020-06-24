%global modname slackclient

Name:               python-%{modname}
Version:            2.7.1
Release:            1%{?dist}
Summary:            Slack Developer Kit for Python

License:            MIT
URL:                https://github.com/slackapi/python-%{modname}
Source0:            %{url}/archive/v%{version}/python-%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python3-websocket-client
BuildRequires:      python3-six
BuildRequires:      python3-requests
BuildRequires:      python3-pytest-runner
BuildRequires:      python3-aiodns
BuildRequires:      python3-aiohttp
Requires:           python3-websocket-client
Requires:           python3-six
Requires:           python3-requests

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_pkgversion} version.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

# re-enable once we have python3-codecov
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname}
%doc README.md docs/
%license LICENSE
%{python3_sitelib}/slack/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- 2.7.1

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.0-1
- 2.7.0

* Fri May 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-1
- 2.6.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-0.rc2
- 2.6.0 rc2

* Fri May 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-0.rc1
- 2.6.0 rc1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.1-1
- 2.3.1

* Wed Oct 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Tue Oct 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.2.1-1
- 2.2.1

* Wed Sep 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Mon May 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-1
- 2.0.1

* Fri Mar 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.1-1
- 1.3.1

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-4
- Drop Python 2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1

* Thu Mar 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-1
- 1.2.0

* Fri Mar 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.3-1
- 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.2-1
- 1.1.2

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-1
- 1.1.0

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.9-1
- 1.0.9

* Thu Aug 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.7-1
- 1.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-2
- Require python-requests.

* Wed Jul 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-1
- Initial package.
